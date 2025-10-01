using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraScript : MonoBehaviour {

    public Transform player;

    public static object main { get; internal set; }

    void Update () {
        if (player.position.y > transform.position.y) {
            transform.position = new Vector3(transform.position.x, player.position.y, transform.position.z);
        }	
	}
}
