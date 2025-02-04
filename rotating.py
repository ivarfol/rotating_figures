from math import cos, sin, ceil, pi
import pygame
from pygame.locals import QUIT
from time import sleep
import sys

class Figure():
    def __init__(self, vertex, edge, color):
        self.vertices = vertex
        self.edges = edge
        self.line_color = color

    def getVertex(self):
        return(self.vertices)

    def getEdges(self):
        return(self.edges)

    def getColor(self):
        return(self.line_color)

    def rotate_y(self, a):
        tmp = []
        for vertex in self.getVertex():
            tmp += [[vertex[0]*cos(a) + vertex[2]*sin(a), vertex[1], vertex[2]*cos(a) - vertex[0]*sin(a)]]
        self.vertices = tmp

    def rotate_x(self, a):
        tmp = []
        for vertex in self.getVertex():
            tmp += [[vertex[0], vertex[1]*cos(a) - vertex[2]*sin(a), vertex[2]*cos(a) + vertex[1]*sin(a)]]
        self.vertices = tmp

    def rotate_z(self, a):
        tmp = []
        for vertex in self.getVertex():
            tmp += [[vertex[0]*cos(a) - vertex[1]*sin(a), vertex[1]*cos(a) + vertex[0]*sin(a), vertex[2]]]
        self.vertices = tmp

    def getProjected(self, fov):
        projected = []
        for vertex in self.getVertex():
            projected += [[vertex[0]*fov/(vertex[2]+fov), vertex[1]*fov/(vertex[2]+fov)]]
        return(projected)

    def output(self, fov, screen, width, height, scale):
        projected = self.getProjected(fov)
        for edge in self.getEdges():
            pygame.draw.line(screen, self.getColor(), (round(projected[edge[0]][0]*scale+width/2), round(projected[edge[0]][1]*scale+height/2)), (round(projected[edge[1]][0]*scale+width/2), round(projected[edge[1]][1]*scale+height/2)), 1)

def main():
    vertex = [[-2, -2, -2], [2, -2, -2], [-2, 2, -2], [-2, -2, 2], [2, 2, -2], [2, -2, 2], [-2, 2, 2], [2, 2, 2]]
    edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 4], [2, 6], [3, 6], [3, 5], [5, 7], [6, 7], [7, 4]]
    fov = -20
    screen_color = (0, 0, 0)
    width = 300
    height = 300
    scale = 30
    screen = pygame.display.set_mode((width,height))
    cube = Figure(vertex, edges, (255, 255, 255))
    while True:
        events = pygame.event.get()
       # cube.rotate_x(0.01*pi)
        cube.rotate_y(0.01*pi)
        cube.rotate_z(0.01*pi)
        screen.fill(screen_color)
        cube.output(fov, screen, width, height, scale)
        pygame.display.flip()
        for event in events:
            if event.type == QUIT:
                sys.exit(0)
        sleep(0.05)

if __name__ == "__main__":
    main()
