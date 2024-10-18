with open('18.txt', 'r') as file:
    lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].split(' ')
    for j in range(len(lines[i])):
        lines[i][j] = int(lines[i][j])
for i in range(len(lines)):
    for j in range(len(lines[i])):
        lines[i][j] = [lines[i][j]]
for line in lines:
    print(line)
for i in range(len(lines)-1):
    for j in range(lines[i]):
        for k in range(len()):

            # c = 0
            # for row in lines[1:-1]:
            #     temp = []
            #     for i in range(len(dist)):
            #         temp.append(dist[i]+row[c])
            #         temp.append(dist[i]+row[c+1])
            #     c += 1
            #     dist = temp
            #     print
            # print(max(dist))
