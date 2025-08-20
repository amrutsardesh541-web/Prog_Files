import cv2
import ultralytics

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter(r"C:\Users\Piyus\OneDrive\Desktop\Coding\Python\OpenCV\sample.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 20, (width, height))

while True:
    ret,frame = cap.read()
    cv2.imshow("frame",frame)
    writer.write(frame)

    if(cv2.waitKey(30) == 27):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()