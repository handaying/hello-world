# main
import area_cal
import math
import tray_cal
import packing_cal

pi = 3.1415926

# Import the process data.
filename = input('Enter the process data file path:')
process_data_lists = []
process_data = []
#process_data_dict = {}
process_data_key = ['stage', 'liquid_flow', 'gas_flow', 'liquid_density', 'gas_density', 'liquid_viscosity', 'gas_viscosity', 'surface_tension']
with open(filename) as file_object:
     lines = file_object.readlines()
     for line in lines:
         line = line.rstrip('\n')
         process_data = line.split(' ')
         #process_data_dict = dict(zip(process_data_key, process_data))
         #print(process_data_dict)
         process_data_lists.append(process_data)

#print(process_data_lists)

#for process_data_list in process_data_lists[:5]:
         #print(process_data_list)

stage_top = int(input('Please enter the top stage:'))
stage_btm = int(input('Please enter the bottom stage:'))

process_data_top = process_data_lists[stage_top-1]
process_data_top_dict = dict(zip(process_data_key, process_data_top))
process_data_btm = process_data_lists[stage_btm-1]
process_data_btm_dict = dict(zip(process_data_key, process_data_btm))

#print(process_data_top_dict)
#print(process_data_btm_dict)

diameter = float(input('Enter the section diameter:'))
#cross_sectinal_area = pi/4*diameter*diameter
#print(cross_sectinal_area)

system_factor = 1.0
#result_top = packing_cal.packing_result(process_data_top_dict,diameter)
internal_type = input('Please choose the internal type:')
# Tray or Packing

if internal_type == 'Tray':

    results_top = tray_cal.tray_result(process_data_top_dict,diameter,pi)
    results_btm = tray_cal.tray_result(process_data_btm_dict,diameter,pi)

elif internal_type == 'Packing':
    
    result_top = packing_cal.packing_result(process_data_top_dict,diameter,pi)
    results_btm = packing_cal.packing_result(process_data_btm_dict,diameter,pi)
    print(result_top)

else:
    print('The input internal type is invald!')


