def astronomical_units_to_kilometers(distance, unit):
    """
    Convert astronomical units to kilometers.

    Parameters:
    - distance (float): The distance value to be converted.
    - unit (str): The astronomical unit to convert from (e.g., 'AU', 'light-year', 'parsecs').

    Returns:
    - float: The equivalent distance in kilometers.
    """
    # Conversion factors
    AU_TO_KILOMETERS = 149597870.7  # 1 Astronomical Unit (AU) is approximately 149.6 million kilometers
    LIGHT_YEAR_TO_KILOMETERS = 9.461e12  # 1 Light-year is approximately 9.461 trillion kilometers
    PARSECS_TO_KILOMETERS = 3.086e13  # 1 Parsec is approximately 30.86 trillion kilometers

    # Convert based on the specified unit
    if unit.lower() == 'au':
        return distance * AU_TO_KILOMETERS
    elif unit.lower() == 'light-year':
        return distance * LIGHT_YEAR_TO_KILOMETERS
    elif unit.lower() == 'parsec':
        return distance * PARSECS_TO_KILOMETERS
    else:
        raise ValueError("Unsupported astronomical unit. Supported units: 'AU', 'light-year', 'parsec'.")

if __name__ == "__main__":
    # Example usage
    distance_value = float(input("Enter the distance value: "))
    distance_unit = input("Enter the astronomical unit ('AU', 'light-year', 'parsec'): ")

    try:
        result = astronomical_units_to_kilometers(distance_value, distance_unit)
        print(f"The equivalent distance in kilometers: {result:.2f} km")
    except ValueError as e:
        print(e)
