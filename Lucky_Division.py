def is_lucky(number):
    return all(digit in "47" for digit in str(number))


def generate_lucky_numbers(n):
    lucky_numbers = [i for i in range(1, 1000) if is_lucky(i)]

    for lucky in lucky_numbers:
        if n % lucky == 0:
            return "YES"

    return "NO"

n=int(input())
print(generate_lucky_numbers(n))
