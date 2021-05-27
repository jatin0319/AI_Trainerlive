import cv2, os, urllib.request
import numpy as np
import time
from . import POSEMODULE as pm
from . import HandCurl as hc
from . import Squats as sq

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    # def __del__(self):
    #     self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        handCurl = hc.HandCurlModule()
        image = handCurl.handCurl(image)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def get_frame2(self):
        success, image = self.video.read()
        s = sq.SquatModule()
        image = s.squat(image)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    # def update(self):
    #     while True:
    #         (self.grabbed, self.frame) = self.video.read()

