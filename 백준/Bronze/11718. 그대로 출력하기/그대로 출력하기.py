import sys
while True:
    try:
        s = sys.stdin.readline().strip()
        if len(s) == 0 : break 
        else:   print(s)
    except:
        break