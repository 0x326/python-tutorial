.. role:: python(code)
   :language: python

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
	$ cd python-intro/examples
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
