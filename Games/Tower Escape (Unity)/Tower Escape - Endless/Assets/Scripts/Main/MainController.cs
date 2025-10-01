using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class MainController : MonoBehaviour {

    public GameObject quitGamePanel;

	void Start () {
        Screen.sleepTimeout = SleepTimeout.NeverSleep;
        Time.timeScale = 1f;
	}
	
	void Update () {
		
	}

    public void PlayGame() {
        SceneManager.LoadScene("Gameplay");
    }

    public void OptionMenu() {
        Debug.Log("Create a scene for Option");
    }

    public void Quit() {
        quitGamePanel.SetActive(true);
    }

    public void QuitGame() {
        Application.Quit();
    }

    public void CancelQuitting() {
        quitGamePanel.SetActive(false);
    }

}
