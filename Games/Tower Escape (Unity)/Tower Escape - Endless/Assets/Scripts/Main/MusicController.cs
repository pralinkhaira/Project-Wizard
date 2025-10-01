using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class MusicController : MonoBehaviour {

    [SerializeField]
    private Button musicBtn;

    [SerializeField]
    private Sprite[] musicIcons;

    void Awake() {
        CheckToPlayMusic();
    }

    void CheckToPlayMusic() {
        if (MusicPreference.GetMusicState() == 1) {
            SoundHandler.instance.PlayMusic(true);
            musicBtn.image.sprite = musicIcons[1];
        }
        else {
            SoundHandler.instance.PlayMusic(false);
            musicBtn.image.sprite = musicIcons[0];
        }
    }

    public void MusicButton() {
        if (MusicPreference.GetMusicState() == 0) {
            MusicPreference.SetMusicState(1);
            SoundHandler.instance.PlayMusic(true);
            musicBtn.image.sprite = musicIcons[1];
        }
        else if (MusicPreference.GetMusicState() == 1) {
            MusicPreference.SetMusicState(0);
            SoundHandler.instance.PlayMusic(false);
            musicBtn.image.sprite = musicIcons[0];
        }
    }
}
