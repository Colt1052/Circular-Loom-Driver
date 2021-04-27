import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider

from PyQt5.QtCore import Qt

import RPi.GPIO as GPIO

from time import sleep

ledpin = 12

pin_number = 32

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin_number,GPIO.OUT)

pi_pwm = GPIO.PWM(pin_number,1000)

pi_pwm.start(0)

class Example(QMainWindow):



    def __init__(self):

        super().__init__()




        mySlider = QSlider(Qt.Horizontal, self)

        mySlider.setGeometry(30, 40, 200, 30)

        mySlider.valueChanged[int].connect(self.changeValue)



        self.setGeometry(50,50,320,200)

        self.setWindowTitle("Checkbox Example")

        self.show()



    def changeValue(self, value):

        print(value)
        pi_pwm.ChangeDutyCycle(value)



if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())
