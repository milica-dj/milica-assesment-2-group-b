"""
Blackjack
"""
# Provide your solution here
def calculate_score(a:int, b:int, c:int):
    sum = a + b + c
    if sum <= 21:
        return sum
        print(sum)
    elif sum > 21:
        sum2 = sum - 10
        if int(sum2) > 21:
            return
            print("BUST!")
        else:
            print(sum2)
calculate_score(2, 11, 8)

def calculate_score(a:int, b:int, c:int):
    for i in range(1, 11):
        sum = a + b + c
        if sum <= 21:
            print(sum)
        elif sum > 21 and (a == 11 or b == 11 or c==11):
            sum2 = sum - 10
            if sum2 > 21:
                print("Bust!")
            else:
                print(sum2)

calculate_score(9, 9, 9)




"""
Even Numbers
"""
# Provide your solution here


def even_positive_numbers(lst: list[int]) -> list[int]:
    even_numbers = []
    for num in lst:
        if num % 2 == 0 and num >= 0:
            return even_numbers
        print(even_positive_numbers(list))
even_positive_numbers()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

even_positive_numbers(1, 2, 3)
