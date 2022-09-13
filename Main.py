from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename

#-----------------------------------------------------------#
# Pixel Blending by Narukami.
# This could be much more efficient, probably, but it works.
#-----------------------------------------------------------#

class Pixel3D:
	def __init__(self, *color):
		try:
			if len(color) > 1 and len(color) < 4:
				self.r = color[0]
				self.g = color[1]
				self.b = color[2]
			elif len(color) == 1:
				if isinstance(color, tuple):
					self.r = color[0][0]
					self.g = color[0][1]
					self.b = color[0][2]
				elif isinstance(color, list):
					self.r = color[0][0]
					self.g = color[0][1]
					self.b = color[0][2]
				elif isinstance(color, Pixel3D):
					self.r = color.r
					self.g = color.g
					self.b = color.b
				else:
					raise TypeError("Invalid type")
			else:
				raise TypeError("You must provide a list or tuple of length 3 or 3 arguments!")
		except IndexError:
			raise IndexError("You must provide a list or tuple of length 3 or 3 arguments!")
		
	def add(self, other):
		self.r += other.r
		self.g += other.g
		self.b += other.b

	def sub(self, other):
		self.r -= other.r
		self.g -= other.g
		self.b -= other.b
	
	def mul(self, other):
		self.r *= other.r
		self.g *= other.g
		self.b *= other.b

	def div(self, other):
		self.r /= other.r
		self.g /= other.g
		self.b /= other.b

	def __add__(self, other):
		return Pixel3D(self.r + other.r, self.g + other.g, self.b + other.b)

	def __sub__(self, other):
		return Pixel3D(self.r - other.r, self.g - other.g, self.b - other.b)
	
	def __mul__(self, other):
		return Pixel3D(self.r * other.r, self.g * other.g, self.b * other.b)

	def __div__(self, other):
		return Pixel3D(self.r / other.r, self.g / other.g, self.b / other.b)

	def __str__(self):
		return f"({self.r}, {self.g}, {self.b})"
	
	def __repr__(self):
		return self.__str__()


class Pixel4D:
	def __init__(self, *color):
		try:
			if len(color) > 1 and len(color) < 5:
				self.r = color[0]
				self.g = color[1]
				self.b = color[2]
				self.a = color[3]
			elif len(color) == 1:
				if isinstance(color, tuple):
					self.r = color[0][0]
					self.g = color[0][1]
					self.b = color[0][2]
					self.a = color[0][3]
				elif isinstance(color, list):
					self.r = color[0][0]
					self.g = color[0][1]
					self.b = color[0][2]
					self.a = color[0][3]
				elif isinstance(color, Pixel4D):
					self.r = color.r
					self.g = color.g
					self.b = color.b
					self.a = color.a
				else:
					raise TypeError("Invalid type")
			else:
				raise TypeError("You must provide a list or tuple of length 4 or 4 arguments!")
		except IndexError:
			raise IndexError("You must provide a list or tuple of length 4 or 4 arguments!")

	def add(self, other):
		self.r += other.r
		self.g += other.g
		self.b += other.b
		self.a += other.a

	def sub(self, other):
		self.r -= other.r
		self.g -= other.g
		self.b -= other.b
		self.a -= other.a
	
	def mul(self, other):
		self.r *= other.r
		self.g *= other.g
		self.b *= other.b
		self.a *= other.a

	def div(self, other):
		self.r /= other.r
		self.g /= other.g
		self.b /= other.b
		self.a /= other.a

	def __add__(self, other):
		return Pixel4D(self.r + other.r, self.g + other.g, self.b + other.b, self.a + other.a)

	def __sub__(self, other):
		return Pixel4D(self.r - other.r, self.g - other.g, self.b - other.b, self.a - other.a)
	
	def __mul__(self, other):
		return Pixel4D(self.r * other.r, self.g * other.g, self.b * other.b, self.a * other.a)

	def __div__(self, other):
		return Pixel4D(self.r / other.r, self.g / other.g, self.b / other.b, self.a / other.a)

	def __str__(self):
		return f"({self.r}, {self.g}, {self.b}, {self.a})"
	
	def __repr__(self):
		return self.__str__()


def main_3d(filename):
	for x in range(width):
		for y in range(height):

			# Cast pixel to the Pixel3D class
			source = Pixel3D(pixels[x, y])
			
			# Get the neighboring pixels
			# If any of the neighboring pixels are beyond the bounds of the image, set them to (0, 0, 0)
			surrounding = [
				Pixel3D(pixels[x, y - 1]) if y - 1 >= 0 else Pixel3D(0, 0, 0),
				Pixel3D(pixels[x - 1, y]) if x - 1 >= 0 else Pixel3D(0, 0, 0),
				Pixel3D(pixels[x + 1, y]) if x + 1 < width else Pixel3D(0, 0, 0),
				Pixel3D(pixels[x, y + 1]) if y + 1 < height else Pixel3D(0, 0, 0)
			]
			
			# Get the average of the surrounding pixels and assign the result to the source pixel
			average = Pixel3D(0, 0, 0)
			for i in surrounding:
				average.add(i)
			average.div(Pixel3D(len(surrounding), len(surrounding), len(surrounding)))
			pixels[x, y] = (int(average.r), int(average.g), int(average.b))


def main_4d(filename):
	for x in range(width):
		for y in range(height):
			
			# Cast pixel to the Pixel4D class
			source = Pixel4D(pixels[x, y])

			# Get the neighboring pixels
			# If any of the neighboring pixels are beyond the bounds of the image, set them to (0, 0, 0, 0)
			surrounding = [
				Pixel4D(pixels[x, y - 1]) if y - 1 >= 0 else Pixel4D(0, 0, 0, 0),
				Pixel4D(pixels[x - 1, y]) if x - 1 >= 0 else Pixel4D(0, 0, 0, 0),
				Pixel4D(pixels[x + 1, y]) if x + 1 < width else Pixel4D(0, 0, 0, 0),
				Pixel4D(pixels[x, y + 1]) if y + 1 < height else Pixel4D(0, 0, 0, 0)
			]

			# loop through the neighboring pixels and discard any that are transparent
			for i in surrounding:
				if i.a == 0:
					surrounding.remove(i)
			
			# Get the average of the surrounding pixels and assign the result to the source pixel
			average = Pixel4D(0, 0, 0, 0)
			for i in surrounding:
				average.add(i)
			average.div(Pixel4D(len(surrounding), len(surrounding), len(surrounding), len(surrounding)))
			pixels[x, y] = (int(average.r), int(average.g), int(average.b), int(average.a))


if __name__ == "__main__":
	filename = askopenfilename()
	
	img = Image.open(filename)
	pixels = img.load()
	width, height = img.size

	sample = pixels[0, 0]
	if len(sample) == 3:
		main_3d(filename)
	elif len(sample) == 4:
		main_4d(filename)

	img.save(filename)
