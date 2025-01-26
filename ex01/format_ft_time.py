import time
from datetime import datetime

# Get current epoch time
current_timestamp = time.time()

# Format timestamp
seconds_str = f"{current_timestamp:,.4f}"
scientific_str = f"{current_timestamp:.2e}"

# Convert to UTC datetime
date_utc = datetime.utcfromtimestamp(current_timestamp)
date_str = date_utc.strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {seconds_str} or {scientific_str} in scientific notation$")
print(date_str)
