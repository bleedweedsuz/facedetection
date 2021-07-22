from Realtime68Landmarks import Realtime68Landmarks
from Image68Landmarks import Image68Landmarks
from AName import app_name

class UI:
    def initUI(self):
        print(app_name)
        while True:
            print("Select Modes: \n1. Realtime Video Capture (Camera)= '1' or 'r' or 'R' \n2. Static Image= '2' or 's' or 'S'\n3. Quit= '3' or 'q' or 'Q'")
            mode = input("Enter Mode:")
            if(mode == "r" or mode == "R" or mode == "1"):
                self.realTimeInit()
            elif(mode == "s" or mode == "S" or mode == "2"):
                self.staticImage()
            elif(mode == "q" or mode == "Q" or mode == "3"):
                break
            
    def realTimeInit(self):
        try:
            print("Enter Realtime Parameters:")
            width = int(input("Enter screen width (integer): ").strip())
            height = int(input("Enter screen height (integer): ").strip())
            isFacebox = (input("Enable Facebox (y/n): ").strip()=="y")
            isLandmarks = (input("Enable Landmarks (integer) (y/n): ").strip()=="y")
            print("Use 'q' to quit the frame.")
            Realtime68Landmarks(width, height, isFacebox, isLandmarks)
        except:
            print("Something goes wrong..")

    def staticImage(self):
        try:
            print("Enter Static Parameters:")
            path = input("Enter image path (d:/img/xyz.jpg): ").strip()
            isFacebox = (input("Enable Facebox (y/n): ").strip()=="y")
            isLandmarks = (input("Enable Landmarks (integer) (y/n): ").strip()=="y")
            print("Use 'q' to quit the frame.")
            Image68Landmarks(path, isFacebox, isLandmarks)
        except:
            print("Something goes wrong..")