x = [7, 1, 6, 3, 8, 4]

counter = 0

for value in range(len(x)):

    for value_2 in range(value + 1, len(x)):

        counter += 1

print(counter)