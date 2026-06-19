# 36. Valid Sudoku

## Category

Arrays & Hashing

## Difficulty

Medium

---

# Problem Understanding

A Sudoku board is valid if:

1. Every row contains unique digits.
2. Every column contains unique digits.
3. Every 3×3 box contains unique digits.

Important:

* Ignore "." cells.
* We only validate filled cells.
* We do NOT need to solve the Sudoku.

---

# My Thought Process

The phrase:

```text
No Repetition
```

immediately suggests:

```python
set()
```

because sets are excellent for duplicate detection.

If a number already exists in a set:

```python
if value in seen:
```

then we have found a duplicate.

---

# Main Idea

The Sudoku board is valid only if:

```text
Rows are valid
AND
Columns are valid
AND
3×3 boxes are valid
```

Therefore I perform three independent checks:

1. Row Validation
2. Column Validation
3. Box Validation

If any check fails:

```python
return False
```

Otherwise:

```python
return True
```

---

# Part 1: Row Validation

For every row:

Create a new set.

Example:

```text
5 3 . . 7 . . . .
```

Initialize:

```python
seen = set()
```

---

Read:

```text
5
```

Set:

```python
{"5"}
```

---

Read:

```text
3
```

Set:

```python
{"5","3"}
```

---

Read:

```text
7
```

Set:

```python
{"5","3","7"}
```

---

If another:

```text
5
```

appears:

```python
if board[i][j] in seen:
```

becomes True.

Immediately:

```python
return False
```

because rows cannot contain duplicates.

---

# Part 2: Column Validation

Same idea as rows.

Instead of:

```python
board[i][j]
```

we traverse:

```python
board[j][i]
```

which moves vertically.

Example Column:

```text
5
6
.
8
4
7
.
.
.
```

Set grows as:

```python
{"5"}
{"5","6"}
{"5","6","8"}
{"5","6","8","4"}
{"5","6","8","4","7"}
```

If any number appears twice:

```python
return False
```

---

# Part 3: 3×3 Box Validation

This is the most unique part of my solution.

---

# Key Observation

The Sudoku board contains:

```text
9 boxes
```

organized as:

```text
+-------+-------+-------+
| Box 1 | Box 2 | Box 3 |
+-------+-------+-------+
| Box 4 | Box 5 | Box 6 |
+-------+-------+-------+
| Box 7 | Box 8 | Box 9 |
+-------+-------+-------+
```

Each box contains:

```text
3 rows
3 columns
```

---

# How My Traversal Works

I process boxes three rows at a time.

Loop:

```python
for i in range(0,9,3):
```

Values of i:

```python
0
3
6
```

Meaning:

```text
Rows 0-2
Rows 3-5
Rows 6-8
```

---

# Using iterator

```python
iterator = 0
```

represents the current column.

Initially:

```text
Column 0
```

Then:

```text
Column 1
Column 2
```

These three columns belong to:

```text
First 3×3 box
```

---

# Example

When:

```python
i = 0
```

the code checks:

```python
board[0][iterator]
board[1][iterator]
board[2][iterator]
```

which means:

```text
Rows 0,1,2
Current Column
```

---

For:

```python
iterator = 0
```

Visited cells:

```text
(0,0)
(1,0)
(2,0)
```

---

For:

```python
iterator = 1
```

Visited cells:

```text
(0,1)
(1,1)
(2,1)
```

---

For:

```python
iterator = 2
```

Visited cells:

```text
(0,2)
(1,2)
(2,2)
```

Together these form:

```text
Top Left 3×3 Box
```

---

# Why seen.clear() Works

After:

```python
iterator = 2
```

we have finished the first box.

Then:

```python
iterator += 1
```

becomes:

```python
iterator = 3
```

At this point:

```python
seen.clear()
```

is executed.

Purpose:

```text
Forget all values from Box 1
```

because now we are moving to:

```text
Box 2
```

---

Similarly:

```python
iterator == 6
```

means:

```text
Box 3 starts
```

Again:

```python
seen.clear()
```

is called.

Purpose:

```text
Forget Box 2 values
Start checking Box 3
```

---

# Visual Example

Rows:

```text
0
1
2
```

Columns:

```text
0 1 2 | 3 4 5 | 6 7 8
```

Traversal:

```text
Box 1
-------
0 1 2

clear()

Box 2
-------
3 4 5

clear()

Box 3
-------
6 7 8
```

This is how one set is reused for all three boxes.

---

# Example Walkthrough

Suppose Top Left Box contains:

```text
5 3 .

6 . .

. 9 8
```

Initialize:

```python
seen = set()
```

---

Read:

```text
5
```

Set:

```python
{"5"}
```

---

Read:

```text
3
```

Set:

```python
{"5","3"}
```

---

Read:

```text
6
```

Set:

```python
{"5","3","6"}
```

---

Read:

```text
9
```

Set:

```python
{"5","3","6","9"}
```

---

Read:

```text
8
```

Set:

```python
{"5","3","6","8","9"}
```

---

If another:

```text
8
```

appears inside the same box:

```python
if value in seen:
```

becomes True.

Immediately:

```python
return False
```

---

# Complete Flow

Step 1:

```text
Check all rows
```

↓

Step 2:

```text
Check all columns
```

↓

Step 3:

```text
Check all 3×3 boxes
```

↓

If all pass:

```python
return True
```

---

# Data Structures Used

## Set

```python
seen = set()
```

Purpose:

Store digits already encountered.

Allows fast duplicate detection.

---

# Functions Used

## set()

Creates an empty set.

---

## add()

Usage:

```python
seen.add(value)
```

Purpose:

Insert value into the set.

---

## clear()

Usage:

```python
seen.clear()
```

Purpose:

Remove all values from the set.

Used when moving from one 3×3 box to the next.

---

## range()

Usage:

```python
range(0,9,3)
```

Output:

```python
0,3,6
```

Used to jump between row groups.

---

# DSA Concepts Used

## Hashing

Sets internally use hashing.

---

## Duplicate Detection

Main purpose of the problem.

---

## Matrix Traversal

Traversing:

* Rows
* Columns
* 3×3 Boxes

---

## State Resetting

Using:

```python
seen.clear()
```

to reuse the same set for multiple boxes.

---

# Complexity Analysis

Row Validation:

```text
O(81)
```

Column Validation:

```text
O(81)
```

Box Validation:

```text
O(81)
```

Total:

```text
O(243)
```

Since Sudoku size is fixed:

```text
O(1)
```

---

Space Complexity

Set stores at most:

```text
9 values
```

Therefore:

```text
O(1)
```

---

# Pattern Recognition

Keywords:

* No Repetition
* Duplicate Detection
* Sudoku
* Grid Validation
* Matrix Traversal

Common Data Structure:

```python
set()
```

---

# Interview Takeaway

The key observation is:

```text
Rows must be unique
Columns must be unique
Boxes must be unique
```

Whenever an interviewer says:

```text
No duplicates allowed
```

immediately think:

```python
set()
```

because duplicate detection is one of the strongest use cases of hashing.

---

# Key Learning

1. Sets are ideal for duplicate detection.
2. Sudoku validation consists of three independent checks.
3. `range(0,9,3)` helps process row groups.
4. `iterator` moves through columns.
5. `seen.clear()` is used to switch between 3×3 boxes.
6. Matrix problems often require separate row, column, and box traversal logic.
