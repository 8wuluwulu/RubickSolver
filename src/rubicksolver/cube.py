from .colors import Color
from .colors import ANSI_BG_CODES, RESET

class Cube:

    COLORS_OF_SOLVED_RUBICK = {
        "U": Color.WHITE,
        "D": Color.YELLOW,
        "F": Color.GREEN,
        "B": Color.BLUE,
        "L": Color.ORANGE,
        "R": Color.RED,
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


if __name__ == "__main__":
    cube = Cube()
    print(cube)

