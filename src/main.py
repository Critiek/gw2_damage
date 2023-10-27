import PySimpleGUI as pg
import yaml

with open('data/gear.yaml') as file:
    gear_data = yaml.safe_load(file)

armour_slots = ['helmet', 'shoulders', 'coat', 'gloves', 'leggings', 'boots', 'amulet', 'ring', 'ring', 'earring', 'earring', 'back']

best_combination = None
best_damage = 0

skill_coefficient = 2

armour = int(input('How much armour does the target have (recommended: 2000)? \n> '))
weapon_max_damage = int(input('How much damage does your weapon do? \n> '))

def calculate_damage(power, crit_chance, critical_damage, skill_coefficient, armour, weapon_max_damage):
    damage = ((power * weapon_max_damage * skill_coefficient) / armour) * (1 + crit_chance * (critical_damage - 1))
    return damage


for armour_slot in armour_slots:
    for prefix in gear_data[armour_slot]:
        print(str(armour_slot) + ': ' + str(prefix))


power = None 
precision = None
ferocity = None 

# crit_chance = (precision - 895) / 21
# critical_damage = (ferocity / 1500) + 1.5

# damage = calculate_damage(power, crit_chance, critical_damage, skill_coefficient, armour, weapon_max_damage)
