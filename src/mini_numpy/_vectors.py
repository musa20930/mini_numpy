from __future__ import annotations
from typing import Union


class Vector:
    """Vector class, with some functionality 
    necessary for vector operations.
    Supported operations include:
    Addition, subtraction, multiplication, division.

    Examples
    --------

    >>> v1 = Vector((1, 2, 3))
    Vector(1, 2, 3)
    >>> v2 = Vector((4, 5, 6))
    Vector(4, 5, 6)
    >>> v1 - v2
    Vector(-3, -3, -3)
    >>> v1 + v2
    Vector(5, 7, 9)
    >>> v1 * v2
    32
    >>> v1 * 5
    Vector(5, 10, 15)
    >>> v1 / v2
    1.15
    >>> v2 / 2
    Vector(2.0, 2.5, 3.0)

    """
    def __init__(self, v_tuple: tuple) -> None:
        self.coordinates = v_tuple     # tuple of coordinates
    
    def __repr__(self) -> str:
        return f'Vector{self.coordinates}'
    
    def __add__(self, other: Vector) -> Vector:
        """Add two vectors together.

        Returns
        -------
        Vector
            New vector object.
        
        Examples
        --------

        >>> v1 = Vector((1, 2, 3))
        Vector(1, 2, 3)
        >>> v2 = Vector((4, 5, 6))
        Vector(4, 5, 6)
        >>> v1 + v2
        Vector(5, 7, 9)

        """
        result = tuple(a + b for a, b in zip(other.coordinates, 
                                             self.coordinates))
        return Vector(result)
    
    def __sub__(self, other: Vector) -> Vector:
        """Subtract two vectors.
        
        Returns
        -------
        Vector
            New vector object.
        
        Examples
        --------

        >>> v1 = Vector((1, 2, 3))
        Vector(1, 2, 3)
        >>> v2 = Vector((4, 5, 6))
        Vector(4, 5, 6)
        >>> v1 - v2
        Vector(-3, -3, -3)

        """
        result = tuple(a - b for a, b in zip(self.coordinates, 
                                             other.coordinates))
        return Vector(result)
    
    def __mul__(self, other: Union[Vector, int, float]) -> Union[Vector, int, float]:
        """Returns the dot product of the two vectors 
        or multiplication by a scalar result.
        
        Returns
        -------
        Vector
            New vector object if other was int or float.
            Otherwise, dot product or 2 vectors.
        
        Examples
        --------

        >>> v1 = Vector((1, 2, 3))
        Vector(1, 2, 3)
        >>> v2 = Vector((4, 5, 6))
        Vector(4, 5, 6)
        >>> v1 * v2
        32
        >>> v1 * 5
        Vector(5, 10, 15)

        """
        if isinstance(other, Vector):
            if len(other.coordinates) == len(self.coordinates):
                result = (a * b 
                          for a, b in zip(other.coordinates, self.coordinates))
                return sum(result)  # dot-product
            else:
                raise ValueError(f'Cannot multiply {self} and {other}')
        elif isinstance(other, (int, float)):
            result = tuple(a * other for a in self.coordinates)
            return Vector(result)
        else:
            raise TypeError(f'Cannot multiply {self} and {other}')
    
    def __truediv__(self, other: Union[Vector, int, float]) -> Union[Vector, int, float]:
        """Returns a dot-product divided by a scalar or vector elements.
        Works similar to '__mul__' method, 
        but 2nd vector elements are raised to -1 power.

        Returns
        -------
        Vector
            New vector object if other was int or float.
            Otherwise, dot product or 2 vectors.
        
        Examples
        --------

        >>> v1 = Vector((1, 2, 3))
        Vector(1, 2, 3)
        >>> v2 = Vector((4, 5, 6))
        Vector(4, 5, 6)
        >>> v1 / v2
        1.15
        >>> v2 / 2
        Vector(2.0, 2.5, 3.0)
        
        """
        if isinstance(other, Vector):
            if len(other.coordinates) == len(self.coordinates):
                result = (a / b 
                          for a, b in zip(self.coordinates, other.coordinates))
                return sum(result)  # dot-product
            else:
                raise ValueError(f'Cannot multiply {self} and {other}')
        elif isinstance(other, (int, float)):
            result = tuple(a / other for a in self.coordinates)
            return Vector(result)
        else:
            raise TypeError(f'Cannot multiply {self} and {other}')

