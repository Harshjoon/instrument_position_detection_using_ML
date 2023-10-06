import bpy
import os
import math
import random
import pickle

no_of_data_points = 1000

#render_data_path = "D:\Harsh Workspace\Software\data\instrument_detection_test/"
#label_data_path  = "D:\Harsh Workspace\Software\data\instrument_detection_test/labels/"

render_data_path = "D:/Harsh Workspace/Software/GU/instrument_position_detection_using_ML/data/set_3/images/"
label_data_path  = "D:/Harsh Workspace/Software/GU/instrument_position_detection_using_ML/data/set_3/labels/"

def make_random_location():
#    x = random.randint(-3,3)
#    y = random.randint(-3,3)
#    z = random.randint(-2,2)
#    return [0,0,0]
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    z = random.uniform(-1,1)
    return [0,y,0]

def make_random_angle():
    x = random.uniform(0,3.1415926)
    y = random.uniform(0,3.1415926)
    z = random.uniform(0,3.1415926)
    return [0,0,0]

def render_and_save(locations, angles, name):
    
    print(name)
    
    bpy.data.objects['Cylinder'].location = locations
    bpy.data.objects['Cylinder'].keyframe_insert(data_path='location', frame=1)
    bpy.data.objects['Cylinder'].rotation_euler = angles
    bpy.data.objects['Cylinder'].keyframe_insert(data_path='rotation_euler', frame=1)
    
    bpy.context.scene.render.filepath = render_data_path + name
    bpy.ops.render.render(write_still=True)
    
    with open( label_data_path + name , 'wb' ) as fp:
        pickle.dump([locations, angles],fp)    

for i in range(no_of_data_points):
    render_and_save(make_random_location(),make_random_angle(), str(i) )

print("Done")