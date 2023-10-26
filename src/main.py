import PySimpleGUI as pg
import yaml

with open('db/gear.yaml') as file:
    gear = yaml.safe_load(file)

# print(gear['hemlets']['ascended']['berserker'])
# print(gear)

for armour_piece in gear:
    # print(armour_piece)
    for armour_prefix in armour_piece:
        print(armour_prefix)
