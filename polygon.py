import numpy as np


class Polygon:
    def __init__(self, n, R):
        """
        Instantiate a Polygon
        :param n: number of vertices
        :param R: circum radius
        """

        if n < 3:
            raise ValueError('Minimum 3 sides must be present in a polygon')

        self._count_edges = n
        self._circumradius = R

        self._count_vertices = None
        self._interior_angle = None
        self._side_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    @property
    def count_edges(self):
        return self._count_edges

    @property
    def circumradius(self):
        return self._circumradius

    @property
    def count_vertices(self):
        if self._count_vertices is None:
            self._count_vertices = self.count_edges
        return self._count_vertices

    @property
    def interior_angle(self):
        if self._interior_angle is None:
            self._interior_angle = (self.count_edges - 2) * (180 / self.count_edges)
        return self._interior_angle

    @property
    def side_length(self):
        if self._side_length is None:
            self._side_length = 2 * self.circumradius * np.sin(np.pi / self.count_edges)
        return self._side_length

    @property
    def apothem(self):
        if self._apothem is None:
            self._apothem = self.circumradius * np.cos(np.pi / self.count_edges)
        return self._apothem

    @property
    def area(self):
        if self._area is None:
            self._area = 0.5 * self.count_edges * self.side_length * self.apothem
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = self.count_edges * self.side_length
        return self._perimeter

    def __repr__(self):
        """
        Representation of a polygon
        :return: str
        """
        # Polygon(n=3, R=1)
        return f'Polygon(n={self.count_edges}, R={self.circumradius})'
    
    def __eq__(self, other):
        """
        Check for equality of two polygons
        :param other: Other Polygon
        :return: bool
        """
        if self.count_edges == other.count_edges and self.circumradius == other.circumradius:
            return True
        return False

    def __gt__(self, other):
        """
        Verify if the current polygon is greater than the other polygon
        :param other: another polygon
        :return: bool
        """
        if self.count_vertices > other.count_vertices:
            return True
        return False


if __name__ == '__main__':
    p1 = Polygon(5, 10)
    print(p1.__repr__())

    p2 = Polygon(5, 10)
    p3 = Polygon(5, 5)

    print(p1 == p2)
    print(p1 == p3)

    p4 = Polygon(10, 2)
    print(p1 > p4)
    print(p1 < p4)
