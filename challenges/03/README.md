# Challenge: ISBN-10 Validator

The objective is to develop a function that validates whether an ISBN-10 code is legitimate. Validity is determined by a specific mathematical weighted sum rule and formatting criteria.

## Formatting Rules
1. **Length**: The input must be exactly 10 characters long.
2. **Characters**: The first 9 characters must be numeric digits (0-9).
3. **Check Digit**: The 10th character can be a digit (0-9) or the letter 'X'.
4. **Value of X**: If the last character is 'X', it must be treated as the value 10.

## Validation Logic
The validity calculation follows these steps:

1. Each digit must be multiplied by its weight according to its position (from 1st to 10th).
   * Example: (1st digit * 1) + (2nd digit * 2) + ... + (10th digit * 10).
2. Calculate the total sum of all multiplications.
3. The code is considered **valid** only if the total sum is divisible by 11 (meaning the remainder of the division by 11 must be zero).

## Reference Examples

* **Valid ISBN**: `0306406152`
  * Sum: (0*1)+(3*2)+(0*3)+(6*4)+(4*5)+(0*6)+(6*7)+(1*8)+(5*9)+(2*10) = 165
  * Validation: 165 is divisible by 11.
  * Result: True

* **Valid ISBN (with X)**: `123456789X`
  * Sum: (1*1)+(2*2)+(3*3)+(4*4)+(5*5)+(6*6)+(7*7)+(8*8)+(9*9)+(10*10) = 385
  * Validation: 385 is divisible by 11.
  * Result: True

* **Invalid ISBN**: `1234567890`
  * Sum: 285
  * Validation: 285 is not divisible by 11 (remainder 10).
  * Result: False

Challenge by: <span class="notranslate">OneBitCode</span>