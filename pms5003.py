import serial
import struct
import time

ser = serial.Serial("/dev/serial0", baudrate=9600, timeout=2)

def read_pms5003():
    while True:
        data = ser.read(32)
        if data[0] == 0x42 and data[1] == 0x4D:
            frame_length = struct.unpack(">H", data[2:4])[0]
            if frame_length == 28:
                pm1_cf1 = struct.unpack(">H", data[4:6])[0]
                pm25_cf1 = struct.unpack(">H", data[6:8])[0]
                pm10_cf1 = struct.unpack(">H", data[8:10])[0]

                pm1_0 = struct.unpack(">H", data[10:12])[0]
                pm2_5 = struct.unpack(">H", data[12:14])[0]
                pm10 = struct.unpack(">H", data[14:16])[0]

                print("PM1.0: {} μ g/m3,\nPM2.5: {} μ g/m3,\nPM10: {} μ g/m3\n\n".format(pm1_0, pm2_5, pm10))
                time.sleep(1)
        else:
            print("IDK");
try:
    read_pms5003()
except KeyboardInterrupt:
    print("Stop")
    ser.close()

