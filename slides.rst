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
in the *values* stored at each variable.

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
