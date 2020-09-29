from time import sleep
import RPi.GPIO as GPIO

from twilio.rest import Client
from datetime import datetime
 
account_sid = 'AC43646f3e357755789789ac41e31f01fd'
auth_token = 'f530094a999a70697a587b12c0e03360'
client = Client(account_sid,auth_token)
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

LedOut = 18
Flamein = 21

#Switch Pin
GPIO.setup(Flamein, GPIO.IN)

#Switch Led
GPIO.setup(LedOut, GPIO.OUT)
count = 0

while True:
    try:
        if (GPIO.input(21) == False):
            #DateTime Updation setup
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Fire in your house at= ",current_time)
            
            messgae = client.messages.create(body='Fire at Your House',
                                            from_= 'whatsapp:+14155238886',
                                            to ='whatsapp:+919082064984')


            GPIO.output(LedOut, 1)
            sleep(0.1)
            GPIO.output(LedOut, 0)
            sleep(0.1)
            GPIO.output(LedOut, 1)
            
         
        else:
            
            GPIO.output(LedOut, 0)
         
    except KeyboardInterrupt:
        exit()
GPIO.cleanup()



