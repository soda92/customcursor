from pathlib import Path

file = Path("aero_link.ico")
data = bytearray(file.read_bytes())
data[10] = 102
data[2] = 0x02

Path("aero_link.cur").write_bytes(data)
