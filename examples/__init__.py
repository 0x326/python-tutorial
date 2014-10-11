from __future__ import absolute_import, division

from .vowels import *


class Fraction:
	def __init__(self, numerator, denominator=1):
		if denominator == 0:
			raise ValueError(
				'Cannot have fraction with zero denominator'
			)
		self.numerator = numerator
		self.denominator = denominator


	def __float__(self):
		return self.numerator / self.denominator


	def clone(self):
		return Fraction(
			self.numerator,
			self.denominator
		)


	def __int__(self):
		return self.numerator // self.denominator


	def __repr__(self):
		return 'Fraction: {}/{}'.format(
			self.numerator,
			self.denominator
		)


	def __str__(self):
		return '{}/{}'.format(
			self.numerator,
			self.denominator
		)


	def get_inverse(self):
		if self.numerator == 0:
			raise ValueError(
				'Inverting this fraction would result in zero denominator'
			)
		return Fraction(self.denominator, self.numerator)


	def factors(self, num):
		return [i for i in range(1, num+1) if num % i == 0]


	def gcd(self):
		num_factors = self.factors(abs(self.numerator))
		denom_factors = self.factors(abs(self.denominator))

		return max([i for i in num_factors if i in denom_factors])


	def fix_signs(self):
		if self.denominator < 0:
			self.denominator *= -1
			self.numerator *= -1


	def simplify(self):
		self.fix_signs()
		gcd = self.gcd()
		self.numerator //= gcd
		self.denominator //= gcd


	def __mul__(self, other):
		new_frac = Fraction(
			self.numerator * other.numerator,
			self.denominator * other.denominator
		)
		new_frac.simplify()
		return new_frac


	def __truediv__(self, other):
		if other.numerator == 0:
			raise ValueError('Cannot divide by zero')
		return self.__mul__(other.get_inverse())


	def __add__(self, other):
		num = self.numerator * other.denominator
		num += other.numerator * self.denominator

		denom = self.denominator * other.denominator

		new_frac = Fraction(num, denom)
		new_frac.simplify()

		return new_frac


	def __sub__(self, other):
		return Fraction(
			-1 * self.numerator,
			self.denominator
		).__add__(other)


	def __eq__(self, other):
		simple_self = self.clone()
		simple_other = other.clone()

		simple_self.simplify()
		simple_other.simplify()

		equal_num = simple_self.numerator == simple_other.numerator
		equal_denom = simple_self.denominator == simple_other.denominator

		return equal_num and equal_denom
