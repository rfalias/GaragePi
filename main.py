from fastapi import FastAPI, Request, HTTPException
import relay
from fastapi.middleware.cors import CORSMiddleware
from starlette.concurrency import run_in_threadpool
import logging
import time
import geofence

app = FastAPI()

origins = [
    "https://yoursite.com:8000",
    "https://yoursite.com",
    "http://yoursite.com",
    "http://yoursite.com:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import os
import glob
import time
import json
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

def read_token():
    try:
        with open('.token', 'r') as f:
            t = str(f.read().strip())
            logging.warning(f"Got token {t} from file")
            return t
    except Exception as e:
        logging.error(f"Could not read token {e}")
        return False

def get_pin_status():
    return GPIO.input(8)

def toggle_pin(token, loc):
    if not isAllowed(token, loc):
        logging.warning(f"Invalid token {token} or GPS, request denied")
        return False 
    relay.relay_on()
    time.sleep(1)
    relay.relay_off()
    logging.info(f"Toggled Relay")
    return {"data":f"Request Accepted, Toggled Relay"}
        
def throw401():
  raise HTTPException(status_code=401, detail="Unauthorized")

def isAllowed(token, loc):
    inrange = geofence.isInRange(loc, 2)
    logging.warning(f"Testing {vars(loc)} against geofence. In range? {inrange}")
    if not inrange:
      throw401()     
    rt = read_token()
    if token != rt:
        logging.warning(f"Supplied token '{token}' did not match '{rt}'")
        throw401()
    return True

@app.get("/garage/toggle")
async def toggle(token: str, lat: str, lng: str, request: Request):
    logging.info(f"/garage/toggle called, token: {token} {lat} {lng}")
    loc = geofence.location()
    loc.lat = lat
    loc.lng = lng
    return await run_in_threadpool(toggle_pin, token, loc)

