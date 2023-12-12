import struct
import sys

def get_hotspot(filename):
    with open(filename, 'rb') as f:
        f.seek(10)
        hotspot = struct.unpack('2H', f.read(4))
    return hotspot

def set_hotspot(filename, x, y):
    with open(filename, 'r+b') as f:
        f.seek(10)
        f.write(struct.pack('2H', x, y))

def main():
    if len(sys.argv) < 2:
        print("Usage: cur_hotspot.py <filename.cur> [<hotspot x> <hotspot y>]")
        return

    filename = sys.argv[1]

    if len(sys.argv) == 4:
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        set_hotspot(filename, x, y)
    else:
        hotspot = get_hotspot(filename)
        print(f"{hotspot[0]} {hotspot[1]}")

if __name__ == "__main__":
    main()

