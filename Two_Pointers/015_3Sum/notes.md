# 15. 3Sum

## Category

Two Pointers

## Difficulty

Medium

---

# Problem Understanding

Given an array:

```python
nums = [-1,0,1,2,-1,-4]
```

Find all triplets:

```python
[a,b,c]
```

such that:

```python
a + b + c = 0
```

Important:

1. All three indices must be different.
2. Duplicate triplets are not allowed.
3. Order inside the answer does not matter.

---

# My Thought Process

The first thing I noticed is:

```text
Need 3 numbers whose sum is 0
```

This looks similar to:

```text
Two Sum
```

The trick is:

```text
Fix one number
+
Use Two Pointers for the remaining two numbers
```

This converts the brute force:

```text
O(n³)
```

into:

```text
O(n²)
```

---

# Step 1: Sort The Array

```python
nums.sort()
```

Example:

```python
[-1,0,1,2,-1,-4]
```

becomes:

```python
[-4,-1,-1,0,1,2]
```

Why sort?

Because:

```text
Moving left pointer right
increases the sum

Moving right pointer left
decreases the sum
```

This is exactly what makes Two Pointers possible.

---

# Step 2: Fix One Number

Loop:

```python
for i in range(len(nums)):
```

Treat:

```python
nums[i]
```

as the first number of the triplet.

---

# Example

Sorted array:

```python
[-4,-1,-1,0,1,2]
```

Start:

```python
i = 0

nums[i] = -4
```

Now we need:

```text
Two more numbers
```

that make the total sum equal to:

```text
0
```

---

# Step 3: Skip Duplicate First Elements

```python
if i > 0 and nums[i] == nums[i - 1]:
    continue
```

Purpose:

Avoid generating the same triplet multiple times.

Example:

```python
[-4,-1,-1,0,1,2]
```

The second:

```python
-1
```

would produce the same triplets as the first:

```python
-1
```

Therefore we skip it.

---

# Step 4: Initialize Two Pointers

```python
l = i + 1
r = len(nums) - 1
```

Example:

```text
-4  -1  -1   0   1   2
 i    l               r
```

Meaning:

```text
i = fixed number

l = left pointer

r = right pointer
```

---

# Step 5: Calculate Current Sum

```python
currsum = nums[i] + nums[l] + nums[r]
```

Example:

```python
-4 + (-1) + 2
```

Result:

```python
-3
```

---

# Case 1: Sum Too Small

```python
if currsum < 0:
```

Example:

```python
-3
```

Need a larger sum.

Move:

```python
l += 1
```

because:

```text
Array is sorted
```

Moving left pointer right increases the sum.

---

# Case 2: Sum Too Large

```python
elif currsum > 0:
```

Example:

```python
4
```

Need a smaller sum.

Move:

```python
r -= 1
```

because:

```text
Moving right pointer left decreases the sum.
```

---

# Case 3: Found A Triplet

Suppose:

```python
nums[i] = -1
nums[l] = -1
nums[r] = 2
```

Sum:

```python
0
```

Found:

```python
[-1,-1,2]
```

---

# Avoiding Duplicate Triplets

You used:

```python
x = sorted([nums[i], nums[l], nums[r]])
t = tuple(x)
```

Example:

```python
[-1,2,-1]
```

becomes:

```python
[-1,-1,2]
```

Convert to:

```python
(-1,-1,2)
```

because tuples can be stored in a set.

---

# Using Seen Set

```python
seen = set()
```

Before adding:

```python
if t not in seen:
```

Only unseen triplets are added.

Then:

```python
seen.add(t)
```

This prevents duplicate triplets.

---

# Complete Flow Example

Input:

```python
[-1,0,1,2,-1,-4]
```

After sorting:

```python
[-4,-1,-1,0,1,2]
```

---

Choose:

```python
i = 1
```

Value:

```python
-1
```

Pointers:

```text
-4  -1  -1   0   1   2
     i   l           r
```

Sum:

```python
-1 + (-1) + 2
```

Result:

```python
0
```

Add:

```python
[-1,-1,2]
```

---

Move pointers.

Now:

```text
-4  -1  -1   0   1   2
     i       l   r
```

Sum:

```python
-1 + 0 + 1
```

Result:

```python
0
```

Add:

```python
[-1,0,1]
```

---

Final Answer:

```python
[
    [-1,-1,2],
    [-1,0,1]
]
```

---

# Data Structures Used

## List

```python
result
```

Stores all valid triplets.

---

## Set

```python
seen
```

Stores unique triplets.

Purpose:

```text
Duplicate Removal
```

---

## Tuple

```python
t = tuple(x)
```

Used because:

```text
Lists cannot be inserted into sets.
```

Tuples can.

---

# Functions Used

## sort()

```python
nums.sort()
```

Sorts the array.

---

## sorted()

```python
sorted([a,b,c])
```

Sorts a triplet.

---

## tuple()

```python
tuple(x)
```

Converts list into tuple.

---

## add()

```python
seen.add(t)
```

Inserts tuple into set.

---

# DSA Concepts Used

## Two Pointers

One pointer from left.

One pointer from right.

---

## Sorting

Makes pointer movement meaningful.

---

## Duplicate Removal

Using:

```python
set()
```

and

```python
tuple()
```

---

## Search Space Reduction

Instead of checking every triplet:

```text
O(n³)
```

we reduce to:

```text
O(n²)
```

---

# Complexity Analysis

Sorting:

```text
O(n log n)
```

Outer Loop:

```text
O(n)
```

Two Pointer Traversal:

```text
O(n)
```

Total:

```text
O(n²)
```

---

Space Complexity

Seen Set:

```text
O(k)
```

where:

```text
k = number of unique triplets
```

---

# Pattern Recognition

Keywords that indicate this pattern:

* Triplets
* Three Numbers
* Sum Equals Target
* Sorted Array

Common Technique:

```text
Fix One Element
+
Two Pointers
```

---

# Interview Takeaway

The key observation is:

```text
3Sum
=
Fix One Number
+
Two Sum
```

After sorting:

```text
If sum is too small
→ move left pointer right

If sum is too large
→ move right pointer left
```

This reduces the complexity from:

```text
O(n³)
```

to:

```text
O(n²)
```

---

# Key Learning

1. Sort before applying Two Pointers.
2. Fix one number and search for the other two.
3. Use left and right pointers to adjust the sum.
4. Sets help remove duplicate triplets.
5. Tuples can be stored in sets, lists cannot.
6. 3Sum is a classic extension of Two Sum.
