class PlayerCords(object):
    def __init__(self):
        p_levels = [22, 33, 44, 55, 66, 77, 88, 99, 110, 123, 134]
        p_health_y = 149
        #p_health_y = 196
        #p_health_y = 150 laptop
        p_mana_y = 187
        #p_mana_y = 191
        p_spirit_y = 227
        #p_spirit_y = 232
        #p_overcharge_y = 267
        p_overcharge_y = 265
        self.under_color = (0, 0, 0) #Black
        self.over_color = (0, 166, 23) #Green
        spirit_over_color = (120, 70, 0)
        self.p_health_levels = ((p_levels[0], p_health_y),
                                (p_levels[1], p_health_y),
                                (p_levels[2], p_health_y),
                                (p_levels[3], p_health_y),
                                (p_levels[4], p_health_y),
                                (p_levels[5], p_health_y),
                                (p_levels[6], p_health_y),
                                (p_levels[7], p_health_y),
                                (p_levels[8], p_health_y),
                                (p_levels[9], p_health_y),
                                (p_levels[10], p_health_y))

        self.p_mana_levels = ((p_levels[0], p_mana_y),
                              (p_levels[1], p_mana_y),
                              (p_levels[2], p_mana_y),
                              (p_levels[3], p_mana_y),
                              (p_levels[4], p_mana_y),
                              (p_levels[5], p_mana_y),
                              (p_levels[6], p_mana_y),
                              (p_levels[7], p_mana_y),
                              (p_levels[8], p_mana_y),
                              (p_levels[9], p_mana_y),
                              (p_levels[10], p_mana_y))

        self.p_spirit_levels = ((p_levels[0], p_spirit_y),
                                (p_levels[1], p_spirit_y),
                                (p_levels[2], p_spirit_y),
                                (p_levels[3], p_spirit_y),
                                (p_levels[4], p_spirit_y),
                                (p_levels[5], p_spirit_y),
                                (p_levels[6], p_spirit_y),
                                (p_levels[7], p_spirit_y),
                                (p_levels[8], p_spirit_y),
                                (p_levels[9], p_spirit_y),
                                (p_levels[10], p_spirit_y))

        self.p_overcharge_levels = ((p_levels[0], p_overcharge_y),
                                    (p_levels[1], p_overcharge_y),
                                    (p_levels[2], p_overcharge_y),
                                    (p_levels[3], p_overcharge_y),
                                    (p_levels[4], p_overcharge_y),
                                    (p_levels[5], p_overcharge_y),
                                    (p_levels[6], p_overcharge_y),
                                    (p_levels[7], p_overcharge_y),
                                    (p_levels[8], p_overcharge_y),
                                    (p_levels[9], p_overcharge_y),
                                    (p_levels[10], p_overcharge_y))


class EnemyCords(object):
    def __init__(self):
        e_x = 890
        e1_health = (e_x,  73)
        e2_health = (e_x,  131)
        e3_health = (e_x,  188)
        e4_health = (e_x,  246)
        e5_health = (e_x,  305)
        e6_health = (e_x,  362)
        e7_health = (e_x,  420)
        e8_health = (e_x,  479)
        e9_health = (e_x,  537) #untested
        e10_health = (e_x,  595) #untested
        self.under_color = (0, 0, 0) #Black
        self.over_color = (0, 166, 23) #Green
        self.enemy_press = {e1_health: "1",
                            e2_health: "2",
                            e3_health: "3",
                            e4_health: "4",
                            e5_health: "5",
                            e6_health: "6",
                            e7_health: "7",
                            e8_health: "8",
                            e9_health: "9",
                            e10_health: "0"}

        self.enemies = (e1_health,
                        e2_health,
                        e3_health,
                        e4_health,
                        e5_health,
                        e6_health,
                        e7_health,
                        e8_health,
                        e9_health,
                        e10_health)



class ItemCords(object):
    def __init__(self):
        item_xloc = 261
        self.item_cat_loc = (418,  65)
        self.gem_loc = (item_xloc,  210)
        i1 = (item_xloc,  235)
        i2 = (item_xloc,  258)
        i3 = (item_xloc,  281)
        i4 = (item_xloc,  304)
        i5 = (item_xloc,  327)
        i6 = (item_xloc,  350)
        i7 = (item_xloc,  373)
        i8 = (item_xloc,  391) #here and below are not updated to latest settings
        i9 = (item_xloc,  414)
        i10 = (item_xloc,  438)
        i11 = (item_xloc,  460)
        i12 = (item_xloc,  482)
        i13 = (item_xloc,  507)
        i14 = (item_xloc,  530)
        i15 = (item_xloc,  556)
        scroll_xloc = 550
        scroll1_loc = (scroll_xloc,  234)
        infusion1_loc = [scroll_xloc,  253]
        self.item_locs = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, scroll1_loc, infusion1_loc]
        itemx_begin = 200
        itemx_end = 378
        self.ibox_gem = [itemx_begin, 205, itemx_end, 212]
        ibox1 = [itemx_begin, 229, itemx_end, 236]
        ibox2 = [itemx_begin, 252, itemx_end, 259]
        ibox3 = [itemx_begin, 275, itemx_end, 282]
        ibox4 = [itemx_begin, 298, itemx_end, 305]
        ibox5 = [itemx_begin, 321, itemx_end, 328]
        ibox6 = [itemx_begin, 344, itemx_end, 351]
        ibox7 = [itemx_begin, 367, itemx_end, 374]
        ibox8 = [itemx_begin, 390, itemx_end, 397]
        ibox9 = [itemx_begin, 413, itemx_end, 420]
        ibox10 = [itemx_begin, 436, itemx_end, 443]
        ibox11 = [itemx_begin, 459, itemx_end, 466]
        ibox12 = [itemx_begin, 482, itemx_end, 489]
        ibox13 = [itemx_begin, 505, itemx_end, 512]
        ibox14 = [itemx_begin, 528, itemx_end, 535]
        ibox15 = [itemx_begin, 551, itemx_end, 558]
        self.ibox_list = [ibox1, ibox2, ibox3, ibox4, ibox5, ibox6, ibox7, ibox8, ibox9, ibox10, ibox11, ibox12, ibox13, ibox14, ibox15]


class SkillHKCords(object):
    def __init__(self):
        sk_x1 = 169
        sk_x2 = 199
        sk_y1 = 80
        sk_y2 = 112
        sk_0 = (0*37 + sk_x1, sk_y1, 0*37 + sk_x2, sk_y2)
        sk_1 = (1*37 + sk_x1, sk_y1, 1*37 + sk_x2, sk_y2)
        sk_2 = (2*37 + sk_x1, sk_y1, 2*37 + sk_x2, sk_y2)
        sk_3 = (3*37 + sk_x1, sk_y1, 3*37 + sk_x2, sk_y2)
        sk_4 = (4*37 + sk_x1, sk_y1, 4*37 + sk_x2, sk_y2)
        sk_5 = (5*37 + sk_x1, sk_y1, 5*37 + sk_x2, sk_y2)
        sk_6 = (6*37 + sk_x1, sk_y1, 6*37 + sk_x2, sk_y2)
        sk_7 = (7*37 + sk_x1, sk_y1, 7*37 + sk_x2, sk_y2)
        sk_8 = (8*37 + sk_x1, sk_y1, 8*37 + sk_x2, sk_y2)
        sk_9 = (9*37 + sk_x1, sk_y1, 9*37 + sk_x2, sk_y2)
        sk_10 = (10*37 + sk_x1, sk_y1, 10*37 + sk_x2, sk_y2)
        sk_11 = (11*37 + sk_x1, sk_y1, 11*37 + sk_x2, sk_y2)
        sk_12 = (12*37 + sk_x1, sk_y1, 12*37 + sk_x2, sk_y2)
        sk_13 = (13*37 + sk_x1, sk_y1, 13*37 + sk_x2, sk_y2)
        sk_14 = (14*37 + sk_x1, sk_y1, 14*37 + sk_x2, sk_y2)
        sk_15 = (15*37 + sk_x1, sk_y1, 15*37 + sk_x2, sk_y2)
        self.skill_box_locs = [sk_0, sk_1, sk_2, sk_3, sk_4, sk_5, sk_6, sk_7, sk_8, sk_9, sk_10, sk_11, sk_12, sk_13, sk_14, sk_15]
        s_y = 96
        #s_y = 290
        s1 = (188, s_y)
        s2 = (225, s_y)
        s3 = (262, s_y)
        s4 = (299, s_y)
        s5 = (338,  s_y)
        s6 = (375, s_y)
        s7 = (412, s_y)
        s8 = (447, s_y)
        s9 = (485, s_y)
        s10 = (523, s_y)
        s11 = (559, s_y)
        s12 = (598, s_y)
        s13 = (630, s_y)
        s14 = (671, s_y)
        s15 = (707, s_y)
        s16 = (743, s_y)
        self.skill_locs = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16]


class SpiritCords(object):
    def __init__(self):
        self.spirit_cat_loc = (494,  60) #changed, confirm with Chrome. X used to be 508
        self.spirit_active_color = (250, 59, 56) #(170, 36, 36)


class StatusCords(object):
    def __init__(self):
            st_y1 = 13
            st_y2 = 45
            st1 = (167, st_y1, 197, st_y2)
            st2 = (200, st_y1, 230, st_y2)
            st3 = (233, st_y1, 263, st_y2)
            st4 = (266, st_y1, 296, st_y2)
            st5 = (299, st_y1, 329, st_y2)
            st6 = (332, st_y1, 362, st_y2)
            st7 = (365, st_y1, 395, st_y2)
            st8 = (398, st_y1, 428, st_y2)
            st9 = (431, st_y1, 461, st_y2)
            self.status_locs = (st1, st2, st3, st4, st5, st6, st7, st8, st9)


class Cord:
    chrome_popup_padding_y = 52
    firefox_padding_y = 85
    chrome_padding_y = 61

    #window_padding_y = chrome_popup_padding_y
    window_padding_y = 0
    window_padding_x = 0
    #Cure = (188,  96)
    Items = -1
     # 0 = Health, 1 = Mana, 2 = Spirit, 9 = used
    # Health has 30 round cooldown, Mana and Spirit have 15 round cooldown

#Mapped Menu Buttons
    grindfest_button = (670,  327)
    restoratives_button = (78,  249)
    restore_health_button = (78,  283)
    restore_mana_button = (78,  303)
    restore_spirit_button = (78,  321)
    restore_all_button = (78,  340)


    spirit_cat_loc = (494,  60) #changed, confirm with Chrome. X used to be 508
    spirit_active_color = (250, 59, 56) #(170, 36, 36)
    #round_won = (550, 191)
    round_won = (550,  139) #UNTESTED
    #round_won_color = (251, 221, 65) #UNTESTED
    round_won_color = (165, 111, 44)
    under_color = (0, 0, 0) #Black
    over_color = (0, 166, 23) #Green
    spirit_over_color = (120, 70, 0)
    empty_color = (237, 235, 223) #Background Color UNTESTED
    dead_color = (166, 165, 156) #Dead Enemy Color UNTESTED
    spark_of_life_color = (192, 192, 192) #Color when Spark of Life is Active UNTESTED
    Pony_check_loc = ((706, 170), (760, 122))  #(518,  185) TEST
    Pony_check_color = (237, 235, 223)
#Skills
    s_y = 96
    #s_y = 290
    s1 = ( 188, s_y)
    s2 = ( 225, s_y)
    s3 = ( 262, s_y)
    s4 = ( 299, s_y)
    s5 = ( 338,  s_y)
    s6 = ( 375, s_y)
    s7 = ( 412, s_y)
    s8 = ( 447, s_y)
    s9 = ( 485, s_y)
    s10 = ( 523, s_y)
    s11 = ( 559, s_y)
    s12 = ( 598, s_y)
    s13 = ( 630, s_y)
    s14 = ( 671, s_y)
    s15 = ( 707, s_y)
    s16 = ( 743, s_y)
    skills = (s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16)
#Items
    item_xloc = 261
    Item_cat_loc = (418,  65)
    gem_loc = (item_xloc,  210)
    i1 = (item_xloc,  235)
    i2 = (item_xloc,  258)
    i3 = (item_xloc,  281)
    i4 = (item_xloc,  304)
    i5 = (item_xloc,  327)
    i6 = (item_xloc,  350)
    i7 = (item_xloc,  373)
    i8 = (item_xloc,  391) #here and below are not updated to latest settings
    i9 = (item_xloc,  414)
    i10 = (item_xloc,  438)
    i11 = (item_xloc,  460)
    i12 = (item_xloc,  482)
    i13 = (item_xloc,  507)
    i14 = (item_xloc,  530)
    i15 = (item_xloc,  556)
    scroll_xloc = 550
    scroll1_loc = (scroll_xloc,  234)
    infusion1_loc = [scroll_xloc,  253]
    item_locs = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, scroll1_loc, infusion1_loc]
    itemx_begin = 200
    itemx_end = 378
    ibox_gem = [itemx_begin, 205, itemx_end, 212]
    ibox1 = [itemx_begin, 229, itemx_end, 236]
    ibox2 = [itemx_begin, 252, itemx_end, 259]
    ibox3 = [itemx_begin, 275, itemx_end, 282]
    ibox4 = [itemx_begin, 298, itemx_end, 305]
    ibox5 = [itemx_begin, 321, itemx_end, 328]
    ibox6 = [itemx_begin, 344, itemx_end, 351]
    ibox7 = [itemx_begin, 367, itemx_end, 374]
    ibox8 = [itemx_begin, 390, itemx_end, 397]
    ibox9 = [itemx_begin, 413, itemx_end, 420]
    ibox10 = [itemx_begin, 436, itemx_end, 443]
    ibox11 = [itemx_begin, 459, itemx_end, 466]
    ibox12 = [itemx_begin, 482, itemx_end, 489]
    ibox13 = [itemx_begin, 505, itemx_end, 512]
    ibox14 = [itemx_begin, 528, itemx_end, 535]
    ibox15 = [itemx_begin, 551, itemx_end, 558]
    ibox_list = [ibox1, ibox2, ibox3, ibox4, ibox5, ibox6, ibox7, ibox8, ibox9, ibox10, ibox11, ibox12, ibox13, ibox14, ibox15]

    #Item Color Sums
    h_1 = 574086 #lesser health potion
    h_2 = 553816 #average health potion
    h_3 = 552132 #greater health potion
    h_4 = 0 #superior health potion
    h_5 = 575009 #heroic health potion
    h_5_c = 574965 #heroic health potion chrome
    m_1 = 590679 #lesser mana potion
    m_2 = 570409 #average mana potion
    m_3 = 568725 #greater mana potion
    m_4 = 0 #superior mana potion
    m_5 = 591602 #heroic mana potion
    m_5_c = 591551 #heroic mana potion chrome
    s_1 = 0 #lesser spirit potion
    s_2 = 0 #average spirit potion
    s_3 = 561838 #greater spirit potion
    s_4 = 541838 #superior spirit potion
    s_5 = 584715 #heroic spirit potion
    h_potions = [h_1, h_2, h_3, h_4, h_5, h_5_c]
    m_potions = [m_1, m_2, m_3, m_4, m_5, m_5_c]
    s_potions = [s_1, s_2, s_3, s_4, s_5]





    # 0 = Health, 1 = Mana, 2 = Spirit, 9 = used
    # Health has 30 round cooldown, Mana and Spirit have 15 round cooldown
    #Items = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2] #main character
    p_dead = False
    battle_cat_loc = [640,  12]
    Grindfest_cat_loc = [640,  81]
#Statuses
    st_y1 = 13
    st_y2 = 45
    st1 = (167, st_y1, 197, st_y2)
    st2 = (200, st_y1, 230, st_y2)
    st3 = (233, st_y1, 263, st_y2)
    st4 = (266, st_y1, 296, st_y2)
    st5 = (299, st_y1, 329, st_y2)
    st6 = (332, st_y1, 362, st_y2)
    st7 = (365, st_y1, 395, st_y2)
    st8 = (398, st_y1, 428, st_y2)
    st9 = (431, st_y1, 461, st_y2)
    Status = (st1, st2, st3, st4, st5, st6, st7, st8, st9)
    Current_Status = []

#Arena Locations
    arena_cat_loc = (626, 40)
    a_x = 1140
    a_next_loc = (771, 60)
    #a_window_ok_loc = (638, 307)
    a1 = (a_x,128)
    a2 = (a_x,165)
    a3 = (a_x,200)
    a4 = (a_x,236)
    a5 = (a_x,271)
    a6 = (a_x,307)
    a7 = (a_x,342)
    a8 = (a_x,381)
    a9 = (a_x,418)
    a10 = (a_x,452)
    a11 = (a_x,486)
    arenas = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11]

#Skill Hotkey Locations
    #37x
    sk_x1 = 169
    sk_x2 = 199
    sk_y1 = 80
    sk_y2 = 112
    sk_0 = (0*37 + sk_x1, sk_y1, 0*37 + sk_x2, sk_y2)
    sk_1 = (1*37 + sk_x1, sk_y1, 1*37 + sk_x2, sk_y2)
    sk_2 = (2*37 + sk_x1, sk_y1, 2*37 + sk_x2, sk_y2)
    sk_3 = (3*37 + sk_x1, sk_y1, 3*37 + sk_x2, sk_y2)
    sk_4 = (4*37 + sk_x1, sk_y1, 4*37 + sk_x2, sk_y2)
    sk_5 = (5*37 + sk_x1, sk_y1, 5*37 + sk_x2, sk_y2)
    sk_6 = (6*37 + sk_x1, sk_y1, 6*37 + sk_x2, sk_y2)
    sk_7 = (7*37 + sk_x1, sk_y1, 7*37 + sk_x2, sk_y2)
    sk_8 = (8*37 + sk_x1, sk_y1, 8*37 + sk_x2, sk_y2)
    sk_9 = (9*37 + sk_x1, sk_y1, 9*37 + sk_x2, sk_y2)
    sk_10 = (10*37 + sk_x1, sk_y1, 10*37 + sk_x2, sk_y2)
    sk_11 = (11*37 + sk_x1, sk_y1, 11*37 + sk_x2, sk_y2)
    sk_12 = (12*37 + sk_x1, sk_y1, 12*37 + sk_x2, sk_y2)
    sk_13 = (13*37 + sk_x1, sk_y1, 13*37 + sk_x2, sk_y2)
    sk_14 = (14*37 + sk_x1, sk_y1, 14*37 + sk_x2, sk_y2)
    sk_15 = (15*37 + sk_x1, sk_y1, 15*37 + sk_x2, sk_y2)
    skill_status = [sk_0, sk_1, sk_2, sk_3, sk_4, sk_5, sk_6, sk_7, sk_8, sk_9, sk_10, sk_11, sk_12, sk_13, sk_14, sk_15]
