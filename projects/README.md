# Example Projects

This folder contains example projects that showcase how to use the flight-status tool in different contexts and programming languages.

## Projects

### 1. Python Client (`python-client/`)

A simple Python client library that wraps the flight-status command-line tool, providing an easy way to check flight status programmatically.

**Features:**
- Clean Python API for checking flight status
- Error handling and status parsing
- Easy integration into Python applications

**Usage:**
```python
from flight_status_client import FlightStatusClient

client = FlightStatusClient()
status = client.get_status('LH400')
print(f"Flight {status['number']} is {status['status']}")
```

### 2. Node.js Dashboard (`nodejs-dashboard/`)

A Node.js web application that creates a real-time flight status dashboard.

**Features:**
- Express.js web server
- Interactive flight search
- Real-time status updates
- Clean web UI

**Usage:**
```bash
cd nodejs-dashboard
npm install
npm start
```

Then visit `http://localhost:3000` in your browser.

## Getting Started

1. Clone the repository
2. Navigate to the desired project folder
3. Follow the README in that folder for setup instructions
4. Run the examples to see flight-status in action

## Contributing

Feel free to add more example projects! Just create a new folder with:
- A descriptive README
- Working code examples
- Installation/setup instructions
