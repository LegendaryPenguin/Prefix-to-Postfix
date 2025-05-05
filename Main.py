'''
Name: Nischay Rawal
Date: 05/05/2025
Date Modified: 05/05/2025
Lab: Tuesday 8am Lab 11
Collaborators: None
Program Description: This program takes an equation in prefix form and converts the input prefix form into
an equivalent postfix form equation. 
'''
def is_operator(char):
    """This checks if the character is an operator."""
    return char in ['+', '-', '*', '/', '^']

def is_operand(char):
    """This checks if the character is an operand (variable or number)."""
    return char.isalnum()

def prefix_to_postfix(expression):
    """This converts the prefix expression to postfix expression."""
    # Remove spaces from the expression
    expression = expression.replace(" ", "")
    
    # Reverse the expression for easier processing
    expression = expression[::-1]
    
    stack = []
    result = []
    
    for char in expression:
        if is_operator(char):
            # If operator, pop two operands/expressions from stack
            if len(stack) < 2:
                # Not enough operands
                return "Invalid prefix expression"
            
            operand1 = stack.pop()
            operand2 = stack.pop()
            
            # Form a postfix expression and push back to stack
            temp = operand1 + operand2 + char
            stack.append(temp)
        
        elif is_operand(char):
            # If operand, push to stack
            stack.append(char)
        
        else:
            # Invalid character
            return "Invalid character in expression"
    
    # Final result should be a single expression in the stack
    if len(stack) == 1:
        return stack[0]
    else:
        return "Invalid prefix expression"

def main():
    print("Prefix to Postfix Converter")
    print("Enter prefix expressions with variables (x, y, z), numbers, and operations (+, -, *, /, ^)")
    print("Example: ^-xy2 will be converted to xy-2^")
    
    # This takes the user input
    prefix_expr = input("Enter a prefix expression: ")
    
    # This converts the input by calling the function and displays result
    postfix_expr = prefix_to_postfix(prefix_expr)
    print(f"Postfix expression: {postfix_expr}")

if __name__ == "__main__":
    main()