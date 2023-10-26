import PySimpleGUI as pg
import yaml

with open('db/gear.yaml') as file:
    gear = yaml.safe_load(file)

# print(gear['hemlets']['ascended']['berserker'])
# print(gear)

# for armour_type in gear:
#     for armour_rarity in gear[armour_type]:
#         for armour_prefix in gear[armour_type][armour_rarity]:
#             for armour_stat in gear[armour_type][armour_rarity][armour_prefix]:
#                 print(str(armour_type) + ': ' + str(armour_prefix) + str(armour_stat))

power = 2600
skill_coefficient = 2
weapon_max_damage = 1100
armour = 2000
crit_chance = 0.05
ferocity = 1.5

damage = ((power * weapon_max_damage * skill_coefficient) / armour) * (1 + crit_chance * (ferocity - 1))

print(damage)




# ((power * 1100 * 2.0) / armour ) * (1 + crit_chance (ferocity - 1))

# assume armour = 2000
# 1100 = max greatsword damage 
# Crit_chance and ferocity as decimals
