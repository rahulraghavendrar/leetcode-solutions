# 217. Contains Duplicate

## Problem Category

Arrays & Hashing

## Difficulty

Easy

---

## My Approach

I used a Python dictionary to keep track of the occurrences of each number.

### Step 1

Traverse the array and insert every element into the dictionary with an initial value of 0.

Example:

nums = [1,2,3,1]

Dictionary after first pass:

{
    1: 0,
    2: 0,
    3: 0
}

---

### Step 2

Traverse the array again.

For each element:

- If its count is already 1, a duplicate has been found.
- Return True immediately.
- Otherwise increment its count.

Example:

Element = 1

Dictionary:

{
    1: 1,
    2: 0,
    3: 0
}

When 1 appears again:

Dictionary[1] == 1

Return True.

---

## Data Structures Used

### Dictionary (Hash Map)

Purpose:

- Store each unique number as a key.
- Track whether the number has appeared before.

Example:

```python
hash = {}
```

---

## Python Functions Used

### len()

Purpose:

Returns the size of the array.

Usage:

```python
len(nums)
```

Example:

```python
nums = [1,2,3]

len(nums)
```

Output:

```python
3
```

---

### Dictionary Access

Usage:

```python
hash[nums[i]]
```

Purpose:

Retrieve the value associated with a key.

Example:

```python
hash[1]
```

Output:

```python
0
```

---

### Dictionary Assignment

Usage:

```python
hash[nums[i]] = 0
```

Purpose:

Insert or update a key-value pair.

Example:

```python
hash[5] = 0
```

Dictionary:

```python
{
    5:0
}
```

---

## DSA Concepts Used

### Hashing

Hashing allows constant-time average lookup.

Why used?

- Quickly determine whether a number has already appeared.
- Faster than comparing every element with every other element.

---

### Duplicate Detection

Goal:

Identify whether any value appears more than once.

Common interview keywords:

- duplicate
- repeated element
- unique element
- frequency counting

These keywords often indicate the use of:

- Dictionary
- Hash Set
- Counter

---

## Complexity Analysis

### Time Complexity

First loop:

O(n)

Second loop:

O(n)

Overall:

O(n)

---

### Space Complexity

Dictionary stores all unique elements.

O(n)

---

## Pattern Recognition

When a problem contains words like:

- Duplicate
- Repeated
- Frequency
- Count
- Occurrence

Consider using:

- Hash Map
- Hash Set
- Counter

---

## Alternative Optimal Solution

A Hash Set can solve this problem with a single traversal.

```python
class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False
```

Time Complexity: O(n)

Space Complexity: O(n)

This is the most commonly expected interview solution.

---

## Key Learning

1. Dictionaries provide O(1) average lookup.
2. Hashing is a common technique for duplicate detection.
3. Problems involving frequency counting often use dictionaries or sets.
4. Duplicate detection is one of the most common Arrays & Hashing interview patterns.