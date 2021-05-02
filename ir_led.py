import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(14,IO.IN) #GPIO 14 -> IR sensor as input
while 1:
    #time.sleep(0.2)
    if(IO.input(14)==True):
        print("object Detected")
    
    #else:
        #print("No Obstacle Detected")
        
