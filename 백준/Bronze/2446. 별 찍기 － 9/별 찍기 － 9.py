n = int(input())
for i in range(1,2*n):
    if i <= n :
        print(' '*(i-1)+'*'*(2*n-2*i+1))
    else:
        j = i - n 
        print(' '*(i-(2*j+1))+'*'*(2*j+1))
