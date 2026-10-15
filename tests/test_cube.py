import pytest
from rubicksolver.cube import Cube
from rubicksolver.colors import Color

def test_solved_cube_faces_are_one_color():
    cube = Cube()
    assert is_solved(cube)

def test_move_U_colors():
    cube = Cube()
    cube.move_U()
    assert cube.faces["F"][0] == [Color.RED] * 3
    assert cube.faces["L"][0] == [Color.GREEN] * 3
    assert cube.faces["B"][0] == [Color.ORANGE] * 3
    assert cube.faces["R"][0] == [Color.BLUE] * 3

def test_four_moves_return_to_solved():
    methods = [Cube.move_U, Cube.move_D, Cube.move_B, Cube.move_F, Cube.move_L, Cube.move_R]
    for i in range(6):
        cube = Cube()
        for j in range(4):
            methods[i](cube)
        assert is_solved(cube)


def is_solved(cube) -> bool:
    for face, grid in cube.faces.items():
        for i in range(3):
            for j in range(3):
                if grid[i][j] != Cube.COLORS_OF_SOLVED_RUBICK[face]:
                    return False

    return True

def test_tangle_and_untangle():
    cube = Cube()
    cube.move_R()
    cube.move_U()
    cube.move_F()
    assert not is_solved(cube)
    for _ in range(3):
        cube.move_F()
    for _ in range(3):
        cube.move_U()
    for _ in range(3):
        cube.move_R()

    assert is_solved(cube)

def test_piff_paff():
    cube = Cube()
    for _ in range(6):
        cube.move_R()
        cube.move_U()
        for _ in range(3):
            cube.move_R()
        for _ in range(3):
            cube.move_U()

    assert is_solved(cube)
