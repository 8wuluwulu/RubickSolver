from enum import Enum

class Color(Enum):
    WHITE = "W"
    YELLOW = "Y"
    GREEN = "G"
    BLUE = "B"
    ORANGE = "O"
    RED = "R"

ANSI_BG_CODES = {
    Color.WHITE: "\033[48;5;15m",
    Color.YELLOW: "\033[48;5;226m",
    Color.GREEN: "\033[48;5;34m",
    Color.BLUE: "\033[48;5;21m",
    Color.ORANGE: "\033[48;5;208m",
    Color.RED: "\033[48;5;196m",
}

RESET = "\033[0m"
    