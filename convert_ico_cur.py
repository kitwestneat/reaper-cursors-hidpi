import sys

# http://www.daubnet.com/en/file-format-ico
# http://www.daubnet.com/en/file-format-cur
def convert_ico_to_cur(ico_path, cur_path, hotspot_x, hotspot_y):
    with open(ico_path, 'rb') as ico_file:
        ico_data = ico_file.read()

    with open(cur_path, 'wb') as cur_file:
        # Write .CUR header
        cur_file.write(b'\x00\x00\x02\x00\x01\x00')
        cur_file.write(ico_data[6:10])  # Copy image dimensions from .ICO
        cur_file.write(hotspot_x.to_bytes(2, 'little'))  # Write hotspot X coordinate
        cur_file.write(hotspot_y.to_bytes(2, 'little'))  # Write hotspot Y coordinate
        cur_file.write(ico_data[14:])  # Copy rest of ico

# Usage
infn = sys.argv[1]
outfn = sys.argv[2]
x = int(sys.argv[3]) * 2
y = int(sys.argv[4]) * 2
convert_ico_to_cur(infn, outfn, x, y)

