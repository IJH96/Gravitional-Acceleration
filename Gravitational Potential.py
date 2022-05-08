import math
class particle:
    def __init__  (self, position, mass, velocity):
        self.position = position
        self.mass = m
        self.velocity = velocity


U = []
def gravPotential(position, particles):
    phi = 0.0
    G = 6.67430E-11
    for particle in U:
        r = math.sqrt((p.x - pos.x)**2 + (p.y - pos.y)**2 + (p.z - pos.z)**2)
        phi += -G*particle.mass/r
        return phi



particles = []
f = open("particlesmall.txt","r")
lines = f.readlines()
for line in lines:
    position = [float(x), float(y), float(z) ]
    position, m  = line.split()
    P = particle(position, float(m), [0,0,0])
    particle.append(particle)
    f.close()

def centDiffGrav3D(f, position, h, n, particles):
    

    x_1 = position.copy()
    x_1[n] += h/2
    x_2 = position.copy()
    x_2[n] -= h/2
    
    D_c = (f(x_1,particles) - f(x_2,particles))/h
    return D_c
x = input("Enter the x value")
y = input("Enter the y value")
z = input("Enter the z value")

a_x = -centDiffGrav3D(gravPotential,[x,y,z])

print(a_x)