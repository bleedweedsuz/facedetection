import cv2, dlib, os
from datetime import datetime
from Utility import Utility

class Image68Landmarks:
    def __init__(self, path = "", outputPath = "", exportFBCapture = False, isFacebox = False, isLandmarks = False, imShow = False, leftEye =False, rightEye=False, bothEye=False, nose=False, mouth=False):
        self.isFacebox = isFacebox
        self.isLandmarks = isLandmarks
        self.imShow = imShow
        self.outputPath = outputPath

        self.leftEye = leftEye
        self.rightEye = rightEye
        self.bothEye = bothEye
        self.nose = nose
        self.mouth = mouth

        self.exportFBCapture = exportFBCapture

        self.utility = Utility(cv2)
        self.capture = cv2.imread(path)
        self.detector = dlib.get_frontal_face_detector() #Frontal detector using dlib
        self.predictor = dlib.shape_predictor("dat/shape_predictor_68_face_landmarks.dat") #Initilize 68 landmarks in faces
        self.drawLandmarks() #draw landmarks in faces

    def drawLandmarks(self):
        print("Strted ", datetime.now().strftime("%d-%m-%Y-%H-%M-%S-%f"))

        if(self.outputPath != ""): path = self.outputPath # + (datetime.now().strftime("%d-%m-%Y-%H-%M-%S-%f")) + ".jpg"
        else: path = os.path.dirname(os.path.realpath(__file__)) + "/exports/"# + (datetime.now().strftime("%d-%m-%Y-%H-%M-%S-%f")) + ".jpg"

        frame = self.capture
        gColor = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.detector(gColor) #Detect face using dat file predeictor
        for face in faces: #Loop all faces capture by detector
            if self.isFacebox: cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2) #Create rectangle box in face

            if(self.exportFBCapture):
                fBoxExport = path + "_Fbox_" + (datetime.now().strftime("%d-%m-%Y-%H-%M-%S-%f")) + ".jpg"
                exportImage = frame.copy()
                exportImage = exportImage[face.top():face.bottom(), face.left():face.right()] #Crop image
                cv2.imwrite(fBoxExport, exportImage)
                print("Facebox exported: " + fBoxExport)

            lMarks = self.predictor(gColor, face) #Get landmarks using predictor file in dlib
            if self.isLandmarks: 
                for i in range(0, 68): cv2.circle(frame, (lMarks.part(i).x, lMarks.part(i).y), 2, (255, 0, 0), -1) #Adding landmarks using circle  #Loop landmarks in face
            
            if self.bothEye: self.utility.drawOnFullEyeLMark(frame, lMarks)
            if self.leftEye: self.utility.drawOnLeftEyeLMark(frame, lMarks)
            if self.rightEye: self.utility.drawOnRightEyeLMark(frame, lMarks)
            if self.nose: self.utility.drawOnNoseLMark(frame, lMarks)
            if self.mouth: self.utility.drawOnMouthLMark(frame, lMarks)

            

        if self.imShow: cv2.imshow("Image 68 Landmarks", self.capture)
        exportLocation = path + (datetime.now().strftime("%d-%m-%Y-%H-%M-%S-%f")) + ".jpg"
        cv2.imwrite(exportLocation, frame)
        print("End ", datetime.now().strftime("%d-%m-%Y-%H-%M-%S-%f"))
        print("Exported To: ", exportLocation)
        if self.imShow: 
            if(cv2.waitKey(1) == ord('q')): cv2.destroyAllWindows()