from minesweeper.implementation import *


came_from, cost_so_far = dijkstra_search(diagram4, (1, 4), (7, 8))
draw_grid(diagram4, width=3, point_to=came_from, start=(1, 4), goal=(7, 13))
print()
draw_grid(diagram4, width=3, number=cost_so_far, start=(1, 4), goal=(7, 13))
print()
draw_grid(diagram4, width=3, path=reconstruct_path(came_from, start=(1, 4), goal=(7, 13)))


def breadth_first_search_3(graph, start, goal):
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()


        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    return came_from


g = SquareGrid(15, 15)


parents = breadth_first_search_3(g, (0, 0), (14, 2))
draw_grid(g, width=2, point_to=parents, start=(0, 0), goal=(14, 2))


