# hydro
Hydroponic Control System

Protected by MIT Licence. 
Copyright (C) Steven Williams 2017


# Relay Control
This is a simple relay control system for a Raspberry Pi. 
Currently configured for 8 relays (8 GPIO pins). One pin per relay. 
Default Pin Configuration:
- Relay 1: BCM Pin 17 (Board Pin 11)
- Relay 2: BCM Pin 27 (Board Pin 13)
- Relay 3: BCM Pin 22 (Board Pin 15)
- Relay 4: BCM Pin 23 (Board Pin 16)
- Relay 5: BCM Pin 24 (Board Pin 17)
- Relay 6: BCM Pin 25 (Board Pin 22)
- Relay 7: BCM Pin 5 (Board Pin 29)
- Relay 8: BCM Pin 6 (Board Pin 31)

`timers.csv` can be updated without turning off the program.
Delay times of 2 or more relays running simultaneously must be the same. 
TODO: Update program to handle various time delays.



Layout: `Relay number,24hr time,delay (seconds)`
>Example 1: Set Relay 1 to run at 10:00am for 5 minutes (300 seconds): In timers.csv: `1,10:00,300`

>Example 2: Set Relay 5 to run at 20:00 (8pm) for 1 minute 30 seconds: In timers.csv: `5,20:00,90`

