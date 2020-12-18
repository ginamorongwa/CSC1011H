import math

UTC = "11:59:53.03+02"  # input("Enter a time (hh:mm:ss.sTZD):\n")

s = UTC[UTC.index('.') - 2:-3]

s = round(float(s), 3)
ss = math.floor(s)

s = str(s)
s = s[s.index('.') + 1:]
if len(s) == 2:
    s = s + '0'
s = int(s)
s = '{:03}'.format(s)

ss = ss / 60
f = math.floor(ss)
ss = (ss - f) * 60
ss = '{:02}'.format(int(ss))


mm = int(UTC[3:5]) + f
mm = mm / 60
f = math.floor(mm)
mm = (mm - f) * 60
mm = '{:02}'.format(int(mm))

hh = int(UTC[0:2]) + f
TZD = int(UTC[-3:])
hh = hh + TZD

if hh >= 24:
    hh = hh - 24
elif hh < 0:
    hh = hh + 24
hh = '{:02}'.format(hh)

print("The local time is {}:{}:{}:{}".format(hh, mm, ss, s))
