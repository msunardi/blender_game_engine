from bge import logic

def Player():
    cont = logic.getCurrentController()
    obj = cont.owner
    print("Hello - I'm at ", obj.position)