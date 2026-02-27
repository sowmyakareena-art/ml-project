def calculator(num1, num2, operator):
    
    if operator == '+':
        result = num1 + num2
        return f"The result is: {result}"
    elif operator == '-':
        result = num1 - num2
        return f"The result is: {result}"
    elif operator == '*':
        result = num1 * num2
        return f"The result is: {result}"
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
            return f"The result is: {result}"
        else:
            
            return "Error: Cannot divide by zero."
    else:
        return "Error: Invalid operator. Please use +, -, *, or /."
    

print(calculator(10, 5, '+'))