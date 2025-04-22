import numpy as np

s = input()
s = [np.array(s)]

right_padding = np.array([x.rjust(15, '_') for x in s])
# left_padding = np.array([x.ljust(15, '_') for x in s])
# center_padding = np.char.center(s, width=15, fillchar='_')

