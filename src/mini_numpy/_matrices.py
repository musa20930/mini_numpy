from __future__ import annotations
from typing import Union


class Matrix:
    """Matrix class, with some functionality 
    necessary for matrix operations.
    Only 2d matrices supported for now.
    Supported operations include:
    Check matrix validity, negative form, addition, 
    subtraction, multiplication, matrix shape, 
    method for getting matrix column, 
    getting and receiving matrix rows, 
    matrix transposing.

    Examples
    --------

    >>> l1 = [[1, 2, 3], [4, 5, 6]]
    >>> m1 = Matrix(l1)
    >>> m1
    Matrix([[1, 2, 3], [4, 5, 6]])
    >>> m1.transpose()
    Matrix([[1, 4], [2, 5], [3, 6]])
    >>> -m1
    Matrix([[-1, -2, -3], [-4, -5, -6]])
    >>> m1.get_col(0)
    [1, 4]
    >>> m1 * 2
    Matrix([[2, 4, 6], [8, 10, 12]])

    >>> l2 = [[10, 11], [20, 21], [30, 31]]
    >>> m2 = Matrix(l2)
    >>> m2
    Matrix([[10, 11], [20, 21], [30, 31]])
    >>> m1 * m2
    Matrix([[140, 146], [320, 335]])
    >>> m1 - m3
    Matrix([[-9, -18, -27], [-36, -45, -54]])
    >>> m1 - m2
    ValueError: Matrices must be the same shape. 
    Shape of Matrix([[1, 2, 3], [4, 5, 6]]) is (2, 3) 
    and shape of Matrix([[10, 11], [20, 21], [30, 31]]) is (3, 2)

    >>> m1[1]
    [4, 5, 6]
    >>> m1[1] = [460, 5, 6]
    >>> m1
    Matrix([[1, 2, 3], [460, 5, 6]])
    >>> m1[1] = [460, 5, 6, 7]
    ValueError: All rows must be the same length

    """
    def __init__(self, m: list) -> None:
        """
        Parameters
        ----------
        m : list
            Multidimensional list to store matrix elements.
            
        """
        self.coordinates = list(m)
        self.h = len(self.coordinates)
        self.w = len(self.coordinates[0])
        self.__check_matrix__()
    
    def __repr__(self) -> str:
        return f'Matrix({self.coordinates})'
    
    def __check_matrix__(self) -> str:
        """Check that matrix rows have the same length"""
        if not isinstance(self, Matrix):
            raise TypeError(f"Matrix operations only supported, "
                            f"not {type(self)}")
        
        if any(len(row) != self.w for row in self.coordinates):
            raise ValueError("All rows must be the same length")
    
    def __getitem__(self, idx: int) -> list:
        """Used to define behaviour of getting matrix element 
        with '[]' python operator.

        Parameters
        ----------
        idx : int
            Index of matrix row.
        
        Examples
        --------

        >>> l1 = [[1, 2, 3], [4, 5, 6]]
        >>> m1 = Matrix(l1)
        >>> m1
        Matrix([[1, 2, 3], [4, 5, 6]])
        >>> m1[1]
        [4, 5, 6]

        """
        return self.coordinates[idx]
    
    def __setitem__(self, idx: int, value: list) -> None:
        """Used to define behaviour of setting matrix element 
        with '[]' python operator.

        Parameters
        ----------
        idx : int
            Index of matrix row.
        value : list
            New matrix row. 
            Must the same size as the one it is replacing.
        
        Examples
        --------

        >>> l1 = [[1, 2, 3], [4, 5, 6]]
        >>> m1 = Matrix(l1)
        >>> m1
        Matrix([[1, 2, 3], [4, 5, 6]])
        >>> m1[1]
        [4, 5, 6]
        >>> m1[1] = [460, 5, 6]
        >>> m1
        Matrix([[1, 2, 3], [460, 5, 6]])
        >>> m1[1] = [460, 5, 6, 7]
        ValueError: All rows must be the same length

        """
        self.coordinates[idx] = value
        self.__check_matrix__()
    
    @property
    def shape(self) -> tuple[int, int]:
        """Returns matrix shape.

        Returns
        -------
        tuple[int, int]
            Matrix height and width.
        
        Examples
        --------

        >>> l1 = [[1, 2, 3], [4, 5, 6]]
        >>> m1 = Matrix(l1)
        >>> m1
        Matrix([[1, 2, 3], [4, 5, 6]])
        >>> m1.shape
        (2, 3)

        """
        return len(self.coordinates), len(self.coordinates[0])
    
    def __neg__(self) -> Matrix:
        """Returns the negative of the matrix by negating each element.

        Returns
        -------
        Matrix
            New matrix object.
        
        Examples
        --------
        
        >>> l1 = [[1, 2, 3], [4, 5, 6]]
        >>> m1 = Matrix(l1)
        >>> m1
        Matrix([[1, 2, 3], [4, 5, 6]])
        >>> -m1
        Matrix([[-1, -2, -3], [-4, -5, -6]])
        
        """
        result = list(list(-x for x in a) for a in self.coordinates)
        return Matrix(result)
    
    def __add__(self, other: Matrix) -> Matrix:
        """Used to define behaviour of python '+' operator.
        Addition is performed between matrices only 
        and matrices of the same shape.

        Returns
        -------
        Matrix
            New matrix object.

        Raises
        ------
        ValueError
            If 2nd matrix shape was not the same.

        """
        if other.shape == self.shape:
            result = list(list(x + y for x, y in zip(a, b)) 
                          for a, b in zip(other.coordinates, 
                                          self.coordinates))
            return Matrix(result)
        else:
            raise ValueError(f'Matrices must be the same shape. '
                             f'Shape of {self} is {self.shape} '
                             f'and shape of {other} is {other.shape}')
    
    def __sub__(self, other: Matrix) -> Matrix:
        """Used to define behaviour of python '-' operator.
        Subtraction is performed between matrices only 
        and matrices of the same shape.

        Returns
        -------
        Matrix
            New matrix object.

        Raises
        ------
        ValueError
            If 2nd matrix shape was not the same.

        """
        if other.shape == self.shape:
            result = self + (-other)
            return result
        else:
            raise ValueError(f'Matrices must be the same shape. '
                             f'Shape of {self} is {self.shape} '
                             f'and shape of {other} is {other.shape}')
    
    def transpose(self) -> Matrix:
        """Returns transpose of a matrix as a new object.

        Returns
        -------
        Matrix
            New matrix object.
        
        Examples
        --------

        >>> l1 = [[1, 2, 3], [4, 5, 6]]
        >>> m1 = Matrix(l1)
        >>> m1
        Matrix([[1, 2, 3], [4, 5, 6]])
        >>> m1.transpose()
        Matrix([[1, 4], [2, 5], [3, 6]])

        """
        result = list(list(a) for a in zip(*self.coordinates))
        return Matrix(result)
    
    def get_col(self, col: int) -> list:
        """Return matrix column as a list.

        Parameters
        ----------
        col : int
            Matrix column index.

        Returns
        -------
        list
            Matrix column as a list.
        
        Examples
        --------

        >>> l1 = [[1, 2, 3], [4, 5, 6]]
        >>> m1 = Matrix(l1)
        >>> m1
        Matrix([[1, 2, 3], [4, 5, 6]])
        >>> m1.get_col(0)
        [1, 4]

        """
        return list(map(lambda x : x[col], self.coordinates))
    
    def __mul__(self, other: Union[int, float, Matrix]) -> Matrix:
        """Returns multiplication result for 2 matrices 
        or result for matrix by a number.

        Parameters
        ----------
        other : Union[int, float, Matrix]
            Number of type int or float that matrix is multiplied by.
            Or matrix that is multiplied.

        Returns
        -------
        Matrix
            New matrix object.

        Raises
        ------
        ValueError
            Unable to perform matrix multiplication for matrices 
            with different width of first matrix 
            and height of second matrix.
        TypeError
            If type of 'other' is not int, float or Matrix.

        Examples
        --------

        >>> l1 = [[1, 2, 3], [4, 5, 6]]
        >>> m1 = Matrix(l1)
        >>> m1
        Matrix([[1, 2, 3], [4, 5, 6]])
        >>> m1 * 2
        Matrix([[2, 4, 6], [8, 10, 12]])

        >>> l2 = [[10, 11], [20, 21], [30, 31]]
        >>> m2 = Matrix(l2)
        >>> m2
        Matrix([[10, 11], [20, 21], [30, 31]])
        >>> m1 * m2
        Matrix([[140, 146], [320, 335]])

        """
        if isinstance(other, Matrix):
            if self.w == other.h:
                result = [[0 for i in range(self.h)] for j in range(other.w)]
                for i, row_a in enumerate(self.coordinates):
                    for j in range(other.w):
                        result[i][j] = sum(a * b 
                                           for a, b in zip(row_a, 
                                                           other.get_col(j)))
                return Matrix(result)
            else:
                raise ValueError(f'Matrices must be compatible '
                                 f'for matrix multiplication. '
                                 f'Shape of {self} is {self.shape} '
                                 f'and shape of {other} is {other.shape}')
        elif isinstance(other, int) or isinstance(other, float):
            result = list(list(x * other for x in a) for a in self.coordinates)
            return Matrix(result)
        else:
            raise TypeError(f"Can only multiply matrices to matrices "
                            f"or matrix by a number, not {type(self)}")


