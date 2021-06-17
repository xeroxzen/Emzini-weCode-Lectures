# Generalization and Higher order functions
# Generalizing patterns using arguments

from math import pi, sqrt

def area_square(r):
	"""Return the area of a square with the side length R

	"""
	return r * r * 1

def area_circle(r):
	"""Return the area of a circle with radius R
	"""
	return r * r * pi

def area_hexagon(r):
	"""Return the area of a hexagon with side length R."""
	return r * r * 3 * sqrt(3) / 2

def area(r, shape_constant):
	"""Return the area of a shop from length measurement is R"""
	assert r > 0, "A length must be positive"
	return r * r * shape_constant

def a_square(r):
	return area(r, 1)

def a_circle(r):
	return area(r, pi)

def a_hexagon(r):
	return area(r, 3 * sqrt(3) / 2)

def sum_naturals(n):
	"""Sum of N natural numbers
	
	>>> sum_naturals(5)
	15
	"""
	total, k = 0, 1
	while k <= n:
		total, k = total + k, k + 1
	return total

def sum_cubes(n):
	"""Sum the first N cubes of natural numbers.
	>>> sum_cubes(5)
	225
	"""
	total, k = 0, 1
	while k <= n:
		total, k = total + pow(k, 3), k + 1
	return total

def identity(k):
	return k


def cube(k):
	return pow(k, 3)
 
# term is a varible representation of a function
def summation(n, term):
	"""Sum the first N terms of a sequence
	>>> summation(5, cube)
	225
	"""

	total, k = 0, 1
	while k <= n:
		total, k = total + term(k), k + 1
	return total

from operator import mul

def pi_term(k):
	return 8 / mul(4 * k - 3, 4 * k - 1)

# Functions as Return values

def make_adder(n):
	"""Return the functions that takes one argument K and return K + N

	>>> add_three =  make_adder(3)
	>>> add_three(4)
	7
	>>> make_adder(5)(6)
	11
	"""

	def adder(k):
		return k + n
	return adder

def split(n):
	"""Splits a positive integer into all but its last digit"""
	return n // 10, n % 10

def sum_digits_iter(n):
	"""Return the sum of the digits of positive integer n. """
	digit_sum = 0
	while n > 0:
		n, last = split(n)
		digit_sum = digit_sum + last
	return digit_sum

def sum_digits(n):
	"""Return the sum of the digits of positive integer n. """
	if n < 10:
		return n
	else:
		all_but_last, last = split(n)
		return sum_digits(all_but_last) + last

def sum_digits_rec(n, digit_sum):
	if n == 0:
		return digit_sum
	else:
		n, last = split(n)
		return sum_digits_rec(n, digit_sum + last)

def fact(n):
	"""Return the factorial of N.
	>>> fact(0)
	1
	>>> fact(4)
	24
	"""
	if n == 0:
		return 1
	else:
		return n * fact(n-1)

	"""
	4! = 4 * 3 * 2 * 1
	3! = 3 * 2 * 1
	2! = 2 * 1

	Facts
	4! = 4 * 3!
	n! = n * (n-1)!

	n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1
	(n - 1)! = (n - 1) * (n - 2) * ... * 3 * 2 * 1

	factorial of n
	0! = 1
	"""

def fact_iter(n):
	"""Return the factorial of N.
	>>> fact_iter(0)
	1
	>>> fact_iter(4)
	24
	"""

	total, k = 1, 1
	while k <= n:
		total, k = total * k, k + 1
	return total
