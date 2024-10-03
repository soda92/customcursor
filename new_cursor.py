from pathlib import Path

file = Path("py/aero_link.ico")
data = bytearray(file.read_bytes())
data[10] = 102
data[11] = 0
data[12] = 0
data[13] = 0
data[2] = 0x02

Path("py/aero_link.cur").write_bytes(data)


file = Path("py/221.ico")
data = bytearray(file.read_bytes())
data[10] = 127
data[11] = 0
data[12] = 0
data[13] = 0
data[2] = 0x02

Path("py/33.cur").write_bytes(data)
