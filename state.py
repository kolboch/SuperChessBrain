class State:

    def __init__(self):
        self._first_corner = (0., 0.)
        self._second_corner = (0., 0.)
        self._set_first_corner = False
        self._set_second_corner = False

    def clear_border_position(self):
        self._set_first_corner = False
        self._set_second_corner = False

    def set_corner(self, point):
        if not self._set_first_corner:
            self._first_corner = point
            self._set_first_corner = True
            return True
        elif not self._set_second_corner:
            self._second_corner = point
            self._set_second_corner = True
            return True
        else:
            return False

    # returns 4 corners of the board, in order: top left, top right, bot right, bot left
    def get_border_corners(self):
        (width, height) = self._second_corner - self._first_corner
        if self._first_corner.first < self._second_corner.first:
            p1 = self._first_corner
            p2 = self._second_corner
        else:
            p1 = self._second_corner
            p2 = self._first_corner

        p3 = p1 + (width, 0)
        p4 = p2 + (-width, 0)
        points = [p1, p2, p3, p4]
        return sorted(points, key=lambda tup: (tup[0], -tup[1]))
