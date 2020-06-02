from __future__ import division
import Adafruit_PCA9685
from adafruit_servokit import ServoKit
import adafruit_motor.servo
import time

pca = Adafruit_PCA9685.PCA9685()

kit = ServoKit(channels=16)

servo_0 = kit.servo[0]  # base joint (MG996R)
servo_1 = kit.servo[1]  # shoulder joint (MG996R)
servo_2 = kit.servo[2]  # elbow joint (MG996R)
servo_3 = kit.servo[3]  # wrist longitudinal rotation (MG996R)
servo_4 = kit.servo[4]  # wrist perpendicular rotation (MG90S)
servo_5 = kit.servo[5]  # gripper (MG90S)
servo_list = [servo_0, servo_1, servo_2, servo_3, servo_4, servo_5]

"""Test ranges for the all servos"""
pca.frequency = 50
servo_0.actuation_range = 180
servo_0.set_pulse_width_range(800, 2600)

servo_1.actuation_range = 90  # 180 by default already. This is to change the sweep of the motor
servo_1.set_pulse_width_range(800, 1500)  # the pulse width range dictates the actuation range: (min, max) angles

servo_2.actuation_range = 135
servo_2.set_pulse_width_range(800, 2200)

servo_3.actuation_range = 180
servo_3.set_pulse_width_range(800, 2600)

servo_4.actuation_range = 180
servo_4.set_pulse_width_range(800, 2400)

servo_5.actuation_range = 100
servo_5.set_pulse_width_range(800, 1500)


# Function to smooth the shoulder servo suffering from heavy load
def smooth_sm(sm, degree):  # sm - servo motor, degree - degree to move to
    if degree > sm.angle:
        while degree > sm.angle and (degree - sm.angle) >= 5:
            sm.angle = sm.angle + 5
            print(sm.angle)
            time.sleep(0.5)
        else:
            sm.angle = degree
            print(sm.angle)
            time.sleep(0.5)
    else:
        while degree < sm.angle and (sm.angle - degree) >= 5:
            sm.angle = sm.angle - 5
            print(sm.angle)
            time.sleep(0.5)
        else:
            sm.angle = degree
            print(sm.angle)
            time.sleep(0.5)


# Home sequence of all joints
servo_0.angle = 90
servo_1.angle = 90
servo_2.angle = 100
servo_3.angle = 0
servo_4.angle = 90
time.sleep(1)
servo_5.angle = 100
time.sleep(1)
servo_5.angle = 0
time.sleep(1)

servo_0.angle = 15
time.sleep(0.5)
servo_2.angle = 120
time.sleep(0.5)
servo_1.angle = 45
time.sleep(0.5)
servo_4.angle = 30
servo_3.angle = 75
time.sleep(1)
servo_5.angle = 100
time.sleep(1)
smooth_sm(servo_1, 0)
servo_5.angle = 0
time.sleep(2)

servo_0.angle = 90
servo_1.angle = 90
servo_2.angle = 100
servo_3.angle = 0
servo_4.angle = 90
time.sleep(1)
