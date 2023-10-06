import bpy
import os
import math
import random
import pickle


def make_random_location():
    #x = random.randint(-1,1)
    #y = random.randint(-3,3)
    #z = random.randint(-2,2)
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    z = random.uniform(-1,1)
    return [0,y,0]

def make_random_angle():
    x = random.uniform(0,3.1415926)
    y = random.uniform(0,3.1415926)
    z = random.uniform(0,3.1415926)
    return [0,0,0]


bpy.data.objects['Cylinder'].location =  make_random_location()
bpy.data.objects['Cylinder'].rotation_euler = make_random_angle()



