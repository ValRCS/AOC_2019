print("Day 1")
# with open('input1.txt') as f:
#     alist = [line.rstrip() for line in f]
# # file is closed here and we have our list ready to process
# print(alist[:5])
with open('input1.txt') as f:
    print(sum([int(line.rstrip()) // 3 - 2 for line in f]))
