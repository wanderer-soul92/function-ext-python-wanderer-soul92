import Early_warnings

BMS_allowed_range = {'temperature': {'min': 0, 'max': 45},
                'soc': {'min': 20, 'max': 80},
                'charge_rate': {'min': 0, 'max': 0.8}}

def get_out_of_range_parameter(BMS_input):
    out_of_range_parameters = {}
    actions_on_parameters ={}
    for parameter,value in BMS_input.items() :
        check_tolerance_range(parameter,value,out_of_range_parameters,actions_on_parameters)
       
    return out_of_range_parameters, actions_on_parameters

def check_tolerance_range(parameter,value,out_of_range_parameters,actions_on_parameters):
     if (value < BMS_allowed_range[parameter]['min']):
            out_of_range_parameters[parameter] = " Low Breach"
            actions_on_parameters[parameter]= 'value to be increased'
     elif (value > BMS_allowed_range[parameter]['max']):
            out_of_range_parameters[parameter] = " High Breach"
            actions_on_parameters[parameter]= 'value to be decreased'
     else :
         Early_warnings.get_warnings(parameter,value,out_of_range_parameters,actions_on_parameters)




def check_battery_is_ok(BMS_input):
    out_of_range_parameters, actions_on_parameters = get_out_of_range_parameter(BMS_input)
    if len(out_of_range_parameters) == 0: 
        return True
    else :
        return False
