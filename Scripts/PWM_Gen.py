'''

Control the Brightness of LED using PWM on Raspberry Pi

http://www.electronicwings.com

'''



import RPi.GPIO as GPIO

from time import sleep



ledpin = 12				# PWM pin connected to LED

pin_number = 32

GPIO.setwarnings(False)			#disable warnings

GPIO.setmode(GPIO.BOARD)		#set pin numbering system

GPIO.setup(pin_number,GPIO.OUT)

pi_pwm = GPIO.PWM(pin_number,1000)		#create PWM instance with frequency

pi_pwm.start(0)				#start PWM of required Duty Cycle 



for duty in range(0,50,1):

    pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100

    sleep(0.01)

sleep(0.5)


pi_pwm.ChangeDutyCycle(100)
sleep(10)
'''

    for duty in range(50,-1,-1):

        pi_pwm.ChangeDutyCycle(duty)

        sleep(0.01)

    sleep(0.5)
'''
