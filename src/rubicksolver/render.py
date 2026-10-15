from .colors import Color

ANSI_BG_CODES = {
    Color.WHITE: "\033[48;5;15m",
    Color.YELLOW: "\033[48;5;226m",
    Color.GREEN: "\033[48;5;34m",
    Color.BLUE: "\033[48;5;21m",
    Color.ORANGE: "\033[48;5;208m",
    Color.RED: "\033[48;5;196m",
}
RESET = "\033[0m"
STICKER = "   "

def render(cube):
    lines = []
    indent = ((STICKER) * 3) + " " + "  " # Пробел между гранями + 2 пробела межжду квадратиками..
    for row in cube.faces["U"]:
        lines.append(indent + _draw_row(row))
    for i in range(3):
        L = _draw_row(cube.faces['L'][i])
        F = _draw_row(cube.faces['F'][i])
        R = _draw_row(cube.faces['R'][i])
        B = _draw_row(cube.faces['B'][i])
        result = [L, F, R, B]
        lines.append(" ".join(result))
    for row in cube.faces["D"]:
        lines.append(indent + _draw_row(row))

    return "\n".join(lines)

def _draw_row(row):
    return " ".join(f"{ANSI_BG_CODES[color]}{STICKER}{RESET}" for color in row)