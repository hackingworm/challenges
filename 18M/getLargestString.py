def getLargestString(s: list, k: int) -> list:
    sorted_s = sorted(s, reverse = True);

    i = 0
    while len(sorted_s) > i:
        j = i + 1
        while len(sorted_s) > j and (i + k) > j and sorted_s[i] == sorted_s[j]:
            j += 1

        nxt = j
        if i + k == j:
            while len(sorted_s) > j and sorted_s[i] == sorted_s[j]:
                j += 1

            if len(sorted_s) > j:
                c = sorted_s[i + k]
                sorted_s[i + k] = sorted_s[j]
                sorted_s[j] = c
            else:
                del sorted_s[i + k]
        i = nxt

    return ''.join(sorted_s)

if __name__ == '__main__':
    print(getLargestString("baccc", 2))
    print(getLargestString("zzzazz", 2))
    print(getLargestString("axxzzx", 2))
