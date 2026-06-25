# 853. Car Fleet

## Category

Stack

## Difficulty

Medium

---

# Problem

There are **n** cars travelling towards a common destination called **target**.

Each car has:

* A starting position
* A speed

A car **cannot overtake** another car.

If a faster car catches a slower car, they move together as a **single fleet** at the slower car's speed.

Return the number of fleets that reach the target.

---

# My Thought Process

At first glance, the problem looks like it requires simulating the movement of every car.

However, we don't actually care where cars meet.

The only thing that matters is:

```text
How long does each car take to reach the target?
```

Time taken:

```python
(target - position) / speed
```

---

# Key Observation 1

## Reverse Sort By Position

The very first step is:

```python
pair = [(p, s) for p, s in zip(position, speed)]

pair.sort(reverse=True)
```

This sorts the cars from:

```text
Closest to target
        ↓
Farthest from target
```

Example:

```python
target = 12

position = [10,8,0,5,3]

speed = [2,4,1,1,3]
```

Pairs before sorting:

```text
(10,2)
(8,4)
(0,1)
(5,1)
(3,3)
```

After reverse sorting:

```text
(10,2)
(8,4)
(5,1)
(3,3)
(0,1)
```

Now every car only needs to consider the fleet directly in front of it.

---

# Why Reverse Sorting Is Important

Suppose the cars are:

```text
Target
|
|
|

Car A  (closest)

Car B

Car C  (farthest)
```

Car C can never directly jump to Car A.

If Car B forms a fleet before that, Car C will first merge into **Car B's fleet**.

Therefore,

```text
Every car only compares with the fleet immediately ahead.
```

This is why reverse sorting works perfectly.

---

# Key Observation 2

Compute Arrival Time

For every car:

```python
time = (target - position) / speed
```

Example:

```python
target = 12

Car:
position = 10
speed = 2
```

Arrival time:

```python
(12-10)/2

= 1 hour
```

---

# Why Use a Stack?

The stack stores:

```text
Arrival times of fleets
```

Initially:

```python
stack = []
```

---

# Main Logic

For every car:

Calculate:

```python
time = (target-p)/s
```

Push:

```python
stack.append(time)
```

Now compare with the fleet in front.

If:

```python
stack[-1] <= stack[-2]
```

that means:

```text
The current car reaches the target earlier
(or at the same time)
than the fleet ahead.
```

So it catches that fleet.

They become one fleet.

Therefore:

```python
stack.pop()
```

Only the slower fleet remains.

---

# Important Catch

This is the most important concept in the problem.

Suppose:

```text
Target

Car A

Car B

Car C
```

Even if:

```text
Car C is very fast
```

it **cannot directly join Car A**.

Why?

Because Car B is in between.

If Car B forms a fleet first,

then Car C can only merge into **that fleet**.

So the order is always:

```text
Car A

↓

Fleet

↓

Car B joins

↓

New Fleet

↓

Car C joins that Fleet
```

It is impossible to skip a fleet.

This is why we only compare with the **top of the stack**.

---

# Complete Example

Input:

```python
target = 12

position = [10,8,0,5,3]

speed = [2,4,1,1,3]
```

After sorting:

```text
(10,2)
(8,4)
(5,1)
(3,3)
(0,1)
```

Arrival times:

```text
1
1
7
3
12
```

---

## Car 1

Time:

```text
1
```

Stack:

```text
[1]
```

---

## Car 2

Time:

```text
1
```

Stack becomes:

```text
[1,1]
```

Since:

```text
1 <= 1
```

they form one fleet.

Pop:

```text
[1]
```

---

## Car 3

Time:

```text
7
```

Stack:

```text
[1,7]
```

---

## Car 4

Time:

```text
3
```

Stack:

```text
[1,7,3]
```

Since:

```text
3 <= 7
```

Car 4 catches Car 3.

Pop:

```text
[1,7]
```

---

## Car 5

Time:

```text
12
```

Stack:

```text
[1,7,12]
```

No merge.

Final fleets:

```text
3
```

---

# Solution Code

```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [(p, s) for p, s in zip(position, speed)]

        pair.sort(reverse=True)

        stack = []

        for p, s in pair:

            stack.append((target - p) / s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
```

---

# Functions Used

## zip()

```python
zip(position, speed)
```

Combines:

```python
position
speed
```

into pairs.

---

## List Comprehension

```python
[(p, s) for p, s in zip(position, speed)]
```

Creates the list of cars.

---

## sort(reverse=True)

```python
pair.sort(reverse=True)
```

Sorts cars by position in descending order.

---

## append()

```python
stack.append(time)
```

Pushes arrival time.

---

## pop()

```python
stack.pop()
```

Removes merged fleet.

---

# Data Structures Used

## List of Pairs

Stores:

```python
(position, speed)
```

---

## Stack

Stores:

```text
Arrival times of fleets
```

---

# DSA Concepts Used

## Sorting

Cars are sorted from nearest to farthest.

---

## Stack

Maintains fleet arrival times.

---

## Greedy

Each car only checks the fleet immediately ahead.

---

# Complexity Analysis

Let:

```text
n = number of cars
```

Sorting:

```text
O(n log n)
```

Stack traversal:

```text
O(n)
```

Overall Time Complexity:

```text
O(n log n)
```

---

Space Complexity:

```text
O(n)
```

for the pairs and stack.

---

# Pattern Recognition

Keywords that indicate this pattern:

* Cars
* Fleet
* Cannot Overtake
* Merge
* Arrival Time

Common Pattern:

```text
Sorting + Stack + Greedy
```

---

# Interview Takeaway

The biggest insight is:

```text
A car never needs to compare with every car.
```

After reverse sorting,

every car only checks the **fleet immediately ahead**.

If it catches that fleet,

it automatically becomes part of it.

If there are multiple cars in between,

those cars will already have formed fleets before the current car reaches them.

---

# Key Learning

1. Convert every car into its arrival time.
2. Reverse sort cars by their position.
3. The stack stores fleet arrival times.
4. If a car reaches earlier than the fleet ahead, it joins that fleet.
5. A car cannot skip a fleet that lies in between.
6. This is a classic **Sorting + Stack + Greedy** interview problem.
