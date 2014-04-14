import code
from Click_Press import mousePos, leftClick
from Coordinates import Cord
from Cooldown import Cooldown


def attack(enemy):
    try:
        mousePos(enemy)
        leftClick()
    except ValueError:
        print "no more enemies"


def activate_cure(current_health, current_mana):
    if current_health <= 50 and Cooldown.cure <= 0 and current_mana >= 10 and Cord.Cure >= 0:
        use_skill(Cord.Cure)
        Cooldown.cure = 5
        return True
    else:
        return False


def activate_regen(current_health):
    if current_health <= 60 and Cooldown.regen <= 0 and Cord.Regen >=0:
        print "using Regen"
        use_skill(Cord.Regen)
        Cooldown.regen = 45
        return True
    else:
        return False


def activate_iris_strike(current_spirit, current_overcharge):
    if current_overcharge >= 30 and current_spirit < 100 and Cord.Iris_Strike >= 0:
        use_skill(Cord.Iris_Strike)
        return True
    else:
        return False


def activate_premium():
    for i in range(0, len(Cord.premium)):
        if Cooldown.premium[i] <= 0 and Cord.premium[i] >=0:
            use_skill(Cord.premium[i])
            Cooldown.premium[i] = 45
            return True
        else:
            print "%d greater than 0 and %d less than 0?" % (Cooldown.premium[i], Cord.premium[i])
    return False


def activate_shield_bash(current_spirit, current_overcharge):
    if current_overcharge >= 50 and current_spirit < 80 and Cord.shield_bash >= 0 and Cooldown.shield_bash <= 0:
        use_skill(Cord.shield_bash)
        Cooldown.shield_bash = 11
        return True
    else:
        return False


def activate_protection():
    if Cord.Protection >= 0 and Cooldown.protection <= 0:
        use_skill(Cord.Protection)
        Cooldown.protection = 19
        return True
    else:
        return False


def getOvercharge(im):
    p_overcharge = 0
    for level in Cord.p_overcharge_levels:
        if im.getpixel(level) != Cord.under_color:
            p_overcharge += 10
        else:
            return p_overcharge
    return 100


def getSpirit(im):
    p_spirit = 0
    for level in Cord.p_spirit_levels:
        if im.getpixel(level) != Cord.under_color:
            p_spirit += 10
        else:
            return p_spirit
    return 100


def is_spirit_active(im):
    if im.getpixel(Cord.spirit_cat_loc) == Cord.spirit_active_color:
        return True
    else:
        return False


def multiple_enemy_attack(enemies):
    if len(enemies) >= 5:
        return 2
    elif len(enemies) >= 3:
        return 1
    else:
        return 0


def special_attack(im, current_enemies, style):
    current_spirit = getSpirit(im)
    current_overcharge = getOvercharge(im)
    #print "Is Spirit Active? %r" %is_spirit_active(im)
    if not is_spirit_active(im):
            if use_spirit(current_spirit, current_overcharge, im):
                print "Spirit Activated"
            elif current_overcharge >= 30 and current_spirit < 100:
                if style == 0:
                    attack(current_enemies[special_attack_dualwield(current_enemies, current_overcharge)])
                #elif activate_iris_strike(current_spirit, current_overcharge):
                #    if len(current_enemies) > 0:
                #        attack(current_enemies[0])
                #        print "Iris Strike Used"
                elif activate_shield_bash(current_spirit, current_overcharge):
                    if len(current_enemies) > 0:
                        attack(current_enemies[0])
                        print "Shield Bash Used"
                else:
                    if len(current_enemies) > 0:
                        attack(current_enemies[0])
            else:
                if len(current_enemies) > 0:
                    attack(current_enemies[0])
    else:
        if len(current_enemies) > 0:
            attack(current_enemies[0])


def special_attack_dualwield(current_enemies, current_overcharge):
    if current_enemies > 6:
        if Cord.special_1 and Cord.special_2 and Cord.special_attack[2] >= 0:
            use_skill(Cord.special_attack[2])
            Cord.special_1 = False
            Cord.special_2 = False
            return multiple_enemy_attack(current_enemies)
        elif Cord.special_1 and Cord.special_attack[1] >= 0:
            use_skill(Cord.special_attack[1])
            Cord.special_2 = True
            return 0
        elif current_overcharge >= 50 and Cord.special_attack[2] >= 0 and Cord.special_attack[1] >= 0 and Cord.special_attack[0] >= 0:
            use_skill(Cord.special_attack[0])
            Cord.special_1 = True
            return 0
        else:
            if Cord.special_1 and Cord.special_attack[1] >= 0:
                use_skill(Cord.special_attack[1])
                Cord.special_2 = True
                return 0
            elif Cord.special_attack[0] >= 0:
                use_skill(Cord.special_attack[0])
                Cord.special_1 = True
                return 0
    else:
        if Cord.special_1 and Cord.special_attack[1] >= 0:
            use_skill(Cord.special_attack[1])
            Cord.special_2 = True
            return 0
        elif Cord.special_attack[0] >= 0:
            use_skill(Cord.special_attack[0])
            Cord.special_1 = True
            return 0


def use_skill(skill):
    #mousePos(Cord.Cure)
    if skill >= 0:
        mousePos(Cord.skills[skill])
        leftClick()

def use_spirit(current_spirit, current_overcharge, im):
    if current_overcharge >= 80 and Cooldown.overcharge <= 0 and current_spirit >= 30 and not is_spirit_active(im):
        mousePos(Cord.spirit_cat_loc)
        leftClick()
        Cooldown.overcharge = 10
        return True
    else:
        return False