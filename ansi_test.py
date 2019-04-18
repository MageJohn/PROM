ESC = "\x1b["
print(ESC + "45m")  # set background color
print(ESC + "32m")  # set foreground color
print(ESC + "2J")   # clear screen
for i in range(21):
    print(ESC + "{0};{0}H".format(i) + "█", end="")  # print block at 1,1
try:
    input()
finally:
    print(ESC + "0m")
