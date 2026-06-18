# 271. Encode and Decode Strings

## Category

Arrays & Hashing

## Difficulty

Medium

---

# Problem Understanding

We need to convert:

```python
["Hello", "World"]
```

into a single string that can be sent over a network.

Then later reconstruct:

```python
["Hello", "World"]
```

from that encoded string.

Important:

The strings may contain any ASCII characters.

Therefore we cannot simply join strings using a separator because the separator might already exist inside the strings.

We need a reliable way to know:

1. Where each string starts.
2. Where each string ends.

---

# My Thought Process

To reconstruct strings later, I need to know the length of every string.

Idea:

Store:

```text
length,length,length,...#
```

followed by the actual strings.

Example:

```python
["Hello","World"]
```

Lengths:

```python
[5,5]
```

Header:

```text
5,5,#
```

Then append the actual strings:

```text
5,5,#HelloWorld
```

Now the decoder knows:

* First string length = 5
* Second string length = 5

So it can correctly split the data.

---

# Encoding Approach

Store:

```text
length1,length2,length3,...#
```

Then append all strings.

Example:

```python
["cat","dog"]
```

Lengths:

```python
3
3
```

Encoded:

```text
3,3,#catdog
```

---

# Decoding Approach

1. Read lengths until '#'
2. Store lengths in a list
3. Start reading strings after '#'
4. Extract substrings using stored lengths

---

# Complete Flow Example

Input:

```python
["Hello","World"]
```

---

## Encoding Phase

Initialize:

```python
sizes = []
```

---

Read:

```python
"Hello"
```

Length:

```python
5
```

sizes:

```python
[5]
```

---

Read:

```python
"World"
```

Length:

```python
5
```

sizes:

```python
[5,5]
```

---

Create Header

```python
5,5,#
```

---

Append Strings

```python
HelloWorld
```

---

Final Encoded String

```text
5,5,#HelloWorld
```

---

# Decoding Phase

Input:

```text
5,5,#HelloWorld
```

---

Read Until '#'

Extract:

```python
[5,5]
```

---

Start After '#'

Current Position:

```text
HelloWorld
```

---

Read First Length

```python
5
```

Extract:

```python
Hello
```

Move pointer.

---

Read Second Length

```python
5
```

Extract:

```python
World
```

Move pointer.

---

Result:

```python
["Hello","World"]
```

---

# Why This Works

The decoder never has to guess.

It already knows exactly how many characters belong to each string.

Example:

```text
4,3,#abcdxyz
```

Means:

First string:

```python
abcd
```

Second string:

```python
xyz
```

No ambiguity.

---

# Main Trick

The most important idea is:

Store metadata before storing actual data.

Metadata = Length Information

Example:

```text
5,5,#HelloWorld
```

Header:

```text
5,5,#
```

contains all information needed to reconstruct the original list.

This is a common concept used in:

* Networking
* Serialization
* Communication Protocols
* File Formats

---

# Code Used

```python
class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes=[]
        result=[]

        for i in range(len(strs)):
            a=len(strs[i])
            sizes.append(a)

        for i in sizes:
            result.append(str(i))
            result.append(",")

        result.append("#")
        result.extend(strs)

        return "".join(result)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        sizes=[]
        k=0
        num=""

        while s[k] != '#':
            if s[k] == ',':
                sizes.append(int(num))
                num=""
            else:
                num += s[k]

            k += 1

        count = k + 1
        result=[]

        for length in sizes:
            result.append(s[count:count+length])
            count += length

        return result
```

---

# Data Structures Used

## List

Used for:

```python
sizes
result
```

Purpose:

Store lengths and decoded strings.

---

## String

Used to build:

```python
encoded_string
```

and extract substrings.

---

# Functions Used

## len()

Usage:

```python
len(strs[i])
```

Purpose:

Find string length.

---

## append()

Usage:

```python
sizes.append(a)
```

Purpose:

Add element to list.

---

## extend()

Usage:

```python
result.extend(strs)
```

Purpose:

Add all strings into result list.

Difference:

```python
append()
```

adds one item.

```python
extend()
```

adds multiple items.

---

## join()

Usage:

```python
"".join(result)
```

Purpose:

Convert list into one string.

Example:

```python
["Hello","World"]
```

becomes:

```python
HelloWorld
```

---

## int()

Usage:

```python
int(num)
```

Purpose:

Convert extracted length text into an integer.

---

# DSA Concepts Used

## Encoding

Convert structured data into a transferable format.

---

## Decoding

Reconstruct original data from encoded format.

---

## Serialization

Convert objects into a form that can be stored or transmitted.

This problem is essentially a simple serialization problem.

---

## Pointer Traversal

Used during decoding.

```python
count
```

acts as a pointer.

Moves through the encoded string.

---

# Complexity Analysis

Let:

```text
n = number of strings
m = total number of characters
```

Encoding:

```text
O(m)
```

Decoding:

```text
O(m)
```

Total:

```text
O(m)
```

---

Space Complexity:

Store encoded string and results.

```text
O(m)
```

---

# Pattern Recognition

Keywords indicating this pattern:

* Encode
* Decode
* Serialize
* Deserialize
* Network Transfer
* Communication

Typical solutions:

1. Length Prefix Encoding
2. Escape Character Encoding
3. Serialization Formats

---

# Interview Takeaway

When data must be reconstructed later:

Store metadata along with the data.

Your solution stores:

```text
Length Information + Actual Data
```

which guarantees accurate reconstruction.

This same principle is used in:

* HTTP packets
* TCP protocols
* Binary file formats
* Database storage systems

---

# Key Learning

1. Store metadata before data.
2. Length information removes ambiguity.
3. Serialization is a common interview topic.
4. Encoding and decoding often rely on pointer traversal.
5. `join()` and `extend()` are useful for string construction.
6. This problem introduces the Serialization Pattern.
