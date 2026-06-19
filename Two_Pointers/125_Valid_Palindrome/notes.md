# 125. Valid Palindrome

## Category

Two Pointers

## Difficulty

Easy

---

# Problem Understanding

A palindrome is a string that reads the same:

Forward:

```text
madam
```

Backward:

```text
madam
```

Same result.

Therefore:

```text
Palindrome
```

---

# Important Observation

The problem states:

1. Ignore uppercase and lowercase differences.
2. Ignore special characters.
3. Ignore spaces.
4. Keep only letters and numbers.

Example:

```python
"A man, a plan, a canal: Panama"
```

After cleaning:

```python
"amanaplanacanalpanama"
```

Now check whether it reads the same from both ends.

---

# My Thought Process

The string contains:

```text
Spaces
Commas
Colons
Special Characters
```

These should not participate in palindrome checking.

Therefore my first step is:

```text
Create a clean string
```

containing only:

```text
Letters
Numbers
```

and convert everything to lowercase.

After that:

```text
Use Two Pointers
```

to compare characters from both ends.

---

# Step 1: Build A Clean String

Initialize:

```python
newstr = ""
```

Loop through every character.

Check:

```python
s[i].isalnum()
```

Purpose:

```text
Keep only letters and digits.
```

---

# Example

Input:

```python
"A man, a plan, a canal: Panama"
```

Characters kept:

```text
A
m
a
n
a
p
l
a
n
a
c
a
n
a
l
P
a
n
a
m
a
```

Convert to lowercase:

```python
"amanaplanacanalpanama"
```

---

# Functions Used

## isalnum()

Usage:

```python
s[i].isalnum()
```

Purpose:

Checks whether the character is:

```text
Letter
OR
Digit
```

Examples:

```python
"A".isalnum() → True
"7".isalnum() → True
",".isalnum() → False
" ".isalnum() → False
```

---

## lower()

Usage:

```python
s[i].lower()
```

Purpose:

Convert uppercase letters to lowercase.

Example:

```python
"A" → "a"
"P" → "p"
```

---

# Step 2: Two Pointer Technique

After cleaning:

```python
newstr = "amanaplanacanalpanama"
```

Create:

```python
l = 0
r = len(newstr)-1
```

Meaning:

```text
l = Left Pointer
r = Right Pointer
```

---

# Visual Example

```text
a m a n a p l a n a c a n a l p a n a m a
^                                       ^
l                                       r
```

Compare:

```python
newstr[l]
newstr[r]
```

---

Both are:

```text
a
```

Match.

Move pointers.

```python
l += 1
r -= 1
```

---

Now:

```text
a m a n a p l a n a c a n a l p a n a m a
  ^                                   ^
  l                                   r
```

Compare:

```text
m
m
```

Match.

Move again.

---

Continue until:

```python
l >= r
```

---

# When Do We Return False?

Suppose:

```python
"raceacar"
```

Clean string:

```python
raceacar
```

Pointers:

```text
r a c e a c a r
^             ^
```

Compare:

```text
r == r
```

Good.

Move.

---

Compare:

```text
a == a
```

Good.

Move.

---

Compare:

```text
c == c
```

Good.

Move.

---

Compare:

```text
e != a
```

Mismatch.

Immediately:

```python
return False
```

because palindrome property is broken.

---

# Empty String Case

Suppose:

```python
s = " "
```

After cleaning:

```python
newstr = ""
```

Length:

```python
0
```

Return:

```python
True
```

because an empty string is considered a palindrome.

---

# Complete Flow Example

Input:

```python
s = "A man, a plan, a canal: Panama"
```

---

Step 1:

Create cleaned string.

```python
newstr = "amanaplanacanalpanama"
```

---

Step 2:

Initialize:

```python
l = 0
r = 20
```

---

Step 3:

Compare:

```text
a == a
m == m
a == a
...
```

All characters match.

---

Step 4:

Pointers cross.

Return:

```python
True
```

---

# Code Used

```python
class Solution(object):
    def isPalindrome(self, s):
        newstr=''

        for i in range(len(s)):
            if s[i].isalnum()==True:
                newstr+=s[i].lower()

        l,r=0,len(newstr)-1

        if len(newstr)==0:
            return True

        while l<r:

            if newstr[l]!=newstr[r]:
                return False

            l=l+1
            r=r-1

        return True
```

---

# Data Structures Used

## String

```python
newstr
```

Stores the cleaned version of the input.

---

# DSA Concepts Used

## String Processing

Removing unwanted characters.

---

## Two Pointers

Using:

```python
l
r
```

to compare characters from both ends.

---

## Palindrome Checking

Compare symmetric positions.

---

# Complexity Analysis

Let:

```text
n = length of original string
```

Cleaning String:

```text
O(n)
```

Palindrome Check:

```text
O(n)
```

Total:

```text
O(n)
```

---

Space Complexity

Clean string stores up to:

```text
n characters
```

Therefore:

```text
O(n)
```

---

# Pattern Recognition

Keywords that indicate this pattern:

* Palindrome
* Forward and Backward
* Symmetry
* Compare Ends

Common Technique:

```text
Two Pointers
```

---

# Interview Takeaway

Whenever a problem says:

```text
Compare from both ends
Check palindrome
```

immediately think:

```python
l = 0
r = len(data)-1
```

and move:

```python
l += 1
r -= 1
```

This is one of the most common Two Pointer patterns.

---

# Key Learning

1. `isalnum()` keeps letters and numbers.
2. `lower()` makes comparison case-insensitive.
3. Palindromes are checked using symmetric positions.
4. Two pointers compare both ends simultaneously.
5. If a mismatch occurs, return False immediately.
6. Valid Palindrome is one of the foundational Two Pointer problems.
