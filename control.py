from bge import logic, events, constraints
import random
import redis

from mathutils import Vector

# Ref: https://blender.stackexchange.com/questions/34439/blender-game-how-can-i-make-a-ball-roll-while-moving
#r = redis.Redis()
#pubsub = r.pubsub()
#pubsub.subscribe(['test'])
controller = logic.getCurrentController()
keyboard = logic.keyboard.events
owner = controller.owner
obj = logic.getCurrentScene().objects['Cube']
prop = obj['prop']

x,y = 0,0
n = 0.5
#if keyboard[events.UPARROWKEY]: x += n
#if keyboard[events.DOWNARROWKEY]: x -= n
#if keyboard[events.LEFTARROWKEY]: y += n
#if keyboard[events.RIGHTARROWKEY]: y -= n

foo = "up,down,up,up,left,left,right"
steps = foo.split(',')

print("Prop: %s" % prop)

#foo = pubsub.listen()
#obj['prop'] = random.choice(steps)
#obj['prop'] = foo

# Ref: https://stackoverflow.com/a/12073686

propx = "".join(map(chr, prop))
if propx == 'up':
    print('Prop is up')
    y += n
if propx == 'down':
    print('Prop is down')
    y -= n
if propx == 'left':
    print('Prop is left')
    x -= n
if propx == 'right':
    print('Prop is right')
    x += n
print("Prop is: %s***" % propx)

print('Applying movement: (%s,%s,0)' % (x,y))

vec = Vector((x,y,0))

# owner.applyTorque(vec)
owner.applyMovement(vec)
# owner.setLinearVelocity(vec)
# pysOwn = constraints.getCharacter(owner)
# pysOwn.walkDirection = vec

# To use:
# Create an Always sensor (keep at default setting)
# Create a Python controller, set to Module: control.subsub
# Connect the Always sensor to the new controller

# For the main script:
# Create an Always sensor with some time delay
# Create a Python controller, set as Script to control.py
# Connect the sensor to the controller

import threading
class rSub(threading.Thread):
    def __init__(self, prop):
        self.prop = prop
        self.r = redis.StrictRedis(host="localhost", port=6379, db=0)
        self.pubsub = self.r.pubsub()
        self.pubsub.subscribe(['test'])
        threading.Thread.__init__(self)
    
    def run(self):
        foo = self.pubsub.listen()
        for f in foo:
            print(f)
            obj['prop'] = f['data']

def subsub():
    rsub = rSub(obj['prop'])
    rsub.start()