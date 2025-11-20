# P5: Consider int val=0xCAFE; Write expressions using bitwise operators that do the following:
                # 1. test if at least three of last four bits (LSB) are on
                # 2. reverse the byte order (i.e., produce val=0xFECA)
                # 3. rotate four bits (i.e., produce val=0xECAF)

val = 0xCAFE

last4 = val & 0xF
three_on = (bin(last4).count("1") >= 3)

print("1. At least 3 of last 4 bits ON? :", three_on)


reversed_bytes = ((val & 0xFF) << 8) | ((val >> 8) & 0xFF)

print("2. Reverse byte order        :", hex(reversed_bytes))
rotated = ((val >> 4) | ((val & 0xF) << 12)) & 0xFFFF

print("3. Rotate 4 bits             :", hex(rotated))  