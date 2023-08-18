import machine
import time

## Init
adc = machine.ADC(0)            				## create ADC object on ADC pin
motor = machine.PWM(machine.Pin(2, machine.Pin.OUT))

motor_PWM_freq=200               				## about as fast as it'll go
motor_PWM_min = int(motor_PWM_freq*1024/1000) 	## 1 ms pulse: off
motor_PWM_max = 2*motor_PWM_min  				## 2 ms pulse: full on

motor.freq(motor_PWM_freq) 
motor.duty(motor_PWM_min)
    
def scale_throttle(p):
    """scale PWM duty cycle into throttle percent"""
    p = max(p,0)
    p = min(p, 100)
    full_off = int(motor.freq()*1024/1000)
    full_on = full_off*2
    return int(p*(full_on-full_off)/100) + full_off

def throttle(p):
    """set it live"""
    motor.duty(scale_throttle(p))


    

    
