# 238. Product of Array Except Self

## Category

Arrays

## Difficulty

Medium

---

# Problem Understanding

For every index i:

Return:

```text
Product of every element except nums[i]
```

Example:

```python
nums = [1,2,3,4]
```

For index 0:

```text
2 × 3 × 4 = 24
```

For index 1:

```text
1 × 3 × 4 = 12
```

For index 2:

```text
1 × 2 × 4 = 8
```

For index 3:

```text
1 × 2 × 3 = 6
```

Result:

```python
[24,12,8,6]
```

---

# My Thought Process

At first glance, we might think:

```text
For every index,
multiply all other elements.
```

That would take:

```text
O(n²)
```

which is too slow.

Then comes the key observation:

```text
Everything Except Me
=
Everything To My Left
×
Everything To My Right
```

For example:

```python
nums = [2,3,4]
```

At index 1:

```text
Current Number = 3

Left Side = 2

Right Side = 4
```

Answer:

```text
2 × 4 = 8
```

This idea leads directly to the Prefix + Suffix solution.

---

# Main Insight

For every index i:

```text
Answer[i]
=
(Product of elements before i)
×
(Product of elements after i)
```

Think of every index as a wall.

Example:

```python
nums = [2,3,4]
```

Index 1:

```text
[2] | [3] | [4]
```

Left Product:

```text
2
```

Right Product:

```text
4
```

Answer:

```text
2 × 4 = 8
```

---

# Step 1: Prefix Products

Prefix means:

```text
Product of everything before me
```

Example:

```python
nums = [2,3,4]
```

Create:

```python
res = [1,2,6]
```

Why?

Index 0:

```text
Nothing before 2
```

Product:

```text
1
```

---

Index 1:

```text
2
```

Product:

```text
2
```

---

Index 2:

```text
2 × 3
```

Product:

```text
6
```

So:

```python
res = [1,2,6]
```

---

# Complete Prefix Pass Example

Input:

```python
nums = [1,2,3,4]
```

Initial:

```python
pre = 1

res = [0,0,0,0]
```

---

i = 0

```python
res[0] = 1
```

```python
res = [1,0,0,0]
```

Update:

```python
pre = 1 × 1
```

```python
pre = 1
```

---

i = 1

```python
res[1] = 1
```

```python
res = [1,1,0,0]
```

Update:

```python
pre = 1 × 2
```

```python
pre = 2
```

---

i = 2

```python
res[2] = 2
```

```python
res = [1,1,2,0]
```

Update:

```python
pre = 2 × 3
```

```python
pre = 6
```

---

i = 3

```python
res[3] = 6
```

```python
res = [1,1,2,6]
```

---

Now:

```python
res
```

contains:

```text
Left Products
```

---

# Step 2: Suffix Products

Suffix means:

```text
Product of everything after me
```

We now traverse from right to left.

---

Initial:

```python
suf = 1
```

Current:

```python
res = [1,1,2,6]
```

---

i = 3

```python
res[3] *= 1
```

```python
res = [1,1,2,6]
```

Update:

```python
suf = 1 × 4
```

```python
suf = 4
```

---

i = 2

```python
res[2] *= 4
```

```python
2 × 4 = 8
```

```python
res = [1,1,8,6]
```

Update:

```python
suf = 4 × 3
```

```python
suf = 12
```

---

i = 1

```python
res[1] *= 12
```

```python
1 × 12 = 12
```

```python
res = [1,12,8,6]
```

Update:

```python
suf = 12 × 2
```

```python
suf = 24
```

---

i = 0

```python
res[0] *= 24
```

```python
1 × 24 = 24
```

```python
res = [24,12,8,6]
```

---

Final Answer:

```python
[24,12,8,6]
```

---

# Why This Works

After the first loop:

```python
res[i]
```

contains:

```text
Product of all elements LEFT of i
```

After the second loop:

```python
res[i] *= suffix_product
```

becomes:

```text
(Product Left of i)
×
(Product Right of i)
```

which is exactly:

```text
Product of every element except nums[i]
```

---

# Code Used

```python
class Solution(object):
    def productExceptSelf(self, nums):
        pre=1
        res=[0]*len(nums)

        for i in range(len(nums)):
            res[i]=pre
            pre*=nums[i]

        suf=1

        for i in range(len(nums)-1,-1,-1):
            res[i]*=suf
            suf*=nums[i]

        return res
```

---

# Data Structures Used

## List

```python
res
```

Purpose:

Store prefix products first.

Then transform into final answer.

---

# Variables Used

## pre

Stores:

```text
Running Prefix Product
```

Example:

```python
1
1
2
6
```

---

## suf

Stores:

```text
Running Suffix Product
```

Example:

```python
1
4
12
24
```

---

# DSA Concepts Used

## Prefix Product

Product of elements before current index.

---

## Suffix Product

Product of elements after current index.

---

## Running Product

Continuously update product while traversing.

---

## Space Optimization

Instead of storing:

```python
prefix[]
suffix[]
```

we reuse:

```python
res[]
```

to reduce extra space.

---

# Functions Used

## len()

Purpose:

Get array size.

---

# Complexity Analysis

First Pass:

```text
O(n)
```

Second Pass:

```text
O(n)
```

Total:

```text
O(n)
```

---

Space Complexity:

```text
O(1) extra space
```

The output array is not counted as extra space.

---

# Pattern Recognition

Keywords that indicate this pattern:

* Product Except Self
* Prefix Product
* Suffix Product
* Running Product

---

# Interview Takeaway

The key observation is:

```text
Everything Except Me
=
Left Product × Right Product
```

Instead of multiplying every element for every index, store:

```text
Product Before Me
```

and

```text
Product After Me
```

Then multiply them together.

This transforms an O(n²) solution into an O(n) solution.

---

# Key Learning

1. Prefix means product before the current index.
2. Suffix means product after the current index.
3. Answer[i] = Prefix × Suffix.
4. Every index acts as a dividing wall.
5. Reusing the result array avoids extra space.
6. This is a classic Prefix-Suffix Pattern problem.
