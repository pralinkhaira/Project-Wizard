using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PlayerScore : MonoBehaviour {

    public static PlayerScore instance;

    public int scoreCount;
    
	void Start () {
        MakeInstance();    
    }

    void MakeInstance() {
        if (instance == null) {
            instance = this;
        }
    }

    private void OnTriggerEnter2D(Collider2D collision) {
        if (collision.tag == "Floor") {
            collision.tag = "Untagged";
            CountScore(+10);
        }
    }

    void CountScore(int score) {
        GameplayController.instance.PlayerScore(score);
    }    
}
