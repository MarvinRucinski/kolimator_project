import time

def setup_connection():
    autobdr = bytes([0x55])
    rdstatus = bytes([0xAA, 0x80, 0x00, 0x00, 0x80])
    rdiv = bytes([0xAA, 0x80, 0x00, 0x06, 0x86])

    try:
        import serial
        ser = serial.Serial('/dev/serial0', 19200, timeout=2)
        ser.write(autobdr)
        time.sleep(0.1)
        ser.write(rdstatus)
        time.sleep(0.1)
        ser.write(rdiv)
        time.sleep(0.1)
        return ser, None
    except Exception as e:
        return None, f"Błąd łączenia: {e}"

def read_data(ser, fast):
    shotslow = bytes([0xAA, 0x00, 0x00, 0x20, 0x00, 0x01, 0x00, 0x01, 0x22])
    shotfast = bytes([0xAA, 0x00, 0x00, 0x20, 0x00, 0x01, 0x00, 0x02, 0x23])

    if fast:
        ser.write(shotfast)
    else:
        ser.write(shotslow)
    
    time.sleep(2)
    if ser.in_waiting > 0:
        incomingByte = ser.read(18)
        incomingByte = ser.read(13)
        if len(incomingByte) >= 10:
            val = incomingByte[6] << 24 | incomingByte[7] << 16 | incomingByte[8] << 8 | incomingByte[9]
            val_m = val / 1000
            return val_m, None
        else:
            return None, "Odebrano niepełne dane."
    else:
        return None, "Brak danych, czekam..."
        
def get_distance(fast=False):
    ser, err = setup_connection()
    if ser:
        try:
            return read_data(ser, fast)
        finally:
            ser.close()
    else:
        return None, err

