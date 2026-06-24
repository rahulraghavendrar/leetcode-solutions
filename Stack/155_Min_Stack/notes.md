# 155. Min Stack

## Category

Stack

## Difficulty

Medium

---

# Problem

Design a stack that supports:

```python
push()
pop()
top()
getMin()
```

All operations must run in:

```text
O(1)
```

time.

---

# Problem With Normal Stack

Suppose:

```python
stack = [-2, 0, -3]
```

Minimum:

```python
-3
```

Easy.

---

Now:

```python
stack.pop()
```

Stack becomes:

```python
[-2, 0]
```

Minimum is now:

```python
-2
```

---

If we use only one stack, every time we call:

```python
getMin()
```

we would need to search the entire stack:

```python
O(n)
```

which violates the problem requirement.

---

# My Thought Process

The question asks:

```text
Get minimum element in O(1)
```

This means we must always know the minimum without searching.

The solution is:

```text
Use Two Stacks
```

---

# Data Structures Used

## Main Stack

```python
self.stack
```

Stores actual values.

Example:

```python
[-2, 0, -3]
```

---

## Minimum Stack

```python
self.minstack
```

Stores the minimum value at every position.

Example:

```python
[-2, -2, -3]
```

Notice:

```text
Index 0 → minimum so far = -2
Index 1 → minimum so far = -2
Index 2 → minimum so far = -3
```

---

# Core Idea

For every value pushed into:

```python
stack
```

also push something into:

```python
minstack
```

The top of:

```python
minstack
```

always contains the minimum element of the stack.

---

# Push Operation

Input:

```python
push(-2)
```

Main stack:

```python
[-2]
```

Minimum stack:

```python
[-2]
```

---

Push:

```python
push(0)
```

Current minimum:

```python
-2
```

Since:

```python
0 > -2
```

store:

```python
-2
```

again.

Main stack:

```python
[-2, 0]
```

Minimum stack:

```python
[-2, -2]
```

---

Push:

```python
push(-3)
```

Since:

```python
-3 < -2
```

New minimum becomes:

```python
-3
```

Main stack:

```python
[-2, 0, -3]
```

Minimum stack:

```python
[-2, -2, -3]
```

---

# Why Duplicate Minimum Values?

This is the main trick of the problem.

Suppose:

```python
stack     = [-2, 0]
minstack  = [-2, -2]
```

Even though:

```python
0
```

is not the minimum,

we still store:

```python
-2
```

again.

Reason:

```text
Every index of minstack
stores the minimum value up to that position.
```

---

# Pop Operation

Before:

```python
stack    = [-2, 0, -3]
minstack = [-2, -2, -3]
```

Pop:

```python
-3
```

Both stacks pop.

After:

```python
stack    = [-2, 0]
minstack = [-2, -2]
```

Current minimum automatically becomes:

```python
-2
```

No searching required.

---

# Top Operation

Simply return:

```python
self.stack[-1]
```

Example:

```python
[-2,0,-3]
```

Top:

```python
-3
```

---

# Get Minimum Operation

Simply return:

```python
self.minstack[-1]
```

Example:

```python
minstack = [-2,-2,-3]
```

Return:

```python
-3
```

---

# Complete Example

Operations:

```python
push(-2)
push(0)
push(-3)
```

Stacks:

```python
stack    = [-2,0,-3]
minstack = [-2,-2,-3]
```

---

Call:

```python
getMin()
```

Returns:

```python
-3
```

---

Call:

```python
pop()
```

Stacks:

```python
stack    = [-2,0]
minstack = [-2,-2]
```

---

Call:

```python
top()
```

Returns:

```python
0
```

---

Call:

```python
getMin()
```

Returns:

```python
-2
```

---

# Solution Code

```python
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, value):
        self.stack.append(value)

        if not self.minstack or value <= self.minstack[-1]:
            self.minstack.append(value)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self):
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minstack[-1]
```

---

# Functions Used

## append()

```python
self.stack.append(value)
```

Push element.

---

## pop()

```python
self.stack.pop()
```

Remove top element.

---

## List Indexing

```python
stack[-1]
```

Access top element.

---

# DSA Concepts Used

## Stack

LIFO:

```text
Last In First Out
```

---

## Auxiliary Stack

```python
minstack
```

Maintains minimum values.

---

## Constant Time Retrieval

```python
getMin()
```

works in:

```text
O(1)
```

because minimum is already stored.

---

# Complexity Analysis

## push()

```text
O(1)
```

---

## pop()

```text
O(1)
```

---

## top()

```text
O(1)
```

---

## getMin()

```text
O(1)
```

---

## Space Complexity

Two stacks.

```text
O(n)
```

---

# Pattern Recognition

Keywords that indicate this pattern:

* Stack
* Minimum Element
* Constant Time Retrieval
* Design Data Structure

Common Pattern:

```text
Main Stack + Auxiliary Stack
```

---

# Interview Takeaway

The key insight is:

```text
Store the minimum value at every level.
```

Instead of searching for the minimum later,

we remember it during every push.

This allows:

```python
getMin()
```

to run in:

```text
O(1)
```

time.

---

# Key Learning

1. A normal stack cannot return minimum in O(1).
2. Use a second stack to track minimum values.
3. Every position in minstack stores the minimum so far.
4. Pop from both stacks together.
5. Top of minstack always contains the current minimum.
6. This is a classic Stack Design interview problem.
