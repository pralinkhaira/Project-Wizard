using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SpawnBackground : MonoBehaviour {

    private GameObject[] background;

    private float lastBackground;

    void Start() {
        background = GameObject.FindGameObjectsWithTag("Wall");
        lastBackground = background[0].transform.position.y;

        for (int i = 1; i < background.Length; i++) {
            if (lastBackground < background[i].transform.position.y) {
                lastBackground = background[i].transform.position.y;
            }
        }
    }

    void OnTriggerEnter2D(Collider2D collision) {
        if (collision.tag == "Wall") {
            Vector3 temp = collision.transform.position;
            float width = ((BoxCollider2D)collision).size.y;

            temp.y = lastBackground + width;
            collision.transform.position = temp;
            lastBackground = temp.y;
        }
    }


}
