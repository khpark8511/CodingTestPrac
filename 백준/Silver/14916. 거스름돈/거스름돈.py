def sol():
    n = int(input())
    f = 0
    if n < 5 : 
        if n%2 == 0 : return int(n//2)
        else: return -1
    else:
        num = n//5
        for i in range(num,-1,-1):
            f  = i  # 5의몫
            n2  = n-(5*i)  #n을 5를곱한값을 빼주기 
            if n2 %2 ==0 : return f + int(n2//2)
        return -1

print(sol())