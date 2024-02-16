# GaragePi
Why spend nominal amounts of money to call for help when your garage door won't accept remotes anymore. Now you can DIY for the small cost of hours of your time, and at a minimum of $50 on random parts. 

Hastily and poorly written garage automation. nginx frontend, fastapi backend. Basic geofence and token auth so randos can't just open your garage from where ever. It's not secure at all and anyone that really tried could probably open my garage.

Put your secret in the .token file, and your geofence loc in .geo_home. The front end will take a url param ?token=TOKEN. The js will ask for the geo location of your device, then add it &lat=$LAT&lng=lng. The fastapi reads these and compares them to the configured values. If they both match, the relay connected to the garage door will open. 

There is no documentation, code comments or support. I have 3 dogs so if someone does open my garage through this hastily crafted and hardly secure pile of garbage, at least I'd know. 


## kbd.py
Pair this remote to your pi w zero 2: https://www.amazon.com/dp/B084VTFS4X?psc=1&ref=ppx_yo2ov_dt_b_product_details

That remote creates /dev/input/event#. The kbd.py script can run as a service and will wait for the shutter button to be pressed and open up. Who needs rolling security codes when you can just replay attack a glorified bluetooth keyboard! It's mostly fine though, it's unlikely someone would be able to get into the pi and configure their own bluetooth device right?



