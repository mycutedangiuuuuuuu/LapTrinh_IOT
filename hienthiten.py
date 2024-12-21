from sense_emu import SenseHat
import time
sense = SenseHat()
x=[255,0,0]
o=[0,0,0]
m=[
    x,x,o,o,o,o,o,x,
    x,o,x,o,o,o,x,x,
    x,o,o,x,x,x,o,x,
    x,o,o,x,x,o,o,x,
    x,o,o,x,x,o,o,x,
    x,o,o,x,x,o,o,x,
    x,o,o,x,x,o,o,x,
    x,o,o,x,x,o,o,x,
]

sense.set_pixels(m)

nhietdo =sense.temperature
doam =sense.humidity

print ("nhiet do :",nhietdo)
print ("do am :",doam)




    
    
