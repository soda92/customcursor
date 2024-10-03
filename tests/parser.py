from kaitaistruct import KaitaiStream, BytesIO
from ico import Ico
from bmp import Bmp


from pathlib import Path

CURRENT = Path(__file__).resolve().parent
raw = bytearray(CURRENT.joinpath("Cursors_ico/aero_arrow.ico").read_bytes())
raw[2] = 1
CURRENT.joinpath("1.ico").write_bytes(raw)

data = Ico(KaitaiStream(BytesIO(raw)))

print(data)
a=1

bmp1 = bytearray(data.images[0].img)
a =  bytearray(b'BM\x28\x08\x01\x00\x00\x00\x00\x00\x40\x00\x00\x00')
CURRENT.joinpath("1.bmp").write_bytes(a)
a = a+ bmp1

data2 = Bmp(KaitaiStream(BytesIO(a)))
print(data2)
