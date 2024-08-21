n = int(input())
s = input()
g = [[] for i in range(n)]
for i in range(n - 1):
    u, v = map(int, input().split())
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

ans = 0
for i in range(n):
    cnt1 = [0] * 26
    cnt2 = [[] for j in range(26)]
    for j in g[i]:
        cnt1[ord(s[j]) - 97] += 1
        cnt2[ord(s[j]) - 97].append(j)

    for j in range(26):
        ans += cnt1[j] * (cnt1[j] - 1) // 2

    for j in range(26):
        for k in cnt2[j]:
            for l in cnt2[j]:
                if k < l:
                    ans += cnt1[ord(s[k]) - 97] - 1
                    print("%c -> %c -> %c -> %c" % (chr(ord('a') + j), s[k], s[i], s[l]))

print(ans)