import battery_test
import Early_warnings




if __name__ == '__main__':
    #assert(EV_test.battery_is_ok(25, 70, 0.7) is True)
    #assert(EV_test.battery_is_ok(50, 85, 0) is False)
    battery_test.set_language('DE')
    #Early_warnings.get_warning({'temperature' : 3,'soc' : 76,'charge_rate' : 0.7})
    assert(battery_test.check_battery_is_ok({'temperature' : 25,'soc' : 78,'charge_rate' : 0.9}) is False) 
    #assert(battery_test.check_battery_is_ok({'temperature' : 25,'soc' : 78,'charge_rate' : 0.4}) is True)
    assert(battery_test.check_battery_is_ok({'temperature' : 50,'soc' : 85,'charge_rate' : 0}) is False)
