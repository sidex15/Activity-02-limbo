import math
import random

i=1
while i <11:
    pokemon = {
    "lvl":90,
    "atk":205,
    "def":188,
    "pow":110
}

    poke_modif = {
    "tgt":1,
    "wthr":1,
    "bdge":1,
    "crit":1,
    "rnd":random.randint(85,100)/100,
    "stab":1.5,
    "type":0.5,
    "burn":1,
    "misc":1
}
    modifier = math.prod(poke_modif.values())
    dmg = ((((((2*pokemon["lvl"])/5)+2)*pokemon["pow"]*pokemon["atk"]/pokemon["def"])/50)+2)*modifier
    print (round(dmg,2))
    i+=1
