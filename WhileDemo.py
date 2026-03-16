it = 4
while it > 1:
    print(it)
    it = it - 1

print('while loop execution is done') # O/P = 4 3 2

# Code Explanation here below
#Initial value
#it = 4
#The loop runs while it > 1

#| Iteration | it value | Condition (it>1) | Printed    | New it value |
#| --------- | -------- | ---------------- | ---------- | ------------ |
#| 1         | 4        | True             | 4          | 3            |
#| 2         | 3        | True             | 3          | 2            |
#| 3         | 2        | True             | 2          | 1            |
#| 4         | 1        | False            | Loop stops | —            |


print("*********")
it = 4
while it > 1:
    if it != 3:
        print(it)
    it = it - 1

print('while loop execution is done') # O/P = 4  2

# Code Explanation here below
#Initial value
#it = 4
#The loop runs while it != 3
#Meaning:
# Print only if it is NOT equal to 3

#| Iteration | it value | it != 3 | Printed         | New it |
#| --------- | -------- | ------- | --------------- | ------ |
#| 1         | 4        | True    | 4               | 3      |
#| 2         | 3        | False   | (skip printing) | 2      |
#| 3         | 2        | True    | 2               | 1      |

#while with BREAK
it = 10
while it>1:
    if it == 3:
        break
    print(it)
    it = it - 1
print('while loop execution is done')

# Explanation of the previous code
#| Value | Action         |
#| ----- | -------------- |
#| 10    | Print          |
#| 9     | Print          |
#| 8     | Print          |
#| 7     | Print          |
#| 6     | Print          |
#| 5     | Print          |
#| 4     | Print          |
#| 3     | **Break loop** |


#Continue

it = 10
while it > 1:
    if it == 9:
        continue
    if it == 3:
        break
    print(it)
    it = it - 1

#| Iteration | it (start) | Condition `it>1` | Check `it==9` | Check `it==3` | Action                   | it after iteration |
#| --------- | ---------- | ---------------- | ------------- | ------------- | ------------------------ | ------------------ |
#| 1         | 10         | True             | False         | False         | Print 10                 | 9                  |
#| 2         | 9          | True             | **True**      | —             | **continue (skip rest)** | **9 (no change)**  |
#| 3         | 9          | True             | **True**      | —             | **continue**             | **9**              |
#| 4         | 9          | True             | **True**      | —             | **continue**             | **9**              |

print("*****")
it = 10
while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break
    print(it)
    it = it - 1

#| Iteration | it (start) | it > 1 | it == 9 | it == 3 | Action              | it (end) |
#| --------- | ---------- | ------ | ------- | ------- | ------------------- | -------- |
#| 1         | 10         | True   | False   | False   | Print 10            | 9        |
#| 2         | 9          | True   | True    | —       | Decrease → continue | 8        |
#| 3         | 8          | True   | False   | False   | Print 8             | 7        |
#| 4         | 7          | True   | False   | False   | Print 7             | 6        |
#| 5         | 6          | True   | False   | False   | Print 6             | 5        |
#| 6         | 5          | True   | False   | False   | Print 5             | 4        |
#| 7         | 4          | True   | False   | False   | Print 4             | 3        |
#| 8         | 3          | True   | False   | True    | **Break loop**      | —        |


