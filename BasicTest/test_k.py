def test_big():
    str1 = ['A', 'b', 'C', 'd', 'e', 'F', 'G']
    num = 3
    str2 = sorted(str1)
    m = len(str2)
    n = len(str1)
    if num > n:
        print(m)
    else:
        for i in range(n):
            if str1[i] == str2[num-1]:
                print(i)
                break