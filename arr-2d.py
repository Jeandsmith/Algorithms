def build_board (dimension: int = 2):
"""
Generate a board with $dimension
"""
	return [['.' for i in range(dimension)] for j in range(dimension)]

a = build_board(5)

print(a)