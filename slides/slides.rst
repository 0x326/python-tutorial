.. role:: python(code)
   :language: python

.. role:: java(code)
   :language: java

======================
Introduction to Python
======================

Nate Mara

2014-10-15

===========
A Few Words
===========

Python is a very powerful and easy to use programming language that
emphasizes programmer time over computer time. It allows for the
programmer to use many popular programming paradigms with ease:

	- Object-Oriented
	- Purely functional
	- Imperative

=================
Let's Get Sarted!
=================

We're going to use some examples that I've prepared.

.. code-block:: bash

	$ git clone https://github.com/natemara/python-tutorial
	$ cd python-tutorial
	$ python3.4

============
Hello World!
============

----
Java
----


.. code-block:: java

	public class HelloWorld {
		public static void main(String[] args) {
			System.out.println("Hello, World!");
		}
	}

------
Python
------

.. code-block:: python

	>>> print('Hello, World!')

=========
Variables
=========

Python uses the concept of **Duck Typing**, coming from the `Duck Test
<https://www.youtube.com/watch?v=fDlaJ4Y8UXY>`_.

Basically, this means *"If it looks like a duck, swims like a duck,
and quacks like a duck, then it probably is a duck."* Python's
variables have no types assigned to them. Instead, Python stores types
in the *values* stored at each variable. We can use the
:python:`type()` function to get the type of any value.

.. code-block:: python

	>>> x = 'Hello, World!'
	>>> print(type(x))
	<class 'str'>

	>>> x = 135
	>>> print(type(x))
	<class 'int'>

	>>> x += 1.5
	>>> print(type(x))
	<class 'float'>

==================
Defining Functions
==================

Python functions are defined with the :python:`def` keyword, and
instead of using curly braces to show the scope of a block, Python
uses indentation.

.. code-block:: python

	>>> def multiply():
		return 300*50

Many Python users use 4 spaces to denote an indentation level, but a
tab works just as well.

==============
Function Types
==============

Just as variables in Python have no defined type, functions and their
arguments can also be of any type. It is important to note that in
Python, functions are no different from variables, except they have
the type :python:`<class 'function'>`.

.. code-block:: python

	>>> def my_great_function(x, y):
		print(x + y)
		return x + y

	>>> type(my_great_function)
	<class 'function'>

	>>> some_value = my_great_function(10, 20)
	>>> print(some_value)
	30
	>>> type(some_value)
	<class 'int'>
	>>> some_value = my_great_function('Hello ', 'World!')
	>>> print(some_value)
	Hello World!

	>>> type(some_value)
	<class 'str'>

============
Conditionals
============

Conditional statements are largely the same as in Java or C++, with
the exception of not requiring parenthesis around the condition, and
having an explicit *else if* statement called :python:`elif`. Just
like functions, the bodies of conditional statements are required to
be indented. Also, instead of :java:`||` or :java:`&&`, Python uses
the words :python:`or`, and :python:`and`.

.. code-block:: python

	>>> if 300 * 50 >= 100:
		print('That is a big number!')
	elif 20 < 10:
		print('It is still pretty big.')
	else:
		print('Alright, it is a small number.')

=====
Lists
=====

Python default colleciton class is the :python:`list`. In contrast to
the array from C-like languages, a list is dynamic, and can hold
values of any type.

.. code-block:: python

	>>> values = ['Hello', 130, object]
	>>> values.append(50000)
	>>> print(values)
	['Hello', 130, <class 'object'>, 50000]

=========
For Loops
=========

Since :python:`for` loops are generally used to iterate through the
contents of a collection, Python's :python:`for` loop has this
behavior by default.

.. code-block:: python

	>>> for i in values:
		print(i)
	Hello
	130
	<class 'object'>
	50000

Important to mention is that the variable created by the loop, in this
case :python:`i`, is a *reference* to the location in the collection,
so you can do this...

.. code-block:: python

	>>> for i in values:
		i = 0
	>>> print(values)
	[0, 0, 0, 0]

===========
While Loops
===========

:python:`while` loops are virtually identical to those in C-like
languages, with the exception of the lack of perenthesis around the
condition, and the indentation denoting the block.

.. code-block:: python

	>>> i = 0
	>>> while i < 10:
		print(i)
		i += 2
	0
	2
	4
	6
	8

==========
Dictionary
==========

A dictionary, or :python:`dict` is a type of collection where each
element is referred to not by a numerical index between :python:`0`
and :python:`n`, but can be referred to by any immutable value, called
a :python:`key`.


.. code-block:: python

	>>> values = {
		'green': 1,
		'red': [1, 3, 4],
		3: 'three',
		4: 'four',
		'blue': 5.0
	}
	>>> print(values['green'])
	1
	>>> print(values[3])
	three
	>>> print(values['red'])
	[1, 3, 4]

===================
List Comprehensions
===================

One of the most powerful aspects of the Python language is the concept
of list comprehensions. A list comprehension is like a formula for
building a list.

.. code-block:: python

	>>> values = [i for i in range(0, 100) if i % 2 == 0]

===================
Putting it Together
===================

As an exercise, let's write a function that that counts the number of
vowels that occur in a string using a list comprehension. Things to
know:

	- the :python:`in` keyword
	- the :python:`sum` function

========
Solution
========

---------
Iterative
---------

.. code-block:: python

	>>> def count_vowels(word):
		total = 0
		for letter in word:
			if letter in 'aeiouAEIOU':
				total += 1
		return total

--------
Pythonic
--------

.. code-block:: python

	>>> def count_vowels(word):
		return sum([1 for i in word if i in 'aeiouAEIOU'])

=======
Classes
=======

Python classes are similar to classes in other languages, except all
attributes are public by default. There are some slightly different
semantics:

	- Instance methods must have :python:`self` as the first parameter
	- Instance variable must be referenced as :python:`self.*`
	- The constructor is called :python:`__init__()`
	- :java:`toString()` is replaced with :python:`__str__()`

.. code-block:: python

	>>> class Fraction():
		def __init__(self, numerator, denominator):
			self.numerator = numerator
			self.denominator = denominator
		def __str__(self):
			return '{:.2f}/{:.2f}'.format(self.numerator, self.denominator)

=================
Source Code Files
=================

	- :python:`.py` extension
	- exactly the same syntax as the interactive mode
	- :python:`hello.py`:

.. code-block:: python

	print('Hello World!')
