import Record_warnings_DE
import battery_test
def get_out_of_range_parameter_DE(BMS_input,out_of_range_parameters,actions_on_parameters):
    
    for parameter,value in BMS_input.items() :
        check_tolerance_range_DE(parameter,value,out_of_range_parameters,actions_on_parameters)
       
    return out_of_range_parameters, actions_on_parameters

def check_tolerance_range_DE(parameter,value,out_of_range_parameters,actions_on_parameters):
     if (value < battery_test.BMS_allowed_range[parameter]['min']):
            out_of_range_parameters[parameter] = " Niedriger Bruch"
            actions_on_parameters[parameter]= 'Wert erhht werden'
     elif (value > battery_test.BMS_allowed_range[parameter]['max']):
            out_of_range_parameters[parameter] = " Hoher Bruch"
            actions_on_parameters[parameter]= 'Wert verringert werden'
     else :
         Record_warnings_DE.get_warning_DE(parameter,value,out_of_range_parameters,actions_on_parameters)


