
import HP34401A as DMM
import time

dmm0 = DMM.HP34401A('com44')

# if not dmm0.dmm_id_check():
#    print('HP34401A not found')
#    exit(1)
#
dmm0.set_display("test1")
dmm0.route_terminals()

print("step ADC")
mode = dmm0.OperMode.ADC
dmm0.set_mode_(mode)
dmm0.set_sample_count(1)
if not dmm0.error_check():
    exit(1)
time.sleep(0.5)
while True:
    sample = dmm0.get_sample()
    print('sample ', sample)
    if not dmm0.error_check():
        exit(1)
    time.sleep(0.5)

print("step AAC")
mode = dmm0.OperMode.AAC
dmm0.set_mode_(mode)
dmm0.set_sample_count(1)
if not dmm0.error_check():
    exit(1)
time.sleep(1)
#dmm0.set_sample_count(1)
sample = dmm0.get_sample()
print('sample ', sample)
#dmm0.error_check()

print("step VAC")
mode = dmm0.OperMode.VAC
dmm0.set_mode_(mode)
dmm0.set_sample_count(1)
if not dmm0.error_check():
    exit(1)
time.sleep(1)
sample = dmm0.get_sample()
print('sample ', sample)
#dmm0.error_check()

print("step VDC")
mode = dmm0.OperMode.VDC
dmm0.set_mode_(mode)
dmm0.set_sample_count(1)
if not dmm0.error_check():
    exit(1)
time.sleep(1)
sample = dmm0.get_sample()
print('sample ', sample)

print("step RS2")
mode = dmm0.OperMode.RS2
dmm0.set_mode_(mode)
dmm0.set_sample_count(1)
if not dmm0.error_check():
    exit(1)
time.sleep(1)
sample = dmm0.get_sample()
print('sample ', sample)

print("step RS4")
mode = dmm0.OperMode.RS4
dmm0.set_mode_(mode)
dmm0.set_sample_count(1)
if not dmm0.error_check():
    exit(1)
time.sleep(1)
sample = dmm0.get_sample()
print('sample ', sample)

print("step PER")
mode = dmm0.OperMode.PER
dmm0.set_mode_(mode)
dmm0.set_sample_count(1)
if not dmm0.error_check():
    exit(1)
time.sleep(1)
sample = dmm0.get_sample()
print('sample ', sample)

print("step FREQ")
mode = dmm0.OperMode.FREQ
dmm0.set_mode_(mode)
dmm0.set_sample_count(1)
if not dmm0.error_check():
    exit(1)
time.sleep(1)
sample = dmm0.get_sample()
print('sample ', sample)

print("step CONT")
mode = dmm0.OperMode.CONT
dmm0.set_mode_(mode)
dmm0.set_sample_count(1)
if not dmm0.error_check():
    exit(1)
time.sleep(1)
sample = dmm0.get_sample()
print('sample ', sample)

