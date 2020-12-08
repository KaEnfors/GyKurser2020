import pygame
from vector import Vector2
from constants import *
from stack import Stack

class Node(object):
    def __init__(self, row, column):
        self.row, self.column = row, column
        self.position = Vector2(column*TILEWIDTH, row*TILEHEIGHT)
        self.neighbors = {UP:None, DOWN:None, LEFT:None, RIGHT:None}
        self.portalNode = None
        self.portalVal = 0
        
    def render(self, screen):
        for n in self.neighbors.keys():
            if self.neighbors[n] is not None:
                line_start = self.position.asTuple()
                line_end = self.neighbors[n].position.asTuple()
                pygame.draw.line(screen, WHITE, line_start, line_end, 4)
                pygame.draw.circle(screen, RED, self.position.asInt(), 12)


class NodeGroup(object):
    def __init__(self, level):
        self.nodeList = []
        self.level = level
        self.grid = None
        self.nodeStack = Stack()
        self.portalSymbols = ["1"]
        self.nodeSymbols = ["+"] + self.portalSymbols
        self.createNodeList(level, self.nodeList)
        self.setupPortalNodes()
        
    def readMazeFile(self, textfile):
        f = open(textfile, "r")
        lines = [line.rstrip('\n') for line in f]
        lines = [line.rstrip('\r') for line in lines]
        return [line.split(' ') for line in lines]

    def createNodeList(self, textFile, nodeList):
        self.grid = self.readMazeFile(textFile)
        startNode = self.findFirstNode(len(self.grid), len(self.grid[0]))
        self.nodeStack.push(startNode)
        while not self.nodeStack.isEmpty():
            node = self.nodeStack.pop()
            self.addNode(node, nodeList)
            leftNode = self.getPathNode(LEFT, node.row, node.column-1, nodeList)
            rightNode = self.getPathNode(RIGHT, node.row, node.column+1, nodeList)
            upNode = self.getPathNode(UP, node.row-1, node.column, nodeList)
            downNode = self.getPathNode(DOWN, node.row+1, node.column, nodeList)
            node.neighbors[LEFT] = leftNode
            node.neighbors[RIGHT] = rightNode
            node.neighbors[UP] = upNode
            node.neighbors[DOWN] = downNode
            self.addNodeToStack(leftNode, nodeList)
            self.addNodeToStack(rightNode, nodeList)
            self.addNodeToStack(upNode, nodeList)
            self.addNodeToStack(downNode, nodeList)

    def findFirstNode(self, rows, cols):
        nodeFound = False
        for row in range(rows):
            for col in range(cols):
                if self.grid[row][col] in self.nodeSymbols:
                    node = Node(row, col)
                    if self.grid[row][col] in self.portalSymbols:
                        node.portalVal = self.grid[row][col]
                    return node
        return None
    
    def getNode(self, x, y, nodeList=[]):
        for node in nodeList:
            if node.position.x == x and node.position.y == y:
                return node
        return None
    
    def getNodeFromNode(self, node, nodeList):
        if node is not None:
            for inode in nodeList:
                if node.row == inode.row and node.column == inode.column:
                    return inode
        return node
    
    def getPathNode(self, direction, row, col, nodeList):
        tempNode = self.followPath(direction, row, col)
        return self.getNodeFromNode(tempNode, nodeList)

    def addNode(self, node, nodeList):
        nodeInList = self.nodeInList(node, nodeList)
        if not nodeInList:
            nodeList.append(node)
            
    def addNodeToStack(self, node, nodeList):
        if node is not None and not self.nodeInList(node, nodeList):
            self.nodeStack.push(node)
            
    def nodeInList(self, node, nodeList):
        for inode in nodeList:
            if node.position.x == inode.position.x and node.position.y == inode.position.y:
                return True
        return False

    def followPath(self, direction, row, col):
        rows = len(self.grid)
        columns = len(self.grid[0])
        if direction == LEFT and col >= 0:
            return self.pathToFollow(LEFT, row, col, "-")
        elif direction == RIGHT and col < columns:
            return self.pathToFollow(RIGHT, row, col, "-")
        elif direction == UP and row >= 0:
            return self.pathToFollow(UP, row, col, "|")
        elif direction == DOWN and row < rows:
            return self.pathToFollow(DOWN, row, col, "|")
        else:
            return None
        
    def pathToFollow(self, direction, row, col, path):
        tempSymbols = [path]+self.nodeSymbols
        if self.grid[row][col] in tempSymbols:
            while self.grid[row][col] not in self.nodeSymbols:
                if direction is LEFT: col -= 1
                elif direction is RIGHT: col += 1
                elif direction is UP: row -= 1
                elif direction is DOWN: row += 1
            node = Node(row, col)
            if self.grid[row][col] in self.portalSymbols:
                node.portalVal = self.grid[row][col]
            return node
        else:
            return None

    def setupPortalNodes(self):
        portalDict = {}
        for i in range(len(self.nodeList)):
            if self.nodeList[i].portalVal != 0:
                if self.nodeList[i].portalVal not in portalDict.keys():
                    portalDict[self.nodeList[i].portalVal] = [i]
                else:
                    portalDict[self.nodeList[i].portalVal] += [i]
        for key in portalDict.keys():
            node1, node2 = portalDict[key]
            self.nodeList[node1].portalNode = self.nodeList[node2]
            self.nodeList[node2].portalNode = self.nodeList[node1]
            
    def render(self, screen):
        for node in self.nodeList:
            node.render(screen)
