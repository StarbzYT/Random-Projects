# I am making a personal project; a calculator
# it will divide, add, multiply, and subtract


def calculator(command, *nums):
    command2 = command.lower()
    if command2 == "add":
        total = 0
        for num in nums:
            total += num
        return total
# now for subtraction, unfortunately this will only take in two values
    elif command2 == "subtract":
        total2 = nums[0]
        for num in nums[1:]:
            total2 -= num
        return total2
# now for multiplication
    elif command2 == "multiply":
        total3 = 1
        for num in nums:
            total3 = total3 * num
        return total3
# lastly, division, unfortunately this will only take in two values
    elif command2 == "divide":
        total4 = nums[0]
        for num in nums[1:]:
            total4 = total4 / num
        return total4
    else:
        return "Please enter a valid command..."


print(calculator("MULTIPly", 5, 5))
