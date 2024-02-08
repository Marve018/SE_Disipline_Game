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
