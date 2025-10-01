using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SoundHandler : MonoBehaviour {

    public static SoundHandler instance;

    public AudioSource ads;

    void Start () {
        MakeSingleton();
        ads = GetComponent<AudioSource>();
	}

    void MakeSingleton() {
        if (instance != null) {
            Destroy(gameObject);
        } else {
            instance = this;
            DontDestroyOnLoad(gameObject);
        }
    }

    public void PlayMusic(bool play) {
        if (play) {
            if (!ads.isPlaying) {
                ads.Play();
            }
        } else {
            if (ads.isPlaying) {
                ads.Stop();
            }
        }
    }
}
