from pathlib import Path

CURRENT = Path(__file__).resolve().parent

CURRENT.joinpath("Cursors_ico").mkdir(exist_ok=True)
files = list(CURRENT.joinpath("Cursors").glob("*.cur"))

for file in files:
    dest = CURRENT.joinpath("Cursors_ico")
    data = file.read_bytes()
    data = bytearray(data)
    data[2] = 0x01
    dest.joinpath(file.stem + ".ico").write_bytes(data)
