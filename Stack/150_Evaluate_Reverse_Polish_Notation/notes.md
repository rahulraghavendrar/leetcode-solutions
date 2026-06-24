# 150. Evaluate Reverse Polish Notation

## Category

Stack

## Difficulty

Medium

---

# Problem

You are given an expression in:

```text
Reverse Polish Notation (RPN)
```

Example:

```python
["2","1","+","3","*"]
```

Evaluate the expression and return the result.

---

# What Is Reverse Polish Notation?

Normally we write:

```python
(2 + 1) * 3
```

This is called:

```text
Infix Notation
```

because the operator is between the numbers.

---

Reverse Polish Notation writes:

```python
2 1 + 3 *
```

or:

```python
["2","1","+","3","*"]
```

Notice:

```text
Operator comes AFTER operands
```

This removes the need for brackets.

---

# Why Stack?

When we see a number:

```python
2
```

we do not know yet what operation will be applied.

So we store it.

A stack is perfect because:

```text
Last In First Out (LIFO)
```

The most recently seen numbers are used first.

---

# Main Idea

For every token:

If it is:

```python
number
```

Push into stack.

---

If it is:

```python
+
-
*
/
```

Pop two numbers.

Perform operation.

Push result back.

---

# Example 1

Input:

```python
["2","1","+","3","*"]
```

---

Read:

```python
"2"
```

Stack:

```python
[2]
```

---

Read:

```python
"1"
```

Stack:

```python
[2,1]
```

---

Read:

```python
"+"
```

Pop:

```python
1
2
```

Calculate:

```python
2 + 1 = 3
```

Push:

```python
[3]
```

---

Read:

```python
"3"
```

Stack:

```python
[3,3]
```

---

Read:

```python
"*"
```

Pop:

```python
3
3
```

Calculate:

```python
3 * 3 = 9
```

Push:

```python
[9]
```

Final Answer:

```python
9
```

---

# Example 2

Input:

```python
["4","13","5","/","+"]
```

---

Push:

```python
4
13
5
```

Stack:

```python
[4,13,5]
```

---

Read:

```python
"/"
```

Pop:

```python
5
13
```

Calculate:

```python
13 / 5
```

Result:

```python
2
```

because division truncates toward zero.

Push:

```python
[4,2]
```

---

Read:

```python
"+"
```

Calculate:

```python
4 + 2
```

Result:

```python
6
```

Answer:

```python
6
```

---

# Important Observation

For:

```python
+
*
```

Order does not matter.

Example:

```python
2 + 3
```

same as:

```python
3 + 2
```

---

For:

```python
-
/
```

Order matters.

Example:

```python
10 - 3 = 7
```

but:

```python
3 - 10 = -7
```

Different answer.

---

# Why Use

```python
second, first = st.pop(), st.pop()
```

Suppose stack:

```python
[10,3]
```

Top:

```python
3
```

First pop:

```python
second = 3
```

Second pop:

```python
first = 10
```

Then:

```python
10 - 3
```

which is correct.

---

# Division Handling

Problem statement says:

```text
Division truncates toward zero
```

Example:

```python
13 / 5
```

Result:

```python
2
```

---

Example:

```python
-13 / 5
```

Result:

```python
-2
```

not:

```python
-3
```

That is why the solution uses:

```python
int(first / second)
```

instead of:

```python
first // second
```

---

# Complete Flow

For each token:

If number:

```python
st.append(int(c))
```

---

If operator:

Pop two numbers.

Perform operation.

Push result.

---

At the end:

```python
st[0]
```

contains the final answer.

---

# Solution Code

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for c in tokens:

            if c == "+":
                st.append(st.pop() + st.pop())

            elif c == "-":
                second, first = st.pop(), st.pop()
                st.append(first - second)

            elif c == "*":
                st.append(st.pop() * st.pop())

            elif c == "/":
                second, first = st.pop(), st.pop()
                st.append(int(first / second))

            else:
                st.append(int(c))

        return st[0]
```

---

# Data Structures Used

## Stack

```python
st = []
```

Stores numbers and intermediate results.

---

# Functions Used

## append()

```python
st.append(value)
```

Push element into stack.

---

## pop()

```python
st.pop()
```

Remove top element.

---

## int()

```python
int(first / second)
```

Used to truncate division toward zero.

---

# DSA Concepts Used

## Stack

LIFO:

```text
Last In First Out
```

---

## Expression Evaluation

Building results step by step.

---

## Reverse Polish Notation

Operators appear after operands.

---

# Complexity Analysis

Let:

```python
n = len(tokens)
```

Each token is processed once.

Time Complexity:

```python
O(n)
```

---

Space Complexity:

Stack may contain up to:

```python
n
```

elements.

Therefore:

```python
O(n)
```

---

# Pattern Recognition

Keywords that indicate this pattern:

* Expression Evaluation
* Calculator
* Reverse Polish Notation
* Postfix Expression

Common Pattern:

```text
Stack Based Evaluation
```

---

# Interview Takeaway

Whenever you see:

```text
Postfix Expression
Reverse Polish Notation
Expression Evaluation
```

immediately think:

```python
stack = []
```

because operators always act on the most recent operands.

---

# Key Learning

1. Reverse Polish Notation places operators after operands.
2. Numbers are pushed onto the stack.
3. Operators pop two values and push the result.
4. Order matters for subtraction and division.
5. Use `int(a / b)` to truncate toward zero.
6. This is a classic Stack Expression Evaluation problem.
