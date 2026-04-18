#Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.
class Vector:
    def __init__(self, components):
        self.components = components

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition.")
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for dot product.")
        return sum(a * b for a, b in zip(self.components, other.components))

    def __str__(self):
        return f"Vector({', '.join(map(str, self.components))})"