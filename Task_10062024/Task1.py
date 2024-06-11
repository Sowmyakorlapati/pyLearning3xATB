# 1.Explain the difference between the = operator and the == operator in Python.
# = operator(Assignment Operator) used to assign a value to a variable
# age = 25 # = is used to assign the value '25' to the variable age
# == operator(Equality Operator) used to compare two values for equality.It will return only Boolean values as output
x = 10     # Assignment
y = 20     # Assignment
print(x == y)  # Comparison, prints False
print(x == 10) # Comparison, prints True


# 2.What does the ** operator do in Python, and how is it used?
# The ** operator in Python is used for exponentiation i.e, power operator.It returns power of given number.
print(2 ** 3)  # Output: 8
print(5 ** 2)  # Output: 25
# calculates 2*2*2=8

# 3.What does the ^ operator do in Python, and in what context is it commonly used?
# The ^ operator in Python is a bitwise XOR operator.
# It follows XOR table. It compares each bit of the first operand to the respective second operand.
# i.e., If one bit is 1 and other bit is 0 , it returns 1.

a = 5  # Binary: 0101
b = 3  # Binary: 0011
print(a ^ b)  # Result: 0110 (binary) = 6 (decimal)

