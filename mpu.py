import serial
def parsData():
    ser = serial.Serial("COM4", 115200)
    while True:
        line = ser.readline().decode(errors="ignore").strip()

        if not line.startswith("IMU,"):
            continue
        data = line.split(",")

        if len(data) != 4:
            continue

        return data

