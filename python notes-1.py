#variable storing the data inside the program
name="Charmi"
"""
Data Types:int,float,str-""(string),list-[](changeable),dict-{},tuple-()(immutable or unchangeable),set-{}(no duplicates),bool(true or false),byte,byte,byte an array
There are 4 types:
1.Numeric Datatypes
2.Text Datatypes
3.Set Datatypes
4.Boolean Datatypes
"""
#1.Numeric ADD,SUB,MUL,DIV
a=12
b=23
print(f"add:{a+b},sub:{a-b},mul:{a*b},div:{a/b}")
#2.Text datatypes---(str),... (single,double,triple)
#single
c='charmi'
#double
d="manasa"
#triple
e="charmi,is a good girl"
#Using formating methods:
n="charmi"
print(n.upper())
print(n.lower())
print(len(n))
print(n.title())
print(n.strip())#remove the space in front and end
print(n.lstrip())#remove the s[ace in front
print(n.rstrip())#remove the space in end
print(n.startswith('aravapalli'))
print(n.endswith('Venkata Nagalakshmi'))
#3.Set data types
fruits={"apple","banana","mango"}
vegetables = {"spinach", "carrot", "broccoli"}
print(fruits)
#Checking membership in the set:
fruits = {"banana", "apple", "orange"}
print("banana" in fruits)  # Output: True
print("pear" in fruits)    # Output: False
#3.2.Adding Elements to a Set
fruits.add("pear")
print(fruits)
#3.3.Removing Elements from a Set
fruits.remove("apple")
print(fruits)  # Example Output: {"banana", "orange", "pear"}
#3.4.Basic Set Operations
fruits = {"banana", "apple", "orange"}
vegetables = {"spinach", "carrot", "broccoli","orange"}
food = fruits.union(vegetables)
print(food)
common_items = fruits.intersection(vegetables)
print(common_items)
unique_fruits = fruits.difference(vegetables)
print(unique_fruits)
"""
output:{'spinach', 'apple', 'carrot', 'broccoli', 'banana', 'orange'}
       {'orange'}
       {'apple', 'banana'}
"""
#4.Boolean Data Type:
is_sunny = True
is_raining = False
print(is_sunny)   # Output: True
print(is_raining) # Output: False
#30-11-2025
"""
Operators:
1.Arithmetic Operators
add(+)
subraction(-)
Multiplication(*)
Division(/)       ###7 / 2..............o/p:3.5
Modulus(%)##give only remaider
Exponentiation(**)
Floor Division(//)##7 // 2............. # because 7 ÷ 2 = 3.5, quotient = 3
"""
a=23
b=13
print(f"add:{a+b} sub:{a-b} mul:{a*b} div:{a/b} modulus:{a%b} expontation:{a**b} floor division:{a//b})

2.Comparison Operators:

| Operator | Meaning               | Example         |
| -------- | --------------------- | --------------- |
| `==`     | Equal to              | `5 == 5 → True` |
| `!=`     | Not equal to          | `5 != 3 → True` |
| `>`      | Greater than          | `10 > 7 → True` |
| `<`      | Less than             | `2 < 9 → True`  |
| `>=`     | Greater than or equal | `5 >= 5 → True` |
| `<=`     | Less than or equal    | `3 <= 6 → True` |


3.Logical Operators:

| Operator | Meaning                      |
| -------- | ---------------------------- |
| `and`    | True if both are True        |
| `or`     | True if at least one is True |
| `not`    | Reverses True/False          |

x = True
y = False
print(x and y)   # False
print(x or y)    # True
print(not x)     # False

4.Assignment Operators:

| Operator | Meaning             | Example  |
| -------- | ------------------- | -------- |
| `=`      | Assign              | `a = 10` |
| `+=`     | Add and assign      | `a += 5` |
| `-=`     | Subtract and assign | `a -= 3` |
| `*=`     | Multiply and assign | `a *= 2` |
| `/=`     | Divide and assign   | `a /= 4` |
| `%=`     | Modulus and assign  | `a %= 3` |

a = 10
a += 5   #10+5
a -= 2   #15-2
a *= 3   #13*3
a /= 4   #39/4
a %= 2
print(a)

5.Bitwise Operators:

| Operator | Meaning     | 
| -------- | ----------- |
| `&`      | Bitwise AND |            
| `|'      | Bitwise OR  |
| `^`      | Bitwise XOR |            

a = 5   # 0101
b = 3   # 0011
print(a & b)  # 1
print(a | b)  # 7
print(a ^ b)  # 6
"""
      
5.Contol Statements:




