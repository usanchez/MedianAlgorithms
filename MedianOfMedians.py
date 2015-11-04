__author__ = 'Unai'


def medianOfMedians(l, j):
    if len(l) < 10:
        l.sort()
        return l[j]
    s = []
    lIndex = 0
    while lIndex+5 < len(l)-1:
        s.append(l[lIndex:lIndex+5])
        lIndex += 5
    s.append(l[lIndex:])
    meds = []
    for subList in s:
        meds.append(medianOfMedians(subList, int((len(subList)-1)/2)))
    med = medianOfMedians(meds, int((len(meds)-1)/2))
    l1 = []
    l2 = []
    l3 = []
    for i in l:
        if i < med:
            l1.append(i)
        elif i > med:
            l3.append(i)
        else:
            l2.append(i)
    if j < len(l1):
        return medianOfMedians(l1, j)
    elif j < len(l2) + len(l1):
        return l2[0]
    else:
        return medianOfMedians(l3, j-len(l1)-len(l2))

lst = [70, 120, 170, 200, 254, 422, 42, 43, 423, 453, 523, 52, 323, 42, 3, 42, 34]

print(medianOfMedians(lst, len(lst)/2))