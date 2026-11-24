#1
"""a = input("a :")

b = " "
for i in range (len(a) -1,-1,-1):
    b = b + a[i]
    
print ("rev string",b)"""

#2

"""x = input( )

s =0

for i in x :
    if i == " ":
        count = 0 
    else :
        count += 1 
print (count)"""

"""n = input(" ")

count = 0 

for i in range (1,len(n)+1):
    if n[-i]== 0:
        break 
    else :
        count += 1 
print (count)"""


#3
"""x = input("sentence :")

y = input("word :")
count = 0 
for i in x :
    if y == i :
        count = count +1 
    print (count)"""
    
    
#4
"""x = input("Enter a sentence: ").lower()
y = "abcdefghijklmnopqrstuvwxyz"
s = ""

for i in y:
    m = 0

    while m < len(x):
        if x[m] == i:
            break
        m = m + 1

    if m == len(x):
        s = s + i

if s == "":
    print("It is a pangram.")
else:
    print("It is not a pangram.")"""
    
    
#5
"""s = input("Enter a string: ")
shift = int(input("Enter shift value: "))

small = "abcdefghijklmnopqrstuvwxyz"
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = ""

for i in s:
    if i in small:
        x = small.index(i)
        x = (x + shift) % 26
        result = result + small[x]

    elif i in capital:
        x = capital.index(i)
        x = (x + shift) % 26
        result = result + capital[x]

print("Caesar Cipher:", result)"""

#6
"""a = 0
b = 0
c = 0
d = 0
e = 0
total = 0

while True:
    n = int(input("Enter a number: "))

    if n == -1:
        break

    if n >= 1 and n <= 2:
        a = a + 1

    elif n >= 3 and n <= 4:
        b = b + 1

    elif n >= 5 and n <= 6:
        c = c + 1

    elif n >= 7 and n <= 8:
        d = d + 1

    elif n >= 9 and n <= 10:
        e = e + 1

    else:
        print("Enter number between 1 and 10")
        continue

    total = total + 1

if total > 0:
    print("1 - 2:", "#" * a, format(a / total * 100, ".2f"), "%")
    print("3 - 4:", "#" * b, format(b / total * 100, ".2f"), "%")
    print("5 - 6:", "#" * c, format(c / total * 100, ".2f"), "%")
    print("7 - 8:", "#" * d, format(d / total * 100, ".2f"), "%")
    print("9 - 10:", "#" * e, format(e / total * 100, ".2f"), "%")"""

#7
"""s = input("Enter a string: ")

rev = ""

i = len(s) - 1

while i >= 0:
    rev = rev + s[i]
    i = i - 1

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")"""


#8 (i)
"""n = int(input("Enter number of elements: "))

a = []

for i in range(n):
    x = int(input("Enter element: "))
    a = a + [x]

total = 0

for i in range(len(a)):
    total = total + a[i]

print("Sum =", total)"""

#8 (ii)
"""n = int(input("Enter number of elements: "))

a = []

for i in range(n):
    x = int(input("Enter element: "))
    a = a + [x]

product = 1

for i in range(len(a)):
    product = product * a[i]

print("Product =", product)"""

#8 (iii)
"""n = int(input("Enter number of elements: "))

a = []

for i in range(n):
    x = int(input("Enter element: "))
    a = a + [x]

smallest = a[0]

for i in range(1, len(a)):
    if a[i] < smallest:
        smallest = a[i]

print("Smallest element =", smallest)"""

#9
"""n = int(input("Enter number of elements: "))

a = []

for i in range(n):
    x = int(input("Enter element: "))
    a = a + [x]

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] < a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print("List in descending order:")

for i in range(len(a)):
    print(a[i], end=" ")"""

#10
"""s = input("Enter hyphen-separated words: ")

a = []
word = ""

for i in range(len(s)):
    if s[i] == "-":
        a = a + [word]
        word = ""
    else:
        word = word + s[i]

a = a + [word]

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

for i in range(len(a)):
    if i < len(a) - 1:
        print(a[i], end="-")
    else:
        print(a[i])"""

#11
"""s = input("Enter a paragraph: ")

digit = 0
alpha = 0
special = 0
upper = 0
lower = 0

for i in s:
    if i.isdigit():
        digit = digit + 1

    elif i.isalpha():
        alpha = alpha + 1

        if i.isupper():
            upper = upper + 1

        elif i.islower():
            lower = lower + 1

    else:
        special = special + 1

print("Digits =", digit)
print("Alphabets =", alpha)
print("Special characters =", special)
print("Uppercase alphabets =", upper)
print("Lowercase alphabets =", lower)"""

#12
"""s = input("Enter a sentence: ")

new = ""

for i in s:
    if i not in new:
        new = new + i

print("String after removing duplicates:", new)"""