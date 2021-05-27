import cv2
import numpy as np
import time
from . import POSEMODULE as pm 

class SquatModule:

    def squat(self, img):
        detector = pm.poseDetector()
        pTime = 0
        count = 0
        stage = None

        img = cv2.resize(img, (1180, 720))
        img = detector.findPose(img, False)
        lmList = detector.findPosition(img, False)
        if len(lmList) != 0:
                    
            # Left leg
            angle1 = detector.findAngle(img, 23, 25, 27, False)
            # Right leg
            angle2 = detector.findAngle(img, 24, 26, 28, False)

            bar1 = np.interp(angle1, (85, 170), (200,650))
            per1 = np.interp(angle1, (85, 170), (100,0))
            bar2 = np.interp(angle2, (85, 170), (200,650))
            per2 = np.interp(angle2, (85, 170), (100,0))


            # checking the stage and squats
            color=(255,0,255)
            if angle1 >= 170 and angle2 >=170 :
                color=(0,255,0)
                stage = "up"
            if angle1 <= 85 and angle2 <=85:
                color=(0,255,0)
                if stage =='up':
                    stage="down"
                    count +=1
                    print(count)

        
            # Setup status box
            cv2.rectangle(img, (0,0), (300,100), (245,117,16), -1)

            # Draw  left Bar
            cv2.rectangle(img, (10, 200), (80, 650), color, 3)
            cv2.rectangle(img, (10, int(bar2) ), (80, 650), color, cv2.FILLED)
            cv2.putText(img, f'{int(per2)}%', (10, 175), cv2.FONT_HERSHEY_PLAIN, 3,
                        color, 4)

            #Draw right bar
            cv2.rectangle(img, (1080, 200), (1160, 650), color, 3)
            cv2.rectangle(img, (1080, int(bar1) ), (1160, 650), color, cv2.FILLED)
            cv2.putText(img, f'{int(per1)}%', (1080, 175), cv2.FONT_HERSHEY_PLAIN, 3,
                        color, 4)
        
            # Rep data
            cv2.putText(img, 'REPS', (15,25), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.90, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(img, str(int(count)), 
                        (10,80), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
            
            # Stage data
            cv2.putText(img, 'STAGE', (120,25),cv2.FONT_HERSHEY_SIMPLEX, 0.90, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(img, stage, (110,80),cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {str(int(fps))}', (1000, 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 4)

        return img


def main():
    cap = cv2.VideoCapture(0)


if __name__ == "__main__":
    main()