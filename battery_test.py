BMS_allowed_range = {'temperature': {'min': 0, 'max': 45},
                'soc': {'min': 20, 'max': 80},
                'charge_rate': {'min': 0, 'max': 0.8}}


def get_out_of_range_parameter(BMS_input):
    out_of_range_parameters = []
    for parameter,value in BMS_input.items() :
        check_tolerance_range(parameter,value,out_of_range_parameters)
       
    return out_of_range_parameters

def check_tolerance_range(key,value,out_of_range_parameters):
     if (value < BMS_allowed_range[key]['min']) or (value > BMS_allowed_range[key]['max']):
            out_of_range_parameters.append(key)


def check_battery_is_ok(BMS_input):
    out_of_range_parameter_count = get_out_of_range_parameter(BMS_input)
    if len(out_of_range_parameter_count) == 0: 
        return True
    else :
        return False
