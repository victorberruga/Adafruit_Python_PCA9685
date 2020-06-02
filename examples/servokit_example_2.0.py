from __future__ import division
import Adafruit_PCA9685
from adafruit_servokit import ServoKit
import adafruit_motor.servo
import time

pca = Adafruit_PCA9685.PCA9685()

kit = ServoKit(channels=16)
# I do not know what this is for, but it works without it
# servo = adafruit_motor.servo.Servo(0)

servo_0 = kit.servo[0]
servo_1 = kit.servo[1]

pca.frequency = 50
servo_0.actuation_range = 180  # 180 by default already. This is to change the sweep of the motor
servo_0.set_pulse_width_range(800, 2500)

servo_1.actuation_range = 180
servo_1.set_pulse_width_range(800, 2600)
# Move servo channel 0 and channel 1 from 180 to 0
while True:
    servo_0.angle = 180
    time.sleep(1)
    servo_0.angle = 0
    time.sleep(1)

    servo_1.angle = 180
    time.sleep(1)
    servo_1.angle = 0
    time.sleep(1)
