# 153. Find Minimum in Rotated Sorted Array

## Category

Binary Search

## Difficulty

Medium

---

# Problem

You are given a sorted array that has been rotated.

Example:

```python
nums = [4,5,6,7,0,1,2]
```

Originally, the array was:

```python
[0,1,2,4,5,6,7]
```

After rotating it becomes:

```python
[4,5,6,7,0,1,2]
```

Return the **minimum element** in the array.

The algorithm must run in **O(log n)** time.

---

# My Thought Process

Unlike a normal Binary Search problem, there is **no target element**.

Instead, the goal is to find the **rotation point**, because the smallest element is exactly where the rotation occurs.

My approach is:

* Maintain a variable called `mini`.
* During every Binary Search iteration, compare `mini` with `nums[mid]`.
* Keep updating the minimum value while shrinking the search space.

---

# Important Observation

A rotated sorted array actually consists of **two individually sorted halves**.

Example:

```text
4 5 6 7 | 0 1 2
```

Left Half:

```text
4 5 6 7
```

Right Half:

```text
0 1 2
```

The minimum element always lies in one of these halves.

Binary Search helps eliminate one half every iteration.

---

# ⭐ Key Concept

The Binary Search decision is **not** based on:

```python
nums[l]
```

Instead, it is based on:

```python
nums[mid]
```

and

```python
nums[r]
```

because the last element tells us which half is sorted.

---

# Why Compare nums[mid] and nums[r]?

Suppose

```python
nums = [4,5,6,7,0,1,2]
```

Current values:

```text
mid = 7
right = 2
```

Since

```text
7 > 2
```

the minimum cannot be on the left.

It must be on the right.

Therefore,

```python
l = mid + 1
```

---

Now consider

```python
nums = [6,7,1,2,3]
```

Suppose

```text
mid = 2
right = 3
```

Since

```text
2 < 3
```

the minimum is either:

* At `mid`
* Somewhere to the left

Therefore,

```python
r = mid - 1
```

---

# ⭐ Why Maintain mini?

This solution keeps track of the smallest middle element encountered.

Initially,

```python
mini = nums[0]
```

Every iteration,

```python
mini = min(mini, nums[mid])
```

This guarantees that every middle element visited is checked.

Even though Binary Search skips many elements, the smallest visited middle value is always stored.

---

# Complete Example

Input:

```python
nums = [4,5,6,7,0,1,2]
```

---

### Iteration 1

```text
l = 0
r = 6
mid = 3
```

```text
nums[mid] = 7
```

Update:

```python
mini = min(4,7)
```

Result:

```text
mini = 4
```

Since

```text
7 > 2
```

Move right.

```python
l = mid + 1
```

---

### Iteration 2

```text
l = 4
r = 6
mid = 5
```

```text
nums[mid] = 1
```

Update:

```python
mini = min(4,1)
```

Result:

```text
mini = 1
```

Since

```text
1 < 2
```

Move left.

```python
r = mid - 1
```

---

### Iteration 3

```text
l = 4
r = 4
mid = 4
```

```text
nums[mid] = 0
```

Update:

```python
mini = min(1,0)
```

Result:

```text
mini = 0
```

Loop finishes.

Return

```python
0
```

---

# Solution Code

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1

        mini = nums[0]

        while l <= r:

            mid = (l + r) // 2

            mini = min(mini, nums[mid])

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        return mini
```

---

# Functions Used

## min()

```python
mini = min(mini, nums[mid])
```

Returns the smaller of the two values.

Time Complexity:

```text
O(1)
```

---

## len()

Used for:

```python
r = len(nums) - 1
```

Time Complexity:

```text
O(1)
```

---

# Data Structures Used

## Array

The input rotated sorted array.

No extra data structures are required.

---

# DSA Concepts Used

## Binary Search

Searches for the rotation point instead of a target.

---

## Rotated Sorted Array

The array is divided into two sorted halves.

The comparison between `nums[mid]` and `nums[r]` identifies which half contains the minimum.

---

## Tracking Minimum

Maintain a variable:

```python
mini
```

Update it every iteration using:

```python
mini = min(mini, nums[mid])
```

---

# Complexity Analysis

Let

```text
n = len(nums)
```

Binary Search performs:

```text
O(log n)
```

iterations.

Each iteration performs constant work.

### Time Complexity

```text
O(log n)
```

### Space Complexity

```text
O(1)
```

---

# Pattern Recognition

Keywords that indicate this pattern:

* Rotated Sorted Array
* Minimum Element
* O(log n)
* Rotation
* Binary Search

Pattern:

```text
Binary Search on Rotated Sorted Array
```

---

# Interview Takeaway

The biggest insight is:

> A rotated sorted array is actually two sorted halves joined together.

Comparing

```python
nums[mid]
```

with

```python
nums[r]
```

tells us which half contains the minimum.

This allows Binary Search to eliminate half of the search space in every iteration.

---

# Key Learning

1. A rotated sorted array consists of two sorted halves.
2. Compare `nums[mid]` with `nums[r]`.
3. If `nums[mid] > nums[r]`, search the right half.
4. Otherwise, search the left half.
5. Maintain `mini` by updating it with every middle element.
6. Binary Search reduces the search space by half each iteration.
7. Time Complexity is **O(log n)**.
