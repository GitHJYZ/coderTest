def test_big():
    S ="password__a12345678_timeout_100"
    S1="aaa_password_\"a12_45678\"_timeout__100_\"\"_"
    S =S.strip('_')
    s1 = "\""
    s2 = "_"
    res = []
    gps = 0
    res1 = []

    if s1 not in S and s2 not in S:
        print("ERROR")
    else:
        for i in range(len(S)):
            res.append(S[i])
            if (S[i] == '_' and S[i + 1] == '_') or (S[i] == '_' and S[i + 1] == '\"'):
                break

        for j in range(len(res),len(S)):
            if s1 in S and (S[j] == '\"' and S[j + 1] == '_'):
                gps = j
                break
            elif s1 not in S and (S[j].isalnum()) and S[j+1]=='_':
                gps = j
                break

        for k in range(gps+1,len(S)):
            res1.append(S[k])
        print(''.join(res) + '******'+ ''.join(res1))


