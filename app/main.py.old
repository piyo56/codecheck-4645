#!/usr/bin/env python3
import sys

def is_valid(argv):
    if len(argv) < 3:
        return False
    
    hour   = argv[1]
    minute = argv[2]

    if len(hour) > 2 or len(minute) > 2:
        return False
    
    if hour[0] == "0" or minute[0] == "0":
        return False
    
    valid_nums = [str(d) for d in range(1,10)]
    for d in hour:
        if not d in valid_nums:
            return False

    for d in minute:
        if not d in valid_nums:
            return False

    return True

def calc_flags(num):
   
    flags = [0,0,0,0,0]
    num = int(num)

    if num == 11:
        flags = [1,0,1,1,1]
    if num == 10:
        flags = [1,1,0,1,1]
    if num == 9:
        flags = [0,1,0,1,1]
    if num == 8:
        flags = [0,0,0,1,1]
    if num == 7:
        flags = [0,0,1,0,1]
    if num == 6:
        flags = [1,0,1,1,0]
    if num == 5:
        flags = [1,1,0,1,0]
    if num == 4:
        flags = [1,1,1,0,0]
    if num == 3:
        flags = [1,0,1,0,0]
    if num == 2:
        flags = [1,1,0,0,0]
    if num == 1:
        flags = [1,0,0,0,0]
    if num == 0:
        flags = [0,0,0,0,0]

    return flags

def main(argv):
    if not is_valid(sys.argv):
      print("rrrrr")
      return

    hour   = int(sys.argv[1])
    minute = int(sys.argv[2])

    minute = int(minute/5)
    
    hour_flags   = calc_flags(hour)
    minute_flags = calc_flags(minute)
    
    ans = []
    for h, m in zip(hour_flags, minute_flags):
        if h == 1 and  m == 1:
            ans.append("g")
        elif h == 0 and m == 1:
            ans.append("r")
        elif h == 1 and m == 0:
            ans.append("b")

    for e in ans:
        print(e, end="")

if __name__=="__main__":
    main(sys.argv)
