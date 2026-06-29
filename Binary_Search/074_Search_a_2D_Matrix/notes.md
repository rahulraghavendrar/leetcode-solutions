# 74. Search a 2D Matrix

## Category

Binary Search

## Difficulty

Medium

---

# Problem

You are given a 2D matrix with two important properties:

1. Every row is sorted in ascending order.
2. The first element of every row is greater than the last element of the previous row.

Example:

```python
matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
]
```

Search for a target value and return:

```python
True
```

if it exists,

otherwise return:

```python
False
```

The required time complexity is:

```text
O(log(m × n))
```

---

# Problem Understanding

Notice the matrix:

```text
1   3   5   7
10 11 16 20
23 30 34 60
```

Although it looks like a 2D matrix,

it is actually sorted like one long array:

```text
1 3 5 7 10 11 16 20 23 30 34 60
```

Instead of flattening the matrix,

we use Binary Search twice.

---

# My Thought Process

The important observation is:

```text
Every row has a range of values.
```

Example:

```text
Row 0

1 ............ 7
```

```text
Row 1

10 .......... 20
```

```text
Row 2

23 .......... 60
```

The target can belong to only one row.

So the first Binary Search is used to determine:

```text
Which row can possibly contain the target?
```

Once that row is found,

perform another Binary Search inside that row.

---

# ⭐ Key Observation (Most Important)

This problem uses **Binary Search twice**.

## First Binary Search

Find the correct row.

---

## Second Binary Search

Find the target inside that row.

Think of it as:

```text
Binary Search

↓

Filter the correct row

↓

Binary Search Again

↓

Find the element
```

This is the most important idea to remember.

---

# First Binary Search (Finding the Row)

Initialize:

```python
top = 0
bot = ROWS-1
```

These represent the rows.

Suppose:

```text
1   3   5   7
10 11 16 20
23 30 34 60
```

Target:

```python
16
```

Middle row:

```text
10 11 16 20
```

Check:

If:

```python
target > last element
```

move downward.

If:

```python
target < first element
```

move upward.

Otherwise,

the target must lie inside this row.

Break.

---

# Why Compare First And Last Element?

Suppose:

```text
Row

10 11 16 20
```

If target is:

```python
25
```

Then:

```text
25 > 20
```

Target cannot be inside this row.

Move down.

---

Suppose target is:

```python
5
```

Since:

```text
5 < 10
```

Target cannot be inside this row.

Move up.

---

Only when:

```python
10 <= target <= 20
```

can this row contain the target.

---

# Second Binary Search

After selecting the correct row,

perform a normal Binary Search.

Initialize:

```python
l = 0
r = COLS-1
```

Now search exactly like Problem 704.

---

# Complete Example

Input:

```python
matrix = [
[1,3,5,7],
[10,11,16,20],
[23,30,34,60]
]

target = 16
```

---

## Step 1

Rows:

```text
Row 0

1 ... 7
```

Target:

```text
16
```

Since:

```text
16 > 7
```

Discard Row 0.

---

Now check:

```text
10 ... 20
```

Target satisfies:

```text
10 <= 16 <= 20
```

Correct row found.

---

## Step 2

Binary Search inside:

```text
10 11 16 20
```

Middle:

```text
11
```

Target is larger.

Search right half.

---

Middle becomes:

```text
16
```

Found.

Return:

```python
True
```

---

# Example 2

Target:

```python
13
```

First Binary Search selects:

```text
10 11 16 20
```

Second Binary Search:

```text
10 11 16 20
```

13 is not found.

Return:

```python
False
```

---

# Solution Code

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])

        top = 0
        bot = ROWS - 1

        while top <= bot:

            midrow = (top + bot) // 2

            if target > matrix[midrow][-1]:
                top = midrow + 1

            elif target < matrix[midrow][0]:
                bot = midrow - 1

            else:
                break

        if not (top <= bot):
            return False

        mid = (top + bot) // 2

        l = 0
        r = COLS - 1

        while l <= r:

            m = (l + r) // 2

            if target > matrix[mid][m]:
                l = m + 1

            elif target < matrix[mid][m]:
                r = m - 1

            else:
                return True

        return False
```

---

# Functions Used

## len()

Used to find:

```python
ROWS
COLS
```

---

## List Indexing

```python
matrix[row][column]
```

Accesses an element.

---

# Data Structures Used

## 2D Array

The matrix itself.

No additional data structures are required.

---

# DSA Concepts Used

## Binary Search

Used twice.

---

## Row Filtering

First Binary Search determines the only possible row.

---

## Binary Search on Array

Second Binary Search finds the element inside that row.

---

# Complexity Analysis

Let:

```text
m = number of rows

n = number of columns
```

First Binary Search:

```text
O(log m)
```

Second Binary Search:

```text
O(log n)
```

Overall:

```text
O(log m + log n)
```

Since:

```text
log(m × n) = log(m) + log(n)
```

This satisfies:

```text
O(log(m × n))
```

---

Space Complexity:

```text
O(1)
```

---

# Pattern Recognition

Keywords that indicate this pattern:

* Sorted Matrix
* Row Wise Sorted
* First Element Greater Than Previous Row
* O(log n)
* Search

Common Pattern:

```text
Binary Search Twice
```

---

# Interview Takeaway

The biggest observation is:

```text
Do NOT search every row.
```

Instead:

1. Use Binary Search to identify the only possible row.
2. Use Binary Search again inside that row.

This converts a 2D search problem into two efficient Binary Searches.

---

# Key Learning

1. The matrix behaves like one sorted array.
2. Use the first Binary Search to determine the correct row.
3. Compare the target with the first and last element of each row.
4. Once the row is found, perform a normal Binary Search.
5. Binary Search is used twice in this problem.
6. Time Complexity is **O(log(m × n))**.
