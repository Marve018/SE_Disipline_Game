# TOPIC: CONDITIONAL STATEMENTS

## DAY 1
DEFINITION:
  In programming, conditional statements are instructions which lets the computer decide based on if certain coditions
  are TRUE or FALSE. These statements enable the program to execute different sets of instructions or actions depending
  on the outcome of these conditions. The most common types of conditional statements include "if" statements, "else"
  statements, and "else if" (or "elif") statements.

TYPES
  IF STATEMENTS: The "if" statement is a fundamental control structure in programming that allows you to execute a block 
  of code only if a specified condition is true.
  ELSE STATEMENTS: The "else" statement follows an if statement and executes a block of code if the if condition is false.
  ELIF STATEMENTS: The "elif" statement allows you to check multiple conditions sequentially after an initial if statement. It is short for "else if".

## DAY 2
### SYNTAX AND STRUCTURE:
### PROGRAMMING LANGUAGE -> PYTHON

IF STATEMENTS:
The if keyword initiates the conditional statement.condition is an expression that evaluates to either True or False. If the condition is True, the code block immediately following the if statement is executed.
```
if condition:
    # code block to execute if condition is true

```

ELSE STATEMENTS:
The else keyword provides an alternative code block to execute when the condition in the preceding "if" statement is False. The "else" block is optional, but if included, it will always execute when the "if" condition is False.
```
if condition:
    # code block to execute if condition is true
else:
    # code block to execute if condition is false

```

ELIF STATEMENTS:
The elif keyword introduces an alternative condition to check after the initial "if" condition. You can include multiple "elif" statements to check for additional conditions. If none of the conditions are true, the code block inside the "else" statement will execute.
```
if condition1:
    # code block to execute if condition1 is true
elif condition2:
    # code block to execute if condition2 is true
else:
    # code block to execute if all conditions are false

```
## DAY 3
### EXAMPLE OF CONDITIONAL STATEMENTS
```
x = 10

if x > 15:
    print("x is greater than 15")
elif x > 10:
    print("x is greater than 10 but not greater than 15")
else:
    print("x is 10 or less")
```
The examples show both the if, else and elif statements at work. In this example it is the else block that will run cause
both the if and elif return false so their blocks can't execute.

###  CONDITIONAL EXPRESSIONS:
Conditional expressions involve comparisons and logical operations to create conditions for decision-making in programming.
They are very essential to the flow of conditional statements and they include

. COMPARISON OPERATORS:
Comparison operators are used to compare values and create conditions. They return either True or False based on the comparison.

Equal to (==): Returns True if two values are equal.
Not equal to (!=): Returns True if two values are not equal.
Greater than (>): Returns True if the left operand is greater than the right operand.
Less than (<): Returns True if the left operand is less than the right operand.
Greater than or equal to (>=): Returns True if the left operand is greater than or equal to the right operand.
Less than or equal to (<=): Returns True if the left operand is less than or equal to the right operand.

. LOGICAL OPERATORS:
Logical operators are used to combine multiple conditions and create complex conditions.

AND (and): Returns True if both conditions on its left and right sides are true.
OR (or): Returns True if at least one of the conditions on its left and right sides is true.
NOT (not): Returns the opposite boolean value of the condition. If the condition is True, returns False, and vice versa.

## DAY 4
### EXAMPLE WITH CONDITIONAL EXPRESSIONS
```
x = 10
y = 5

# Using comparison operators
if x > y:
    print("x is greater than y")

# Using logical operators
if x > 5 and y < 10:
    print("Both conditions are true")

# Nested conditions
if x > 5:
    if y < 10:
        print("Nested conditions: Both conditions are true")

# Combining comparison and logical operators
if x > 5 or y > 10:
    print("At least one condition is true")

```
In the provided example:

Comparison operators (>, <) are used to create conditions for decision-making.
Logical operators (and, or) are used to combine multiple conditions.
Nested conditions are used for more complex decision-making scenarios.

### FLOW CONTROL
Looping Constructs:

1. Looping constructs allow you to repeat a block of code multiple times. There are two main types of loops:

for Loops: You use a "for" loop to iterate over a sequence (e.g., list, tuple, string) and execute a block of code for each item in the sequence.

while Loops: You use a "while" loop to repeatedly execute a block of code as long as a specified condition is true.

```
# for loop
for item in sequence:
    # code block to execute for each item

# while loop
while condition:
    # code block to execute while condition is true

```

2. Control Statements:

Control statements allow you to alter the normal flow of execution within loops and conditional statements.

break Statement: Terminates the loop it is in and transfers control to the statement immediately following the loop.

continue Statement: Skips the rest of the code inside a loop for the current iteration and continues with the next iteration.

pass Statement: Acts as a placeholder and does nothing when executed. It is commonly used when a statement is syntactically required but no action is needed.

### day_4.py results
```
./day_4.py
Enter the student's score: 85
The student's grade is: B
```

The loops constructs and control statements are crucial with conditional statements especially when writing complex code.
