using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Floor : MonoBehaviour {

    public static Floor instance;

    private BoxCollider2D Bcollider;
    public Rigidbody2D rigidB;
    private RigidbodyType2D bodyType;

    private bool fall;
   
    public float timeToFall = 2f;

    int score;

	void Start () {
        Bcollider = this.GetComponent<BoxCollider2D>();
        rigidB = this.GetComponent<Rigidbody2D>();
        bodyType = RigidbodyType2D.Kinematic;
        MakeInstance();
     }
	
    void MakeInstance() {
        if (instance == null) {
            instance = this;
        }
    }

    void Update() {
        score = GameplayController.instance.totalScore;
        if (score == 80) {
            fall = true;
        }
        
        if (fall) {
            bodyType = RigidbodyType2D.Dynamic;
        }

        if (score >= 150) {
            timeToFall = 1.5f;
        }
    
        if (score >= 250) {
            timeToFall = 1.25f;
        }
        
         if (score >= 400) {
            timeToFall = 1f;
        }
        
        if (score >= 500) {
            timeToFall = 0.8f;
        }

        if (score >= 650) {
            timeToFall = 0.6f;
        }
        
        if (score >= 1000) {
            timeToFall = 0.5f;
        }
        
    }

    private void OnTriggerEnter2D(Collider2D collision) {
        if (collision.tag == "PlayerFeet" || collision.tag == "SkipFloor") {
            Bcollider.isTrigger = false;
            StartCoroutine(ChangeBodyType());
        }

        if (collision.tag == "SkipFloor") {
            Bcollider.isTrigger = false;
            StartCoroutine(ChangeBodyType());
            //Debug.Log("Skip Floor touch!");
        }

        if (collision.tag == "Floor") {
            Bcollider.isTrigger = false;
            StartCoroutine(ChangeBodyType());
            collision.gameObject.GetComponent<BoxCollider2D>().isTrigger = false;
            collision.gameObject.GetComponent<Rigidbody2D>().bodyType = RigidbodyType2D.Dynamic;
            //Debug.Log("Floor touch floor");
        }       
    }

    IEnumerator ChangeBodyType() {
        yield return new WaitForSeconds(timeToFall);
        rigidB.bodyType = bodyType;
    }
}
