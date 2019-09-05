# For tray type calculation.
import math
import area_cal

result_list_dict = {}
result_list_key = []
def tray_result(process_data_cal,diameter_cal,pi):
    l = float(process_data_cal['liquid_flow'])
    g = float(process_data_cal['gas_flow'])
    den_l = float(process_data_cal['liquid_density'])
    den_g = float(process_data_cal['gas_density'])
    vis_l = process_data_cal['liquid_viscosity']
    vis_g = process_data_cal['gas_viscosity']
    st_l = process_data_cal['surface_tension']
    
    cross_sectinal_area = pi/4*diameter_cal*diameter_cal
    tray_spacing = float(input('Please enter the Tray Spacing:'))

    number_of_passes = float(input('Please enter the Number of Passes:'))
    dc_side_width_top = float(input('Please enter the Side Downcomer Width (Top):'))
    dc_side_width_btm = float(input('Please enter the Side Downcomer Width (bottom):'))
    dc_side_area_top = area_cal.area(dc_side_width_top,diameter_cal)
    dc_side_area_btm = area_cal.area(dc_side_width_btm,diameter_cal)
    dc_side_weir_height = float(input('Please enter the Downcomer Weir Height:'))
    dc_side_clearance = float(input('Please enter the Downcomer Clearance Height:'))

    if number_of_passes == 1:
        flow_path_length_a = diameter_cal-dc_side_width_top-dc_side_width_btm
        bubbling_area_a = cross_sectinal_area-dc_side_area_top-dc_side_area_btm

    elif number_of_passes == 2:
        dc_center_width_top = float(input('Please enter the Center Downcomer Width (top):'))
        dc_center_width_btm = float(input('Please enter the Center Downcomer Width (bottom):'))
        dc_center_area_top = cross_sectinal_area-2*area_cal.area((diameter_cal/2-dc_center_width_top/2),diameter_cal)
        dc_center_area_btm = cross_sectinal_area-2*area_cal.area((diameter_cal/2-dc_center_width_btm/2),diameter_cal)
        dc_center_weir_height = float(input('Please enter the Center Downcomer Weir Height:'))
        dc_center_clearance = float(input('Please enter the Center Downcomer Clearance Height:'))
        flow_path_length_a = diameter_cal/2-dc_center_width_btm/2-dc_side_width_top
        flow_path_length_b = diameter_cal/2-dc_center_width_top/2-dc_side_width_btm
        bubbling_area_a = area_cal.area(diameter_cal-dc_center_width_btm/2,diameter_cal)-area_cal.area(dc_side_width_top,diameter_cal)
        bubbling_area_b = area_cal.area(diameter_cal-dc_center_width_top/2,diameter_cal)-area_cal.area(dc_side_width_btm,diameter_cal)

    elif number_of_passes == 4:
        dc_center_width_top = float(input('Please enter the Center Downcomer Width (top):'))
        dc_center_width_btm = float(input('Please enter the Center Downcomer Width (bottom):'))
        dc_offcenter_width_top = float(input('Please enter the Off Center Downcomer Width (bottom):'))
        dc_offcenter_width_btm = float(input('Please enter the Off Center Downcomer Width (bottom):'))
        dc_offcenter_location = float(input('Please enter the Off Center Downcomer Location:'))
        dc_center_area_top = cross_sectinal_area-2*area_cal.area((diameter_cal/2-dc_center_width_top/2),diameter_cal)
        dc_center_area_btm = cross_sectinal_area-2*area_cal.area((diameter_cal/2-dc_center_width_btm/2),diameter_cal)
        dc_offcenter_area_top = area_cal.area((diameter_cal/2-dc_offcenter_location+dc_offcenter_width_top/2),diameter_cal)-area_cal.area((diameter_cal/2-dc_offcenter_location-dc_offcenter_width_top/2),diameter_cal)
        dc_offcenter_area_btm = area_cal.area((diameter_cal/2-dc_offcenter_location+dc_offcenter_width_btm/2),diameter_cal)-area_cal.area((diameter_cal/2-dc_offcenter_location-dc_offcenter_width_btm/2),diameter_cal)
        dc_center_weir_height = float(input('Please enter the Center Downcomer Weir Height:'))
        dc_center_clearance = float(input('Please enter the Center Downcomer Clearance Height:'))
        flow_path_length_a = diameter_cal/2-dc_offcenter_location-dc_offcenter_width_btm/2-dc_side_width_top
        flow_path_length_b = dc_offcenter_location-dc_offcenter_width_btm/2-dc_center_width_top/2
        flow_path_length_c = diameter_cal/2-dc_offcenter_location-dc_offcenter_width_top/2-dc_side_width_btm
        flow_path_length_d = dc_offcenter_location-dc_offcenter_width_top/2-dc_center_width_btm/2
        bubbling_area_a = area_cal.area((diameter_cal/2-dc_offcenter_location-dc_offcenter_width_btm/2),diameter_cal)-dc_side_area_top
        bubbling_area_b = area_cal.area((diameter_cal/2-dc_center_width_top/2),diameter_cal)-area_cal.area((diameter_cal/2-dc_offcenter_location+dc_offcenter_width_btm/2),diameter_cal)
        bubbling_area_c = area_cal.area((diameter_cal/2-dc_offcenter_location-dc_offcenter_width_top/2),diameter_cal)-dc_side_area_btm
        bubbling_area_d = area_cal.area((diameter_cal/2-dc_center_width_btm/2),diameter_cal)-area_cal.area((diameter_cal/2-dc_offcenter_location+dc_offcenter_width_top/2),diameter_cal)

    else:
        print('The input number of passes is not supported here!')
        
    return tray_spacing



