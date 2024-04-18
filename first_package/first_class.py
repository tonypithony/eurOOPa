# python -i first_class.py

import math

class Point:
	"""
	Represents а point in two-dimensional geometric coordinates
	>>> р_0	= Point()
	>>> p_l	= Point(З,4)
	>>> p_0.calculate_distance(p_l)
	5.0
	"""

	def __init__(
		self,
		x: float = 0,
		y: float = 0
	) -> None:
		'''
		Initialize the position of а new point . The х and у
		coordinates с а п Ье spec ified . If they are not , the
		point defaults to the origin .
		:param х: float x-coordinate
		:param у: float y-coordinate
		'''
		self.move(x, y)

	def move(self, x: float, y: float) -> None:
		'''
		Move the point to а new location in 2D space.
		'''
		self.x = x
		self.y = y 

	def reset(self):
		'''
		Reset the point back to the geometric origin: 0, 0
		'''
		self.move(0, 0)

	def calculate_distance(self, other: "Point") -> float:
		'''
		Calculate the Euclidean distance from this point
		to а second point passed as а parameter .
		:param other: Point instance
		:return: float distance
		'''
		return math.hypot(self.x - other.x, self.y - other.y)

if __name__ == '__main__':
	pass