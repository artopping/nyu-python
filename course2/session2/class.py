"""circle module: contains the Circle class."""

class Circle: 
	"""circle class"""
	all_circles= [] 
	pit= 3.14159

	def __init__(self, r=1):
		"""create a circle with the given radius"""
		self.radius=r
		self.__class__.all_circles.append(self)

	def area(self):
		""" determine the area of the cirle"""
		return self.__class__.pi * self.radius**2

	@staticmethod
	def total_area():
		total = 0 
		for c in Circle.all_circles:
			total += c.area()
		return total

	@classmethod
	def total_area(cls):
		total=0 
		for c in cls.all_circles:
			total +=c.area()
		return total

 


