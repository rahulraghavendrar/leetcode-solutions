# 167. Two Sum II - Input Array Is Sorted

## Category

Two Pointers

## Difficulty

Medium

---

# Problem Understanding

We are given:

```python
numbers = [2,7,11,15]
target = 9
```

Find two numbers whose sum equals:

```python
target
```

Return their indices.

Important:

```text
The array is already sorted.
```

and

```text
Indices are 1-indexed.
```

---

# My Thought Process

The most important clue is:

```text
Array is sorted
```

If the array is sorted:

```python
[2,7,11,15]
```

then:

```text
Moving right pointer left
→ decreases the sum

Moving left pointer right
→ increases the sum
```

This allows us to avoid checking every pair.

Instead of:

```text
O(n²)
```

we can solve it in:

```text
O(n)
```

using Two Pointers.

---

# Main Idea

Place two pointers:

```python
l = 0
r = len(numbers)-1
```

Meaning:

```text
l → smallest number
r → largest number
```

---

# Visual Example

```text
2    7    11    15
^              ^
l              r
```

Current Sum:

```python
2 + 15 = 17
```

Target:

```python
9
```

Since:

```text
17 > 9
```

the sum is too large.

Move:

```python
r -= 1
```

because moving left decreases the sum.

---

# Why Move r Left?

Current:

```text
2    7    11    15
^              ^
l              r
```

Sum:

```python
17
```

Too large.

Since the array is sorted:

```text
Everything left of 15
is smaller than 15
```

So moving:

```python
r -= 1
```

reduces the sum.

---

# Why Move l Right?

Suppose:

```python
numbers = [2,3,4]
target = 6
```

Start:

```text
2    3    4
^         ^
l         r
```

Sum:

```python
6
```

Found immediately.

---

Another example:

```python
numbers = [1,2,5,10]
target = 12
```

Start:

```text
1   2   5   10
^             ^
l             r
```

Sum:

```python
11
```

Too small.

To increase the sum:

```python
l += 1
```

because the array is sorted.

Moving right increases the value.

---

# Complete Flow Example

Input:

```python
numbers = [2,7,11,15]
target = 9
```

Initialize:

```python
l = 0
r = 3
```

---

Current:

```text
2    7    11    15
^              ^
l              r
```

Sum:

```python
17
```

Too large.

Move:

```python
r = 2
```

---

Current:

```text
2    7    11
^         ^
l         r
```

Sum:

```python
13
```

Too large.

Move:

```python
r = 1
```

---

Current:

```text
2    7
^    ^
l    r
```

Sum:

```python
9
```

Target found.

---

# Why Return [l+1, r+1]?

This is one of the most important details of the problem.

Python uses:

```text
0-indexing
```

Example:

```python
numbers = [2,7,11,15]
```

Indices:

```text
Value : 2   7   11   15
Index : 0   1    2    3
```

The solution is:

```python
2 + 7 = 9
```

Python indices:

```python
[0,1]
```

But the problem explicitly asks for:

```text
1-indexed positions
```

Therefore:

```python
[1,2]
```

must be returned.

Hence:

```python
return [l+1, r+1]
```

instead of:

```python
return [l, r]
```

---

# Code Used

```python
class Solution(object):
    def twoSum(self, numbers, target):

        currsum = 0
        l = 0
        r = len(numbers)-1

        while l < r:

            currsum = numbers[l] + numbers[r]

            if currsum > target:
                r -= 1

            elif currsum < target:
                l += 1

            else:
                return [l+1, r+1]
```

---

# Variables Used

## l

Left Pointer.

Starts at:

```python
0
```

Purpose:

```text
Smallest value
```

---

## r

Right Pointer.

Starts at:

```python
len(numbers)-1
```

Purpose:

```text
Largest value
```

---

## currsum

Stores:

```python
numbers[l] + numbers[r]
```

Used to compare with:

```python
target
```

---

# DSA Concepts Used

## Two Pointers

One pointer from left.

One pointer from right.

---

## Sorted Array Optimization

Because the array is sorted:

```text
Move left pointer right
→ increase sum

Move right pointer left
→ decrease sum
```

---

## Search Space Reduction

Each move removes impossible pairs.

This is why we avoid checking every combination.

---

# Complexity Analysis

Let:

```text
n = length of array
```

Each pointer moves at most:

```text
n times
```

Therefore:

```text
Time Complexity = O(n)
```

---

Space Used:

```python
l
r
currsum
```

Only a few variables.

Therefore:

```text
Space Complexity = O(1)
```

---

# Pattern Recognition

Keywords that indicate this pattern:

* Sorted Array
* Pair Sum
* Two Numbers
* Constant Space

Common Technique:

```text
Two Pointers
```

---

# Interview Takeaway

The key observation is:

```text
The array is sorted.
```

Because of sorting:

```text
If sum is too large
→ move right pointer left

If sum is too small
→ move left pointer right
```

This eliminates unnecessary checks and reduces:

```text
O(n²)
```

to:

```text
O(n)
```

---

# Key Learning

1. Sorted arrays often suggest Two Pointers.
2. Left pointer increases the sum.
3. Right pointer decreases the sum.
4. Only one pass through the array is needed.
5. Always check whether the problem wants 0-indexed or 1-indexed answers.
6. Two Sum II is a classic Two Pointer problem.
