import cv2, dlib, os
from datetime import datetime
from Utility import Utility

class Image68Landmarks:
    def __init__(self, path = "", isFacebox = False, isLandmarks = False):
        self.isFacebox = isFacebox
        self.isLandmarks = isLandmarks
        self.utility = Utility(cv2)
        self.capture = cv2.imread(path)
        self.detector = dlib.get_frontal_face_detector() #Frontal detector using dlib
        self.predictor = dlib.shape_predictor("dat/shape_predictor_68_face_landmarks.dat") #Initilize 68 landmarks in faces
        self.drawLandmarks() #draw landmarks in faces

    def drawLandmarks(self):
        frame = self.capture
        gColor = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.detector(gColor) #Detect face using dat file predeictor
        for face in faces: #Loop all faces capture by detector
            if self.isFacebox: cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2) #Create rectangle box in face
            lMarks = self.predictor(gColor, face) #Get landmarks using predictor file in dlib
            if self.isLandmarks: 
                for i in range(0, 68): cv2.circle(frame, (lMarks.part(i).x, lMarks.part(i).y), 2, (255, 0, 0), -1) #Adding landmarks using circle  #Loop landmarks in face
            
            self.utility.drawOnFullEyeLMark(frame, lMarks)
            self.utility.drawOnLeftEyeLMark(frame, lMarks)
            self.utility.drawOnRightEyeLMark(frame, lMarks)
            self.utility.drawOnNoseLMark(frame, lMarks)
            self.utility.drawOnMouthLMark(frame, lMarks)
        cv2.imshow("Image 68 Landmarks", self.capture)
        path = os.path.dirname(os.path.realpath(__file__)) + "/exports/"+ (datetime.now().strftime("%d-%m-%Y-%H-%M-%S")) + ".jpg"
        cv2.imwrite(path, frame)
        print("Exported To: ", path)
        if(cv2.waitKey(1) == ord('q')): cv2.destroyAllWindows()