num = [[] for x in range(9)]  
max = 0 
idx_i = 0 
idx_j = 0 
for i in range(9):
    nums = list(map(int,input().split()))
    nums2 = sorted(nums)
    if nums2[-1] > max :
        max = nums2[-1]
        idx_i = i 
        idx_j = int(nums.index(nums2[-1]))
    num[i].append(nums)
print(max)
print(idx_i+1,end=' ')
print(idx_j+1,end=' ')
