ESC = "\x1b["
print(ESC + "45m")  # set background color
print(ESC + "32m")  # set foreground color
print(ESC + "2J")   # clear screen
for i in range(21):
    print(ESC + "{0};{0}H".format(i) + "█", end="")  # print block at 1,1
print(ESC + "10;15H", end='')
print(ESC + "41m", end='')
print(' '*5, end='')
print(ESC + "10;20H", end='')
try:
    input()
finally:
    print(ESC + "0m")
