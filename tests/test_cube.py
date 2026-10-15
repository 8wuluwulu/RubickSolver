import pytest
from rubicksolver.cube import Cube

def test_solved_cube_faces_are_one_color():
    cube = Cube()
    for face, grid in cube.faces.items():
        for i in range(3):
            for j in range(3):
                assert grid[i][j] == cube.COLORS_OF_SOLVED_RUBICK[face]
