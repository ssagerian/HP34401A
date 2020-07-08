
import HP34401A as DMM
import time

dmm0 = DMM.HP34401A('com44')

if not dmm0.dmm_id_check():
   print('HP34401A not found')
   exit(1)

dmm0.set_display("test1")

dmm0.route_terminals()

print("set ADC")
mode = dmm0.OperMode.ADC
dmm0.set_mode_(mode)
dmm0.set_sample_count(2)
sample = dmm0.get_sample()
print('sample ', sample)
if not dmm0.error_check():
    exit(1)


print("set AAC")
mode = dmm0.OperMode.AAC
dmm0.set_mode_(mode)
time.sleep(2)
dmm0.set_sample_count(1)
sample = dmm0.get_sample()
print('sample ', sample)
if not dmm0.error_check():
    exit(1)

print("set VAC")
mode = dmm0.OperMode.VAC
dmm0.set_mode_(mode)
#dmm0.set_sample_count(1)
sample = dmm0.get_sample()
print('sample ', sample)
if not dmm0.error_check():
    exit(1)


print("set VDC")
mode = dmm0.OperMode.VDC
dmm0.set_mode_(mode)
sample = dmm0.get_sample()
print('sample ', sample)
if not dmm0.error_check():
    exit(1)

print("set RS2")
mode = dmm0.OperMode.RS2
dmm0.set_mode_(mode)
sample = dmm0.get_sample()
print('sample ', sample)
if not dmm0.error_check():
    exit(1)


print("set RS4")
mode = dmm0.OperMode.RS4
dmm0.set_mode_(mode)
sample = dmm0.get_sample()
print('sample ', sample)
if not dmm0.error_check():
    exit(1)

print("set PER")
mode = dmm0.OperMode.PER
dmm0.set_mode_(mode)
sample = dmm0.get_sample()
print('sample ', sample)
if not dmm0.error_check():
    exit(1)

print("set FREQ")
mode = dmm0.OperMode.FREQ
dmm0.set_mode_(mode)
sample = dmm0.get_sample()
print('sample ', sample)
if not dmm0.error_check():
    exit(1)

print("set CONT")
mode = dmm0.OperMode.CONT
dmm0.set_mode_(mode)
sample = dmm0.get_sample()
print('sample ', sample)
if not dmm0.error_check():
    exit(1)


time.sleep(1)
print('done!')