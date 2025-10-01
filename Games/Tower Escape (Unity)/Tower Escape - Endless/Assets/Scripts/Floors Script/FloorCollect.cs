using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FloorCollect : MonoBehaviour {

    void OnTriggerEnter2D(Collider2D collision) {
        if (collision.tag == "Untagged") {
            collision.gameObject.SetActive(false);
            collision.gameObject.tag = "Floor";
            collision.gameObject.GetComponent<Rigidbody2D>().bodyType = RigidbodyType2D.Kinematic;
        }

        if (collision.tag == "Floor") {
            collision.gameObject.SetActive(false);
        }
    }
}
