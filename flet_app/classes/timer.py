from typing import Optional

class Timer():
    def __init__(self):
        self.value: Optional[float] = 0  # Initialize with None

    def get_time(self):
        if self.value is not None:
            return round(self.value, 2)  # Round value to 2 decimal places
        return None  # Return None if value is not set
    
    def get_formatted_time(self):
        return "{:.2f}".format(self.value)
