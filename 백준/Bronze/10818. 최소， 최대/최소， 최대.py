import sys 
input = sys.stdin.readline

n = int(input().strip())
num = list(map(int,input().strip().split()))
num.sort()  # 입력최대개수 : 1000000, sort() 함수 >> O(nlogn)
print(num[0],num[-1])