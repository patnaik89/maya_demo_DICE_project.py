import maya.cmds as mc
import random
random.seed()
def UI():
     if mc.window('diceWindow', exists = True):
         mc.deleteUI('diceWindow')
     mc.window('diceWindow')
     mc.columnLayout()
     mc.intFieldGrp(label = 'Number of Dice', value1 = 1) )
     mc.button(label = 'Roll Die', command ='buttonpress()')
     mc.showWindow('diceWindow')
def buttonpress():
    numOfDice = mc.intFieldGrp('numOfDice', query = True, value1 = True)
    count = 0
    while count < numDice:      
  dieRoll = random.randint(1,6)
  print ('you rolled a 6 side die: ' + str(dieRoll))
  if dieRoll == 1 :
    mc.setAttr ('pCube1.rotateX', 0)
    mc.setAttr ('pCube1.rotateY', 0)
    mc.setAttr ('pCube1.rotateZ', 180)
if dieRoll == 2 :
    mc.setAttr ('pCube1.rotateX', 0)
    mc.setAttr ('pCube1.rotateY', 0)
    mc.setAttr ('pCube1.rotateZ', 270)
if dieRoll == 3 :
    mc.setAttr ('pCube1.rotateX', 90)
    mc.setAttr ('pCube1.rotateY', 0)
    mc.setAttr ('pCube1.rotateZ', 0)
if dieRoll == 4 :
    mc.setAttr ('pCube1.rotateX', 270)
    mc.setAttr ('pCube1.rotateY', 0)
    mc.setAttr ('pCube1.rotateZ', 0)
if dieRoll == 5 :
    mc.setAttr ('pCube1.rotateX', 0)
    mc.setAttr ('pCube1.rotateY', 0)
    mc.setAttr ('pCube1.rotateZ', 90)    
if dieRoll == 6 : 
    mc.setAttr ('pCube1.rotateX', 0)
    mc.setAttr ('pCube1.rotateY', 0)
    mc.setAttr ('pCube1.rotateZ', 0)
UI() 
