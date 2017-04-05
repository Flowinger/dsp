# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

- Similarities: 
	- Lists and tuples are both sequence data types
	- They support (negative) indexing and slicing operations
	- They support slicing operations
	- len() returns number of elements in sequence
	- "for" loop, enumerate
	- Count, index method

- Differences:
	- Lists are enclosed in square brackets [], tuples in parentheses ()
	- List is a mutable sequence of values 
	- Tuple is a immutable sequence of elements
	- List methods: append, sort, remove, reverse, insert
	- Lists supports Aliasing
  - Tuples are faster
Keys in dictionaries:
	- Dictionaries use hashtable algorithms for searching which means keys have to be hashable. Mutable types like lists aren't. 
  - Only immutable types can be used as keys. So only tuples work as keys in dictionaries.


---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?


- Similarities:
  - Both are sequence data types
  
- Differences:
  - Sets are faster in finding elements
  - Sets are unordered collections of unique elements -> no duplicates
  - Lists are ordered collections of elements
  - Sets support operations like: intersection, union, difference, symmetric difference
  - Sets don't support indexing
  - Sets can only contain hashable objects
- Examples: 
>> fridge = ['apple', 'eggs', 'meat', 'banana', 'apple', 'meat']
food_types_available = ['meat', 'eggs', 'banana', 'apple']
shopping_list = ['fish', 'eggs', 'banana']
do_not_buy = food_types_available.intersection(fridge)
  
- Performance:
  - Sets are faster than lists for searching since they are implemented using hash tables 
  - Set uses a hash function that maps to a certain bucket, Python implementations resize the hash table constantly
  - Checking sets for membership of items happens instantly -> the speed of the operation doesn't depend on the size of the set
  - For lists it takes time proportional to the list's lengths since the whole lists needs to be searched


---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

lambda is a way of creating anonymous functions (not bound to a name). It is often used with functions like filter(), map() and reduce(). They can have multiple parameters, execute an expression and return a value.
Example:
>> sorted(['Hello', 'what', 'is', 'going', 'on', 'Mister'], key=(lambda word: len(word)))


---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions:
- It's a way of adapting an input list by iterating through each element and checking for certain conditions. If a condition is met an expression is applied on the element
- Then the element is moved to the output list.
- consists of for clause with a input sequence, 0 or more for/if clauses with a predicate, the clause contains an output expression
- The same result can be achieved with the functions map and filter.

Example list comprehension:  
>>multiplies = []  
for x in range(20):    
multiplies.append(x*4)  

Example map:
>> list(map(x*4,  multiplies))  

Example filter: 
>> list(filter((lamba x: x > 0),  multiplies))  
---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





