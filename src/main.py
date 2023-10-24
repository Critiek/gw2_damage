import PySimpleGUI as pg
import yaml

with open('db/gear.yaml') as file:
    gear = yaml.safe_load(file)

print(gear['hemlets']['ascended']['berserker'])
