def ordre(m1, m2):
    i = 0
    while i < len(m1) and i < len(m2):
        if m1[i] > m2[i]:
            return False 
        if m1[i] < m2[i]:
            return True
        i += 1
    return len(m1) == i
