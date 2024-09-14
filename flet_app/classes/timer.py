import time
import asyncio
from typing import Optional, Callable

class Timer:
    def __init__(self):
        self.value: Optional[float] = 0  # Initialize with 0
        self.running = False  # Flag to control timer loop
        self.on_change_callback: Optional[Callable[[float], None]] = None  # Optional callback function

    def get_time(self):
        if self.value is not None:
            return round(self.value, 2)  # Round value to 2 decimal places
        return None  # Return None if value is not set

    def get_formatted_time(self):
        return "{:.2f}".format(self.value)

    async def start(self):
        self.running = True
        start_time = time.time()
        while self.running:
            await asyncio.sleep(0.02)  # Sleep for 20 milliseconds
            current_time = time.time()
            self.value += current_time - start_time
            start_time = current_time
            if self.on_change_callback:
                self.on_change_callback(self.value)  # Call the callback function with the new time

    def reset(self):
        self.running = False  # Stop the timer loop
        self.value = 0  # Reset the time to zero
        if self.on_change_callback:
            self.on_change_callback(self.value)  # Notify reset with the callback

    def on_change(self, callback: Callable[[float], None]):
        """Assign a callback function to be called when the time changes."""
        self.on_change_callback = callback
