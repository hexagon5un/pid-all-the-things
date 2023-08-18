import time
from demo import adc, throttle

time.sleep(5)

setpoint = 305

P_term = 0
I_term = 0
D_term = 0

error = setpoint - adc.read()
error_sum = 0
last_error = 0
last_time = time.ticks_us()

def debug_print():
    count = 0
    while True:
        time.sleep_ms(10)
        count = count + 1
        if count % 10 == 0:
            print("error", error, "P", P_term, "I", I_term, "D", round(D_term,2))
        yield 
print_and_wait = debug_print()

## Our tuning parameters
kp = 1*1/10
ki = 1 * 1/10000000  
kd = 1*100000

while True:
    
    error = setpoint - adc.read()
    time_change = time.ticks_us() - last_time  
    error_sum = error_sum + error * (time_change)
    
    ## TODO: implement PID loop
    P_term = kp * error
    I_term = ki * error_sum
    D_term = kd * (error-last_error) / time_change;
    
    throttle(P_term + I_term + D_term)
    
    ## update
    last_error = error
    last_time = time.ticks_us()
    next(print_and_wait) 

        