using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityStandardAssets.CrossPlatformInput;

public class PlayerMovements : MonoBehaviour {

    public static PlayerMovements instance;

    public Rigidbody2D rb;
    public Transform[] groundPoints;

    public float groundRadius;
    public LayerMask ground;
    public LayerMask floor;

    public float jumpForce;
    private float walkSpeed = 4f;
    private float direction;
    private bool move;
    private float horiz;

    public bool walking, jumping, flip, isGrounded, isFloor;

    public Animator anim;

    public GameObject playerFeet;

    public AudioSource ads;
    public AudioClip jumpSound, diedSound;

    void Start () {
        rb = GetComponent<Rigidbody2D>();
        anim = GetComponent<Animator>();
        ads = GetComponent<AudioSource>();
        flip = true;
        MakeInstance();        
    }

    void MakeInstance() {
        if (instance == null) {
            instance = this;
        }
    }

    void Update() {
        if (CrossPlatformInputManager.GetButtonDown("Jump")) {
            Jump();
        }

        JumpPlayer();
    }

    void FixedUpdate () {
       
        float horizontal = CrossPlatformInputManager.GetAxis("Horizontal");

        isFloor = PlayerIsFloor();

        WalkMovement(horizontal);
        FlipPlayer(horizontal);
        JumpControllerFloor();
        ResetValues();
        ControlPlayerFloor();

        if (move) {
            this.horiz = Mathf.Lerp(horiz, direction, Time.deltaTime * 2f);
            WalkMovement(horiz);
            FlipPlayer(direction);
        }
    }

    private void WalkMovement(float horizontal) {
        rb.velocity = new Vector2(horizontal * walkSpeed, rb.velocity.y);
        anim.SetFloat("Run", Mathf.Abs(horizontal));
        walking = true;
    }

    private void FlipPlayer(float horizontal) {
        if (horizontal > 0 && !flip || horizontal < 0 && flip) {
            flip = !flip;

            Vector3 scale = transform.localScale;
            scale.x *= -1;
            transform.localScale = scale;
        }
    }

    private void JumpPlayer() {
        if (Input.GetKeyDown(KeyCode.W)) {
            jumping = true;
        }
    }

    private void JumpControllerGround() {
        if (rb.velocity.y <= 0) {
            anim.SetBool("JumpOff", true);
            playerFeet.SetActive(true);
        }

        if (isGrounded && jumping) {
            ads.PlayOneShot(jumpSound);
            isGrounded = false;
            rb.AddForce(new Vector2(0, jumpForce), ForceMode2D.Force);
            anim.SetTrigger("JumpOn");
            playerFeet.SetActive(false);
        }
    }

    private void JumpControllerFloor() {
        if (rb.velocity.y <= 0) {
            anim.SetBool("JumpOff", true);
            playerFeet.SetActive(true);
        }        

        if (isFloor && jumping) {
            ads.PlayOneShot(jumpSound);
            isFloor = false;
            rb.AddForce(new Vector2(0, jumpForce), ForceMode2D.Force);
            anim.SetTrigger("JumpOn");
            playerFeet.SetActive(false);
        }
    }

    private bool PlayerIsGrounded() {
        if (rb.velocity.y <= 0) {

            foreach (Transform point in groundPoints) {
                Collider2D[] col = Physics2D.OverlapCircleAll(point.position, groundRadius, ground);

                for (int i = 0; i < col.Length; i++) {
                    if (col[i].gameObject != gameObject) {
                        anim.ResetTrigger("JumpOn");
                        anim.SetBool("JumpOff", false);
                        return true;
                    }
                }
            }
        }
        return false;        
    }

    private bool PlayerIsFloor() {        
        if (rb.velocity.y <= 0) {
            
            foreach (Transform point in groundPoints) {
                Collider2D[] col1 = Physics2D.OverlapCircleAll(point.position, groundRadius, floor);
               
                for (int i = 0; i < col1.Length; i++) {
                    if (col1[i].gameObject != gameObject) {
                        anim.ResetTrigger("JumpOn");
                        anim.SetBool("JumpOff", false);
                        return true;                        
                    }
                }
            }
        }
        return false;
    }

    private void ControlLayerGround() {
        if (!isGrounded) {
            anim.SetLayerWeight(1, 1);
        } else {
            anim.SetLayerWeight(1, 0);
        }
    }

    private void ControlPlayerFloor() {
        if (!isFloor) {
            anim.SetLayerWeight(1, 1);
        } else {
            anim.SetLayerWeight(1, 0);
        }
    }

    private void ResetValues() {
        jumping = false;
    }

    void OnTriggerEnter2D(Collider2D collision) {
        if (collision.tag == "FloorCollector") {
            StartCoroutine(PlayerDied());            
            ads.PlayOneShot(diedSound);
            GameplayController.instance.GameOver();
        }
    }

    IEnumerator PlayerDied() {
        yield return new WaitForSeconds(1f);
        this.gameObject.SetActive(false);        
    }

    public void Jump() {
        jumping = true;
    }

    public void Moving(float direction) {
        this.direction = direction;
        this.move = true;
    }

    public void StopMoving() {
        this.direction = 0;
        this.move = false;
        this.horiz = 0;
    }
}
