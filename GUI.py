from tkinter import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


gui =Tk()


#red led
redLed = 3
GPIO.setup(redLed,GPIO.OUT)
redLit = 1
#Blue led
GPIO.setup(5,GPIO.OUT)
blueLit = 1
# Yellow led
GPIO.setup(7,GPIO.OUT)
yellowLit =1





    
def clickExit():
    GPIO.cleanup()
    exit() 
    
def redtoggleLed():
    global redLit
    if redLit==1:
        GPIO.output(redLed,GPIO.LOW)
        redLit= 0
        
    else:
        GPIO.output(redLed,GPIO.HIGH)
        redLit=1
def yellowToggle():
    global yellowLit
    if yellowLit==1:
        GPIO.output(7,GPIO.LOW)
        yellowLit = 0
    else:
        GPIO.output(7,GPIO.HIGH)
        yellowLit =1

def blueToggle():
    global blueLit
    if blueLit ==1:
        GPIO.output(5,GPIO.LOW)
        blueLit=0
    else:
        GPIO.output(5,GPIO.HIGH)
        blueLit = 1

        



redledBtn = Button(gui, text = 'RED LED', command = redtoggleLed)

yellowLedBtn = Button(gui, text = 'YELLOW LED', command = yellowToggle)

blueLedBtn = Button(gui, text = 'BLUE LED', command = blueToggle)

exitBtn = Button(gui, text = 'EXIT', command = clickExit)



redledBtn.place(x=0,y=0)
yellowLedBtn.place(x=85,y=0)
blueLedBtn.place(x=195,y=0)
exitBtn.place(x=0,y=90)



 

gui.title("GUI")
gui.geometry("320x200")
gui.mainloop()
