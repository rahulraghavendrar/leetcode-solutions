# 704. Binary Search

## Category

Binary Search

## Difficulty

Easy

---

# Problem

You are given a **sorted** array of unique integers.

Example:

```python
nums = [-1,0,3,5,9,12]
```

and a target value.

Return the index of the target if it exists.

Otherwise return:

```python
-1
```

The solution must run in:

```text
O(log n)
```

time.

---

# Problem Understanding

Example:

```python
nums = [-1,0,3,5,9,12]

target = 9
```

Indices:

```text
Index : 0  1  2  3  4   5
Value : -1 0  3  5  9  12
```

Since:

```text
9
```

is present at index:

```text
4
```

Answer:

```python
4
```

---

# My Thought Process

Since the array is already sorted,

checking every element one by one would take:

```text
O(n)
```

Instead,

every comparison lets us eliminate **half of the remaining array**.

This is exactly what Binary Search does.

---

# Key Observation

The array is sorted.

If the middle element is:

```text
Greater than target
```

then the target **cannot** be on the right side.

So we discard the entire right half.

---

If the middle element is:

```text
Smaller than target
```

then the target **cannot** be on the left side.

So we discard the entire left half.

---

Every comparison removes half of the search space.

---

# Variables Used

## Left Pointer

```python
l = 0
```

Represents the starting index of the current search space.

---

## Right Pointer

```python
r = len(nums)-1
```

Represents the ending index of the current search space.

---

## Middle Index

```python
m = l + ((r-l)//2)
```

Finds the middle element.

---

# Why Use

```python
m = l + ((r-l)//2)
```

instead of

```python
(l+r)//2
```

Both work in Python.

However,

many programming languages have fixed integer sizes.

If:

```python
l+r
```

becomes very large,

it can overflow.

Using:

```python
l + ((r-l)//2)
```

avoids that issue.

This is the standard Binary Search formula used in interviews.

---

# Algorithm

Initialize:

```python
l = 0
r = len(nums)-1
```

---

Repeat while:

```python
l <= r
```

because there is still a search space.

---

Find the middle:

```python
m = l + ((r-l)//2)
```

---

Case 1

If:

```python
nums[m] == target
```

Return:

```python
m
```

---

Case 2

If:

```python
nums[m] > target
```

Discard the right half.

Move:

```python
r = m-1
```

---

Case 3

If:

```python
nums[m] < target
```

Discard the left half.

Move:

```python
l = m+1
```

---

If the loop ends,

the target does not exist.

Return:

```python
-1
```

---

# Complete Example

Input:

```python
nums = [-1,0,3,5,9,12]

target = 9
```

---

### Iteration 1

```text
Index : 0 1 2 3 4 5
Value :-1 0 3 5 9 12
```

Pointers:

```text
L           R
```

Middle:

```python
m = 2
```

Value:

```python
3
```

Since:

```text
3 < 9
```

Discard left half.

Move:

```python
l = 3
```

---

### Iteration 2

Search space:

```text
5 9 12
```

Middle:

```python
m = 4
```

Value:

```python
9
```

Target found.

Return:

```python
4
```

---

# Another Example

Input:

```python
nums = [-1,0,3,5,9,12]

target = 2
```

Binary Search keeps removing half of the array.

Eventually:

```python
l > r
```

meaning:

```text
Target does not exist.
```

Return:

```python
-1
```

---

# Solution Code

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1

        while l <= r:

            m = l + ((r-l)//2)

            if nums[m] > target:
                r = m-1

            elif nums[m] < target:
                l = m+1

            else:
                return m

        return -1
```

---

# Functions Used

No built-in searching functions are used.

Only:

* Integer division (`//`)
* List indexing (`nums[m]`)

---

# Data Structures Used

## Array

The input array is already sorted.

No additional data structures are required.

---

# DSA Concepts Used

## Binary Search

Repeatedly divides the search space into two halves.

---

## Two Pointers

```python
l
r
```

represent the current search boundaries.

---

# Complexity Analysis

Let:

```text
n = len(nums)
```

Every iteration removes half of the search space.

Time Complexity:

```text
O(log n)
```

---

Space Complexity:

Only a few variables are used.

```text
O(1)
```

---

# Pattern Recognition

Keywords that indicate Binary Search:

* Sorted Array
* Search
* O(log n)
* Find Target
* Ascending Order

Whenever you see these together,

immediately think:

```text
Binary Search
```

---

# Interview Takeaway

The biggest clue is:

```text
The array is sorted.
```

A sorted array allows us to discard half of the remaining elements after every comparison.

That is why Binary Search is much faster than Linear Search.

---

# Key Learning

1. Binary Search only works on sorted data.
2. Maintain two pointers: `l` and `r`.
3. Find the middle using:

```python
m = l + ((r-l)//2)
```

4. If the middle element is greater than the target, search the left half.
5. If the middle element is smaller than the target, search the right half.
6. Every iteration removes half of the search space.
7. Binary Search runs in **O(log n)** time and **O(1)** space.
