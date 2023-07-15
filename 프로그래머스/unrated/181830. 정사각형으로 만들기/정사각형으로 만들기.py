def solution(arr):
    row = len(arr) 
    col = len(arr[0])
    print(row)
    print(col)
    if row > col : 
        for i in range(row):
            for j in range(row-col):
                arr[i].append(0)
    else:
        addrow = [0 for x in range(col)]
        for i in range(col-row):
            arr.append(addrow)
    return arr
            