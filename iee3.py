def can_rat_pass(test_cases):
    results = []

    for case in test_cases:
        W, H, N, R, sensors_x, sensors_y = case
        coverage = [False] * (H + 1)  # to track y-coordinates from 0 to H

        # Mark coverage based on sensors
        for i in range(N):
            sensor_x = sensors_x[i]
            sensor_y = sensors_y[i]

            # Check if the sensor's x is in range of the living room
            if 0 <= sensor_x <= W:
                # Calculate the horizontal distance from the sensor's x to the edges of its coverage circle
                horizontal_distance = (
                    R**2 - (sensor_x)**2) ** 0.5 if R**2 >= sensor_x**2 else 0

                # Calculate the range of y coordinates affected by this sensor
                min_y = max(0, sensor_y - horizontal_distance)
                max_y = min(H, sensor_y + horizontal_distance)

                # Mark the coverage
                for y in range(int(min_y), int(max_y) + 1):
                    coverage[y] = True

        # Now check for any unmarked y-coordinate
        safe_passage = any(not coverage[y] for y in range(H + 1))

        if safe_passage:
            results.append("CAN")
        else:
            results.append("CAN'T")

    return results


# Example usage
T = 1
W = 5
H = 5
test_cases = [
    (W, H, 2, 2, [2, 2], [1, 4])
]
results = can_rat_pass(test_cases)
for result in results:
    print(result)  # Expected Output: "CAN'T"
