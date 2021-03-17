import battery_test


BM = {'temperature': {'min': 0, 'max': 45},
                'soc': {'min': 20, 'max': 80},
                'charge_rate': {'min': 0, 'max': 0.8}}


def get_warning_EN(parameter,value,out_of_range_parameters,actions_on_parameters):
	
	if parameter == 'charge_rate':
		check_charge_rate_warning_low_EN(parameter,value,out_of_range_parameters,actions_on_parameters)
		check_charge_rate_warning_high_EN(parameter,value,out_of_range_parameters,actions_on_parameters)
	else :
		check_parameter_warning_EN(parameter,value,out_of_range_parameters,actions_on_parameters)

def check_parameter_warning_EN(parameter,value,out_of_range_parameters,actions_on_parameters):
        if value in range(BM[parameter]['min'], int (BM[parameter]['min'] + BM[parameter]['max']*0.05+1)):
            actions_on_parameters[parameter] = "Increase the " + str(parameter)
            out_of_range_parameters[parameter] = "Approaching low_" + str(parameter)
        elif value in range(int (BM[parameter]['max'] - BM[parameter]['max']*0.05 - 1), BM[parameter]['max']):
            actions_on_parameters[parameter] = "Decrease the " + str(parameter)
            out_of_range_parameters[parameter] = "Approaching low_" + str(parameter)

def check_charge_rate_warning_low_EN(parameter,value,out_of_range_parameters,actions_on_parameters):
        if (value < float(BM[parameter]['min'] + BM[parameter]['max']*0.05)) and ( value >= 0):
            actions_on_parameters[parameter] = "Increase the charge_rate"
            out_of_range_parameters[parameter] = "Approaching low_charge_rate"

def check_charge_rate_warning_high_EN(parameter,value,out_of_range_parameters,actions_on_parameters):
		if (value > float(BM[parameter]['max'] - BM[parameter]['max']*0.05) ) and (value <= 0.8 ):
			actions_on_parameters[parameter] = "Increase the charge_rate"
			out_of_range_parameters[parameter] = "Approaching high_charge_rate"