def change(amount):
    print("amount is set to =")
    print(amount)
    solutions = []
    if amount in range(24,1001):
        for i in range(0,200):
            for j in range(0,200):
                if amount == 5 * i + 7 * j:
                    solutions.append(
                        [5 for k in range(0,i)] + [7 for k in range(0,j)]
                        )
        return solutions
    else:
        return

value = change(24)
print("after call to change")
print(value)
