# Challenge: First Unique Character in a String

This document describes the problem and the implemented solution for identifying the first non-repeated character in a text sequence (string).

## Problem Description

The goal is to develop a function that receives a string as input and identifies the first character that occurs only once throughout the entire sequence.

### Technical Requirements
* The analysis must follow the order from left to right.
* The system must be case-sensitive (e.g., 'A' is different from 'a').
* If no unique characters exist, the mandatory return must be an empty string ("").

## Test Case Examples

| Input | Expected Output | Justification |
| :--- | :--- | :--- |
| "abacabad" | "c" | 'a' and 'b' are duplicates; 'c' is the first unique in the sequence. |
| "swiss" | "w" | 's' occurs three times; 'w' is the first unique. |
| "aabbcc" | "" | All elements have repetitions. |
| "z" | "z" | The only character present is, by definition, non-repeated. |

---

challenge by: <span translate="no">Labs OneBitCode<span>