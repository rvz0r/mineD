import heapq
from minesweeper.test.grid import Grid

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

class GraphPath:
    def __init__(self, width, height):
        self.weights = {}
        self.width = width
        self.height = height
        self.walls = []
        self.mines = []

    def filler(self,tilemap):
        for x in range(15):
            for y in range(15):
                if tilemap[x][y] == 1:
                    self.mines.append(tuple([x, y]))
                if tilemap[x][y] == 2:
                    self.walls.append(tuple([x, y]))

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        if (x + y) % 2 == 0: results.reverse()  # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)

    def heuristic(self, a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

    def search(self, graph, start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[tuple(start)] = None
        cost_so_far[tuple(start)] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            for next in graph.neighbors(current):
                new_cost = cost_so_far[tuple(current)] + graph.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[tuple(next)]:
                    cost_so_far[tuple(next)] = new_cost
                    priority = new_cost + self.heuristic(goal, next)
                    frontier.put(next, priority)
                    came_from[tuple(next)] = current

        return came_from, cost_so_far
