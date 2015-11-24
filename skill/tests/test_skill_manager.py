from skill.skill_manager import SkillGenerator
import os
from nose.tools import raises

TEST_IMAGE = os.path.join("tests", "data", "test_full_window.png")
PREMIUM = ['Heartseeker', 'Spark_Life', 'Spirit_Shield', 'Haste']
SKILLS = ['Cure', 'Regen', 'Heartseeker', 'Spirit_Shield', 'Absorb', 'Special', 'Special', 'Special', 'Blind', 'Drain', 'Weaken', 'Sleep', 'Spark_Life', 'Empty', 'Empty', 'Empty']
SPECIAL = [5, 6, 7]


def test_skill_skill_manager_skillgenerator_init():
    SkillGenerator(SKILLS, PREMIUM, SPECIAL)


@raises(ValueError)
def test_skill_skill_manager_skillgenerator_init_fail():
    SkillGenerator(None, None, None)


def test_skill_skill_manager_skillgenerator_is_invalid_skill_name_true():
    generator = SkillGenerator(SKILLS, PREMIUM, SPECIAL)
    assert(generator._is_invalid_skill_name("Cure") is True)


def test_skill_skill_manager_skillgenerator_is_invalid_skill_name_false():
    generator = SkillGenerator(SKILLS, PREMIUM, SPECIAL)
    assert(generator._is_invalid_skill_name("Empty") is False)


def test_skill_skill_manager_skillgenerator_is_skill_premium_true():
    generator = SkillGenerator(SKILLS, PREMIUM, SPECIAL)
    assert(generator._is_skill_premium("Haste"))


def test_skill_skill_manager_skillgenerator_is_skill_premium_false():
    generator = SkillGenerator(SKILLS, PREMIUM, SPECIAL)
    assert(generator._is_skill_premium("Cure") is False)


def test_skill_skill_manager_skillgenerator_is_skill_special_true():
    generator = SkillGenerator(SKILLS, PREMIUM, SPECIAL)
    assert(generator._is_skill_special("Cure") is False)


def test_skill_skill_manager_skillgenerator_is_skill_special_false():
    generator = SkillGenerator(SKILLS, PREMIUM, SPECIAL)
    assert(generator._is_skill_premium("Cure") is False)


def test_skill_skill_manager_skill_generator_generate_skills():
    skill_list = SkillGenerator.generate_skills(SKILLS, PREMIUM, SPECIAL)
    for skill in skill_list:
        if skill.name in PREMIUM:
            assert(skill.premium)
        if skill.special:
            assert(skill.name == "Special")