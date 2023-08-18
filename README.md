# ControlMacbookSound-with-HandGestures
You can control your macbook sound with your hand !!!<br/>


#How To Use <br/>
Run the Volume Control Macbook.py File
if you made thumbs up every 1 sec the volume will increase 10%<br/>
if you made thumbs down every 1 sec the volume will decrease 10%<br/>

#Explaination<br/>

1- Using mediapipeline library that help to detect hands annotations and draw lines between the  index points<br/>

2-Iterate over each frame and check that the all tips except thumb tip are folded <br/>

3- Check that the thumb is up , if True function 'volume_up' from 'like.py' will create a timer that count time for thumbs up and every 1 sec if it stays up it will  apply a script to increase the volume 10%<br/>

4- Check that the thumb is down , if True function 'volume_down' from 'like.py' will create a timer that count time for thumbs down and every 1 sec if it stays down it will  apply a script to decrease the volume 10%<br/>

5-Apply on both right and left hands<br/>



