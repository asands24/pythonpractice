cart = [15, 42, 120, 9, 5, 380]

discount = int(input())
total = 0

for item in cart:
    total += (item - (item*discount/100))
else:
    print(total)