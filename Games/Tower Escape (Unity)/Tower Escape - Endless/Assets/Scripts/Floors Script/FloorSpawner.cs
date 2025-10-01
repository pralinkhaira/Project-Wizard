using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FloorSpawner : MonoBehaviour {

    [SerializeField]
    private GameObject[] floors;
    private float distanceBetweenFloors = 2.2f;

    private float minX, maxX;
    private float lastFloorPositionY;
    private float controlX;

	void Awake () {
        controlX = 0;
        SetMinMax();
        CreateFloors();     
	}

    void SetMinMax() {
        Vector3 bounds = Camera.main.ScreenToWorldPoint(new Vector3(Screen.width, Screen.height, 0));
        maxX =  bounds.x - 1.5f;
        minX = -bounds.x + 1.5f;            
    }

    void Shuffle(GameObject[] arrayToShuffle) {
        for (int i = 0; i < arrayToShuffle.Length; i++) {
            GameObject temp = arrayToShuffle[i];
            int random = Random.Range(i, arrayToShuffle.Length);
            arrayToShuffle[i] = arrayToShuffle[random];
            arrayToShuffle[random] = temp;
        }
    }

    void CreateFloors() {
        Shuffle(floors);

        float positionY = -1f;
        for (int i = 0; i < floors.Length; i++) {
            Vector3 temp = floors[i].transform.position;
            temp.y = positionY;

            if (controlX == 0)
            {
                temp.x = Random.Range(0.0f, maxX);
                controlX = 1;
            }

            else if (controlX == 1)
            {
                temp.x = Random.Range(0.0f, minX);
                controlX = 2;
            }
            else if (controlX == 2)
            {
                temp.x = Random.Range(1.0f, maxX);
                controlX = 3;
            }

            else if (controlX == 3)
            {
                temp.x = Random.Range(-1.0f, minX);
                controlX = 0;
            }

            lastFloorPositionY = positionY;
            floors[i].transform.position = temp;
            positionY += distanceBetweenFloors;
        }
    }

    void OnTriggerEnter2D(Collider2D collision) {
        if (collision.tag == "Floor") {
            if (collision.transform.position.y == lastFloorPositionY) {
                Shuffle(floors);
               
                Vector3 temp = collision.transform.position;
                for (int i = 0; i < floors.Length; i++) {
                    if (!floors[i].activeInHierarchy)
                    {

                        if (controlX == 0)
                        {
                            temp.x = Random.Range(0.0f, maxX);
                            controlX = 1;
                        }
                        else if (controlX == 1)
                        {
                            temp.x = Random.Range(0.0f, minX);
                            controlX = 2;
                        }
                        else if (controlX == 2)
                        {
                            temp.x = Random.Range(1.0f, maxX);
                            controlX = 3;
                        }
                        else if (controlX == 3)
                        {
                            temp.x = Random.Range(-1.0f, minX);
                            controlX = 0;
                        }

                        temp.y += distanceBetweenFloors;

                        lastFloorPositionY = temp.y;

                        floors[i].transform.position = temp;
                        floors[i].SetActive(true);
                        floors[i].GetComponent<BoxCollider2D>().isTrigger = true;
                       
                    }
                }
            }
        }
    }
}
