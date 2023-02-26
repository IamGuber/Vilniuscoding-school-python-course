# Sukurkite ir išveskite tokius nurodytus ranges:
# [0, 1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
# [1, 3, 5, 7, 9]
# [30, 33, 36, 39, 42, 45, 48]
# [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

print(list( range(7)))
print(list( range(1, 10)))
print(list( range(2, 16)))
print(list( range(20, 31)))
print(list( range(20, 41, 2)))
print(list( range(1, 10, 2)))
print(list( range(30, 50, 3)))
print(list( range(50, 101, 5)))