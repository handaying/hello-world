# For packing type calculation.
import math
result_list_dict = {}
result_list_key = ['F-Factor', 'Liquid load']
def packing_result(process_data_cal,diameter_cal,pi):
    l = float(process_data_cal['liquid_flow'])
    g = float(process_data_cal['gas_flow'])
    den_l = float(process_data_cal['liquid_density'])
    den_g = float(process_data_cal['gas_density'])
    vis_l = process_data_cal['liquid_viscosity']
    vis_g = process_data_cal['gas_viscosity']
    st_l = process_data_cal['surface_tension']

    volumn_flow_g = g/den_g
    volumn_flow_l = l/den_l
    #print(volumn_flow_g)
    cross_sectinal_area = pi/4*diameter_cal*diameter_cal
    #print(cross_sectinal_area)
    u_g = volumn_flow_g/3600/cross_sectinal_area
    #print(u_g)
    f_factor = u_g*math.sqrt(den_g)
    liquid_load = volumn_flow_l/cross_sectinal_area

    #packing_type = input('Please choose the Packing type:')

    result_list = [f_factor, liquid_load]
    result_list_dict = dict(zip(result_list_key,result_list))
    return result_list_dict


