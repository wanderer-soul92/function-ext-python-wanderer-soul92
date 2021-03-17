import record_warnings
import out_of_range_parameters_DE as get_DE

global language

def set_language(lang):
    global language 
    language = lang

BMS_allowed_range = {'temperature': {'min': 0, 'max': 45},
                'soc': {'min': 20, 'max': 80},
                'charge_rate': {'min': 0, 'max': 0.8}}

def out_of_range_parameter_language(BMS_input):
    language
    out_of_range_parameters = {}
    actions_on_parameters ={}    
    if language == 'EN' :
        get_out_of_range_parameter_EN(BMS_input,out_of_range_parameters,actions_on_parameters )
        return out_of_range_parameters, actions_on_parameters
    else :
        get_DE.get_out_of_range_parameter_DE(BMS_input,out_of_range_parameters,actions_on_parameters)
        return out_of_range_parameters, actions_on_parameters

def get_out_of_range_parameter_EN(BMS_input,out_of_range_parameters,actions_on_parameters):
    
    for parameter,value in BMS_input.items() :
        check_tolerance_range_EN(parameter,value,out_of_range_parameters,actions_on_parameters)
       
    return out_of_range_parameters, actions_on_parameters

def check_tolerance_range_EN(parameter,value,out_of_range_parameters,actions_on_parameters):
     if (value < BMS_allowed_range[parameter]['min']):
            out_of_range_parameters[parameter] = " Low Breach"
            actions_on_parameters[parameter]= 'value to be increased'
     elif (value > BMS_allowed_range[parameter]['max']):
            out_of_range_parameters[parameter] = " High Breach"
            actions_on_parameters[parameter]= 'value to be decreased'
     else :
         record_warnings.get_warning_EN(parameter,value,out_of_range_parameters,actions_on_parameters)




def check_battery_is_ok(BMS_input):
    out_of_range_parameters, actions_on_parameters = out_of_range_parameter_language(BMS_input)
    for parameter,value in out_of_range_parameters.items():
        print(f"\nparameter: {parameter} is : {value} : action --> {actions_on_parameters[parameter]}")
    if len(out_of_range_parameters) == 0: 
        #print(out_of_range_parameters)
        #print(actions_on_parameters)
        return True
    else :
       # print(out_of_range_parameters)
        #print(actions_on_parameters)
        return False
