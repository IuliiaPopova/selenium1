def find_missing_letter(chars):
    l = []
    for i in range(0,len(chars)):
        l.append(ord(chars[i]))
    return l

    start = l[0]
    end = l[-1]
    return sorted(set(range(start, end + 1)).difference(l))

print(find_missing_letter(['a','b','c','d','f']))