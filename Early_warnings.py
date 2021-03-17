import battery_test 

BM = {'temperature': {'min': 0, 'max': 45},
                'soc': {'min': 20, 'max': 80},
                'charge_rate': {'min': 0, 'max': 0.8}}


class get_warnings:

    def __init__(self, parameter,value,out_of_range_parameters,actions_on_parameters):
        self.parameter = parameter
        self.value = value
        self.out_of_range_parameters = out_of_range_parameters
        self.actions_on_parameters = actions_on_parameters
        self.get_tolerance()
        self.get_warnings()
        

    def get_tolerance(self):
        tolerance_value = BM[self.parameter]['max'] * 0.05 
        return tolerance_value
    
    
    def get_warnings(self):
        if self.parameter == 'charge_rate':
            self.check_charge_rate_warning_low()
            self.check_charge_rate_warning_high()
        else :
            self.check_parameter_warning()


    def check_parameter_warning(self):
        if self.value in range(BM[self.parameter]['min'], int (BM[self.parameter]['min'] + BM[self.parameter]['max']*0.05+1)):
            self.actions_on_parameters[self.parameter] = "Increase the " + str(self.parameter)
            self.out_of_range_parameters[self.parameter] = "Approaching low_" + str(self.parameter)
            return out_of_range_parameters, actions_on_parameters
        elif self.value in range(int (BM[self.parameter]['max'] - BM[self.parameter]['max']*0.05 - 1), BM[self.parameter]['max']):
            self.actions_on_parameters[self.parameter] = "Decrease the " + str(self.parameter)
            self.out_of_range_parameters[self.parameter] = "Approaching low_" + str(self.parameter)
            return self.out_of_range_parameters, self.actions_on_parameters


    def check_charge_rate_warning_low(self):
        if (self.value < float(BM[self.parameter]['min'] + BM[self.parameter]['max']*0.05)) and ( self.value >= 0):
            self.actions_on_parameters[self.parameter] = "Increase the charge_rate"
            self.out_of_range_parameters[self.parameter] = "Approaching low_charge_rate"
            return self.out_of_range_parameters, self.actions_on_parameters

    def check_charge_rate_warning_high(self):
        if (self.value > float(BM[self.parameter]['max'] - BM[self.parameter]['max']*0.05) ) and (self.value <= 0.8 ):
            self.actions_on_parameters[self.parameter] = "Increase the charge_rate"
            self.out_of_range_parameters[self.parameter] = "Approaching low_charge_rate"
            return self.out_of_range_parameters, self.actions_on_parameters

