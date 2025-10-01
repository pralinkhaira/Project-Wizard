using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class GameplayController : MonoBehaviour {

    public static GameplayController instance;

    public GameObject pausePanel, gameOverPanel;
    public GameObject player, starEffect;
    public Transform spawnPoint;

    public Text bestScore, playerScore, floorReached;
    public Image newHighScore;
    public int scoreJump, scorePowerJump, totalScore, floorReach = 10, totalFloor;

    public Button leftB, rightB, upB;

    bool died, newHscore;

    void Start () {
        player = GameObject.FindGameObjectWithTag("Player");
        Time.timeScale = 1f;
        MakeInstance();
        died = false;
        newHscore = false;
	}

    void Update() {

        totalScore = scoreJump + scorePowerJump;

        totalFloor = totalScore / floorReach;

        playerScore.text = "" + totalScore;
        IfPlayerDied(totalScore);
        IfPlayerDiedFloorReach(totalFloor);
        
        if (totalScore >= 300) {
            Floor.instance.timeToFall = 1.5f;
        }

        if (totalScore >= 500) {
            Floor.instance.timeToFall = 1.3f;
        }

        if (totalScore >= 800) {
            Floor.instance.timeToFall = 1f;
        }

        if (totalScore >= 1000) {
            Floor.instance.timeToFall = 0.8f;
        }
    }

    void MakeInstance() {
        if (instance == null) {
            instance = this;
        }
    }

    public void PauseGame() {
        Time.timeScale = 0f;
        pausePanel.SetActive(true);
        leftB.interactable = false;
        rightB.interactable = false;
        upB.interactable = false;
    }

    public void ResumeGame() {
        Time.timeScale = 1f;
        pausePanel.SetActive(false);
        player.SetActive(true);
        leftB.interactable = true;
        rightB.interactable = true;
        upB.interactable = true;
    }

    public void RestartGame() {
        SceneManager.LoadScene("Gameplay");
    }

    public void MainMenu() {
        SceneManager.LoadScene("Main");
    }

    public void GameOver() {
        died = true;
        gameOverPanel.SetActive(true);
        bestScore.text = "" + ScoreManager.instance.GetHighScore();
        floorReached.text = "" + totalFloor;

        if (died && newHscore) {
            StartCoroutine(NewHighScoreEffects());
            return;
        }
    }

    IEnumerator NewHighScoreEffects() {
        yield return new WaitForSeconds(0.2f);

        GameObject sfx = (GameObject)Instantiate(starEffect, spawnPoint.position, spawnPoint.rotation);
        Destroy(sfx, 1f);
    }

    public void PlayerScore(int score) {
        scoreJump += score;
    }

    public void IfPlayerDied(int score) {
        
        if (score > ScoreManager.instance.GetHighScore()) {
            ScoreManager.instance.SetHighScore(score);
            newHscore = true;
            newHighScore.gameObject.SetActive(true);            
        }
    }

    void IfPlayerDiedFloorReach(int floor) {
        if (floor > ScoreManager.instance.GetHighestFloorReach()) {
            ScoreManager.instance.SetFloorReach(floor);
        }
    }

}
