#!/usr/bin/env python3
########################################################################
# Filename    : Blink.py
# Description : Basic usage of GPIO. Let led blink.
# auther      : www.freenove.com
# modification: 2019/12/28
########################################################################
import RPi.GPIO as GPIO
import time

ledPin = 11    # define ledPin


def setup():
    GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(ledPin, GPIO.LOW)  # make ledPin output LOW level
    print('using pin%d' % ledPin)


def loop():
    while True:
        # make ledPin output HIGH level to turn on led
        GPIO.output(ledPin, GPIO.HIGH)
        print('led turned on >>>')     # print information on terminal
        time.sleep(1)                   # Wait for 1 second
        # make ledPin output LOW level to turn off led
        GPIO.output(ledPin, GPIO.LOW)
        print('led turned off <<<')
        time.sleep(1)                   # Wait for 1 second


def destroy():
    GPIO.cleanup()                      # Release all GPIO


if __name__ == '__main__':    # Program entrance
    print('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()


# ランプの点滅システム
# 実行完了
