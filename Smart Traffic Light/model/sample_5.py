import torch
from IPython.display import display, clear_output
import cv2
from PIL import Image
import time
import serial


model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

ser = serial.Serial('COM4', 9600)  # Adjust port and baud rate as needed
# ser = serial.Serial('/dev/cu.usbserial-10', 9600) 

cl = "person"
# define a video capture object 
phn1 = "http://10.103.223.49:4747/video"
phn2 = "http://10.103.121.121:4747/video"

# Create a VideoCapture object
cap1 = cv2.VideoCapture(phn1)
cap2 = cv2.VideoCapture(phn2)

# Check if the camera is opened successfully
if not cap1.isOpened():
    print("Error: Could not open camera1.")
    exit()
if not cap2.isOpened():
    print("Error: Could not open camera2.")
    exit()
counterA=0
counterB=0
# Read and display frames from the camera
st = time.time()
while True:

    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    if not ret1:
        print("Error: Failed to receive frame1.")
        break
    if not ret2:
        print("Error: Failed to receive frame2.")
        break

    if time.time()-st >= 5:

        result1 = model(frame1)
        result2 = model(frame2)

        # Check if "person" is in detection results
        if cl in str(result1):
            traffic1 = str(result1)[(str(result1).index(cl)-2)]
        else:
            traffic1 = '0'  # No person detected

        if cl in str(result2):
            traffic2 = str(result2)[(str(result2).index(cl)-2)]
        else:
            traffic2 = '0'  # No person detected

        traffic = [traffic1, traffic2]
        print(traffic)
        if(max(traffic)=="0"):
            command = f"{-1}\n"
            print(command)
            ser.write(command.encode())
            counterA=0
            counterB=0
            
        elif traffic.index(max(traffic)) == 0 :
            if(counterA>3) and traffic2!="0":
                command = f"{2}\n"
                print(command)
                ser.write(command.encode())
                counterB+=1
                counterA=0
            else:
                command = f"{1}\n"
                print(command)
                ser.write(command.encode())
                counterB=0
                counterA+=1

        elif traffic.index(max(traffic)) == 1:
            if(counterB>3) and traffic1!="0":
                command = f"{1}\n"
                print(command)
                ser.write(command.encode())
                counterA+=1
                counterB=0
            else:
                command = f"{2}\n"
                print(command)
                ser.write(command.encode())
                counterA=0
                counterB+=1

        st = time.time()

    # Display the frame
    cv2.imshow('DroidCam Feed1', frame1)
    cv2.imshow('DroidCam Feed2', frame2)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all OpenCV windows
cap1.release()
cap2.release()
cv2.destroyAllWindows()