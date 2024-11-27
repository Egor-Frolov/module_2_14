from operator import truediv

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

numbers.remove(1)

primes = []

not_primes = []

for value in numbers:
    sum_value = 0
    for value_2 in range (2,16):
        if value % value_2 == 0:
            sum_value = sum_value + 1
    if sum_value > 1:
        not_primes.append(value)
    else:
        primes.append(value)

print (primes)
print (not_primes)
