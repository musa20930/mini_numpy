# Mini Numpy

Mini Numpy is a lightweight Python library that provides a subset of NumPy's functionality, designed for educational purposes and to help understand the inner workings of NumPy.

## Features

- Basic array operations (addition, subtraction, multiplication, etc.)
- Array broadcasting
- Array slicing and indexing
- Basic linear algebra operations (matrix multiplication, transpose, etc.)

## Installation

You can install Mini Numpy using pip:

pip install mini-numpy

## Versioning

We use [SemVer](http://semver.org/) for versioning. 

## Authors

* **Musa Adygamov** - *Initial work* 

## Usage

Here's a simple example of using Mini Numpy:

import mini_numpy as mini_np

# Create arrays

a = mini_np.array([1, 2, 3])
b = mini_np.array([4, 5, 6])

# Array operations

c = a + b # [5, 7, 9]
d = a \* b # [4, 10, 18]

# Matrix multiplication

A = mini_np.array([[1, 2], [3, 4]])
B = mini_np.array([[5, 6], [7, 8]])
C = mini_np.dot(A, B) # [[19, 22], [43, 50]]

For more examples and documentation, please refer to the [project repository](https://github.com/musa20930/mini-numpy).

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request on the [project repository](https://github.com/musa20930/mini-numpy).

## License

Mini Numpy is released under the [MIT License] - see the [LICENSE.md](LICENSE.md) file for details.

