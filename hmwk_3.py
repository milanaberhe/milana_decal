#1
def computePower(x,y):
    result=1
    for i in range(y):
        result *=x
    return result
print(computePower(2, 4))
#2
readings=[0,10,20]
def temp(x):
    return(min(x),max(x))

#3
def isweekend(day):
    if day in (6,7):
        return (True)
    else:
        return (False)

#4
def fuel_efficiency(distance, fuel):
    if fuel <=0:
        return "Fuel consumed has to be a positive value"
    elif fuel > 0:
        return distance / fuel

#5
def decodeNumbers(n):
    num = (n)
    power = 0
    last = n % 10
    rest = n // 10
    last_num = n % 10
    while n > 0:
        num //= 10
        power +=1
    return last* (10**power) + rest

#6.1.1
numbers = [2024, 98, 131, 2, 3, 72]
def find_min_with_for_loop(numbers):
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum

#6.6.2
numbers = [2024, 98, 131, 2, 3, 72]
def find_max_with_for_loop(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

#6.2.1
numbers = [2024, 98, 131, 2, 3, 72]
def find_min_with_while_loop(numbers):
    minimum = numbers[0]
    index = 0
    while index < len(numbers):
        if numbers[index] < minimum:
            minimum = numbers[index]
        index += 1
    return minimum

#6.2.2
numbers = [2024, 98, 131, 2, 3, 72]
def find_max_with_while_loops(numbers):
    maximum = numbers[0]
    index = 0
    while index < len(numbers):
        if numbers[index] > maximum:
            maximum = numbers[index]
            index += 1
    return maximum

#7
text = "UC Berkeley, founded in 1868!"
def vowel_and_consonant_count(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for character in text:
        if character.isalpha():
            if character in vowels:
                vowel_count +=1
            else:
                consonant_count += 1
    return (vowel_count, consonant_count)

#8
nums = 2468
def digital_root(num):
    sum = 0 
    while num > 0:
        digit = num % 10
        sum+= digit
        num //=10
    return sum

