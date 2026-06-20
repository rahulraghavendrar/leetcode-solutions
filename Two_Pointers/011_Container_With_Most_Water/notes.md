# 11. Container With Most Water

## Category

Two Pointers

## Difficulty

Medium

---

# Problem Understanding

We are given an array:

```python
height = [1,8,6,2,5,4,8,3,7]
```

Each element represents the height of a vertical line.

The goal is to choose two lines that can hold the maximum amount of water.

---

# Formula

For any two lines:

```python
left
right
```

Area is:

```python
Area = Length × Breadth
```

where:

```python
Length = min(height[left], height[right])
```

because water can only rise to the shorter wall.

and

```python
Breadth = right - left
```

because width is the distance between the lines.

Therefore:

```python
Area = min(height[left], height[right]) * (right-left)
```

---

# My Thought Process

Brute Force would be:

```text
Try every pair of lines
```

Example:

```python
(0,1)
(0,2)
(0,3)
...
```

This takes:

```text
O(n²)
```

which is too slow.

---

# Key Observation

The width:

```python
right-left
```

always decreases whenever a pointer moves.

Therefore:

```text
To get a larger area,
we need a taller wall.
```

This leads to the Two Pointer solution.

---

# Step 1: Place Two Pointers

```python
left = 0
right = len(height)-1
```

Visual:

```text
1 8 6 2 5 4 8 3 7
^               ^
L               R
```

---

# Step 2: Compute Area

Current walls:

```python
1 and 7
```

Length:

```python
min(1,7) = 1
```

Breadth:

```python
8
```

Area:

```python
1 × 8 = 8
```

Store:

```python
maxarea = 8
```

---

# Why Use min()?

Suppose:

```text
1           7
```

Water level cannot reach:

```text
7
```

because the wall of height:

```text
1
```

will overflow first.

Therefore:

```python
min(height[left], height[right])
```

determines the water height.

---

# Step 3: Move A Pointer

Case 1:

```python
height[left] > height[right]
```

Example:

```text
8           3
```

The right wall is limiting the water.

Move:

```python
right -= 1
```

to search for a taller right wall.

---

Case 2:

```python
height[right] > height[left]
```

Example:

```text
3           8
```

The left wall is limiting the water.

Move:

```python
left += 1
```

to search for a taller left wall.

---

# Equal Height Case

Your solution handles:

```python
height[left] == height[right]
```

separately.

Example:

```text
5           5
```

You compare:

```python
height[left+1]
height[right-1]
```

and move towards the side that appears more promising.

If both are equal:

```python
left += 1
```
