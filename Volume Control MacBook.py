#import dependencies
import cv2
import mediapipe as mp
from like import volume_up,volume_down
#Prepare the hand pose estimatation and open the camera
mp_hands=mp.solutions.hands
hands=mp_hands.Hands()
mp_draw=mp.solutions.drawing_utils
cap=cv2.VideoCapture(0)

#define the tips index
finger_tips=[8,12,16,20]
thumb_tip=4
#intialize state and timer 
thumbs_up=False
thumbs_down=False
volume_start_time=0
while True:
    #read from cam
    ret,img=cap.read()
    #flip image
    img=cv2.flip(img,1)
    h,w,c=img.shape
    #extract the results
    results=hands.process(img)
    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            #create list for each id and landmark
            lm_list=[]
            for id,lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)
            #check that the four tips are folded 
            finger_fold_status=[]
            if thumbs_up or thumbs_down:
                cv2.putText(img,' Processing',(15,60),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0))
            #left hand
            if (lm_list[2].x<lm_list[18].x):
                for tip in finger_tips:
                    x,y=int(lm_list[tip].x*w),int(lm_list[tip].y*h)
                    cv2.circle(img,(x,y),15,(255,0,0),cv2.FILLED)

                    if lm_list[tip].x<lm_list[tip-2].x:
                        cv2.circle(img,(x,y),15,(0,255,0),cv2.FILLED)
                        finger_fold_status.append(True)
                    else:
                        finger_fold_status.append(False)
                if all(finger_fold_status):                     
                    #check that the thumb is up
                    if  lm_list[thumb_tip].y<lm_list[thumb_tip-1].y<lm_list[thumb_tip-2].y<lm_list[12].y:
                        thumbs_up, volume_start_time = volume_up(thumbs_up,volume_start_time, img)
                    #check the thumb is down
                    if  lm_list[thumb_tip].y>lm_list[thumb_tip-1].y>lm_list[thumb_tip-2].y>lm_list[12].y:
                        thumbs_down, volume_start_time = volume_down(thumbs_down,volume_start_time, img)
                else :
                    #if the tips are not folded so the thumbs is not up or down
                    thumbs_up=False
                    thumbs_down=False
            #right hand            
            else:
                for tip in finger_tips:
                    x,y=int(lm_list[tip].x*w),int(lm_list[tip].y*h)
                    cv2.circle(img,(x,y),15,(255,0,0),cv2.FILLED)
                    if lm_list[tip].x>lm_list[tip-2].x:
                        cv2.circle(img,(x,y),15,(0,255,0),cv2.FILLED)
                        finger_fold_status.append(True)
                    else:
                        finger_fold_status.append(False)
                if all(finger_fold_status):
                    if  lm_list[thumb_tip].y<lm_list[thumb_tip-1].y<lm_list[thumb_tip-2].y<lm_list[12].y:
                        thumbs_up, volume_start_time = volume_up(thumbs_up, volume_start_time, img)
                    elif  lm_list[thumb_tip].y>lm_list[thumb_tip-1].y>lm_list[thumb_tip-2].y>lm_list[12].y:
                        thumbs_down, volume_start_time = volume_down(thumbs_down, volume_start_time, img)
                else:
                    thumbs_up=False
                    thumbs_down=False
            mp_draw.draw_landmarks(img,hand_landmark,
                                   mp_hands.HAND_CONNECTIONS,
                                   mp_draw.DrawingSpec((255,0,255),6,3),
                                   mp_draw.DrawingSpec((0,255,0),4,2)
                                   )      
    cv2.imshow('HAND',img)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release
cv2.destroyAllWindows()  
            