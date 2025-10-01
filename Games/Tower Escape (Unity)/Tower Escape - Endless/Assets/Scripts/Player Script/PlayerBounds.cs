using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerBounds : MonoBehaviour {

    private float minX, maxX;


	void Start () {
        SetMinAndMax();
	}
	
	void Update () {
        if (transform.position.x < minX) {
            Vector3 temp = transform.position;
            temp.x = minX;
            transform.position = temp;
        }

        if (transform.position.x > maxX) {
            Vector3 temp = transform.position;
            temp.x = maxX;
            transform.position = temp;
        }
	}

    void SetMinAndMax() {
        Vector3 bounds = Camera.main.ScreenToWorldPoint(new Vector3(Screen.width, Screen.height, 0));

        maxX = bounds.x - 1f;
        minX = -bounds.x + 1f;
    }
}
