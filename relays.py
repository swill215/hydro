"""
Hydro: Relay Control Program - Version 1
Timer control based on RasPi Clock.

Times are preset in "timers.csv" file. 
Follow Github link for how to set times in the CSV. 

Protected by MIT Licence. Copyright (C) Steven Williams 2017
https://github.com/swill215/hydro
"""

import RPi.GPIO as GPIO
import csv
from time import strftime, sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

# Solenoid number: GPIO pin number
PINS = {'1': 17, '2': 27, '3': 22, '4': 23, '5': 24, '6': 25, '7': 5, '8': 6}


def main():
    print("Solenoid Timer program. Version 0.1")
    relaytimer()


# Read csv files
def readfile(filename):
    with open(filename) as file:
        file_reader = csv.reader(file)
        data = [row for row in file_reader]
    file.close()
    return data


# Based on time, run solenoids.
def relaytimer():
    # Infinite loop
    while True:
        timers = readfile("timers.csv")
        valves = []
        delays = []
        pins = []
        # Check if clock time is the same as timers.csv
        current_time = strftime('%H:%M')
        for set_time in timers:
            # Run if the time is correct
            if str(current_time) == str(set_time[1]):
                for keys, values in PINS.items():
                    if keys == set_time[0]:
                        valves.append(values)
                        delays.append(set_time[2])
                        pins.append(keys)
        if len(valves) > 0:
            runGPIO(valves, delays, pins)
        # Reset program
        print("{} {} - Sleeping for 30 seconds".format(strftime("%x"), strftime("%X")))
        sleep(30)


# Run Relays based on pins set above on RPi.GPIO
# Command RPi pins
def runGPIO(valves, delays, pins):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(valves, GPIO.OUT)
    GPIO.output(valves, GPIO.HIGH)
    print("{} {} - Valves {} are running for {}".format(strftime("%x"), strftime("%X"), pins, delays[0]))
    sleep(int(delays[0]))
    GPIO.output(valves, GPIO.LOW)
    GPIO.cleanup()


main()
