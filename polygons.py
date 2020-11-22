from collections import namedtuple

from polygon import Polygon

Poly = namedtuple('Poly', 'vertices, radius')


class Polygons(object):
    def __init__(self, m, R):
        """
        Initialize the polynomial sequence
        :param m: maximum number of vertices
        :param R: float circum radius
        """

        if m < 3:
            raise ValueError('The max number of vertices must be >= 3')

        self.max_vertices = m
        self.circum_radius = R
        self.cache = {}
        # self.sequence = [Polygon(num_edges, self.circum_radius) for num_edges in range(3, self.max_vertices + 1)]

    def max_efficiency_polygon(self):
        """
        determine the polynomial with maximum efficiency
        :return: Polynomial
        """
        max_efficient_poly = max([x for x in iter(self)], key=lambda p: p.area / p.perimeter)
        return max_efficient_poly

    def get_polygon(self, n, R):
        p = Poly(n, R)
        if p not in self.cache:
            self.cache[p] = Polygon(n, R)
        return self.cache[p]

    def __getitem__(self, item):
        """
        Implementing getitem to make this Class a sequence
        :param item: index for the sequence
        :return: the polynomial element
        """
        if -(self.max_vertices - 2) <= item <= self.max_vertices - 3:
            return self.get_polygon(item + 3, self.circum_radius)
        else:
            raise ValueError(f'Invalid item index. Allowed item value must be in the range: '
                             f'[0, {self.max_vertices - 3}], but item = {item}')

    def __len__(self):
        """
        Determine the length of the sequence
        :return: int
        """
        return self.max_vertices - 2

    def __repr__(self):
        """
        Formatted representation of the poly sequence
        :return: str
        """
        representation = [
            f'A sequence of element of Polygon class',
            f'\t Num elements: {self.__len__()}',
            f'\t Radius: {self.circum_radius}',
        ]
        return '\n'.join(representation)

    def __iter__(self):
        return self.PolygonsIter(self, self.circum_radius, self.max_vertices)

    class PolygonsIter:
        def __init__(self, polygon, radius, max_vertices):
            self.p = polygon
            self.r = radius
            self.m = max_vertices
            self.n = 3

        def __iter__(self):
            return self

        def __next__(self):
            if self.n > self.m:
                raise StopIteration
            else:
                self.n += 1
                return self.p.get_polygon(self.n - 1, self.r)
