# 242. Valid Anagram

## Problem Category

Arrays & Hashing

## Difficulty

Easy

---

## My Approach

I used two dictionaries to count the frequency of every character in both strings.

If both strings have the same frequency for every character, they are anagrams.

---

## Step 1: Length Check

Before doing any processing, check if both strings have the same length.

```python
if len(s) != len(t):
    return False
```

Why?

Two strings of different lengths can never be anagrams.

Example:

s = "rat"
t = "carp"

Lengths:

3 != 4

Return False immediately.

---

## Step 2: Create Frequency Dictionaries

```python
hash1 = {}
hash2 = {}
```

Purpose:

- hash1 stores frequencies of characters in s
- hash2 stores frequencies of characters in t

---

## Step 3: Initialize Keys

```python
for i in range(len(s)):
    hash1[s[i]] = 0
    hash2[t[i]] = 0
```

Example:

s = "anagram"

Dictionary after initialization:

```python
{
    'a':0,
    'n':0,
    'g':0,
    'r':0,
    'm':0
}
```

---

## Step 4: Count Frequencies

```python
for i in range(len(s)):
    hash1[s[i]] += 1
    hash2[t[i]] += 1
```

Example:

s = "anagram"

Result:

```python
{
    'a':3,
    'n':1,
    'g':1,
    'r':1,
    'm':1
}
```

t = "nagaram"

Result:

```python
{
    'n':1,
    'a':3,
    'g':1,
    'r':1,
    'm':1
}
```

---

## Step 5: Compare Dictionaries

```python
if hash1 == hash2:
    return True
```

Python dictionaries are equal when:

- Keys are identical
- Values are identical

Since the frequency counts match, the strings are anagrams.

---

## Data Structures Used

### Dictionary (Hash Map)

Purpose:

- Store character frequencies
- Enable fast lookup and comparison

Example:

```python
hash1 = {}
```

---

## Python Functions Used

### len()

Purpose:

Returns string length.

Usage:

```python
len(s)
```

Time Complexity:

```python
O(1)
```

---

### Dictionary Assignment

Usage:

```python
hash1[s[i]] = 0
```

Purpose:

Creates or updates a key.

---

### Dictionary Comparison

Usage:

```python
hash1 == hash2
```

Purpose:

Checks whether both dictionaries contain identical key-value pairs.

---

## DSA Concepts Used

### Hashing

Used to store character frequencies efficiently.

Why?

Frequency counting is one of the most common applications of hashing.

---

### Frequency Counting

Track how many times each character appears.

Example:

```text
banana

b → 1
a → 3
n → 2
```

---

### Character Mapping

Each character acts as a key.

Example:

```python
{
    'a': 3,
    'n': 2
}
```

---

## Complexity Analysis

### Time Complexity

Length Check:

O(1)

Initialization Loop:

O(n)

Counting Loop:

O(n)

Dictionary Comparison:

O(n)

Overall:

O(n)

---

### Space Complexity

Two dictionaries storing characters.

O(k)

where:

k = number of unique characters

Worst case:

O(n)

---

## Pattern Recognition

Keywords that suggest frequency counting:

- Anagram
- Character Count
- Frequency
- Occurrence
- Permutation
- Rearrangement

Common Solutions:

- Hash Map
- Counter
- Fixed-size Array (26 letters)

---

## Alternative Optimal Solution

Using Counter:

```python
from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)
```

Time Complexity:

O(n)

Space Complexity:

O(k)

---

## Key Learning

1. Hash Maps are excellent for frequency counting.
2. Anagram problems usually require comparing frequencies.
3. Dictionary equality can be used directly in Python.
4. Character frequency counting is a fundamental Arrays & Hashing pattern.