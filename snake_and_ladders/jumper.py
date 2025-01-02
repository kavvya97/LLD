# class Jumper:
#     def __init__(self, start, end) -> None:
#         self.start = start
#         self.end = end

# class Snake(Jumper):
#     def __init__(self, start, end) -> None:
#         if end >= start:
#             raise ValueError("End position of a snake must be less than the start position")
#         super().__init__(start, end)

#     def get_snake_tail(self):
#         return self.end

# class Ladder(Jumper):
#     def __init__(self, start, end) -> None:
#         if end <= start:
#             raise ValueError("End position of a ladder must be greater than the start position")
#         super().__init__(start, end)

#     def get_ladder_head(self):
#         return self.end


    