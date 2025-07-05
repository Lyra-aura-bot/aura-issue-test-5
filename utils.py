def parse_input():
    """
    Prompts the user for two integers, separated by space.
    Returns a tuple of two ints.
    """
    raw = input("Enter two integers separated by space: ")
    parts = raw.strip().split()
    if len(parts) != 2:
        raise ValueError("Please enter exactly two numbers.")
    return int(parts[0]), int(parts[1])
