import numpy as np

class Utility:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def __init__(self, cv2):
        self.cv2 = cv2

    def addPolygon(self, image, points, color):
        self.cv2.fillConvexPoly(image, points, color)
    
    def drawOnLeftEyeLMark(self, frame, lMarks):
        Utility.addPolygon(self.cv2, frame, np.array([[lMarks.part(36).x,lMarks.part(37).y], [lMarks.part(39).x,lMarks.part(37).y], [lMarks.part(39).x,lMarks.part(40).y], [lMarks.part(36).x,lMarks.part(41).y]], dtype=np.int32), (0, 255, 0)) #leftEye
    
    def drawOnRightEyeLMark(self, frame, lMarks):
        Utility.addPolygon(self.cv2, frame, np.array([[lMarks.part(42).x,lMarks.part(43).y], [lMarks.part(45).x,lMarks.part(43).y], [lMarks.part(45).x,lMarks.part(46).y], [lMarks.part(42).x,lMarks.part(47).y]], dtype=np.int32), (0, 255, 0)) #rightEye

    def drawOnFullEyeLMark(self, frame, lMarks):
        Utility.addPolygon(self.cv2, frame, np.array([[lMarks.part(36).x,lMarks.part(37).y], [lMarks.part(45).x,lMarks.part(44).y], [lMarks.part(45).x,lMarks.part(46).y], [lMarks.part(36).x,lMarks.part(40).y]], dtype=np.int32), (0, 255, 255)) #Full Eyes

    def drawOnNoseLMark(self, frame, lMarks):
        Utility.addPolygon(self.cv2, frame, np.array([[lMarks.part(31).x,lMarks.part(28).y], [lMarks.part(35).x,lMarks.part(28).y], [lMarks.part(35).x,lMarks.part(33).y], [lMarks.part(31).x,lMarks.part(33).y]], dtype=np.int32), (255, 0, 0)) #Nose

    def drawOnMouthLMark(self, frame, lMarks):
        Utility.addPolygon(self.cv2, frame, np.array([[lMarks.part(48).x,lMarks.part(50).y], [lMarks.part(54).x,lMarks.part(50).y], [lMarks.part(54).x,lMarks.part(57).y], [lMarks.part(48).x,lMarks.part(57).y]], dtype=np.int32), (255, 0, 0)) #Mouth
    
    @staticmethod
    def log(color, str):
        print(f"{color}{str}")