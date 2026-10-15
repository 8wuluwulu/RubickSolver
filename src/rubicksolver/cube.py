from .colors import Color
from .render import render

class Cube:

    COLORS_OF_SOLVED_RUBICK = {
        "U": Color.WHITE,
        "D": Color.YELLOW,
        "F": Color.GREEN,
        "B": Color.BLUE,
        "L": Color.ORANGE,
        "R": Color.RED
    }

    def __init__(self):
        self.faces = {}
        for face, color in self.COLORS_OF_SOLVED_RUBICK.items():
            self.faces[face] = [[color for _ in range(3)] for _ in range(3)]

    def __str__(self):
        return render(self)

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

    def move_R(self):
        self._rotate_face("R")
        old_f = self._get_col("F", 2)
        old_u = self._get_col("U", 2)
        old_d = self._get_col("D", 2)
        old_b = self._get_col("B", 0)

        self._set_col("U", 2, old_f)
        self._set_col("B", 0, old_u[::-1])
        self._set_col("D", 2, old_b[::-1])
        self._set_col("F", 2, old_d)

    def move_L(self):
        self._rotate_face("L")
        old_f = self._get_col("F", 0)
        old_u = self._get_col("U", 0)
        old_d = self._get_col("D", 0)
        old_b = self._get_col("B", 2)

        self._set_col("D", 0, old_f)
        self._set_col("F", 0, old_u)
        self._set_col("B", 2, old_d[::-1])
        self._set_col("U", 0, old_b[::-1])

    def move_F(self):
        self._rotate_face("F")
        old_u = self.faces["U"][2][:]
        old_r = self._get_col("R", 0)
        old_d = self.faces["D"][0][:]
        old_l = self._get_col("L", 2)

        self._set_col("R", 0, old_u)
        self.faces["D"][0] = old_r[::-1]
        self._set_col("L", 2, old_d)
        self.faces["U"][2] = old_l[::-1]

    def move_B(self):
        self._rotate_face("B")
        old_u = self.faces["U"][0][:]
        old_r = self._get_col("R", 2)
        old_d = self.faces["D"][2][:]
        old_l = self._get_col("L", 0)

        self._set_col("L", 0, old_u[::-1])
        self.faces["U"][0] = old_r
        self._set_col("R", 2, old_d[::-1])
        self.faces["D"][2] = old_l

    def _get_col(self, face, j):
        col = []
        for i in range(3):
            col.append(self.faces[face][i][j])

        return col

    def _set_col(self, face, j, col):
        for i in range(3):
            self.faces[face][i][j] = col[i]



if __name__ == "__main__":
    cube = Cube()
    print(cube)
    cube.move_F()
    print(cube)
