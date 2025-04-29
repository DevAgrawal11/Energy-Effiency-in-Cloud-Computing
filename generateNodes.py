import numpy as np

def generate_table():
    BW_arr = np.zeros([4, 3])
    Energy_arr = np.zeros([4, 3])
    
    # Initialize BW_arr with the values from your commented example
    BW_arr[1][0] = 0.5
    BW_arr[1][1] = 0.65
    BW_arr[1][2] = 0.6
    BW_arr[2][0] = 0.6
    BW_arr[2][1] = 0.7
    BW_arr[2][2] = 0.7
    BW_arr[3][0] = 0.75
    BW_arr[3][1] = 0.8
    BW_arr[3][2] = 0.8

    # Initialize Energy_arr with the values from your commented example
    Energy_arr[1][0] = 100
    Energy_arr[1][1] = 80
    Energy_arr[1][2] = 95
    Energy_arr[2][0] = 110
    Energy_arr[2][1] = 85
    Energy_arr[2][2] = 100
    Energy_arr[3][0] = 125
    Energy_arr[3][1] = 90
    Energy_arr[3][2] = 110
    
    return BW_arr, Energy_arr


