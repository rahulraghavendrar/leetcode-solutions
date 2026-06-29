# 875. Koko Eating Bananas

## Category

Binary Search

## Difficulty

Medium

---

# Problem

Koko has several piles of bananas.

Each pile contains:

```python
piles[i]
```

bananas.

She chooses an eating speed:

```python
k bananas/hour
```

Every hour:

* She eats from **only one pile**.
* If the pile has fewer than **k** bananas, she finishes the pile and waits for the next hour.

We need to find the **minimum eating speed** so that she finishes all the bananas within **h hours**.

---

# My Thought Process

At first glance, this does not look like a Binary Search problem because there is no sorted array.

The important observation is:

```text
We are not searching in the piles.

We are searching for the answer.
```

The answer is the eating speed.

Possible eating speeds are:

```text
1
2
3
...
max(piles)
```

These speeds are already sorted.

Therefore we can Binary Search on the answer.

---

# Why is the Search Space

```python
1 ..... max(piles)
```

Minimum speed:

```python
1
```

Koko can eat at least one banana every hour.

Maximum speed:

```python
max(piles)
```

If Koko eats as many bananas as the largest pile in one hour,

she can always finish every pile.

So:

```python
l = 1

r = maxPile
```

---

# Main Observation

For every speed,

calculate:

```text
How many hours does Koko need?
```

If the hours are:

```text
Too many
```

increase the speed.

If the hours are:

```text
Enough
```

try a smaller speed.

---

# ⭐ Important Concept — Using ceil()

This is one of the most important concepts in this problem.

Suppose:

```python
pile = 7

speed = 3
```

Normal division gives:

```python
7 / 3

= 2.33
```

But Koko cannot eat for:

```text
2.33 hours
```

She needs:

```text
Hour 1 → Eat 3

Hour 2 → Eat 3

Hour 3 → Eat 1
```

Total:

```python
ceil(7 / 3)

= ceil(2.33)

= 3
```

Therefore:

```python
hours += ceil(pile / speed)
```

is used.

---

Another example:

```python
pile = 10

speed = 4
```

Hours:

```text
Hour 1 → 4

Hour 2 → 4

Hour 3 → 2
```

Total:

```python
ceil(10 / 4)

= ceil(2.5)

= 3
```

Without using **ceil()**, the answer would be incorrect.

---

# Why Don't We Use

```python
sum(piles) // speed
```

Suppose:

```python
piles = [3,6,7]
```

Speed:

```python
3
```

Wrong calculation:

```python
16 // 3

= 5
```

Actual hours:

```text
3 → 1 hour

6 → 2 hours

7 → 3 hours
```

Total:

```text
6 hours
```

Each pile must be calculated separately.

---

# ⭐ Important Concept — Why There Is No

```python
elif
```

This is another important Binary Search pattern.

Initially we may think:

```python
if hours > h:

    l = mid + 1

elif hours < h:

    r = mid - 1

else:

    return mid
```

This is **wrong**.

---

Why?

Because the question asks for:

```text
The MINIMUM valid eating speed.
```

Suppose:

| Speed | Hours |
| ----: | ----: |
|     3 |    10 |
|     4 |     8 |
|     5 |     7 |
|     6 |     6 |

If:

```text
h = 8
```

Both:

```text
4
5
6
```

are valid speeds.

We must return:

```text
4
```

the smallest one.

---

Therefore,

whenever:

```python
hours <= h
```

the speed is already valid.

Instead of stopping,

save the answer.

```python
ans = midrate
```

Then continue searching on the left.

```python
r = midrate - 1
```

This is why the code becomes:

```python
if hours > h:

    l = midrate + 1

else:

    ans = midrate

    r = midrate - 1
```

Notice that

```python
elif
```

is completely removed.

The **else** automatically means:

```text
hours <= h
```

Both

```text
hours == h
```

and

```text
hours < h
```

are valid answers.

---

# Complete Example

Input:

```python
piles = [3,6,7,11]

h = 8
```

Search Space:

```text
1 .......... 11
```

---

Try:

```text
Speed = 6
```

Hours:

```text
3 → 1

6 → 1

7 → 2

11 → 2
```

Total:

```text
6 hours
```

Valid.

Save:

```python
ans = 6
```

Search left.

---

Try:

```text
Speed = 3
```

Hours:

```text
3 → 1

6 → 2

7 → 3

11 → 4
```

Total:

```text
10 hours
```

Too slow.

Search right.

---

Try:

```text
Speed = 4
```

Hours:

```text
1 + 2 + 2 + 3

= 8
```

Valid.

Save:

```python
ans = 4
```

Search left.

Eventually,

Binary Search ends.

Answer:

```text
4
```

---

# Solution Code

```python
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        maxPile = 0

        for i in piles:
            if i > maxPile:
                maxPile = i

        l = 1
        r = maxPile

        ans = maxPile

        while l <= r:

            midrate = (l + r) // 2

            hours = 0

            for i in piles:
                hours += ceil(i / midrate)

            if hours > h:
                l = midrate + 1

            else:
                ans = midrate
                r = midrate - 1

        return ans
```

---

# Functions Used

## ceil()

```python
ceil(i / midrate)
```

Rounds the division upward.

Example:

```python
ceil(7/3)

= 3
```

---

## max()

Can also be used as:

```python
maxPile = max(piles)
```

Time Complexity:

```text
O(n)
```

---

# Data Structures Used

## Array

Stores the banana piles.

No extra data structures are required.

---

# DSA Concepts Used

## Binary Search on Answer

Instead of searching an array,

Binary Search is performed on the possible eating speeds.

---

## Greedy Validation

For every speed,

calculate whether it is sufficient.

---

# Complexity Analysis

Let:

```text
n = len(piles)

m = max(piles)
```

Finding maximum:

```text
O(n)
```

Binary Search:

```text
O(log m)
```

Each Binary Search iteration checks every pile:

```text
O(n)
```

Overall:

```text
O(n log m)
```

---

Space Complexity:

```text
O(1)
```

---

# Pattern Recognition

Keywords that indicate this pattern:

* Minimum
* Maximum
* Smallest Valid Answer
* Binary Search on Answer
* Search Space

Common Pattern:

```text
Binary Search on Answer
```

---

# Interview Takeaway

This problem teaches one of the most important Binary Search patterns.

Whenever the problem asks for:

* Minimum speed
* Minimum capacity
* Minimum days
* Smallest valid value

Immediately think:

```text
Binary Search on the Answer
```

Instead of searching the input,

search the possible answers.

---

# Key Learning

1. Binary Search is performed on the eating speed.
2. The search space is from **1** to **max(piles)**.
3. Use **ceil()** because every pile takes whole hours.
4. Calculate hours for **each pile individually**.
5. Remove the `elif` because both `hours == h` and `hours < h` are valid.
6. Whenever `hours <= h`, save the answer and continue searching left.
7. This is a classic **Binary Search on Answer** problem.
