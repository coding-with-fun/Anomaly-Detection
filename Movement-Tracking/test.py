import cv2
import numpy as np
def main():
    cnt = 0
    while 1:
        # window_name="Cam feed"
        # cv2.namedWindow(window_name)
        # cap=cv2.VideoCapture(0)
        
        # Captures video "testVideo.mp4"
        # cap=cv2.VideoCapture("testVideo.mp4")
        
        # Captures video of camera
        cap=cv2.VideoCapture(0)

        # filename = 'sample.avi'
        # codec=cv2.VideoWriter_fourcc('X','V','I','D')
        # framerate=30
        # resolution = (500,500)

        # VideoFileOutput = cv2.VideoWriter(filename,codec,framerate,resolution)

        
        if cap.isOpened():
            ret,frame = cap.read()

        else:
            ret =False


        ret,frame1 = cap.read()
        ret,frame2 = cap.read()

        while ret:
            ret,frame = cap.read()
            # VideoFileOutput.write(frame2)

            d=cv2.absdiff(frame1,frame2)

            grey=cv2.cvtColor(d,cv2.COLOR_BGR2GRAY)

            blur =cv2.GaussianBlur(grey,(5,5),0)
            ret,th=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
            dilated=cv2.dilate(th,np.ones((3,3),np.uint8),iterations=4)
            img,c,h=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            
            for contour in c:
                (x, y, w, h) = cv2.boundingRect(contour)
                # Set the sensitivity
                if cv2.contourArea(contour) < 2000:
                    continue
                # cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.drawContours(frame1,c,-1,(0,255,0),2)
                cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                

            # cv2.imshow("win1",frame2)
            cv2.imshow("inter",frame1)
            
            if cv2.waitKey(40) == 27:
                cnt = 1
                break
            frame1 = frame2
            ret,frame2= cap.read()
        cv2.destroyAllWindows()
        # VideoFileOutput.release()
        cap.release()
    
        if cnt == 1:
            break
main()   
