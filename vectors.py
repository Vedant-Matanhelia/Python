# THIS PROGRAM IS WRITTEN FOR THE VECTOR PHYSICS

class Vector2d:
    """Vector2d -> A class for doing basic 3d vector calculations"""

    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __add__(self, v):
        return Vector2d(self.i + v.i, self.j + v.j)

    def __mul__(self, v) -> float:
        return (self.i * v.i) + (self.j * v.j)

    def __sub__(self, v):
        return Vector2d(self.i - v.i, self.j + v.j)

    def __str__(self) -> str:
        return f"{self.i}i + {self.j}j"

class Vector3d:
    """Vector3d -> A class for doing basic 3d vector calculations"""

    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, v):
        return Vector3d(self.i + v.i, self.j + v.j, self.k, v.k)

    def __mul__(self, v) -> float:
        return (self.i * v.i) + (self.j * v.j) + (self.k, v.k)

    def __sub__(self, v):
        return Vector3d(self.i - v.i, self.j - v.j, self.k - v.k)

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

if __name__ == "__main__":
    v1 = Vector2d(1, 10)
    v2 = Vector2d(2, 20)
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    v3 = v1 + v2
    print("v1 + v2 = ", v3)
    prod = v1*v2
    print("v1*v2 = " ,prod)
    v3 = v1 - v2
    print("v1 - v2 = ", v3)
