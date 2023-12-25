cal = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
DD = ['MON','TUE','WED','THU','FRI','SAT','SUN']
sum,mon, day = 0,0,0

x,y = map(int,input().split())
if x != 1 : 
    for i in range(1,x):
        sum += cal[i]
    sum += y
else:
    sum += y 

print(DD[sum%7-1]) 
