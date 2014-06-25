from Click_Press import mousePos, leftClick
from Coordinates import Cord
from Status import is_status_active, get_pixel_sum, get_pixel_sum_color
import Settings
import logging


class Skills:
    #Cure_a = 12676
    #Cure_i = 16439
    #Special_a = 20065
    #Special_i = 21045
    #Protection_a = 13194
    #Protection_i = 16270
    #Haste_a = 21690
    #Haste_i = 22154
    #Regen_a = 13459
    #Regen_i = 17261
    #Shadow_Veil_a = 0
    #Shadow_Veil_i = 0
    #Empty = 4431
    overcharge_cooldown = 0
    Active_Collection = {}
    Inactive_Collection = {}
    #Active_Collection = {Cure_a: "Cure",
    #                     Special_a: "Special",
    #                     Protection_a: "Protection",
    #                     Haste_a: "Haste",
    #                     Regen_a: "Regen",
    #                     Shadow_Veil_a: "Shadow_Veil",
    #                     Empty: ""}
    #Inactive_Collection = {Cure_i: "Cure",
    #                       Special_i: "Special",
    #                       Protection_i: "Protection",
    #                       Haste_i: "Haste",
    #                       Regen_i: "Regen",
    #                       Shadow_Veil_i: "Shadow_Veil"}

    Current = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    Exceptions = ["Shadow_Veil", "Corruption", "Shockblast", "Smite"]


def attack(enemy):
    try:
        mousePos(enemy)
        leftClick()
    except ValueError:
        logging.warning("no more enemies")

"""
def activate_cooldown(special, style):
    if style == 0 and (special == 0 or special == 1):
        Cooldown.special_attack[special] = 5
    else:
        Cooldown.special_attack[special] = 10
"""

#Done, base Activate functions on this
def activate_cure(current_health):
    if current_health <= 50 and is_skill_active("Cure"):
        use_skill(lookup_skill("Cure"))
        return True
    else:
        return False


def activate_premium():
    for i in range(0, len(Settings.Player.premium)):
        if is_skill_active(Settings.Player.premium[i]) and not is_status_active(Settings.Player.premium[i]):
            use_skill(lookup_skill(Settings.Player.premium[i]))
            return True
    return False


def activate_regen(current_health):
    if current_health <= 60 and is_skill_active("Regen") and not is_premium_skill("Regen") and not is_status_active("Regen"):
        use_skill(lookup_skill("Regen"))
        return True
    else:
        return False


def activate_absorb():
    if is_skill_active("Absorb") and not is_premium_skill("Absorb") and not is_status_active("Absorb"):
        use_skill(lookup_skill("Absorb"))
        return True
    else:
        return False


def activate_protection():
    if is_skill_active("Protection") and not is_premium_skill("Protection") and not is_status_active("Protection"):
        use_skill(lookup_skill("Protection"))
        return True
    else:
        return False

"""
def activate_special(special, overcharge, current_overcharge, style):
    if special == 2 and Settings.Player.special_attack[2] >= 0 >= Cooldown.special_attack[2]:
        if is_status_active("special_1") and is_status_active("special_2") and overcharge < current_overcharge:
            use_skill(Settings.Player.special_attack[2])
            logging.debug("special 3 used")
            activate_cooldown(2, style)
            return True
    if special == 1 and Settings.Player.special_attack[1] >= 0 >= Cooldown.special_attack[1]:
        if is_status_active("special_1") and overcharge < current_overcharge:
            use_skill(Settings.Player.special_attack[1])
            logging.debug("special 2 used")
            activate_cooldown(1, style)
            return True
    if special == 0 and Settings.Player.special_attack[0] >= 0 >= Cooldown.special_attack[0]:
        if overcharge < current_overcharge:
            use_skill(Settings.Player.special_attack[0])
            logging.debug("special 1 used")
            activate_cooldown(0, style)
            return True
    return False"""


def activate_special2(special, overcharge=0, current_overcharge=0):
    logging.debug("checking if special can be activated")
    if special == 2 and Settings.Player.special_attack[2] >= 0:
        if is_special_active(2):
            use_skill(Settings.Player.special_attack[2])
            logging.debug("special 3 used")
            return True
    elif special == 1 and Settings.Player.special_attack[1] >= 0:
        if is_special_active(1):
            use_skill(Settings.Player.special_attack[1])
            logging.debug("special 2 used")
            return True
    elif special == 0 and Settings.Player.special_attack[0] >= 0:
        if is_special_active(0) and overcharge <= current_overcharge:
            use_skill(Settings.Player.special_attack[0])
            logging.debug("special 1 used")
            return True
    return False


def buffer_Skill_Find(pixel_sum, collection):
    logging.info("Skill Buffer Being Used")
    for key, value in collection.items():
        if key - Settings.skill_buffer <=  pixel_sum  <= key + Settings.skill_buffer:
            logging.debug("Skill sum {} is {} away from {} which is {}".format(pixel_sum, Settings.skill_buffer, key, value))
            return value
    return None


def get_skills():
    skill_count = 0
    skill_kill = False
    for skill in Cord.skill_status:
        #sum = get_pixel_sum_color(skill)
        sum = get_pixel_sum_color(skill)
        logging.debug("Skill {}: {}".format(skill_count, sum))
        result = Skills.Active_Collection.get(sum)
        result2 = Skills.Inactive_Collection.get(sum)
        if result is not None:
            Settings.Player.skills[skill_count] = result
        elif result2 is not None:
            Settings.Player.skills[skill_count] = result2
        else:
            result = buffer_Skill_Find(sum, Skills.Active_Collection)
            if result is not None:
                Settings.Player.skills[skill_count] = result
                Skills.Active_Collection[sum] = result
            else:
                result2 = buffer_Skill_Find(sum, Skills.Inactive_Collection)
                if result2 is not None:
                    Settings.Player.skills[skill_count] = result2
                    Skills.Inactive_Collection[sum] = result2
                else:
                    logging.warning("UNKNOWN skill: %d" % sum)
                    get_pixel_sum_color(skill, True)
                    skill_kill = True
        skill_count += 1
    if skill_kill:
        logging.critical("Not all skills were identified. Shutting down now.")
        quit()


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


def is_exception_skill_active(skill):
    skill_status = get_pixel_sum_color(Cord.skill_status[lookup_skill(skill)])
    if skill == "Shadow_Veil" or skill == "Corruption":
        if skill_status <= 200000:
            return True
    elif skill == "Shockblast":
        if skill_status <= 450000:
            return True
    elif skill == "Smite":
        if skill_status <= 500000:
            return True
    return False


def is_premium_skill(skill):
    for p_skill in Settings.Player.premium:
        if p_skill == skill:
            return True
    return False


def is_skill_active(skill):
    if lookup_skill(skill) <= 15:
        for e_skill in Skills.Exceptions:
            if e_skill == skill:
                return is_exception_skill_active(skill)
        skill_status = get_pixel_sum_color(Cord.skill_status[lookup_skill(skill)])
        if skill_status <= 400000:
            return True
        else:
            return False
    return False


def is_skill_active_dynamic(skill):
    #skill: 20065
    if lookup_skill(skill) <= 15:
        skill_status = get_pixel_sum_color(Cord.skill_status[lookup_skill(skill)])
        if Skills.Active_Collection.get(skill_status) is not None:
            return True
        elif Skills.Inactive_Collection.get(skill_status) is not None:
            return False
        else:
            #print skill_status
            logging.debug("skill {0} sum unidentified: {1}. Skill Position: {2}".format(skill, skill_status, lookup_skill(skill)))
            result = buffer_Skill_Find(skill_status, Skills.Active_Collection)
            if result is not None:
                Skills.Active_Collection[skill_status] = result
                return True
            else:
                result2 = buffer_Skill_Find(skill_status, Skills.Inactive_Collection)
                if result2 is not None:
                    Skills.Inactive_Collection[skill_status] = result2
                    return False
            return False
    return False


def is_special_active(special):
    skill_status = get_pixel_sum_color(Cord.skill_status[Settings.Player.special_attack[special]])
    if skill_status <= 400000:
        return True
    else:
        return False


def is_special_active_original(skill):
    #skill: 20065
    skill_status = get_pixel_sum_color(Cord.skill_status[Settings.Player.special_attack[skill]])
    if Skills.Active_Collection.get(skill_status) is not None:
        return True
    elif Skills.Inactive_Collection.get(skill_status) is not None:
        return False
    else:
        #print skill_status
        logging.info("special sum unidentified: {0}".format(skill_status))
        return False


#def is_special_active(skill):
#    #skill: 20065
#    skill_status = get_pixel_sum(Cord.skill_status[Settings.Player.special_attack[skill]])
#    if skill_status == 20065 or skill_status == 21073:
#        return True
#    elif skill_status == 21045 or skill_status == 20979 or skill_status == 20572:
#        return False
#    else:
#        print skill_status
#        logging.info("special sum unidentified: {0}".format(skill_status))
#        return False


def is_spirit_active(im):
    if im.getpixel(Cord.spirit_cat_loc) == Cord.spirit_active_color:
        return True
    else:
        return False


def lookup_skill(c_skill):
    for i in range(0, len(Settings.Player.skills)-1):
        if Settings.Player.skills[i] == c_skill:
            return i
    return 16


def multiple_enemy_attack(enemies):
    if len(enemies) >= 5:
        return 2
    elif len(enemies) >= 3:
        return 1
    else:
        return 0


def special_attack(im, current_enemies, style):
    try:
        current_spirit = get_spirit(im)
        current_overcharge = get_overcharge(im)
        #print "Is Spirit Active? %r" %is_spirit_active(im)
        if not is_spirit_active(im):
                if use_spirit(current_spirit, current_overcharge, im):
                    logging.debug("Spirit Activated")
                    return
                elif current_overcharge >= 30:
                    if style == 0:
                        attack(current_enemies[special_attack_dual(current_enemies, current_overcharge)])
                        return
                    elif style == 1:
                        attack(current_enemies[special_attack_single(current_overcharge)])
                        return
        if len(current_enemies) > 0:
            attack(current_enemies[0])
    except Exception, e:
        logging.warning("Issue with Special Attack function. returning. Specials: {}".format(Settings.Player.special_attack))
        logging.exception(e)
        return



#need to test
#special 1 costs 50
#special 2 costs 50
#special 3 costs 75
#together the cost is 175
#10% of overcharge is roughly 30 overcharge
def special_attack_dual(current_enemies, current_overcharge):
    if Settings.Player.special_attack[2] >= 0:
        if activate_special2(2):
            return multiple_enemy_attack(current_enemies)
        elif activate_special2(1):
            return 0
        elif activate_special2(0, 80, current_overcharge):
            return 0
    else:
        if activate_special2(1):
            return 0
        elif activate_special2(0, 60, current_overcharge):
            return 0
    return 0

"""
def special_attack_dual_original(current_enemies, current_overcharge):
    if Settings.Player.special_attack[2] >= 0:
        if activate_special(2, 10, current_overcharge, 0):
            return multiple_enemy_attack(current_enemies)
        elif activate_special(1, 20, current_overcharge, 0):
            return 0
        elif activate_special(0, 70, current_overcharge, 0):
            return 0
        else:
            if activate_special(1, 20, current_overcharge, 0):
                return 0
            elif activate_special(0, 70, current_overcharge, 0):
                return 0
            else:
                return 0
    else:
        if activate_special(1, 20, current_overcharge, 0):
            return 0
        elif activate_special(0, 60, current_overcharge, 0):
            return 0
    return 0"""


#special 1 costs 25
#special 2 costs 50
#special 3 costs 75
#together the cost is 150
#10% of overcharge is roughly 30 overcharge
def special_attack_single(current_overcharge):
    if Settings.Player.special_attack[2] >= 0:
        if activate_special2(2):
            return 0
        elif activate_special2(1):
            return 0
        elif activate_special2(0, 70, current_overcharge):
            return 0
    else:
        if activate_special2(1):
            return 0
        elif activate_special2(0, 50, current_overcharge):
            return 0
    return 0

"""
def special_attack_single_original(current_overcharge):
    if Settings.Player.special_attack[2] >= 0:
        if activate_special(2, 10, current_overcharge, 1):
            return 0
        elif activate_special(1, 20, current_overcharge, 1):
            return 0
        elif activate_special(0, 70, current_overcharge, 1):
            return 0
        else:
            if activate_special(1, 20, current_overcharge, 1):
                return 0
            elif activate_special(0, 70, current_overcharge, 1):
                return 0
            else:
                return 0
    else:
        if activate_special(1, 20, current_overcharge, 1):
            return 0
        elif activate_special(0, 50, current_overcharge, 1):
            return 0
    return 0"""


def use_skill(skill):
    #mousePos(Cord.Cure)
    if skill >= 0:
        mousePos(Cord.skills[skill])
        leftClick()


def use_spirit(current_spirit, current_overcharge, im):
    if current_overcharge >= 80 and Skills.overcharge_cooldown <= 0 and current_spirit >= 40 and not is_spirit_active(im) and Settings.Player.spirit:
        mousePos(Cord.spirit_cat_loc)
        leftClick()
        Skills.overcharge_cooldown = 10
        return True
    else:
        Skills.overcharge_cooldown -= 1
        return False