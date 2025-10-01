using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ScoreManager : MonoBehaviour {

    public static ScoreManager instance;

    private const string BEST_SCORE = "bestScore";
    private const string FLOOR = "floorReach";

    void Awake () {
        MakeSingleton();
        GameStartedFirstTime();
	}

    void MakeSingleton() {
        if (instance != null) {
            Destroy(gameObject);
        } else {
            instance = this;
            DontDestroyOnLoad(gameObject);
        }
    }

    void GameStartedFirstTime() {
        if (!PlayerPrefs.HasKey("isGameStartedFirstTime")) {
            PlayerPrefs.SetInt(BEST_SCORE, 0);
            PlayerPrefs.SetInt(FLOOR, 0);
            PlayerPrefs.SetInt("isGameStartedFirstTime", 0);
        }
    }

    public void SetHighScore(int score) {
        PlayerPrefs.SetInt(BEST_SCORE, score);
    }

    public int GetHighScore() {
        return PlayerPrefs.GetInt(BEST_SCORE);
    }

    public void SetFloorReach(int floor) {
        PlayerPrefs.SetInt(FLOOR, floor);
    }

    public int GetHighestFloorReach() {
        return PlayerPrefs.GetInt(FLOOR);
    }
}
