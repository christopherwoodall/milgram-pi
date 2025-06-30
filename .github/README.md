# Milgram-Pi
Proxy local MCP calls to a Raspberry Pi in order to control a relay module.

## Bill of Materials
- Raspberry Pi
- Relay Module

## Getting Started

![](docs/sequence_diagram.jpg)

Flash the Raspberry Pi with the OS of your choice and enable SSH. Follow the pinout and wiring guide to connect the Raspberry Pi and the relay module. After that run the following commands to install the required libraries and run the scripts.


### On the Host

```
git clone https://github.com/christopherwoodall/milgram-pi.git
cd milgram-pi
pip install -e .

mcp dev src/server.py
```

### On the Pi
```
git clone https://github.com/christopherwoodall/milgram-pi.git
cd milgram-pi
pip install -e .

MILGRAM_MODE=remote milgram-pi
```


## Wiring Guide

Begin by slicing the black wire from a TENS unit connector about 4" from the end. Strip the ends of the wire to expose the copper.

![](docs/step1.jpg)


Next, connect the black wire from the TENS unit connector to the plug labeled Common (COM) on the relay module. Connect the other end to the plug labeled Normally Open (NO).

![](docs/step2.jpg)


Shoutout Google Lens (make sure to get the right relay).

![](docs/lens.jpg)


Wire the VCC and GND pins to the Raspberry Pi's 5V and GND pins, respectively. Finally, connect the IN pin to GPIO 21 on the Raspberry Pi.

![](docs/final.jpg)


## Acknowledgements
Inspired by Tim Keeley's [shockbot](https://www.instructables.com/Shockbot/) project.
