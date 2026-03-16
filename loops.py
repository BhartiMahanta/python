greeting = "Good Morning"

if greeting == "Good Morning":
    print("Condition matches")
    print("second line")
else:
    print("condition do not match")

print("if else condition code is completed")

#for loop

obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i)
    print(i*2)

# sum of first natural numbers 1+2+3+4+5 = 15
#range(i,j) -> i to j-1
summation = 0
for j in range(1, 6):
    summation = summation +j
print(summation)

#| Step  | j | summation calculation | summation value |
#| ----- | - | --------------------- | --------------- |
#| Start | – | –                     | 0               |
#| 1     | 1 | 0 + 1                 | 1               |
#| 2     | 2 | 1 + 2                 | 3               |
#| 3     | 3 | 3 + 3                 | 6               |
#| 4     | 4 | 6 + 4                 | 10              |
#| 5     | 5 | 10 + 5                | 15              |

print("****")
for k in range(1, 10, 2):
    print(k)

#| Step  | j | summation calculation | summation value |
#| ----- | - | --------------------- | --------------- |
#| Start | – | –                     | 0               |
#| 1     | 1 | 0 + 1                 | 1               |
#| 2     | 2 | 1 + 2                 | 3               |
#| 3     | 3 | 3 + 2                 | 5               |
#| 4     | 4 | 5 + 2                 | 7               |
#| 5     | 5 | 7 + 2                 | 9               |

print("**SKIPPING FIRST INDEX**")

for m in range(10):
    print(m)
