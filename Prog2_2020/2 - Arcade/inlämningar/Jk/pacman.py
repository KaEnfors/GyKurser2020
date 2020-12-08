import pygame
from pygame.locals import *
from vector import Vector2
from constants import *

class Pacman(object):
    def __init__(self, nodes):
        self.name = "pacman"
        self.direction = STOP
        self.speed = 100
        self.radius = 10
        self.color = YELLOW
        self.nodes = nodes
        self.node = nodes.nodeList[0]
        self.target = self.node
        self.setPosition()
        
    def setPosition(self):
        self.position = self.node.position.copy()

    def portal(self):
        if self.node.portalNode:
            self.node = self.node.portalNode
            self.setPosition()
            
    def update(self, dt):
        self.position += self.direction*self.speed*dt
        direction = self.getValidKey()
        if direction:
            self.moveByKey(direction)
        else:
            self.moveBySelf()

    def getValidKey(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_UP]:
            return UP
        if key_pressed[K_DOWN]:
            return DOWN
        if key_pressed[K_LEFT]:
            return LEFT
        if key_pressed[K_RIGHT]:
            return RIGHT
        return None

    def moveBySelf(self):
        if self.direction is not STOP:
            if self.overshotTarget():
                self.node = self.target
                self.portal()
                if self.node.neighbors[self.direction] is not None:
                    self.target = self.node.neighbors[self.direction]
                else:
                    self.setPosition()
                    self.direction = STOP
                    
    def moveByKey(self, direction):
        if self.direction is STOP:
            if self.node.neighbors[direction] is not None:
                self.target = self.node.neighbors[direction]
                self.direction = direction
        else:
            if direction == self.direction * -1:
                self.reverseDirection()
            if self.overshotTarget():
                self.node = self.target
                self.portal()
                if self.node.neighbors[direction] is not None:
                    self.target = self.node.neighbors[direction]
                    if self.direction != direction:
                        self.setPosition()
                        self.direction = direction
                else:
                    if self.node.neighbors[self.direction] is not None:
                        self.target = self.node.neighbors[self.direction]
                    else:
                        self.setPosition()
                        self.direction = STOP

    def overshotTarget(self):
        if self.target is not None:
            vec1 = self.target.position - self.node.position
            vec2 = self.position - self.node.position
            node2Target = vec1.magnitudeSquared()
            node2Self = vec2.magnitudeSquared()
            return node2Self >= node2Target
        return False

    def reverseDirection(self):
        if self.direction is UP: self.direction = DOWN
        elif self.direction is DOWN: self.direction = UP
        elif self.direction is LEFT: self.direction = RIGHT
        elif self.direction is RIGHT: self.direction = LEFT
        temp = self.node
        self.node = self.target
        self.target = temp
        
    def render(self, screen):
        p = self.position.asInt()
        pygame.draw.circle(screen, self.color, p, self.radius)

                        
