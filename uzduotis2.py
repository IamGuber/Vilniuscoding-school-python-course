# Sukurkite ir išveskite tokius nurodytus ranges:
# [1, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99]
# [3, 12, 21, 30, 39, 48, 57, 66, 75, 84, 93]
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]

print(list( range(1, 100, 7)))
print(list( range(3, 100, 9)))
print(list( range(10, 0, -1)))
print(list( range(100, 0, -10)))
print(list( range(10, -1, -1)))
print(list( range(50, 0, -5)))