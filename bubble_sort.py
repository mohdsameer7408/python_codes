def bubble_sort(num):
    for i in range(0, len(num)):
        for j in range(0, len(num)-i-1):
            if num[j] > num[j+1]:
                t = num[j]
                num[j] = num[j+1]
                num[j+1] = t
    return num
