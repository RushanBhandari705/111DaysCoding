#Override the __len__() method on vector of problem 5 to display the dimension of the vector.
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

    def __len__(self):
        return len(self.components)

    def __str__(self):
        return f"Vector({', '.join(map(str, self.components))})"