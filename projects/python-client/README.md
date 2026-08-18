# Flight Status Python Client

A Python wrapper library for the flight-status command-line tool that provides a clean, Pythonic API for checking flight status.

## Installation

```bash
pip install flight-status-client
# or copy flight_status_client.py to your project
```

## Requirements

- Python 3.6+
- flight-status command-line tool installed and in your PATH

## Quick Start

```python
from flight_status_client import FlightStatusClient

# Initialize the client
client = FlightStatusClient()

# Check a flight's status
status = client.get_status('LH400')
print(f"Flight: {status['number']}")
print(f"Status: {status['status']}")
print(f"Gate: {status.get('gate', 'TBD')}")
```

## API Reference

### FlightStatusClient

Main class for interacting with flight status.

#### Methods

**`get_status(flight_number: str) -> dict`**

Fetch the status of a flight.

- **Parameters:**
  - `flight_number` (str): Flight number (e.g., 'LH400')

- **Returns:**
  - dict: Flight status information including number, status, gate, etc.

- **Raises:**
  - `FlightNotFoundError`: If the flight is not found
  - `FlightStatusError`: If there's an error fetching the status

## Examples

### Check Multiple Flights

```python
from flight_status_client import FlightStatusClient

client = FlightStatusClient()
flights = ['LH400', 'UA123', 'AA456']

for flight_num in flights:
    try:
        status = client.get_status(flight_num)
        print(f"{flight_num}: {status['status']}")
    except Exception as e:
        print(f"{flight_num}: Error - {e}")
```

### Get Status with Retry Logic

```python
from flight_status_client import FlightStatusClient
import time

client = FlightStatusClient()

def get_status_with_retry(flight_num, max_retries=3):
    for attempt in range(max_retries):
        try:
            return client.get_status(flight_num)
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
                continue
            raise

status = get_status_with_retry('LH400')
```

## License

Same as flight-status
