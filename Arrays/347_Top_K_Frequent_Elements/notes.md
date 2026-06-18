# 347. Top K Frequent Elements

## Category

Arrays & Hashing

## Difficulty

Medium

---

# Problem Understanding

We are given:

* An integer array `nums`
* An integer `k`

We need to return the `k` elements that occur most frequently.

Example:

```python
nums = [1,1,1,2,2,3]
k = 2
```

Frequency of elements:

```text
1 → 3 times
2 → 2 times
3 → 1 time
```

Top 2 frequent elements:

```python
[1,2]
```

---

# My Thought Process

The phrase:

```text
Top K Frequent
```

immediately suggests:

```text
Frequency Counting
```

First, we need to know how many times every number appears.

A Hash Map is perfect for storing:

```python
number → frequency
```

After finding frequencies:

1. Store frequency information.
2. Sort based on frequency.
3. Extract the top k elements.

---

# Approach

## Step 1

Count frequencies using a Hash Map.

Example:

```python
{
    1:3,
    2:2,
    3:1
}
```

---

## Step 2

Convert the Hash Map into a list.

Format:

```python
[frequency, number]
```

Example:

```python
[
    [3,1],
    [2,2],
    [1,3]
]
```

---

## Step 3

Sort the list.

After sorting:

```python
[
    [1,3],
    [2,2],
    [3,1]
]
```

The highest frequency automatically moves to the end.

---

## Step 4

Repeatedly pop from the end.

Example:

```python
[3,1]
```

means:

```text
frequency = 3
number = 1
```

Add:

```python
1
```

to the result.

Repeat until k elements are collected.

---

# Complete Flow Example

Input:

```python
nums = [1,1,1,2,2,3]
k = 2
```

---

## Frequency Counting

Initial:

```python
hash = {}
seen = set()
```

---

Read 1

```python
hash = {1:1}
seen = {1}
```

---

Read 1

```python
hash = {1:2}
```

---

Read 1

```python
hash = {1:3}
```

---

Read 2

```python
hash = {
    1:3,
    2:1
}
```

---

Read 2

```python
hash = {
    1:3,
    2:2
}
```

---

Read 3

```python
hash = {
    1:3,
    2:2,
    3:1
}
```

---

# Create Frequency List

Loop:

```python
for num, freq in hash.items():
```

Create:

```python
[
    [3,1],
    [2,2],
    [1,3]
]
```

Format:

```python
[frequency, number]
```

---

# IMPORTANT OBSERVATION (Main Trick)

The most important part of this solution is:

```python
lis.append([freq, num])
```

NOT:

```python
lis.append([num, freq])
```

---

Why?

Python sorts nested lists using the first element.

Example:

```python
[
    [3,1],
    [2,2],
    [1,3]
]
```

After:

```python
lis.sort()
```

Result:

```python
[
    [1,3],
    [2,2],
    [3,1]
]
```

Python sorted using:

```python
frequency
```

because frequency is stored first.

---

Suppose we had stored:

```python
[
    [1,3],
    [2,2],
    [3,1]
]
```

Format:

```python
[number, frequency]
```

Now sorting would happen by:

```python
number
```

instead of frequency.

This would completely break the solution.

---

# Why pop() Works

After sorting:

```python
[
    [1,3],
    [2,2],
    [3,1]
]
```

Largest frequency is at the end.

Therefore:

```python
lis.pop()
```

returns:

```python
[3,1]
```

Extract:

```python
[3,1][1]
```

Result:

```python
1
```

which is the most frequent element.

---

# Extract Top K

Initial:

```python
res = []
k = 2
```

---

Pop #1

```python
[3,1]
```

Add:

```python
res = [1]
```

---

Pop #2

```python
[2,2]
```

Add:

```python
res = [1,2]
```

---

k becomes 0

Return:

```python
[1,2]
```

---

# Code Used

```python
class Solution(object):
    def topKFrequent(self, nums, k):
        hash={}
        seen=set()

        for i in range(len(nums)):
            if nums[i] not in seen:
                hash[nums[i]]=1
                seen.add(nums[i])
            else:
                hash[nums[i]]+=1

        lis=[]

        for num,freq in hash.items():
            lis.append([freq,num])

        lis.sort()

        res=[]

        while True:
            if k==0:
                return res
            else:
                a=lis.pop()[1]
                res.append(a)
                k=k-1
```

---

# Data Structures Used

## Hash Map

```python
hash = {}
```

Purpose:

Store frequencies.

Example:

```python
{
    1:3,
    2:2,
    3:1
}
```

---

## Set

```python
seen = set()
```

Purpose:

Track unique elements already encountered.

---

## List

```python
lis = []
```

Purpose:

Store:

```python
[frequency, number]
```

pairs.

---

# Functions Used

## set()

Usage:

```python
seen = set()
```

Purpose:

Store unique values.

---

## items()

Usage:

```python
hash.items()
```

Purpose:

Return:

```python
(key, value)
```

pairs.

Example:

```python
{
    1:3,
    2:2
}
```

becomes:

```python
(1,3)
(2,2)
```

---

## append()

Usage:

```python
lis.append([freq,num])
```

Purpose:

Add frequency-number pair.

---

## sort()

Usage:

```python
lis.sort()
```

Purpose:

Sort based on frequency because frequency is stored first.

---

## pop()

Usage:

```python
lis.pop()
```

Purpose:

Remove highest-frequency element.

---

# DSA Concepts Used

## Hashing

Used for frequency counting.

---

## Frequency Counting

Example:

```text
1 → 3
2 → 2
3 → 1
```

---

## Sorting

Sort frequency-number pairs.

---

## Top-K Retrieval

After sorting, repeatedly retrieve the largest frequencies.

---

# Complexity Analysis

Let:

```text
n = length of nums
u = number of unique elements
```

Frequency Counting:

```text
O(n)
```

Building Frequency List:

```text
O(u)
```

Sorting:

```text
O(u log u)
```

Total:

```text
O(n + u log u)
```

Worst Case:

```text
O(n log n)
```

---

Space Complexity:

Hash Map:

```text
O(u)
```

List:

```text
O(u)
```

Total:

```text
O(u)
```

---

# Pattern Recognition

Keywords that indicate this pattern:

* Top K
* Most Frequent
* Frequency
* Occurrence Count

Common Solutions:

1. Hash Map + Sorting
2. Hash Map + Heap
3. Hash Map + Bucket Sort

---

# Interview Takeaway

When a problem says:

```text
Top K Frequent
```

Think:

1. Count frequencies.
2. Store frequency information.
3. Retrieve the largest frequencies.

Most Important Insight:

When sorting by a value:

```python
[value_to_sort_by, actual_data]
```

Examples:

Sort by frequency:

```python
[freq, num]
```

Sort by marks:

```python
[marks, student]
```

Sort by profit:

```python
[profit, job]
```

The first element controls Python's sorting order.

---

# Key Learning

1. Hash Maps are excellent for frequency counting.
2. Top-K problems usually require ranking frequencies.
3. Python sorts nested lists using the first element.
4. To sort by frequency, store:

```python
[freq, num]
```

not

```python
[num, freq]
```

5. The sorting key should always be placed first.
6. After sorting, pop() can efficiently retrieve the largest frequencies.
7. This problem introduces the Top-K Retrieval pattern.
