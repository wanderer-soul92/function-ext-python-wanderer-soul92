from battery_test import BMS_allowed_range

class get_warning:

	def __init__(self, BMS_input):
		self.temperature = BMS_input["temperature"]
		self.soc = BMS_input["soc"]
		self.charge_rate = BMS_input["charge_rate"]
		self.check_temperature_warning()
		self.check_soc_warning()
		self.check_charge_rate_warning_low()
		self.check_charge_rate_warning_high()

	def check_temperature_warning(self):
		if self.temperature in range(BMS_allowed_range['temperature']['min'],int (BMS_allowed_range['temperature']['min'] + BMS_allowed_range['temperature']['max']*0.05+1):
			print('Warning: Approaching low_teperature')
		elif self.temperature in range(40,45):
			print("Warning: Approaching peak_temperature")

	def check_soc_warning(self):
		if self.soc in range(20,25):
			print('Warning: Approaching low_teperature')
		elif self.soc in range(75,80):
			print("Warning: Approaching peak_temperature")

	def check_charge_rate_warning_low(self):
		if (self.charge_rate <= 0.1 ):
			print('Warning: Approaching low_charge_rate')
			
	def check_charge_rate_warning_high(self):
		if (self.charge_rate >= 0.7 ) and (self.charge_rate <= 0.8 ):
			print("Warning: Approaching peak_charge_rate")
