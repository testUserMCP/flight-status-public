"""Flight Status Node.js Dashboard Application."""

const express = require('express');
const bodyParser = require('body-parser');
const { execSync } = require('child_process');
const path = require('path');

require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;
const FLIGHT_STATUS_CMD = process.env.FLIGHT_STATUS_CMD || 'flight-status';

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Helper function to get flight status
function getFlightStatus(flightNumber) {
    try {
        const output = execSync(`${FLIGHT_STATUS_CMD} ${flightNumber}`, {
            encoding: 'utf8',
            timeout: 10000
        }).trim();

        // Parse the output
        const status = parseFlightOutput(output, flightNumber);
        return { success: true, data: status };
    } catch (error) {
        return {
            success: false,
            error: `Could not fetch status for ${flightNumber}`,
            details: error.message
        };
    }
}

// Parse flight status output
function parseFlightOutput(output, flightNumber) {
    const lines = output.split('\n');
    const status = { number: flightNumber };

    lines.forEach(line => {
        if (line.includes(':')) {
            const [key, value] = line.split(':').map(s => s.trim());
            status[key.toLowerCase().replace(/\s+/g, '_')] = value;
        } else if (line.trim()) {
            status.status = line.trim();
        }
    });

    return status;
}

// Routes
app.get('/', (req, res) => {
    res.render('index', { title: 'Flight Status Dashboard' });
});

// API endpoint for single flight
app.get('/api/flight/:number', (req, res) => {
    const flightNumber = req.params.number.toUpperCase();
    const result = getFlightStatus(flightNumber);
    res.json(result);
});

// API endpoint for multiple flights
app.post('/api/flights', (req, res) => {
    const flights = req.body.flights || [];
    const results = flights.map(flight => ({
        number: flight,
        ...getFlightStatus(flight).data
    }));

    res.json({ flights: results });
});

// Health check
app.get('/health', (req, res) => {
    res.json({ status: 'OK', timestamp: new Date() });
});

// 404 handler
app.use((req, res) => {
    res.status(404).json({ error: 'Not found' });
});

// Start server
app.listen(PORT, () => {
    console.log(`Flight Status Dashboard running at http://localhost:${PORT}`);
    console.log(`Using flight-status command: ${FLIGHT_STATUS_CMD}`);
});

module.exports = app;
