import RPi.GPIO as GPIO
from time import sleep 

 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(11, GPIO.OUT) 
GPIO.setup(13, GPIO.OUT) 
GPIO.setup(16, GPIO.OUT) 
GPIO.setup(18, GPIO.OUT) 

 
GPIO.setup(22, GPIO.IN) 

 
def sensorchekup(): 
       
      counter==0 
       
      while counter <5: 
             
             sensor=GPIO.input(22) 
           
             if sensor==1:
                print("cant see anything") 
                  print("keep her goooinnn") 
                  sensorcheckup() 
                   
             elif sensor==0: 
                  print("i see sum theng") 
                  GPIO.output(11, GPIO.LOW) 
                 GPIO.output(16, GPIO.LOW) 
                   
             elif counter==5: 
                 break 
                  
             counter = counter + 1 

 
 while True: 
        
         chuckles=input("Type control. Im using WASD") 
        
        if chuckles == "w":                  #forward 
             GPIO.output(11, GPIO.HIGH) 
             ssensorcheckup() 
             GPIO.output(11, GPIO.LOW) 
 
 
        elif chuckles == "s":                #reverse 
            GPIO.output(13, GPIO.HIGH) 
            sensorcheckup() 
            GPIO.output(13, GPIO.LOW) 

 
        elif chuckles == "a":                #steers left 
            GPIO.output(16, GPIO.HIGH)
            sensorcheckup() 
            GPIO.output(16, GPIO.LOW) 
             

        elif chuckles == "d":                #steers right 
            GPIO.output(18, GPIO.HIGH) 
            sensorcheckup() 
            GPIO.output(18, GPIO.LOW)

        elif chuckles == "x":
            GPIO.cleanup()
            print("Good bye 0111011001010010101010101011110001000100101")
            print("srever error 100010101101011010101011")
            sleep(1)
            break

