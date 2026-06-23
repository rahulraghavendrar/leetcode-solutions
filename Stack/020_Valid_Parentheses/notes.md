# 20. Valid Parentheses

## Category

Stack

## Difficulty

Easy

---

# Problem

Given a string containing:

```python
(
)
[
]
{
}
```

determine whether the brackets are valid.

A string is valid if:

1. Every opening bracket has a matching closing bracket.
2. Brackets close in the correct order.
3. No closing bracket appears before its matching opening bracket.

---

# My Thought Process

The important phrase is:

```text
Correct Order
```

Example:

```python
()
```

Valid.

Because:

```text
Open
Close
```

---

Example:

```python
([)]
```

Invalid.

Because:

```text
(
[
)
]
```

The `)` tries to close `(` before `[` has been closed.

---

# Why Stack?

A stack follows:

```text
Last In First Out (LIFO)
```

Example:

```python
stack = []
```

Push:

```python
(
[
{
```

Stack becomes:

```text
Top
{
[
(
```

The most recent opening bracket is always on top.

---

# Main Idea

Store opening brackets in a stack.

Whenever a closing bracket appears:

Check whether the top of the stack contains the matching opening bracket.

If yes:

```python
stack.pop()
```

Otherwise:

```python
return False
```

---

# Mapping Used

```python
closetoopen = {
    ")":"(",
    "]":"[",
    "}":"{"
}
```

Purpose:

Given a closing bracket:

```python
")"
```

immediately know which opening bracket should be on top.

Expected:

```python
"("
```

---

# Example 1

Input:

```python
s = "()"
```

---

Read:

```python
"("
```

Opening bracket.

Push:

```python
stack = ["("]
```

---

Read:

```python
")"
```

Lookup:

```python
closetoopen[")"]
```

Result:

```python
"("
```

Top of stack:

```python
stack[-1]
```

is:

```python
"("
```

Match found.

Remove:

```python
stack.pop()
```

Stack:

```python
[]
```

---

End of string.

Stack is empty.

Return:

```python
True
```

---

# Example 2

Input:

```python
s = "()[]{}"
```

Process:

```python
(
)
[
]
{
}
```

Every opening bracket gets matched and removed.

Final stack:

```python
[]
```

Return:

```python
True
```

---

# Example 3

Input:

```python
s = "(]"
```

Read:

```python
(
```

Stack:

```python
["("]
```

---

Read:

```python
]
```

Expected opening bracket:

```python
[
```

Top of stack:

```python
(
```

Mismatch.

Return:

```python
False
```

---

# Example 4

Input:

```python
s = "([])"
```

Process:

```python
(
[
]
)
```

Stack flow:

```text
(
([
(
empty
```

All brackets matched correctly.

Return:

```python
True
```

---

# Example 5

Input:

```python
s = "([)]"
```

Read:

```python
(
[
```

Stack:

```python
["(", "["]
```

---

Read:

```python
)
```

Expected:

```python
(
```

Top:

```python
[
```

Mismatch.

Return:

```python
False
```

---

# Complete Flow

For every character:

If opening bracket:

```python
stack.append(i)
```

---

If closing bracket:

Check:

```python
stack[-1]
```

against:

```python
closetoopen[i]
```

---

Match:

```python
stack.pop()
```

---

Mismatch:

```python
return False
```

---

After processing the whole string:

If stack is empty:

```python
return True
```

Else:

```python
return False
```

because some opening brackets never got closed.

---

# Solution Code

```python
class Solution(object):
    def isValid(self, s):
        stack = []

        closetoopen = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for i in s:

            if i in closetoopen:

                if stack and stack[-1] == closetoopen[i]:
                    stack.pop()

                else:
                    return False

            else:
                stack.append(i)

        return True if not stack else False
```

---

# Data Structures Used

## Stack

Implemented using:

```python
stack = []
```

Purpose:

Store opening brackets.

---

## Dictionary

```python
closetoopen
```

Purpose:

Map closing brackets to matching opening brackets.

---

# Functions Used

## append()

```python
stack.append(i)
```

Push element onto stack.

---

## pop()

```python
stack.pop()
```

Remove top element from stack.

---

## Dictionary Lookup

```python
closetoopen[i]
```

Get matching opening bracket.

---

# DSA Concepts Used

## Stack

LIFO:

```text
Last In First Out
```

---

## Matching Pairs

Matching:

```python
()
[]
{}
```

---

## Hash Map

Dictionary used for constant-time lookup.

---

# Complexity Analysis

Let:

```python
n = len(s)
```

Each character is processed once.

Time Complexity:

```python
O(n)
```

---

Space Complexity:

In the worst case:

```python
"((((((("
```

All brackets are stored in stack.

Therefore:

```python
O(n)
```

---

# Pattern Recognition

Keywords that indicate this pattern:

* Parentheses
* Brackets
* Matching Pairs
* Nested Structure
* Correct Order

Common Data Structure:

```python
Stack
```

---

# Interview Takeaway

Whenever a problem involves:

```text
Matching symbols
Nested structures
Opening and closing pairs
```

immediately think:

```python
stack = []
```

because the most recently opened symbol must be closed first.

This is exactly the behavior of a stack.

---

# Key Learning

1. Stack follows LIFO.
2. Opening brackets are pushed onto the stack.
3. Closing brackets must match the top of the stack.
4. Dictionary provides O(1) matching lookup.
5. Empty stack at the end means every bracket was matched.
6. Valid Parentheses is one of the most important introductory Stack problems.
