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

    def rotate_x(self):
        pass

    def rotate_z(self):
        pass

    def getProjected(self, fov):
        projected = []
        for vertex in self.getVertex():
            projected += [[vertex[0]*fov/(vertex[2]+fov), vertex[1]*fov/(vertex[2]+fov)]]
        return(projected)

    def output(self, projected, screen):
        for edge in self.getEdges():
            pygame.draw.line(screen, self.getColor(), (round(projected[edge[0]][0]*20+300), round(projected[edge[0]][1]*20+300)), (round(projected[edge[1]][0]*20+300), round(projected[edge[1]][1]*20+300)), 1)
        pygame.display.flip()

def main():
    #vertex = [[1, 1, 1], [2, 1, 1], [1, 2, 1], [1, 1, 2], [2, 2, 1], [2, 1, 2], [1, 2, 2], [2, 2, 2]]
    vertex = [[-2, -2, -2], [2, -2, -2], [-2, 2, -2], [-2, -2, 2], [2, 2, -2], [2, -2, 2], [-2, 2, 2], [2, 2, 2]]
    edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 4], [2, 6], [3, 6], [3, 5], [5, 7], [6, 7], [7, 4]]
    fov = -5
    screen_color = (0, 0, 0)
    screen = pygame.display.set_mode((600,600))
    screen.fill(screen_color)
    cube = Figure(vertex, edges, (255, 255, 255))
    cube.output(cube.getProjected(fov), screen)
    while True:
        events = pygame.event.get()
        cube.rotate_y(0.01*pi)
        screen.fill(screen_color)
        cube.output(cube.getProjected(fov), screen)
        for event in events:
            if event.type == QUIT:
                sys.exit(0)
        sleep(0.05)

if __name__ == "__main__":
    main()
