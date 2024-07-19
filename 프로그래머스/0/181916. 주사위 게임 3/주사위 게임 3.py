def solution(a, b, c, d):
    arr = [a, b, c, d]
    cnt = [arr.count(item) for item in arr]

    if max(cnt)==4: return a*1111

    elif max(cnt)==3:
        return (10 * (arr[cnt.index(3)]) + (arr[cnt.index(1)]))**2       

    elif max(cnt)==2:    
        if 1 in cnt:
            return arr[cnt.index(1)] * arr[cnt.index(1, cnt.index(1)+1,4)]
        else:
            for item in arr:
                if a!=item:
                    return (a+item) * abs(a-item)

    else: return min(arr)