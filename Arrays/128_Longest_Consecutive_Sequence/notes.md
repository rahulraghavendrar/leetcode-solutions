# 128. Longest Consecutive Sequence

## Category

Arrays & Hashing

## Difficulty

Medium

---

# Problem Understanding

Given an unsorted array:

```python
nums = [100,4,200,1,3,2]
```

Find the length of the longest consecutive sequence.

Consecutive means:

```text
1,2,3,4
```

because each number differs by exactly 1.

Result:

```python
4
```

because:

```text
[1,2,3,4]
```

has length:

```text
4
```

---

# My Thought Process

A brute force approach would be:

For every number:

```text
Check num+1
Check num+2
Check num+3
...
```

But this would repeatedly check the same sequences and become too slow.

The key observation is:

```text
Every consecutive sequence has exactly one starting point.
```

Example:

```text
1 2 3 4
```

The true start is:

```text
1
```

because:

```text
0 does not exist
```

But:

```text
2 is not a start because 1 exists
3 is not a start because 2 exists
4 is not a start because 3 exists
```

Therefore we only start building a sequence when:

```python
num - 1 not in seen
```

---

# Main Idea

Convert the array into a set.

Why?

Because:

```python
x in seen
```

takes:

```text
O(1)
```

average time.

This allows us to quickly check whether:

```python
current + 1
```

exists.

---

# Step 1: Store Everything In A Set

Input:

```python
nums = [100,4,200,1,3,2]
```

Create:

```python
seen = {100,4,200,1,3,2}
```

Purpose:

```text
Fast lookup
Remove duplicates automatically
```

---

# Step 2: Find Sequence Starting Points

Loop through every number:

```python
for num in seen:
```

Check:

```python
if num - 1 not in seen:
```

This means:

```text
This number could be the start of a sequence.
```

---

# Example

Number:

```python
100
```

Check:

```python
99 in seen?
```

No.

Therefore:

```python
100
```

is a sequence start.

---

Number:

```python
4
```

Check:

```python
3 in seen?
```

Yes.

Therefore:

```python
4
```

belongs to an already existing sequence.

Skip it.

---

Number:

```python
1
```

Check:

```python
0 in seen?
```

No.

Therefore:

```python
1
```

is a sequence start.

---

# Step 3: Build The Sequence

When a valid starting point is found:

Initialize:

```python
length = 1
current = num
```

Now keep checking:

```python
current + 1
```

---

# Complete Flow Example

Input:

```python
nums = [100,4,200,1,3,2]
```

Set:

```python
{100,4,200,1,3,2}
```

---

## Start At 100

Check:

```python
99 in seen?
```

No.

Start sequence.

Current:

```python
100
```

Check:

```python
101 in seen?
```

No.

Length:

```python
1
```

---

## Start At 200

Check:

```python
199 in seen?
```

No.

Start sequence.

Current:

```python
200
```

Check:

```python
201 in seen?
```

No.

Length:

```python
1
```

---

## Start At 1

Check:

```python
0 in seen?
```

No.

Start sequence.

Current:

```python
1
```

---

Check:

```python
2 in seen?
```

Yes.

Length:

```python
2
```

Current:

```python
2
```

---

Check:

```python
3 in seen?
```

Yes.

Length:

```python
3
```

Current:

```python
3
```

---

Check:

```python
4 in seen?
```

Yes.

Length:

```python
4
```

Current:

```python
4
```

---

Check:

```python
5 in seen?
```

No.

Stop.

Final Length:

```python
4
```

---

Update:

```python
result = max(result, length)
```

Result becomes:

```python
4
```

---

# Why This Works

For:

```text
1 2 3 4
```

Only:

```text
1
```

starts the sequence.

The numbers:

```text
2
3
4
```

are skipped because:

```python
num - 1 in seen
```

This prevents repeatedly traversing the same sequence.

---

# Most Important Observation

Without this condition:

```python
if num - 1 not in seen:
```

we would do:

```text
1 → 2 → 3 → 4
2 → 3 → 4
3 → 4
4
```

Lots of repeated work.

With the condition:

```text
Only start from 1
```

The sequence is traversed exactly once.

This is what makes the solution O(n).

---

# Code Used

```python
class Solution(object):
    def longestConsecutive(self, nums):

        seen = set()

        for num in nums:
            seen.add(num)

        result = 0

        for num in seen:

            if num - 1 not in seen:

                length = 1
                current = num

                while current + 1 in seen:
                    current += 1
                    length += 1

                result = max(result, length)

        return result
```

---

# Data Structures Used

## Set

```python
seen = set()
```

Purpose:

* Fast lookup
* Remove duplicates
* O(1) average membership checking

---

# Functions Used

## set()

Creates an empty set.

---

## add()

Usage:

```python
seen.add(num)
```

Purpose:

Insert elements into the set.

---

## max()

Usage:

```python
result = max(result, length)
```

Purpose:

Store the longest sequence length found so far.

---

# DSA Concepts Used

## Hashing

Sets internally use hashing.

---

## Consecutive Sequence Detection

Checking:

```python
current + 1
```

repeatedly.

---

## Sequence Start Identification

Using:

```python
num - 1 not in seen
```

to identify the beginning of a sequence.

---

## Duplicate Elimination

The set automatically removes duplicates.

Example:

```python
[1,0,1,2]
```

becomes:

```python
{0,1,2}
```

---

# Complexity Analysis

Building Set:

```text
O(n)
```

Traversing Set:

```text
O(n)
```

Sequence Expansion:

```text
O(n)
```

Each number is visited at most a small number of times.

Total:

```text
O(n)
```

---

Space Complexity

Set stores all numbers:

```text
O(n)
```

---

# Pattern Recognition

Keywords that indicate this pattern:

* Consecutive Sequence
* Longest Sequence
* O(n) Requirement
* Fast Lookup
* Unique Elements

Common Data Structure:

```python
set()
```

---

# Interview Takeaway

The key insight is:

```text
Every consecutive sequence has exactly one starting point.
```

A number is a starting point if:

```python
num - 1 not in seen
```

Only start building sequences from these numbers.

This avoids repeated work and reduces the complexity from O(n²) to O(n).

---

# Key Learning

1. Sets provide O(1) average lookup.
2. Consecutive sequences have unique starting points.
3. Use `num - 1 not in seen` to identify sequence starts.
4. Only expand sequences from starting points.
5. Avoid repeatedly traversing the same sequence.
6. This is a classic Hash Set optimization problem.
