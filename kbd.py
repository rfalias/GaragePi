from evdev import InputDevice, categorize, ecodes
import logging
import relay

def doWaitButton():
    ABShutter3 = InputDevice('/dev/input/event1')
    logging.warning(ABShutter3)

    EV_VAL_PRESSED = 1
    EV_VAL_RELEASED = 0
    BTN_SHUTTER = 115
    logging.warning(f"Connected, awaiting buttons")
    for event in ABShutter3.read_loop():
        logging.warning(f"{event}")
        if event.type == ecodes.EV_KEY:
            if event.value == EV_VAL_PRESSED:
                if event.code == BTN_SHUTTER:
                    logging.warning('---')
                    logging.warning('Shutter3 pressed')
                    logging.warning(event)
                    relay.relay_on()
                    time.sleep(1)
                    relay.relay_off()
import time
while True:
    try:
        doWaitButton()
    except Exception as e:
        time.sleep(.5)
