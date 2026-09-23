CM_TO_FEET_RATIO = 30.48
METERS_TO_FEET_RATIO = 3.28
INCHES_TO_FEET_RATIO = 12

def height_to_feet(height):
    for value in height:
        value = value.strip()

        if value.endswith("cm"):
            number = float(value[:-2].strip())

            if number > 0:
                return number / CM_TO_FEET_RATIO

        elif value.endswith("meters"):
            number = float(value[:-6].strip())

            if number > 0:
                return number * METERS_TO_FEET_RATIO

        elif "'" in value:
            value = value.rstrip("'")

            if value.isdigit():
                return float(value)

            feet, inches = value.split("'")
            feet = float(feet)
            inches = float(inches)

            if feet > 0 or inches > 0:
                return feet + inches / INCHES_TO_FEET_RATIO

    return None