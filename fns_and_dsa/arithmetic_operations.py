
#// Create a Python script named arithmetic_operations.py. 
#_ In this script, define a function that performs basic arithmetic operations. 
#_ This function, perform_operation, will be imported and used in a separate main.py script, which we provide.

#* Requirements for arithmetic_operations.py:

#* Function Definition:

#! Define a function named perform_operation.

def perform_operation(num1, num2, operation): #! Parameters: num1 (float), num2 (float), and operation (string). The operation parameter accepts four possible values: 'add', 'subtract', 'multiply', or 'divide'.
    if operation == 'add':
        #! The function should execute the arithmetic operation based on the operation parameter and the numerical values provided.
        return num1 + num2
    elif  operation == 'subtract':
        return num1 - num2  
    elif  operation == 'multiply':
        return num1 * num2  
    elif  operation == 'divide':
        if num2 == 0: #! For division, include handling for division by zero, returning a specific message or value that your main.py script can recognize and display appropriately.
            return('cannot divide by 0') 
        else:
            return num1 / num2   #! Return the result of the arithmetic operation.



