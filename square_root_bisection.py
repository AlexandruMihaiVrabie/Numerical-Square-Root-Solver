def square_root_bisection(number, tolerance=1e-7, max_iterations=100):
    if number < 0:
        raise ValueError(
            "Square root of negative number is not defined in real numbers")

    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number

    low = 0
    high = max(1, number)

    for i in range(max_iterations):
        mid = (low + high) / 2

        if (high - low) <= tolerance:
            print(f"The square root of {number} is approximately {mid}")
            return mid

        if mid**2 < number:
            low = mid
        else:
            high = mid

    print(f"Failed to converge within {max_iterations} iterations")
    return None


square_root_bisection(0)

square_root_bisection(0.001, 1e-7, 50)

square_root_bisection(0.001, 1e-7, 50)

square_root_bisection(0.25, 1e-7, 50)

square_root_bisection(1)

square_root_bisection(81, 1e-3, 50)

square_root_bisection(81, 1e-3, 50)

square_root_bisection(225, 1e-3, 100)

square_root_bisection(225, 1e-5, 100)

square_root_bisection(225, 1e-7, 100)

square_root_bisection(225, 1e-7, 10)
