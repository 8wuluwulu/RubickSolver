from .colors import Color


class Cube:

    COLORS_OF_SOLVED_RUBICK = {
        "U": Color.WHITE,
        "D": Color.YELLOW,
        "F": Color.GREEN,
        "B": Color.BLUE,
        "L": Color.ORANGE,
        "R": Color.RED,
    }

    def __init__(self):
        self.faces = {}
        for face, color in self.COLORS_OF_SOLVED_RUBICK.items():
            self.faces[face] = [[color for _ in range(3)] for _ in range(3)]

    def _draw_row(self, row):
        return " ".join(color.value for color in row)


if __name__ == "__main__":
    cube = Cube()
    print(cube._draw_row(cube.faces["U"][0]))
