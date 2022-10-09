import os
import glob

def load_sensor_data():
    sensor_data=[]
    sensor_files = glob.glob(os.path.join(os.getcwd(),"datasets","*csv"))
    for sensor_file in sensor_files:
        with open(sensor_file) as data_file:
            for row in data_file:
                sensor_data.append(row)
    return sensor_data