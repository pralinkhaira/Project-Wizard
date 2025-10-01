using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MusicPreference : MonoBehaviour {

    public static string IsMucisOn = "IsMucisOn";

    public static int GetMusicState() {
        return PlayerPrefs.GetInt(MusicPreference.IsMucisOn);
    }

    public static void SetMusicState(int state) {
        PlayerPrefs.SetInt(MusicPreference.IsMucisOn, state);
    }
}
