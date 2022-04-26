import math
import numpy as np
class particle:
    def __init__  (self, position, mass):
        self.position = position
        self.m = m
       

G = 6.67430E-11
h= E-5
def gravPotential(position, particles, h):
    
    phi = 0.0
    for p in particles:
        r = math.sqrt((position[0] - p.position[0])**2 + (position[1] - p.position[1])**2 + (position[2] - p.position[2])**2)
        if (r>h/2):
            phi += -G*p.m/r
    return phi

particles = []

f = open("particlesmall.txt","r")
lines = f.readlines()
for line in lines:
    x,y,z , m  = line.split()
    position = np.array([float(x), float(y), float(z) ])
    p = particle(position, float(m),)
    particles.append(p)
f.close()

def centDiffGrav3D(f, position, h, n, particles):
    

    x_1 = position.copy()
    x_1[n] += h/2
    x_2 = position.copy()
    x_2[n] -= h/2
    
    D_c = (f(x_1,particles,h) - f(x_2,particles,h))/h
    return D_c


x = input("Enter the x value")
y = input("Enter the y value")
z = input("Enter the z value")

a_x = -centDiffGrav3D(gravPotential,p.position, h,0,particles)
a_y = -centDiffGrav3D(gravPotential, p.position,h,1, particles)
a_z = -centDiffGrav3D(gravPotential, p.position,h,2, particles)
print(a_x, a_y, a_z)