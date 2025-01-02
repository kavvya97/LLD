from collections import deque
from board import Board
class ShortestPathFinder:
    def __init__(self, board: Board):
        self.board = board

    def find_shortest_path(self, start_pos=1, destination_pos=100):
        visit = set()
        queue = deque([(start_pos, 0)])

        while queue:
            cur_pos, distance = queue.popleft()
            if cur_pos == destination_pos:
                return distance
            
            visit.add(cur_pos)

            for neigh in self.get_neighbors(cur_pos):
                if neigh not in visit:
                    queue.append((neigh, distance + 1))

        return -1 

    def get_neighbors(self, cur_pos):
        neighbors = []
        for die_roll in range(1, 7):
            new_pos = cur_pos + die_roll
            final_pos = self.board.get_final_position(new_pos)
            if final_pos <= self.board.size:
                neighbors.append(final_pos)
        return neighbors

ladders = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    80: 100
}

snakes = {
    98: 78,
    95: 75,
    93: 73,
    87: 24,
    64: 60,
    62: 19,
    56: 53,
    49: 11,
    48: 26
}
board = Board(snakes, ladders, size=100)
path_finder = ShortestPathFinder(board)
start_pos = 1  
destination_pos = 100  
shortest_path = path_finder.find_shortest_path(start_pos, destination_pos)
print(f"The shortest path from {start_pos} to {destination_pos} is {shortest_path} moves.")

