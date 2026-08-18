# Flight Status Node.js Dashboard

A modern web-based dashboard for checking flight statuses using Node.js and Express.

## Features

- Real-time flight status lookup
- Clean, responsive web UI
- Multiple flight tracking
- Status history
- Quick search functionality

## Requirements

- Node.js 12.0+
- npm or yarn
- flight-status command-line tool installed

## Installation

1. Clone the repository or navigate to this folder

2. Install dependencies:
```bash
npm install
```

3. Configure environment (optional):
```bash
cp .env.example .env
# Edit .env with your settings
```

## Running the Application

```bash
npm start
```

The dashboard will be available at `http://localhost:3000`

## Development

Run with auto-reload during development:

```bash
npm run dev
```

## Project Structure

```
.
├── app.js              # Main application file
├── package.json        # Dependencies
├── public/            # Static files
│   └── index.html     # Dashboard HTML
├── routes/            # Express routes
│   └── api.js         # API endpoints
└── views/             # EJS templates
```

## API Endpoints

### GET /api/flight/:number

Get the status of a specific flight.

**Example:**
```bash
curl http://localhost:3000/api/flight/LH400
```

**Response:**
```json
{
  "number": "LH400",
  "status": "On Time",
  "gate": "B12",
  "boarding": "14:30",
  "departure": "15:00"
}
```

### POST /api/flights

Check multiple flights at once.

**Request:**
```json
{
  "flights": ["LH400", "UA123", "AA456"]
}
```

## Configuration

Edit `.env` file to configure:

```env
PORT=3000
FLIGHT_STATUS_CMD=flight-status
NODE_ENV=development
```

## Troubleshooting

### flight-status command not found

Make sure the flight-status tool is installed and in your PATH:

```bash
which flight-status
# or on Windows
where flight-status
```

If not installed, install it according to the flight-status project instructions.

## License

Same as flight-status
