## 68 Land marks Face detection
Face detection system using OpenCV. Two modes available face detection in image and real time video capture. Also available face box, landmarks in frames.

### Requirements:
OS: Windows 10
1. numpy=1.21.1
    ```
    pip install numpy
    ```
2. opencv-python=4.5.3.56
    ```
    pip install opencv-python
    ```
3. cmake=3.21.0 (Before installing dlib make sure you install "cmake")
    ```
    pip install cmake
    ```
4. wheel  (Before installing dlib make sure you install "wheel")
    ```
    pip install wheel
    ```
5. Install latest visual studio build tools: [Visual Studio](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&rel=15)
4. dlib=19.22.0
    ```
    pip install dlib
    ```

## Features
1. Realtime video capture face detection
2. Local image face detection
3. Extract faces from local image


### Example
```
python app.py

*******REAL TIME MODE******
Select Modes: 
1. Realtime Video Capture (Camera)= '1' or 'r' or 'R' 
2. Static Image= '2' or 's' or 'S'
3. Quit= '3' or 'q' or 'Q'
Enter Mode:1
Enter Realtime Parameters:    
Enter screen width (integer): 800
Enter screen height (integer): 800
Enable Facebox (y/n): y
Enable Landmarks (y/n): y
Use 'q' to quit the frame.


*******LOCAL FILE******
Select Modes: 
1. Realtime Video Capture (Camera)= '1' or 'r' or 'R'
2. Static Image= '2' or 's' or 'S'
3. Quit= '3' or 'q' or 'Q'
Enter Mode:2
Enter Static Parameters:
Enter image path (d:/img/xyz.jpg): d:/reference_1.jpg
Enable Facebox (y/n): y
Enable Shapes (y/n): y
Export facebox capture (y/n): y
Enable Landmarks (y/n): y
Use 'q' to quit the frame.
Strted  27-07-2021-22-59-25-398762
End  27-07-2021-22-59-25-446707
Exported To:  D:\exports/27-07-2021-22-59-25-436702.jpg
```
*Note for local file use potrait image of person for better result.

### Example Image (Local image used)
Note: Credit Image: https://unsplash.com/  License: https://unsplash.com/license
