# 739. Daily Temperatures

## Category

Stack

## Difficulty

Medium

---

# Problem

You are given an array of daily temperatures.

Example:

```python
temperatures = [73,74,75,71,69,72,76,73]
```

For every day, find:

```text
How many days do I have to wait until I get a warmer temperature?
```

If no warmer temperature exists in the future:

```python
answer[i] = 0
```

---

# Problem Understanding

Suppose:

```python
temperatures = [73,74,75]
```

Day 0:

```text
73
```

Next warmer temperature:

```text
74
```

Wait:

```text
1 day
```

---

Day 1:

```text
74
```

Next warmer:

```text
75
```

Wait:

```text
1 day
```

---

Day 2:

```text
75
```

No warmer day exists.

Answer:

```text
0
```

Final Answer:

```python
[1,1,0]
```

---

# My Thought Process

The question asks:

```text
Find the next greater temperature.
```

Brute Force:

For every day,

search every future day.

Time Complexity:

```text
O(n²)
```

Too slow.

---

# Key Observation

Suppose:

```python
73 74 75 71 69 72 76
```

When we reach:

```text
76
```

we immediately know the answer for:

```text
72
71
75
```

Therefore:

```text
Instead of searching forward every time,
remember the temperatures that are still waiting.
```

This is exactly what a stack is used for.

---

# Data Structure Used

## Stack

The stack stores:

```python
[temperature, index]
```

Example:

```python
[
    [73,0],
    [74,1],
    [75,2]
]
```

Meaning:

```text
Temperature
Day Index
```

---

# Why Store Index?

Suppose:

Current day:

```python
i = 6
```

Current temperature:

```python
76
```

Earlier temperature:

```python
75
```

at:

```python
index = 2
```

Days waited:

```python
6 - 2 = 4
```

Therefore we store:

```python
index
```

inside the stack.

---

# Algorithm

Initialize:

```python
stack = []
```

Result:

```python
res = [0] * len(temperatures)
```

Initially every answer is:

```python
0
```

because maybe no warmer day exists.

---

Traverse the array:

```python
for i, t in enumerate(temperatures):
```

where

```python
i
```

is the index.

and

```python
t
```

is the temperature.

---

# Main Idea

While:

```python
stack
```

is not empty

and

```python
current temperature
```

is warmer than

```python
stack top temperature
```

we have found the answer for that previous day.

---

Pop:

```python
stacktemp, stackind = stack.pop()
```

Now compute:

```python
i - stackind
```

which is:

```text
Days waited
```

Store:

```python
res[stackind] = i - stackind
```

---

Finally push:

```python
[t, i]
```

because this day is now waiting for its warmer day.

---

# Complete Example

Input:

```python
temperatures = [73,74,75,71,69,72,76,73]
```

---

Day 0

```text
73
```

Stack:

```python
[[73,0]]
```

---

Day 1

```text
74
```

Since:

```text
74 > 73
```

Pop:

```python
[73,0]
```

Answer:

```python
1-0 = 1
```

Result:

```python
[1,0,0,0,0,0,0,0]
```

Push:

```python
[74,1]
```

---

Day 2

```text
75
```

Since:

```text
75 > 74
```

Answer:

```python
2-1 = 1
```

Push:

```python
[75,2]
```

---

Day 3

```text
71
```

Not warmer.

Push.

Stack:

```python
[
[75,2],
[71,3]
]
```

---

Day 4

```text
69
```

Push.

---

Day 5

```text
72
```

72 is warmer than:

```text
69
```

Pop:

```python
[69,4]
```

Answer:

```python
5-4 = 1
```

Still:

```text
72 > 71
```

Pop:

```python
[71,3]
```

Answer:

```python
5-3 = 2
```

Push:

```python
[72,5]
```

---

Day 6

```text
76
```

76 is warmer than:

```text
72
75
```

Both are popped.

Answers become:

```python
75 -> 4 days
72 -> 1 day
```

---

Final Answer

```python
[1,1,4,2,1,1,0,0]
```

---

# Why While Loop?

Notice:

```python
while stack and t > stack[-1][0]:
```

One warmer day can solve multiple previous temperatures.

Example:

```python
70
71
72
80
```

When:

```text
80
```

arrives,

it answers:

```text
72
71
70
```

Therefore:

```python
while
```

is required instead of:

```python
if
```

---

# Solution Code

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []

        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][0]:

                stacktemp, stackind = stack.pop()

                res[stackind] = i - stackind

            stack.append([t, i])

        return res
```

---

# Functions Used

## enumerate()

```python
for i, t in enumerate(temperatures)
```

Returns:

```python
index
value
```

simultaneously.

---

## append()

```python
stack.append([t,i])
```

Push into stack.

---

## pop()

```python
stack.pop()
```

Remove top element.

---

# Data Structures Used

## Stack

Stores:

```python
[temperature,index]
```

Purpose:

Temperatures waiting for a warmer day.

---

## Result Array

Stores:

```text
Days waited
```

for every index.

---

# DSA Concepts Used

## Monotonic Stack

The stack always maintains:

```text
Temperatures in decreasing order
```

Whenever a larger temperature appears,

smaller temperatures are removed.

---

## Stack

LIFO:

```text
Last In First Out
```

---

# Complexity Analysis

Let:

```python
n = len(temperatures)
```

Every temperature is:

* Pushed once
* Popped once

Therefore:

```text
Time Complexity = O(n)
```

---

Space Complexity:

Stack may contain:

```text
n
```

elements.

Therefore:

```text
Space Complexity = O(n)
```

---

# Pattern Recognition

Keywords that indicate this pattern:

* Next Greater Element
* Next Warmer Day
* Future Greater Value
* Waiting Days

Common Pattern:

```text
Monotonic Stack
```

---

# Interview Takeaway

The key observation is:

```text
One larger temperature can answer multiple previous days.
```

Instead of repeatedly searching ahead,

keep unresolved temperatures inside a stack.

Whenever a warmer temperature arrives,

solve all possible previous days immediately.

---

# Key Learning

1. This is a classic Monotonic Stack problem.
2. Store both temperature and its index.
3. A warmer day resolves previous colder days.
4. Each element is pushed and popped at most once.
5. `enumerate()` provides index and value together.
6. This achieves O(n) time instead of O(n²).
