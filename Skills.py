from Click_Press import mousePos, leftClick
from Coordinates import Cord
from Cooldown import Cooldown
from Status import is_status_active


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
    if current_health <= 60 and Cooldown.regen <= 0 <= Cord.Regen:
        print "using Regen"
        use_skill(Cord.Regen)
        Cooldown.regen = 45
        return True
    else:
        return False


def activate_premium():
    for i in range(0, len(Cord.premium)):
        if Cooldown.premium[i] <= 0 <= Cord.premium[i]:
            use_skill(Cord.premium[i])
            Cooldown.premium[i] = 45
            return True
        else:
            print "%d greater than 0 and %d less than 0?" % (Cooldown.premium[i], Cord.premium[i])
    return False


def activate_special(special, overcharge, current_overcharge):
    if special == 2 and Cord.special_attack[2] >= 0:
        if is_status_active("special_1") and is_status_active("special_2") and overcharge < current_overcharge:
            use_skill(Cord.special_attack[2])
            print "special 3 used"
            return True
    if special == 1 and Cord.special_attack[1] >= 0:
        if is_status_active("special_1") and overcharge < current_overcharge:
            use_skill(Cord.special_attack[1])
            print "special 2 used"
            return True
    if special == 0 and Cord.special_attack[0] >= 0:
        if overcharge < current_overcharge:
            use_skill(Cord.special_attack[0])
            print "special 1 used"
            return True
    return False


def activate_shield_bash(current_spirit, current_overcharge):
    if current_overcharge >= 50 and current_spirit < 80 and Cord.shield_bash >= 0 >= Cooldown.shield_bash:
        use_skill(Cord.shield_bash)
        Cooldown.shield_bash = 11
        return True
    else:
        return False


def activate_protection():
    if Cord.Protection >= 0 >= Cooldown.protection:
        use_skill(Cord.Protection)
        Cooldown.protection = 19
        return True
    else:
        return False


def get_overcharge(im):
    p_overcharge = 0
    for level in Cord.p_overcharge_levels:
        if im.getpixel(level) != Cord.under_color:
            p_overcharge += 10
        else:
            return p_overcharge
    return 100


def get_spirit(im):
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
    current_spirit = get_spirit(im)
    current_overcharge = get_overcharge(im)
    #print "Is Spirit Active? %r" %is_spirit_active(im)
    if not is_spirit_active(im):
            if use_spirit(current_spirit, current_overcharge, im):
                print "Spirit Activated"
                return
            elif current_overcharge >= 30 and current_spirit < 100:
                if style == 0:
                    attack(current_enemies[special_attack_dual(current_enemies, current_overcharge)])
                    return
                elif style == 1:
                    attack(current_enemies[special_attack_single(current_overcharge)])
                    return
    if len(current_enemies) > 0:
        attack(current_enemies[0])


#need to test
def special_attack_dual(current_enemies, current_overcharge):
    if Cord.special_attack[2] >= 0:
        if activate_special(2, 0, current_overcharge):
            return multiple_enemy_attack(current_enemies)
        elif activate_special(1, 0, current_overcharge):
            return 0
        elif activate_special(0, 80, current_overcharge):
            return 0
        else:
            if activate_special(1, 0, current_overcharge):
                return 0
            elif activate_special(0, 80, current_overcharge):
                return 0
            else:
                return 0
    else:
        if activate_special(1, 0, current_overcharge):
            return 0
        elif activate_special(0, 60, current_overcharge):
            return 0
    return 0


def special_attack_single(current_overcharge):
    if Cord.special_attack[2] >= 0:
        if activate_special(2, 0, current_overcharge):
            return 0
        elif activate_special(1, 0, current_overcharge):
            return 0
        elif activate_special(0, 70, current_overcharge):
            return 0
        else:
            if activate_special(1, 0, current_overcharge):
                return 0
            elif activate_special(0, 70, current_overcharge):
                return 0
            else:
                return 0
    else:
        if activate_special(1, 0, current_overcharge):
            return 0
        elif activate_special(0, 50, current_overcharge):
            return 0
    return 0


def use_skill(skill):
    #mousePos(Cord.Cure)
    if skill >= 0:
        mousePos(Cord.skills[skill])
        leftClick()


def use_spirit(current_spirit, current_overcharge, im):
    if current_overcharge >= 80 and Cooldown.overcharge <= 0 and current_spirit >= 40 and not is_spirit_active(im):
        mousePos(Cord.spirit_cat_loc)
        leftClick()
        Cooldown.overcharge = 10
        return True
    else:
        return False