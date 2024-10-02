def largestOverlap(self, img1, img2):
    ones1 = set()
    ones2 = set()
    n = len(img1)
    for a in range(n):
        for b in range(n):
            if img1[a][b] == 1:
                ones1.add((a,b))
            if img2[a][b] == 1:
                ones2.add((a,b))

    count = 0

    for i in range(-n + 1, n):
        for j in range(-n + 1, n):
            curr = 0
            for x, y in ones1:
                if (x + i, y + j) in ones2:
                    curr += 1
            count = max(count, curr)

    return count
