#!/usr/bin/python2

from time import sleep
import RPi.GPIO as GPIO

class pinstart():
	def __init__(self,pinnumber):
		self.pin = pinnumber
		GPIO.setup(self.pin, GPIO.OUT)

	def pinoff(self):
		GPIO.output(self.pin, False)

	def pinon(self):
		GPIO.output(self.pin, True)

	def getpinvalue(self):
		print GPIO.input(self.pin)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pin1 = pinstart(21)
pin2 = pinstart(17)
pin3 = pinstart(18)

while 1:
	pin1.pinon()
	sleep(0.05)
	pin1.pinoff()
	sleep(0.05)
	pin2.pinon()
	sleep(0.05)
	pin2.pinoff()
	sleep(0.05)
	pin3.pinon()
	sleep(0.05)
	pin3.pinoff()
	sleep(0.05)
	pin2.pinon()
	sleep(0.05)
	pin2.pinoff()
	sleep(0.05)

GPIO.cleanup()
