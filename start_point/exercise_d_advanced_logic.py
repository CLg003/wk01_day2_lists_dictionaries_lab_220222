# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
# print(even_numbers)

# 2. Print the difference between the largest and smallest value:
# numbers.sort()
# print(numbers)
# print(numbers[-1] - numbers[0])

# 3. Print True if the list contains a 2 next to a 2 somewhere.
# for index in range(0, (len(numbers) - 1)):
#     if (numbers[index] == 2) and (numbers[index + 1] == 2):
#         print(True)

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
six_index = []
seven_index = []
for index in range(0, len(numbers)):
    if numbers[index] == 6:
        six_index.append(index)
    elif numbers[index] == 7:
        seven_index.append(index)
print(six_index)
print(seven_index)
updated_numbers = []


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 
sum = 0
for index in range(0, len(numbers)):
    if (numbers[index] != 13) and (numbers[index - 1] != 13):
        sum += numbers[index]
# print(sum)







