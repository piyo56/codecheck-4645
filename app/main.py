# coding: utf-8
import sys

def is_valid(argv):

    # 引数の数をチェック
    if len(argv) < 3:
        sys.stderr.write('引数の数が不正\n')
        return False
    
    hour   = argv[1]
    minute = argv[2]
    
    # 数字が3桁以上
    if len(hour) >= 3 or len(minute) >= 3:
        sys.stderr.write('数字が3桁以上\n')
        return False

    # 数字の頭に0が入っている
    if hour[0] == "0" or minute[0] == "0":
        sys.stderr.write('頭に0が入っている\n')
        return False
    
    # 数字でないものが混ざっている
    valid_nums = [str(d) for d in range(1,10)]
    for h in hour:
        if not h in valid_nums:
            sys.stderr.write('数字でないものがある\n')
            return False
    for m in minute:
        if not m in valid_nums:
            sys.stderr.write('数字でないものがある\n')
            return False

    return True

def calc_flags(num):
    if num == 1:
        return [[1,0,0,0,0], [0,1,0,0,0]]
    elif num == 2:
        return [[1,1,0,0,0], [0,0,1,0,0]]
    elif num == 3:
        return [[1,0,1,0,0], [0,1,1,0,0], [0,0,0,1,0]]
    elif num == 4:
        return [[1,0,0,1,0], [0,1,0,1,0], [1,1,1,0,0]]
    elif num == 5:
        return [[1,1,0,1,0], [0,0,1,1,0], [0,0,0,0,1]]
    elif num == 6:
        return [[1,0,0,0,1], [0,1,0,0,1]]
    elif num == 7:
        return [[1,1,0,0,1], [1,1,1,1,0],[0,0,1,0,1]]
    elif num == 8:
        return [[0,0,0,1,1], [0,1,1,0,1], [1,0,1,0,1]]
    elif num == 9:
        return [[1,1,1,0,1], [0,1,0,1,1], [1,0,0,1,1]]
    elif num == 10:
        return [[0,0,1,1,1]]
    elif num == 11:
        return [[1,0,1,1,1], [0,1,1,1,1]]

def main(hour, minute):
    hour_flags   = calc_flags(hour)
    minute_flags = calc_flags(minute)
    
    for hour_flag in hour_flags:
        for minute_flag in minute_flags:
            answer = ""
            for i,j in zip(hour_flag, minute_flag):
                if i == 1 and j == 0:
                    answer += "b"
                elif i == 0 and j == 1:
                    answer += "r"
                elif i == 1 and j == 1:
                    answer += "g"
                else:
                    break

            if len(answer) == 5:
                return answer
    return "rrrrr"

if __name__=="__main__":
    if is_valid(sys.argv):
        hour   = int(sys.argv[1])
        minute = int(sys.argv[2])
        answer = main(hour, int(minute / 5))
        print(answer)
    else:
        print("rrrrr")
