import cv2
import dropbox

def take_snapshot():
    # initializing cv2
    videocaptureobject = cv2.VideoCapture(0)
    result=True
    while(result):
        #read the frames while the camera is on.
        ret,frame=videocaptureobject.read()
        print(ret)

        cv2.imwrite("xyz.jpg",frame)
        #cv2.imwrite():-meathod is used to store an image into given path
        result=False

    videocaptureobject.release() 
    #release the camera
    cv2.destroyAllWindows()

take_snapshot()
