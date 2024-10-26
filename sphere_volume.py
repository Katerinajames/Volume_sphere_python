
import math 
class Sphere:
	def __init__(self,radius):
		self.radius=radius
	def volume(self):
		vol = ( 4.0 / 3.0 ) * math.pi * math.pow( self.radius, 3 )
		return vol

print("---------------------------------------------------------------")

s=Sphere(4) 

print("The volume of the sphere is %.2f"%( s.volume()))
