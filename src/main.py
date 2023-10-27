import PySimpleGUI as pg
import yaml

with open('data/gear.yaml') as file:
    gear_data = yaml.safe_load(file)

armour_slots = ['helmet', 'shoulders', 'coat', 'gloves', 'leggings', 'boots', 'amulet', 'ring',  'earring', 'back']
armour_prefixes = ['berserker', 'dragon', 'marauder']

equipped_armour = {
        'helmet': None, 
        'shoulders': None,
        'coat': None,
        'gloves': None,
        'leggings': None,
        'boots': None,
        'amulet': None,
        'ring_1': None,
        'ring_2': None,
        'earring_1': None,
        'earring_2': None,
        'back': None
        }

best_combination = None
best_damage = 0

skill_coefficient = 2

armour = int(input('How much armour does the target have (recommended: 2000)? \n> '))
weapon_max_damage = int(input('How much damage does your weapon do? \n> '))

def calculate_stats(equipped_armour):
    return power, precision, ferocity, vitality

def calculate_damage(power, precision, ferocity, skill_coefficient, armour, weapon_max_damage):
    critical_damage = (ferocity / 1500) + 1.5
    crit_chance = (precision - 895) / 21
    damage = ((power * weapon_max_damage * skill_coefficient) / armour) * (1 + crit_chance * (critical_damage - 1))
    return damage


for armour_slot in armour_slots:
    print(None)

power = None 
precision = None
ferocity = None 

# damage = calculate_damage(power, precision, ferocity, skill_coefficient, armour, weapon_max_damage):
