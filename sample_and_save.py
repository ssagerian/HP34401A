# command line... python sample_and_save.py comport sample_rate csv_file_name


import sys
import HP34401A as DMM
import time
import msvcrt
import csv


def readInput(timeout=1):
    """
    this works for windows platforms, sorry.
    :param timeout:
    :return:
    """
    start_time = time.time()
    input = ''
    while True:
        if msvcrt.kbhit():
            byte_arr = msvcrt.getch()
            if ord(byte_arr) == 13:  # enter_key
                break
            elif ord(byte_arr) >= 32:  # space_char
                if byte_arr.upper() == b'Q':
                    input += "".join(map(chr, byte_arr))
        if len(input) == 0 and (time.time() - start_time) > timeout:
            break
    if len(input) > 0:
        return True
    else:
        return False


# validate inputs..
file_name_index = 3
sample_rate_index = 2
comport_index = 1
file_name = sys.argv[file_name_index]
csv_names = ['time stamp', 'sample 1', 'sample 2']

if len(sys.argv) != 4:
    print('command line : python DMM33401A.py comport  sample_rate file_name')
    exit(1)
# if argv doesnt contain sample_rate the default is 1
sample_rate = eval(sys.argv[sample_rate_index]) - 1  # one second

dmm = DMM.HP34401A(sys.argv[comport_index])

dmm.set_display(file_name)
mode = dmm.OperMode.ADC
dmm.set_mode_(mode)
dmm.set_sample_count(2)

# start sampling
time_since = time.time()

with open(file_name, 'wt', newline='') as csv_sample_writer:
    dmm_writer = csv.writer(csv_sample_writer, dialect='excel')
    while True:
        line = dmm.get_sample()
        line = line.replace(b"\r\n", b"")  # strip off \r\n
        line = str(time_since) + ',' + line.decode()  # add time stamp
        print(line)
        csv_fields = line.split(',')
        dmm_writer.writerow((csv_fields[0], csv_fields[1], csv_fields[2]))
        time.sleep(sample_rate)
        time_since = time.time()
        if readInput():
            break
    csv_sample_writer.close()
