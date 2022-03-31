import math
import random

#Pokemon Damage Calculator

#A Lv. 90 Charizard (Fire/Flying, Sp. Atk: 205) attacks a Lv. 95
#Feraligatr (Water, Sp. Def: 188) with Fire Blast, a Fire-type move
#with a Power of 110 and gains a same-type attack bonus.. It hits
#the target normally but deals a not very effective damage. The
#weather on the field is normal. Given the following conditions,
#determine how much damage Charizard’s attack will deal.

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
