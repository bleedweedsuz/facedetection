import cv2, dlib, numpy as np, time
from Utility import Utility

class Realtime68Landmarks:
    def __init__(self, width = 700, height = 700, isFacebox = False, isLandmarks = False):
        self.isFacebox = isFacebox
        self.isLandmarks = isLandmarks
        self.capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        time.sleep(1) #Initilizing camera it can takes 1 second to load camera
        self.capture.set(3, width)  # set camera frame width
        self.capture.set(4, height)  # set camera frame height
        self.detector = dlib.get_frontal_face_detector() #Frontal detector using dlib
        self.predictor = dlib.shape_predictor("dat/shape_predictor_68_face_landmarks.dat") #Initilize 68 landmarks in faces
        if not(self.capture.isOpened()): print("Could not open camera.") #Camera not opened.
        else: self.drawLandmarks() #draw landmarks in faces

    def drawLandmarks(self):
        while(True):
            ret, frame = self.capture.read() #Read capture data
            if not ret: break #No capture data
            gColor = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Converting color image to gray image
            faces = self.detector(gColor) #Detect face using dat file predeictor
            for face in faces: #Loop all faces capture by detector
                if self.isFacebox: cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2) #Create rectangle box in face
                lMarks = self.predictor(gColor, face) #Get landmarks using predictor file in dlib

                if self.isLandmarks: 
                    for i in range(0, 68): cv2.circle(frame, (lMarks.part(i).x, lMarks.part(i).y), 2, (255, 0, 0), -1) #Adding landmarks using circle  #Loop landmarks in face
                
                self.drawOnFullEyeLMark(frame, lMarks)
                self.drawOnLeftEyeLMark(frame, lMarks)
                self.drawOnRightEyeLMark(frame, lMarks)
                self.drawOnNoseLMark(frame, lMarks)
                self.drawOnMouthLMark(frame, lMarks)
            cv2.imshow("Frame", frame)
            if(cv2.waitKey(1) == ord('q')): break
        
        self.capture.release()
        cv2.destroyAllWindows()

    def drawOnLeftEyeLMark(self, frame, lMarks):
        Utility.addPolygon(cv2, frame, np.array([[lMarks.part(36).x,lMarks.part(37).y], [lMarks.part(39).x,lMarks.part(37).y], [lMarks.part(39).x,lMarks.part(40).y], [lMarks.part(36).x,lMarks.part(41).y]], dtype=np.int32), (0, 255, 0)) #leftEye
    
    def drawOnRightEyeLMark(self, frame, lMarks):
        Utility.addPolygon(cv2, frame, np.array([[lMarks.part(42).x,lMarks.part(43).y], [lMarks.part(45).x,lMarks.part(43).y], [lMarks.part(45).x,lMarks.part(46).y], [lMarks.part(42).x,lMarks.part(47).y]], dtype=np.int32), (0, 255, 0)) #rightEye

    def drawOnFullEyeLMark(self, frame, lMarks):
        Utility.addPolygon(cv2, frame, np.array([[lMarks.part(36).x,lMarks.part(37).y], [lMarks.part(45).x,lMarks.part(44).y], [lMarks.part(45).x,lMarks.part(46).y], [lMarks.part(36).x,lMarks.part(40).y]], dtype=np.int32), (0, 255, 255)) #Full Eyes

    def drawOnNoseLMark(self, frame, lMarks):
        Utility.addPolygon(cv2, frame, np.array([[lMarks.part(31).x,lMarks.part(28).y], [lMarks.part(35).x,lMarks.part(28).y], [lMarks.part(35).x,lMarks.part(33).y], [lMarks.part(31).x,lMarks.part(33).y]], dtype=np.int32), (255, 0, 0)) #Nose

    def drawOnMouthLMark(self, frame, lMarks):
        Utility.addPolygon(cv2, frame, np.array([[lMarks.part(48).x,lMarks.part(50).y], [lMarks.part(54).x,lMarks.part(50).y], [lMarks.part(54).x,lMarks.part(57).y], [lMarks.part(48).x,lMarks.part(57).y]], dtype=np.int32), (255, 0, 0)) #Mouth