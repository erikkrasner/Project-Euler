#!/usr/bin/env python

class Vector(tuple):
	def dot(self, other):
		return self[0] * other[0] + self[1] * other[1] + self[2] * other[2]
	def cross(self, other):
		return Vector((self[1] * other[2] - self[2] * other[1],self[0] * other[2] - self[2] * other[0],self[0]* other[1] - self[1] * other[0]))
	def __add__(self,other):
		return Vector((self[0] + other[0],self[1] + other[1],self[2]+other[2]))
	def __sub__(self,other):
		return self + (other * -1)
	def __mul__(self,scalar):
		return Vector((self[0] * scalar,self[1] * scalar,self[2] * scalar))

def same_side(p1,p2, a,b):
	return ((b-a).cross(p1-a)).dot((b-a).cross(p2-a)) > 0

def point_in_triangle(p,a,b,c):
	return same_side(p,a,b,c) and same_side(p,b,a,c) and same_side(p,c,a,b)

def make_vector(x,y):
	return Vector((x,y,0))

def count_triangles_containing_origin():
	def parse_triangle(line):
		coordinates = map(int,line.split(','))
		return map(lambda x:make_vector(coordinates[2*x],coordinates[2*x+1]),range(3))
	triangle_file = open('triangles.txt','r')
	count = 0
	origin = make_vector(0,0)
	for line in triangle_file:
		if point_in_triangle(origin,*parse_triangle(line)):
			count += 1
	return count

print count_triangles_containing_origin()
