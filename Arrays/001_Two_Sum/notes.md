# 1. Two Sum

## Problem Category

Arrays & Hashing

## Difficulty

Easy

---

## My Approach

I used a hash map (dictionary) to store each number and its index.

### Step 1

Store all numbers in a dictionary.

```python
hash[nums[i]] = i
```

Example:

nums = [2,7,11,15]

Dictionary:

{
    2:0,
    7:1,
    11:2,
    15:3
}

---

### Step 2

For every number, calculate the required complement.

Formula:

target - current_number

```python
n = target - nums[i]
```

Example:

target = 9

Current number = 2

Required complement:

9 - 2 = 7

---

### Step 3

Check whether the complement exists in the hash map.

```python
if n in hash
```

If present:

Return the current index and complement index.

```python
return [i, hash[n]]
```

---

### Step 4

Avoid using the same element twice.

```python
hash[n] != i
```

This ensures different indices are used.

---

## Data Structures Used

### Dictionary (Hash Map)

Purpose:

- Store number → index mapping
- Fast lookup of complements

Example:

```python
{
    2:0,
    7:1,
    11:2
}
```

---

## Python Functions Used

### len()

Purpose:

Returns size of array.

Usage:

```python
len(nums)
```

---

### Dictionary Assignment

Usage:

```python
hash[nums[i]] = i
```

Purpose:

Store value-index mapping.

---

### Dictionary Lookup

Usage:

```python
n in hash
```

Purpose:

Checks whether complement exists.

Time Complexity:

O(1) average

---

## DSA Concepts Used

### Hashing

Store values for constant-time lookup.

Why?

Brute force would require checking every pair.

Hashing reduces lookup time significantly.

---

### Complement Search

Core idea:

For every number:

Find

target - current_number

Example:

```text
target = 9

Current = 2

Need = 7
```

Search for 7 in hash map.

---

### Index Mapping

Store:

value → index

Example:

```python
{
    2:0,
    7:1,
    11:2
}
```

Allows direct access to the required index.

---

## Complexity Analysis

### Time Complexity

Building Hash Map:

O(n)

Searching Complements:

O(n)

Total:

O(n)

---

### Space Complexity

Hash Map stores all elements.

O(n)

---

## Pattern Recognition

Keywords that indicate this pattern:

- Pair Sum
- Two Sum
- Target Sum
- Complement
- Find two numbers

Typical solution:

Hash Map

Formula:

target - nums[i]

---

## Alternative Optimal Solution

One-pass hash map solution:

```python
class Solution(object):
    def twoSum(self, nums, target):
        hash = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hash:
                return [hash[complement], i]

            hash[nums[i]] = i
```

Time Complexity:

O(n)

Space Complexity:

O(n)

This is the most common interview solution.

---

## Key Learning

1. Hash Maps provide O(1) average lookup.
2. Pair-sum problems often use complements.
3. Store values with indices for direct access.
4. Two Sum is one of the most important Hashing interview patterns.
5. When asked to find two elements summing to a target, think:
   
   complement = target - current_element