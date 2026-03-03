rects = []

for i in range(8):
    row = []
    for j in range(8):
        if (i + j) % 2 == 0:
            row.append(1)
        else:
            row.append(0)
    rects.append(row)


for i in range(len(rects)):
    print(rects[i])
