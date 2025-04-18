import streamlit as st

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Streamlit app
def calculator():
    st.title("Simple Streamlit Calculator")

    # User input for operation
    st.write("### Select operation:")
    operation = st.radio("Choose operation", ('Add', 'Subtract', 'Multiply', 'Divide'))

    # User input for numbers
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)

    # Perform the operation based on user's choice
    if operation == 'Add':
        result = add(num1, num2)
    elif operation == 'Subtract':
        result = subtract(num1, num2)
    elif operation == 'Multiply':
        result = multiply(num1, num2)
    elif operation == 'Divide':
        result = divide(num1, num2)

    # Display the result
    st.write(f"### Result: {result}")

if __name__ == "__main__":
    calculator()
