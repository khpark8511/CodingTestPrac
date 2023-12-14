w = list(input())
len = len(w)
w = [w[i:i+10] for i in range(0, len,10)]
for i in w:
    print(''.join(i))