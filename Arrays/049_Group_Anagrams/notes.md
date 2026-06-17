# 49. Group Anagrams

## Category

Arrays & Hashing

## Difficulty

Medium

---

# Problem Understanding

We are given a list of strings.

Strings that contain the same characters with the same frequency belong to the same group.

Example:

"eat"
"tea"
"ate"

All three contain:

a = 1
e = 1
t = 1

Therefore they belong to the same group.

We need to return all such groups.

---

# My Thought Process

When I see the word:

"Anagram"

I immediately think:

"Can I create a common representation for all anagrams?"

Example:

eat → aet
tea → aet
ate → aet

After sorting, all anagrams become identical.

Therefore:

Sorted String = Unique Key

This key can be used inside a Hash Map.

---

# Approach

Use:

defaultdict(list)

where

Key = Sorted String

Value = List of all strings having that sorted string

Example:

{
"aet": ["eat", "tea", "ate"]
}

---

# Complete Flow Example

Input:

strs = ["eat","tea","tan","ate","nat","bat"]

Initial Dictionary:

{}

---

## Iteration 1

Current String:

eat

Sort:

sorted("eat")

Result:

['a','e','t']

Join:

"aet"

Dictionary:

{
"aet": ["eat"]
}

---

## Iteration 2

Current String:

tea

Sort:

sorted("tea")

Result:

['a','e','t']

Join:

"aet"

Dictionary:

{
"aet": ["eat","tea"]
}

---

## Iteration 3

Current String:

tan

Sort:

sorted("tan")

Result:

['a','n','t']

Join:

"ant"

Dictionary:

{
"aet": ["eat","tea"],
"ant": ["tan"]
}

---

## Iteration 4

Current String:

ate

Sorted Key:

"aet"

Dictionary:

{
"aet": ["eat","tea","ate"],
"ant": ["tan"]
}

---

## Iteration 5

Current String:

nat

Sorted Key:

"ant"

Dictionary:

{
"aet": ["eat","tea","ate"],
"ant": ["tan","nat"]
}

---

## Iteration 6

Current String:

bat

Sorted Key:

"abt"

Dictionary:

{
"aet": ["eat","tea","ate"],
"ant": ["tan","nat"],
"abt": ["bat"]
}

---

# Final Dictionary

{
"aet": ["eat","tea","ate"],
"ant": ["tan","nat"],
"abt": ["bat"]
}

Return:

[
["eat","tea","ate"],
["tan","nat"],
["bat"]
]

---

# Code Used

```python
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        ans = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)

        return ans.values()
```

# Data Structures Used

## Hash Map

Implemented using:

```python
defaultdict(list)
```

Purpose:

Store groups efficiently.

Example:

```python
{
    "aet": ["eat","tea","ate"]
}
```

---

## List

Used to store all words belonging to the same group.

Example:

```python
["eat","tea","ate"]
```

---

# Libraries Used

## collections.defaultdict

Import:

```python
from collections import defaultdict
```

Purpose:

Automatically creates an empty list when a new key is encountered.

Without defaultdict:

```python
if key not in ans:
    ans[key] = []

ans[key].append(s)
```

With defaultdict:

```python
ans[key].append(s)
```

Much cleaner.

---

# Functions Used

## sorted()

Usage:

```python
sorted(s)
```

Example:

```python
sorted("eat")
```

Output:

```python
['a','e','t']
```

Purpose:

Sort characters alphabetically.

---

## "".join()

Usage:

```python
"".join(sorted(s))
```

Example:

```python
['a','e','t']
```

becomes

```python
"aet"
```

Purpose:

Convert character list to string.

---

## append()

Usage:

```python
ans[key].append(s)
```

Purpose:

Add word to an anagram group.

---

## values()

Usage:

```python
ans.values()
```

Purpose:

Return all grouped anagrams.

---

# DSA Concepts Used

## Hashing

Store groups using keys.

---

## Grouping

Multiple strings belong to the same bucket.

---

## Canonical Representation

Every anagram is converted into a standard form.

Example:

eat → aet
tea → aet
ate → aet

All map to the same key.

---

# Complexity Analysis

Let:

n = Number of Strings

k = Average Length of String

Sorting each string:

O(k log k)

For n strings:

Time Complexity:

O(n × k log k)

Space Complexity:

O(n × k)

---

# Pattern Recognition

Keywords that indicate this pattern:

* Group
* Anagram
* Rearrange letters
* Same characters
* Character frequency

Typical Solution:

Hash Map + Canonical Key

Common Canonical Keys:

1. Sorted String
2. Character Frequency Count

---

# Interview Takeaway

When a problem says:

"Group all strings that are anagrams"

Think:

1. Convert each string into a standard representation.
2. Use that representation as a Hash Map key.
3. Store all matching strings in the same bucket.

For this solution:

Canonical Representation = Sorted String

Example:

eat → aet
tea → aet
ate → aet

Same key ⇒ Same group.
