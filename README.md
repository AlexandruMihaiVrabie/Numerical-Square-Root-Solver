# Numerical-Square-Root-Solver

A lightweight and robust Python script that calculates the square root of a given number using the **Bisection Method** (a type of binary search). This project demonstrates a fundamental numerical analysis technique for root-finding, offering precise control over the approximation's accuracy and performance.

## 🚀 Features

* **Customizable Precision:** You can easily tweak the `tolerance` and `max_iterations` parameters to balance between computational speed and mathematical accuracy.
* **Fraction Safe:** Intelligently handles numbers between 0 and 1. (Since the square root of a fraction is actually *larger* than the fraction itself, the script dynamically adjusts the upper bound to ensure accurate calculation).
* **Edge-Case Handling:** Safely returns exact results for 0 and 1, and raises a clear `ValueError` if a negative number is inputted (preventing imaginary number complexities).
* **Zero Dependencies:** Built entirely with pure, standard Python.

## 🧠 How the Bisection Algorithm Works


To find the square root of a number $N$, the script looks for the root of the continuous function $f(x) = x^2 - N$. It does this by repeatedly dividing a search interval in half:
1. **Define the Boundaries:** It sets a `low` boundary at 0 and a `high` boundary at either 1 or $N$ (whichever is larger).
2. **Find the Midpoint:** It calculates the exact middle value (`mid`) between `low` and `high`.
3. **Test the Midpoint:** It squares the `mid` value. 
    * If `mid**2` is less than $N$, the true square root must be higher, so the `low` boundary is moved up to `mid`.
    * If `mid**2` is greater than $N$, the true square root must be lower, so the `high` boundary is moved down to `mid`.
4. **Evaluate Tolerance:** This halving process repeats until the difference between `high` and `low` is smaller than the specified `tolerance`, meaning the `mid` value is a highly accurate approximation.

## 🛠️ Requirements & Running

This project requires **Python 3.x**.

1. Clone the repository or download `square_root_bisection.py`.
2. Open your terminal or command prompt.
3. Run the script using:

```bash
python square_root_bisection.py
```

## 💻 Code Example & Usage

You can use the function to calculate square roots with custom tolerances and iteration limits:

```python
# Default usage (tolerance=1e-7, max_iterations=100)
square_root_bisection(0.25)

# High precision requirement
square_root_bisection(225, tolerance=1e-7, max_iterations=100)

# Low iteration limit (might fail to converge if the limit is too strict)
square_root_bisection(225, tolerance=1e-7, max_iterations=10)
```

**Expected Output Example:**
```text
The square root of 0.25 is approximately 0.5
The square root of 225 is approximately 15.0
Failed to converge within 10 iterations
```

## 🤝 Contributing

Contributions are welcome! If you want to optimize the algorithm, add comparisons to other root-finding methods (like the Newton-Raphson method), or implement a graphical visualization of the convergence, feel free to fork the repository and open a Pull Request.
