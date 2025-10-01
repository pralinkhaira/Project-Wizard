using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class DestroyGroundFloor : MonoBehaviour {

   // public Image grndFlrImage;

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.tag == "FloorCollector") {
        //    grndFlrImage.gameObject.SetActive(false);
        }
    }
}
