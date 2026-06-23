# 42. Trapping Rain Water

## Category

Two Pointers

## Difficulty

Hard

---

# Problem

Given an elevation map represented by an array:

```python
height = [0,1,0,2,1,0,1,3,2,1,2,1]
```

Each number represents the height of a wall.

After rain falls, water gets trapped between walls.

Return the total amount of trapped water.

---

# Intuition

For water to be trapped at a position, there must be:

* A wall on the left
* A wall on the right

The water level is determined by the shorter of these two walls.

Example:

```text
3     5
█     █
█ ~~~ █
█ ~~~ █
---------
```

Even though the right wall is height 5, water can only rise to height 3 because it would overflow from the shorter wall.

Therefore:

```python
Water Level = min(Left Maximum, Right Maximum)
```

---

# Key Observation

For every position:

```python
Water Trapped =
min(leftMax, rightMax) - currentHeight
```

Example:

```python
height = [3,0,3]
```

Visual:

```text
█   █
█~~~█
█~~~█
-----
```

At the middle position:

```python
leftMax = 3
rightMax = 3
currentHeight = 0
```

Water:

```python
3 - 0 = 3
```

units.

---

# My Approach

Use two pointers:

```python
left = 0
right = len(height) - 1
```

Track:

```python
leftmax
rightmax
```

where:

```python
leftmax = tallest wall seen from left
rightmax = tallest wall seen from right
```

---

# Why Two Pointers Work

Suppose:

```python
leftmax = 3
rightmax = 7
```

The water level is:

```python
min(3,7)
```

which is:

```python
3
```

Notice that the right side does not matter anymore.

Since the smaller maximum determines the water level, we process the side with the smaller maximum.

---

# Algorithm

### Step 1

Initialize:

```python
left = 0
right = len(height)-1

leftmax = height[left]
rightmax = height[right]

result = 0
```

---

### Step 2

While:

```python
left < right
```

keep moving inward.

---

### Step 3

If:

```python
leftmax < rightmax
```

move the left pointer.

```python
left += 1
```

Update:

```python
leftmax = max(leftmax, height[left])
```

Water trapped:

```python
leftmax - height[left]
```

Add it to the answer.

---

### Step 4

Otherwise move the right pointer.

```python
right -= 1
```

Update:

```python
rightmax = max(rightmax, height[right])
```

Water trapped:

```python
rightmax - height[right]
```

Add it to the answer.

---

# Example Walkthrough

Input:

```python
height = [4,2,0,3,2,5]
```

Initialize:

```python
left = 0
right = 5

leftmax = 4
rightmax = 5
```

---

## Position 1

```python
height[1] = 2
```

Water:

```python
4 - 2 = 2
```

Result:

```python
2
```

---

## Position 2

```python
height[2] = 0
```

Water:

```python
4 - 0 = 4
```

Result:

```python
6
```

---

## Position 3

```python
height[3] = 3
```

Water:

```python
4 - 3 = 1
```

Result:

```python
7
```

---

## Position 4

```python
height[4] = 2
```

Water:

```python
4 - 2 = 2
```

Result:

```python
9
```

Final Answer:

```python
9
```

---

# Solution Code

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        leftmax = height[left]
        rightmax = height[right]

        result = 0

        while left < right:

            if leftmax < rightmax:

                left += 1

                leftmax = max(height[left], leftmax)

                result += leftmax - height[left]

            else:

                right -= 1

                rightmax = max(height[right], rightmax)

                result += rightmax - height[right]

        return result
```

---

# Functions Used

## max()

```python
leftmax = max(height[left], leftmax)
```

Purpose:

Update the tallest wall seen so far.

---

# Data Structures Used

## Variables

```python
left
right
leftmax
rightmax
result
```

No extra arrays are used.

---

# DSA Concepts Used

## Two Pointers

Process the array from both ends.

---

## Prefix Maximum

Represented by:

```python
leftmax
```

---

## Suffix Maximum

Represented by:

```python
rightmax
```

---

## Greedy Observation

Always process the side with the smaller maximum.

---

# Complexity Analysis

## Time Complexity

Each pointer moves at most once through the array.

```python
O(n)
```

---

## Space Complexity

Only a few variables are used.

```python
O(1)
```

---

# Pattern Recognition

Keywords that indicate this pattern:

* Rain Water
* Elevation Map
* Trapped Water
* Walls
* Height Array

Common Pattern:

```text
Two Pointers + Left Maximum + Right Maximum
```

---

# Key Learning

1. Water can only be trapped if walls exist on both sides.
2. Water level is determined by the shorter boundary.
3. Use `leftmax` and `rightmax` to track the tallest walls.
4. Process the side with the smaller maximum.
5. Achieve O(n) time and O(1) space.
6. This is one of the most important Two Pointer interview problems.
