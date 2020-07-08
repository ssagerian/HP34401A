
import serial
import time
from enum import Enum


class HP34401A:
    class OperMode(Enum):
        """
        HP34401A supports the following measurement operational modes..
        ADC DC current
        AAC AC current
        VDC DC voltage
        VAC AC voltage
        RS2 resistance 2 wire
        RS4 resistance 4 wire
        FREQ Frequency
        CONT continuity check
        DIDO diode forward voltage drop
        PER = period
        """
        ADC = 0
        AAC = 1
        VDC = 2
        VAC = 3
        RS2 = 4
        RS4 = 5
        FREQ = 6
        CONT = 7
        DIDO = 8
        PER = 9

    class OperRange(Enum):
        """
         HP34401A supports the following measurement ranges..
         4 DIGIT
         5 DIGIT
         6 DIGIT
         """
        DIG4 = 0
        DIG5 = 1
        DIG6 = 2

    def __init__(self, port, baud_rate=9600 ):
        """
        init function needs the folloing
        requires a comm port to talk
        requires a baud rate or default to 9600
        requires a number of bits per char or defaults to 8
        requires a number of stop bits or defaults to 1
        require parity spec or defaults to none
        """

        try:
            self.serial_port = serial.Serial(port, baud_rate, stopbits=1, bytesize=8, parity='N', timeout=10)
        except serial.SerialException:
            print("Is com port being used by other application?")
            print('SerialException COM port issue {0}'.format(port))
            exit(1)
        time.sleep(0.2)
        self.serial_port.write(b'*RST\x0D\x0A')
        time.sleep(1)
        self.serial_port.write(b':SYST:REMote\x0D\x0A')
        time.sleep(0.1)
        self.serial_port.write(b':SYST:BEEP\x0D\x0A')
        time.sleep(2.5)

    def route_terminals(self):
        time.sleep(0.1)
        self.serial_port.write(b':ROUTE:TERMINALS?\x0D\x0A')
        s = self.serial_port.readline()
        print(s)

    def error_check(self):
        time.sleep(0.1)
        self.serial_port.write(b':SYST:ERR?\x0D\x0A')
        time.sleep(1)
        s = self.serial_port.readline()
        error_str = s.decode('utf-8')
        error_list = error_str.split(',')
        if int(error_list[0]) == 0:
            return True
        print(error_list[0], error_list[1])
        return False

    def set_display(self, display_string):
        """
        the HP34401 has a 12 character display on the front
        use this to display name of test or some other useful info
        """
        if len(display_string) > 12:
            display = b':DISP:TEXT ' + b'\'' + bytes(display_string[:11], 'utf-8') + b'\'\x0D\x0A'
        else:
            display = b':DISP:TEXT ' + b'\'' + bytes(display_string, 'utf-8') + b'\'\x0D\x0A'
        self.serial_port.write(display)

    def set_mode_(self, mode):
        if self.OperMode.AAC == mode:
            b_mode = b':CONF:CURR:AC DEF,DEF\x0D\x0A'
        elif self.OperMode.ADC == mode:
            b_mode = b':CONF:CURR:DC DEF,DEF\x0D\x0A'
        elif self.OperMode.VDC == mode:
            b_mode = b':CONF:VOLT:DC DEF,DEF\x0D\x0A'
        elif self.OperMode.VAC == mode:
            b_mode = b':CONF:VOLT:AC DEF,DEF\x0D\x0A'
        elif self.OperMode.FREQ == mode:
            b_mode = b':CONF:FREQ DEF,DEF\x0D\x0A'
        elif self.OperMode.RS2 == mode:
            b_mode = b':CONF:RES DEF,DEF\x0D\x0A'
        elif self.OperMode.RS4 == mode:
            b_mode = b':CONF:FRES DEF,DEF\x0D\x0A'
        elif self.OperMode.CONT == mode:
            b_mode = b':CONF:CONT \x0D\x0A'
        elif self.OperMode.PER == mode:
            b_mode = b':CONF:PER DEF,DEF\x0D\x0A'
        else:
            b_mode = b':CONF:VOLT:DC DEF,DEF\x0D\x0A'
        self.serial_port.write(b_mode)
        time.sleep(1.5)    # give DMM time to configure itself

    def set_sample_count(self, count):
        """
        HP34401 can be configured to capture a number of samples per trigger event
        the max number of readings is 512, default is set to 1
        Each mode has its own sample count value, some are not changeable.
        NOTE: only change the sample count AFTER changing to the desired mode.
        """
        self.sample_count = count
        bcount = b':SAMPLE:COUNT ' + bytes(str(count), 'utf-8') + b'\x0D\x0A'
        self.serial_port.write(bcount)

    def get_sample(self):
        """
        start sampling of desired measurement, if you have more than one sample measurement
        expect the read to take a bit longer. Also the entire number of samples is returned as a
        single string, with each measurement separated by a commma, and terminated by a \n \r
        for example a two sample reading would look like .. b'-7.50000000E-09,+3.24000000E-08\r\n'
        """
        time.sleep(0.1)
        self.serial_port.write(b':READ?\x0D\x0A')
        line = self.serial_port.readline()
        return line

    def set_resolution (self, resolution):
        #        if resolution == self.OperRange.DIG4:
        #           elif resolution == self.OperRange.DIG5:
        return True

    def set_range(self,  meter_range):
        return True

    def dmm_id(self):
        time.sleep(0.1)
        self.serial_port.write(b'*IDN?\x0D\x0A')
        print(self.serial_port.readline())

    def dmm_id_check(self):
        time.sleep(0.1)
        self.serial_port.write(b'*IDN?\x0D\x0A')
        s = self.serial_port.readline()
        sstr = str(s, "utf=8")
        if sstr.find("34401A") != 0:
            return True
        else:
            return False

    sample_count = 1
