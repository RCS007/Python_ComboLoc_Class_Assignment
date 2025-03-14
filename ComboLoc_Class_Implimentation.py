class ComboLock:
    def __init__(self, secret1, secret2, secret3):
        """Initialize the lock with a three-number combination."""
        self.secret1 = secret1
        self.secret2 = secret2
        self.secret3 = secret3
        self.reset()

    def reset(self):
        """Reset the dial to 0 and clear the entered combination."""
        self.position = 0  # Dial starts at 0
        self.ticks_moved = []  # Stores the number of ticks moved in each step
        self.steps = []  # Tracks left/right movement sequence
        self.current_step = 0  # Step tracker (0 → 1 → 2)

    def turnRight(self, ticks):
        """Turn the dial right (clockwise) by the given number of ticks."""
        if self.current_step not in [0, 2]:  # Only allow right turns in steps 0 and 2
            print("Incorrect move! Resetting lock.")
            self.reset()
            return

        self.position = (self.position + ticks) % 40  # Move clockwise
        self.ticks_moved.append(ticks)  # Store the number of ticks moved
        self.steps.append("right")
        self.current_step += 1

    def turnLeft(self, ticks):
        """Turn the dial left (counterclockwise) by the given number of ticks."""
        if self.current_step != 1:  # Only allow left turns in step 1
            print("Incorrect move! Resetting lock.")
            self.reset()
            return

        self.position = (self.position - ticks) % 40  # Move counterclockwise
        self.ticks_moved.append(ticks)  # Store the number of ticks moved
        self.steps.append("left")
        self.current_step += 1

    def open(self):
        """Check if the entered combination matches the secret combination in the correct order."""
        if self.current_step != 3:  # Ensure all three steps have been completed
            print("Incomplete combination. The lock remains closed.")
            return False

        # Calculate the expected ticks for each step
        expected_ticks = [
            self.secret1,  # First step: turn right to secret1
            (self.secret1 - self.secret2) % 40,  # Second step: turn left to secret2
            (self.secret3 - self.secret2) % 40  # Third step: turn right to secret3
        ]

        # Check if the ticks moved match the expected ticks
        if self.ticks_moved == expected_ticks and self.steps == ["right", "left", "right"]:
            print("Lock opened successfully!")
            return True
        else:
            print("Incorrect combination. The lock remains closed.")
            return False


# Example 1:
lock = ComboLock(35,15,5)

lock.turnRight(35)  # Turn right to 10 (first step)
lock.turnLeft(20)   # Turn left to 20 (second step)
lock.turnRight(30)  # Turn right to 30 (third step)

lock.open()  # Expected Output: "Lock opened successfully!"

# Example 2:
lock = ComboLock(10, 20, 30)

lock.turnRight(10)  # Turn right to 10 (first step)
lock.turnLeft(10)   # Turn left to 20 (second step)
lock.turnRight(10)  # Turn right to 30 (third step)

lock.open()  # Expected Output: "Incorrect combination. The lock remains closed.!"