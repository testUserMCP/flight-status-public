"""Python client library for flight-status command-line tool."""

import subprocess
import json
from typing import Dict, Any, Optional


class FlightStatusError(Exception):
    """Base exception for flight status errors."""
    pass


class FlightNotFoundError(FlightStatusError):
    """Exception raised when a flight is not found."""
    pass


class FlightStatusClient:
    """Python client for checking flight status."""

    def __init__(self, flight_status_cmd: str = 'flight-status'):
        """Initialize the flight status client.

        Args:
            flight_status_cmd: Path to or name of flight-status command
        """
        self.cmd = flight_status_cmd

    def get_status(self, flight_number: str) -> Dict[str, Any]:
        """Get the status of a flight.

        Args:
            flight_number: The flight number (e.g., 'LH400')

        Returns:
            Dictionary containing flight status information

        Raises:
            FlightNotFoundError: If the flight is not found
            FlightStatusError: If there's an error fetching status
        """
        try:
            result = subprocess.run(
                [self.cmd, flight_number],
                capture_output=True,
                text=True,
                timeout=10
            )

            if result.returncode != 0:
                if 'not found' in result.stderr.lower():
                    raise FlightNotFoundError(
                        f"Flight {flight_number} not found"
                    )
                raise FlightStatusError(
                    f"Error checking flight status: {result.stderr}"
                )

            # Parse the output (format depends on flight-status implementation)
            status_data = self._parse_status(result.stdout, flight_number)
            return status_data

        except subprocess.TimeoutExpired:
            raise FlightStatusError(f"Timeout checking status for {flight_number}")
        except FileNotFoundError:
            raise FlightStatusError(
                f"flight-status command not found at '{self.cmd}'. "
                "Make sure it's installed and in your PATH."
            )

    def _parse_status(self, output: str, flight_number: str) -> Dict[str, Any]:
        """Parse the output from flight-status command.

        Args:
            output: Raw output from flight-status command
            flight_number: The flight number that was checked

        Returns:
            Parsed status dictionary
        """
        # Simple parsing - adjust based on actual flight-status output format
        lines = output.strip().split('\n')
        status_dict = {'number': flight_number}

        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                status_dict[key.strip().lower()] = value.strip()
            else:
                status_dict['status'] = line.strip()

        return status_dict
