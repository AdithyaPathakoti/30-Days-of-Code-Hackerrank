#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
a=bin(n)[2:]
b=a.split('0')
c=max(len(i) for i in b)
print(c)
