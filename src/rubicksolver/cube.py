from .colors import Color
from .colors import ANSI_BG_CODES, RESET

class Cube:

    COLORS_OF_SOLVED_RUBICK = {
        "U": Color.WHITE,
        "D": Color.YELLOW,
        "F": Color.GREEN,
        "B": Color.BLUE,
        "L": Color.ORANGE,
        "R": Color.RED
    }

    STICKER = "   "

    def __init__(self):
        self.faces = {}
        for face, color in self.COLORS_OF_SOLVED_RUBICK.items():
            self.faces[face] = [[color for _ in range(3)] for _ in range(3)]

    def _draw_row(self, row):
        return " ".join(f"{ANSI_BG_CODES[color]}{self.STICKER}{RESET}" for color in row)

    def __str__(self):
        lines = []
        indent = ((self.STICKER) * 3) + " " + "  " # Пробел между гранями + 2 пробела межжду квадратиками..
        for row in self.faces["U"]:
            lines.append(indent + self._draw_row(row))
        for i in range(3):
            L = self._draw_row(self.faces['L'][i])
            F = self._draw_row(self.faces['F'][i])
            R = self._draw_row(self.faces['R'][i])
            B = self._draw_row(self.faces['B'][i])
            result = [L, F, R, B]
            lines.append(" ".join(result))
        for row in self.faces["D"]:
            lines.append(indent + self._draw_row(row))

        return "\n".join(lines)

    def _rotate_face(self, face):
        old_face = self.faces[face]
        new_face = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                new_face[i][j] = old_face[2 - j][i]

        self.faces[face] = new_face

    def move_U(self):
        self._rotate_face("U")
        old_l = self.faces["L"][0]
        old_f = self.faces["F"][0]
        old_r = self.faces["R"][0]
        old_b = self.faces["B"][0]

        self.faces["L"][0] = old_f
        self.faces["F"][0] = old_r
        self.faces["R"][0] = old_b
        self.faces["B"][0] = old_l

    def move_D(self):
        self._rotate_face("D")
        old_l = self.faces["L"][2]
        old_f = self.faces["F"][2]
        old_r = self.faces["R"][2]
        old_b = self.faces["B"][2]

        self.faces["L"][2] = old_b
        self.faces["F"][2] = old_l
        self.faces["R"][2] = old_f
        self.faces["B"][2] = old_r
        



if __name__ == "__main__":
    cube = Cube()
    print(cube)
    cube.move_D()
    print(cube)
