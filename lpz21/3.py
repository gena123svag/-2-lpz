powers = [45, 120, 78, 95, 150, 32, 200, 67, 88, 175]

def top_k(lst, k=3):
    top = [float('-inf')] * k
    for x in lst:
        for i in range(k):
            if x > top[i]:
                top.insert(i, x)
                top.pop()
                break
    return top

print("Три самых сильных:", top_k(powers))