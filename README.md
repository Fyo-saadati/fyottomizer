# WeightedRandom Class

The `WeightedRandom` class provides methods to generate random numbers with specific weighted conditions. This allows you to create numbers based on custom rules, such as favoring odd/even numbers or numbers above/below a specific limit.

## Features
- Generate random numbers with a higher weight on odd numbers.
- Generate random numbers with a higher weight on even numbers.
- Generate random numbers with weights based on custom conditions, such as being above or below a limit.

## Methods
### 1. `weight_on_odd(weight, start, end)`
Generates random numbers favoring odd numbers.
- **Parameters:**
  - `weight` (int): Number of odd-weighted numbers to consider (0-100).
  - `start` (int): Lower bound of the random number range.
  - `end` (int): Upper bound of the random number range.
- **Returns:** A single random number.

### 2. `weight_on_even(weight, start, end)`
Generates random numbers favoring even numbers.
- **Parameters:**
  - `weight` (int): Number of even-weighted numbers to consider (0-100).
  - `start` (int): Lower bound of the random number range.
  - `end` (int): Upper bound of the random number range.
- **Returns:** A single random number.

### 3. `weight_on_limit(weight, start, end, limit)`
Generates random numbers favoring numbers above or below a specified limit.
- **Parameters:**
  - `weight` (int): Number of weighted numbers to consider (0-100).
  - `start` (int): Lower bound of the random number range.
  - `end` (int): Upper bound of the random number range.
  - `limit` (dict): A dictionary specifying the condition:
    - `"dir"`: Direction, either "up" (greater than) or "down" (less than).
    - `"int"`: The limit value.
- **Returns:** A single random number.

## Installation
Ensure Python is installed on your system. Save the `WeightedRandom` class in a file named `main.py`.

## Notes
- The `weight` parameter must be between 0 and 100. If the weight is out of range, a `ValueError` will be raised.
- Ensure the range (`start`, `end`) is sufficient to provide valid numbers based on the specified conditions.

## License
This project is licensed under the MIT License. Feel free to modify and use it in your own projects.

