import os
os.system('clear')

# n: 5
# 1
# 22
# 333
# 4444
# 55555

# n = 5
# for a in range(1, n+1): # 1, 2, 3, 4, 5
#     for i in range(1, a+1): # 1..5
#         print (a, end='')
#     print()
# print()

# for luar (selalu yang mengulang tugas for dalam)

# for dalam (selalu yang mencetak bintangnya)
#1 1
#2 1, 2
#3 1, 2, 3
#4 1, 2, 3, 4
#5 1, 2, 3, 4, 5

# 54321
# 5432
# 543
# 54
# 5

# 8..2
# end-nya exclude
# 1, 2, 3, 4
# 4, 3, 2, 1
# n = 5
# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#         print (n-j+1, end='')
#     print()

# *****
#  ****
#   ***
#    **
#     *
# n = 5
# for i in range(1, n+1):
#     for j in range(1, n+1): 
#         if j >= i: 
#             print ('*', end='')
#         else:
#             print (' ', end='')
#     print()

#     *
#    **
#   ***
#  ****
# *****
n = 5
for i in range(n, 0, -1): # 1..5
    for j in range(1, n+1): 
        if j >= i: 
            print ('*', end='')
        else:
            print (' ', end='')
    print()