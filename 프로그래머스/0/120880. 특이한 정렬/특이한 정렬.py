def solution(numlist, n):
    return sorted(numlist, key=lambda i:(abs(n-i),-i))