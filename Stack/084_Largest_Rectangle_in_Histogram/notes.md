# 84. Largest Rectangle in Histogram

## Category

Stack

## Difficulty

Hard

---

# Problem

You are given an array:

```python
heights = [2,1,5,6,2,3]
```

Each number represents the height of a histogram bar.

* Every bar has a width of **1**.
* We need to find the **largest rectangle** that can be formed using one or more consecutive bars.

Return the maximum possible rectangle area.

---

# Problem Understanding

Example:

```python
heights = [2,1,5,6,2,3]
```

Visual:

```text
        █
        █
    █   █
    █ █ █
█   █ █ █
█ █ █ █ █ █
------------
2 1 5 6 2 3
```

The largest rectangle is formed using the bars:

```text
5 6
```

Height:

```text
5
```

Width:

```text
2
```

Area:

```text
5 × 2 = 10
```

---

# My Thought Process

Brute Force:

For every bar,

expand left and right until a smaller bar is found.

Time Complexity:

```text
O(n²)
```

Too slow.

---

# Key Observation

Whenever a **smaller bar** appears,

the previous taller bars **cannot extend any further**.

At that moment,

their maximum rectangle is completely determined.

So we calculate their area immediately.

---

# Why Stack?

The stack stores:

```python
[startIndex, height]
```

Example:

```python
[
    [0,2],
    [2,5],
    [3,6]
]
```

Each element tells us:

* The earliest index from which this height can extend.
* The height of that rectangle.

---

# Main Idea

Traverse the histogram from left to right.

If the current height is:

```text
Greater than or equal to previous height
```

push it into the stack.

If the current height is:

```text
Smaller than previous height
```

keep popping taller bars.

For every popped bar:

```python
Area = Height × Width
```

where:

```python
Width = Current Index - Starting Index
```

After popping,

the new shorter bar inherits the starting index of the last popped bar.

This allows it to extend further to the left.

---

# Why Update

```python
newh = l
```

This is the most important step in the algorithm.

Suppose:

```python
heights = [5,4]
```

When height:

```text
4
```

arrives,

the bar:

```text
5
```

is popped.

The new height:

```text
4
```

can now start from index:

```text
0
```

instead of index:

```text
1
```

So we write:

```python
newh = l
```

instead of:

```python
newh = i
```

Without this step,

the width of future rectangles becomes incorrect.

---

# Complete Example

Input:

```python
heights = [2,1,5,6,2,3]
```

---

## Step 1

Read:

```text
2
```

Stack:

```python
[[0,2]]
```

---

## Step 2

Read:

```text
1
```

Since:

```text
1 < 2
```

Pop:

```python
[0,2]
```

Width:

```python
1-0 = 1
```

Area:

```python
2 × 1 = 2
```

Now:

```python
newh = 0
```

Push:

```python
[0,1]
```

---

## Step 3

Read:

```text
5
```

Greater than 1.

Push:

```python
[2,5]
```

---

## Step 4

Read:

```text
6
```

Push:

```python
[3,6]
```

---

## Step 5

Read:

```text
2
```

Since:

```text
2 < 6
```

Pop:

```python
[3,6]
```

Width:

```python
5-3 = 2
```

Area:

```python
6 × 1 = 6
```

Continue.

Now:

```text
2 < 5
```

Pop:

```python
[2,5]
```

Width:

```python
4-2 = 2
```

Area:

```python
5 × 2 = 10
```

Current maximum:

```text
10
```

The new bar:

```text
2
```

inherits:

```python
start = 2
```

Push:

```python
[2,2]
```

---

# Why Final While Loop?

Some bars never encounter a smaller bar.

Example:

```python
heights = [2,3,4]
```

Nothing gets popped inside the main loop.

So after traversal,

the remaining bars still need their areas calculated.

That is why we process:

```python
while stack:
```

using:

```python
width = len(heights) - start
```

---

# Solution Code

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        maxarea = 0

        for i, j in enumerate(heights):

            newh = i

            while stack and j < stack[-1][1]:

                l, m = stack.pop()

                width = i - l
                area = m * width

                if area > maxarea:
                    maxarea = area

                newh = l

            stack.append([newh, j])

        while stack:

            l, m = stack.pop()

            width = len(heights) - l
            area = m * width

            if area > maxarea:
                maxarea = area

        return maxarea
```

---

# Functions Used

## enumerate()

```python
for i, j in enumerate(heights)
```

Returns:

* Index
* Height

---

## append()

```python
stack.append([start,height])
```

Pushes a new rectangle.

---

## pop()

```python
stack.pop()
```

Removes the tallest rectangle that can no longer extend.

---

# Data Structures Used

## Stack

Stores:

```python
[startIndex,height]
```

Purpose:

Maintain bars whose maximum rectangle has not yet been determined.

---

# DSA Concepts Used

## Monotonic Increasing Stack

The stack always maintains heights in increasing order.

Whenever a smaller height appears,

taller heights are removed.

---

## Greedy

As soon as a shorter bar appears,

the maximum rectangle for taller bars is fixed.

---

# Complexity Analysis

Let:

```text
n = len(heights)
```

Every bar is:

* Pushed once
* Popped once

Time Complexity:

```text
O(n)
```

---

Space Complexity:

The stack may contain all bars.

```text
O(n)
```

---

# Pattern Recognition

Keywords that indicate this pattern:

* Histogram
* Largest Rectangle
* Previous Smaller
* Next Smaller
* Maximum Area

Common Pattern:

```text
Monotonic Increasing Stack
```

---

# Interview Takeaway

The most important insight is:

```text
A rectangle can continue growing only until a smaller bar appears.
```

When a smaller bar is found,

all taller bars have reached their maximum possible width,

so their areas can be calculated immediately.

---

# Key Learning

1. Store `[startIndex, height]` in the stack.
2. Maintain a monotonic increasing stack.
3. When a smaller height appears, pop taller bars.
4. Compute the area using:

   * Height = popped height
   * Width = current index - start index
5. The new shorter bar inherits the starting index of the last popped bar.
6. Process the remaining stack after the traversal.
7. This is one of the most important Monotonic Stack interview problems.
