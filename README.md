# Adafruit Python PCA9685 with ServoKit
Python code to use the PCA9685 PWM servo/LED controller with a Raspberry Pi or BeagleBone black using the ServoKit Python module.

## Installation

To install the library from source (recommended) run the following commands on a Raspberry Pi or other Debian-based OS system:

    sudo apt-get install git build-essential python-dev
    cd ~
    git clone https://github.com/victorberruga/Adafruit_Python_PCA9685_with_ServoKit.git
    cd Adafruit_Python_PCA9685
    sudo python setup.py install
    sudo pip install adafruit-circuitpython-servokit

Alternatively you can install from pip with:

    sudo pip install adafruit-pca9685

Note that the pip install method **won't** install the example code.
