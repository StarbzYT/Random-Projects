# I am making a personal project; a calculator
# it will divide, add, multiply, and subtract


def calculator(command, *nums):  # the command parameter is for the operations
    command2 = command.lower()  # the .lower() method makes the command input case insensitive
    if command2 == "add":
        total = 0
        for num in nums:
            total += num  # we add each value in the *nums parameter to the total variable
        return total
# now for subtraction, but it is different from the addition code
    elif command2 == "subtract":
        total2 = nums[0]  # take the first value from the *nums parameter
        for num in nums[1:]:  # since the first value is already in total2, we can use slicing to iterate through the rest of * nums parameter
            total2 -= num
        return total2
# now for multiplication
    elif command2 == "multiply":
        total3 = 1  # can't be zero!
        for num in nums:
            total3 = total3 * num  # multiply each value in *nums with total3
        return total3
# lastly, division
    elif command2 == "divide":
        total4 = nums[0]  # we have to create the same setup as subtraction
        for num in nums[1:]:
            total4 = total4 / num
        return total4
    else:
        return "Please enter a valid command..."  # if the user does not enter a valid operation for command


print(calculator("MULTIPly", 5, 5))  # one example for multiplication, should return 25
