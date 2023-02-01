def mean(lst):
    n = len(lst)
    ttl = 0
    for i in lst:
        ttl += i
    mean = ttl/n
    return mean

def deviation(lst):
    n = len(lst)
    m = mean(lst)
    # m = float(m)
    # return m
    sum = 0
    for i in lst:
        sum+= (i-m)**2
    std_dev = (sum/(n-1))**0.5
    return float("%.2f"%std_dev)




lst = [10, 8, 13, 9, 14, 25, -5, 20, 7, 7, 4]
r1 = mean(lst)
print(r1)
r2 = deviation(lst)
print(r2)
# r3 = newArray(lst)
# print(r3)