import PySimpleGUI as pg
import yaml

with open('db/gear.yaml') as file:
    gear = yaml.safe_load(file)

power = 1000
precision = 1000
ferocity = 0

crit_chance = (precision - 895) / 21
critical_damage = (ferocity / 1500) + 1.5
skill_coefficient = 2

armour = int(input('How much armour does the target have? \n> '))
weapon_max_damage = int(input('How much damage does your weapon do? \n> '))


damage = ((power * weapon_max_damage * skill_coefficient) / armour) * (1 + crit_chance * (critical_damage - 1))

print('you will deal [{}] damage to the target'.format(damage))


# print(gear['hemlets']['ascended']['berserker'])
# print(gear)

# for armour_type in gear:
#     for armour_rarity in gear[armour_type]:
#         for armour_prefix in gear[armour_type][armour_rarity]:
#             for armour_stat in gear[armour_type][armour_rarity][armour_prefix]:
#                 print(str(armour_type) + ': ' + str(armour_prefix) + str(armour_stat))



# NOTE: stuff below is just formula

# ((power * 1100 * 2.0) / armour ) * (1 + crit_chance (ferocity - 1))

# assume armour = 2000
# 1100 = max greatsword damage 
# Crit_chance and ferocity as decimals
