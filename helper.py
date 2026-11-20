from typing import List

# min max norm
def normalize(x_min, x_max, x):
    return (x-x_min)/(x_max - x_min)

# # NVM NOT USING THIS 
# def duplicate_vals(my_list: List):
#     l = []
#     for val in my_list:
#         l.extend([val] * 2)
#     return l

# duplicate_vals(my_list = [0,1,2]) # Output -> [0,0,1,1,2,2]

