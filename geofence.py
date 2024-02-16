from geopy import distance
import logging
import json
class location:
    lat = ""
    lng = ""

def get_home():
    try:
        with open('.geo_home', 'r') as f:
           loc = location()
           cord = json.loads(f.read())
           loc.lat = cord["lat"]
           loc.lng = cord["lng"]
           return loc
    except Exception as e:
        logging.error(f"Couldn't retrieve home coordinates from .geo_home {e}")
           

def isInRange(loc, radius):
  center_point = get_home()
  radius = radius # in kilometer
  try:
      float(loc.lat)
      float(loc.lng)
  except Exception as e:
      logging.error(f"Could not parse coordinates {vars(loc)} {e}")
      return False
  dis = distance.distance((center_point.lat,center_point.lng), (loc.lat, loc.lng)).km
  logging.error("Distance: {}".format(dis)) # Distance: 0.0628380925748918
  
  if dis <= radius:
      logging.warning(f"{vars(loc)} point is {dis} from the inside of the {radius} km radius from {vars(center_point)} coordinate")
      return True
  else:
      logging.warning(f"{vars(loc)} point is {dis} from the inside of the {radius} km radius from {vars(center_point)} coordinate")
      return False

