import bge

def main():

    cont = bge.logic.getCurrentController()
    own = cont.owner

    mouse = cont.sensors['Mouse']
    fire = cont.sensors['Fire']
    turn = cont.actuators['Turn']
    shoot = cont.actuators['Shoot']

    if mouse.positive:
        print("mouse.positive!")
        cont.activate(shoot)
    else:
        cont.deactivate(fire)
    
    #for i in range(10):
    #    cont.activate(fire)

print("Foo!")
main()
