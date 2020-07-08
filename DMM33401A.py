# command line... python DMM33401A comport sample_rate file_name
import os
import sys
import serial
import time
import msvcrt
from datetime import datetime
import csv


def readInput(timeout=1):
    start_time = time.time()
    input = ''
    while True:
        if msvcrt.kbhit():
            byte_arr = msvcrt.getch()
            if ord(byte_arr) == 13: # enter_key
                break
            elif ord(byte_arr) >= 32: #space_char
                if byte_arr.upper() == b'Q':
                    input += "".join(map(chr,byte_arr))
        if len(input) == 0 and (time.time() - start_time) > timeout:
            break
    if len(input) > 0:
        return True
    else:
        return False


# validate inputs..
file_name_index = 3
sample_rate_index = 2

file_name = sys.argv[file_name_index]

csv_names = ['time stamp', 'sample 1', 'sample 2']

get_ver = b':SYST:VERS?\n'
set_display = b':SYST:BEEP;:DISP:TEXT ' + b'\'' + bytes(file_name, 'utf-8') + b'\'\x0D\x0A'

if len(sys.argv) != 4:
	print('command line : python DMM33401A.py comport  sample_rate file_name')
	exit(1)
# if argv doesnt contain sample_rate the default is 1
sample_rate = eval(sys.argv[sample_rate_index]) - 1 # one second

ser = serial.Serial(sys.argv[1], 9600, stopbits=1,  bytesize=8, parity='N',  timeout=10)
ser.write(b"*RST\x0D\x0A")
time.sleep(2)
ser.write(b"SYSTem:REMote\x0D\x0A")
ser.flush()
ser.write(set_display)
time.sleep(1)
ser.write(b":CONF:CURRENT:DC 1A,DEF\x0D\x0A")
time.sleep(0.2)
ser.write(b":SAMPLE:COUNT 2\x0D\x0A")
#start sampling
time_since = time.time()
ser.write(b":READ?\x0D\x0A")
with open(file_name, 'wt', newline='') as csv_sample_writer:
	dmm_writer = csv.writer(csv_sample_writer, dialect='excel')
	while True:
		line = ser.readline()
		line = line.replace(b"\r\n", b"")       # strip off \r\n
		line = str(time_since) + ',' + line.decode()  # add time stamp
		print(line)
		csv_fields = line.split(',')
		dmm_writer.writerow((csv_fields[0], csv_fields[1], csv_fields[2]))
		time.sleep(sample_rate)
		time_since = time.time()
		ser.write(b":READ?\x0D\x0A")
		if readInput():
			break
	csv_sample_writer.close()



