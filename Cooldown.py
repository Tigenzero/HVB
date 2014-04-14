class Cooldown:
    cure = 0
    overcharge = 0
    h_potion = 0
    m_potion = 0
    s_potion = 0
    regen = 0
    protection = 0
    shield_bash = 0
    shockblast = 0
    collection = [cure, overcharge, h_potion, m_potion, s_potion, regen, protection]
    premium = [0, 0]
    special_attack = [0, 0, 0]

def reduceCooldown():
    #for i in range(0, len(Cooldown.collection)):
    #Cooldown.collection[i] = Cooldown.collection[i] -1 Does not update Values
    Cooldown.cure -= 1
    Cooldown.overcharge -= 1
    Cooldown.h_potion -= 1
    Cooldown.m_potion -= 1
    Cooldown.s_potion -= 1
    Cooldown.protection -= 1
    Cooldown.regen -= 1
    Cooldown.shield_bash -= 1
    Cooldown.shockblast -= 1
    #if Cooldown.shield_bash == 0:
        #print "shield bash now active"
    Cooldown.special_attack[0] -= 1
    Cooldown.special_attack[1] -= 1
    Cooldown.special_attack[2] -= 1
    for i in range(0,len(Cooldown.premium)):
        Cooldown.premium[i] -= 1


def reset_cooldown():
    #for i in range(0, len(Cooldown.collection)):
     #   Cooldown.collection[i] = 0
    Cooldown.cure = 0
    Cooldown.overcharge = 0
    Cooldown.h_potion = 0
    Cooldown.m_potion = 0
    Cooldown.s_potion = 0
    Cooldown.protection = 0
    Cooldown.regen = 0
    Cooldown.shield_bash = 0
    Cooldown.shockblast = 0
    Cooldown.special_attack[0] = 0
    Cooldown.special_attack[1] = 0
    Cooldown.special_attack[2] = 0
    for i in range(0, len(Cooldown.premium)):
        Cooldown.premium[i] = 0