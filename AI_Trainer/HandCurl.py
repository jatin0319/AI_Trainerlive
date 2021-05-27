import cv2
import numpy as np
import time
from . import POSEMODULE as pm


class HandCurlModule:

    def handCurl(self, img):
        detector = pm.poseDetector()
        pTime =0
        count1 =0
        count2 =0
        stage1= None
        stage2 = None

        img = cv2.resize(img, (1180,720))
        img = detector.findPose(img, False)
        lmList = detector.findPosition(img, False)
        if len(lmList) != 0:
                            
            # Left hand
            angle1 = detector.findAngle(img, 11, 13, 15, False)
            # Right hand
            angle2 = detector.findAngle(img, 12, 14, 16, False)
            
            bar1 = np.interp(angle1, (40, 170), (200,650))
            per1 = np.interp(angle1, (40, 170), (100,0))
            bar2 = np.interp(angle2, (40, 170), (200,650))
            per2 = np.interp(angle2, (40, 170), (100,0))


            # checking the stage and curls
            color1=(255,0,255)
            if angle1 >= 170 :
                color1=(0,255,0)
                stage1 = "down"
            if angle1 <= 40 :
                color1=(0,255,0)
                if stage1 =='down':
                    stage1="up"
                    count1 +=1
                    print(count1)

            # checking the stage and curls
            color2=(255,0,255)
            if angle2 >=170 :
                color2=(0,255,0)
                stage2 = "down"
            if angle2 <=40:
                color2=(0,255,0)
                if stage2 =='down':
                    stage2="up"
                    count2 +=1
                    print(count2)


        
            # Setup status box
            cv2.rectangle(img, (0,0), (300,100), (245,117,16), -1)
            cv2.rectangle(img, (880,0), (1180,100), (245,117,16), -1)

            # Draw  left Bar
            cv2.rectangle(img, (10, 200), (80, 650), color2, 3)
            cv2.rectangle(img, (10, int(bar2) ), (80, 650), color2, cv2.FILLED)
            cv2.putText(img, f'{int(per2)}%', (10, 175), cv2.FONT_HERSHEY_PLAIN, 3,
                        color2, 4)

            #Draw right bar
            cv2.rectangle(img, (1080, 200), (1160, 650), color1, 3)
            cv2.rectangle(img, (1080, int(bar1) ), (1160, 650), color1, cv2.FILLED)
            cv2.putText(img, f'{int(per1)}%', (1065, 175), cv2.FONT_HERSHEY_PLAIN, 3,
                        color1, 4)
        
            # Rep data
            cv2.putText(img, 'REPS', (15,25), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.90, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(img, str(int(count2)), 
                        (10,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
            
            cv2.putText(img, 'REPS', (895,25), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.90, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(img, str(int(count1)), 
                        (890,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
            
            # Stage data
            cv2.putText(img, 'STAGE', (120,25),cv2.FONT_HERSHEY_SIMPLEX, 0.90, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(img, stage2, (110,80),cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
            cv2.putText(img, 'STAGE', (1000,25),cv2.FONT_HERSHEY_SIMPLEX, 0.90, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(img, stage1, (990,80),cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {str(int(fps))}', (500, 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 4)
        
        return img
        
def main():
    cap = cv2.VideoCapture(0)



if __name__ == "__main__":
    main()