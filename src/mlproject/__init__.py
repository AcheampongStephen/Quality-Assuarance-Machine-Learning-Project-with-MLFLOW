"""
This script sets up logging forthe project.
It configures the logging to output messages both to a file and to the console.
The log messages include the timestamp, log level, module name, and message.
"""

import os
import sys
import logging

# Define the logging format string to include timestamp, log level, module, and message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"  # Directory where log files will be stored
log_filepath = os.path.join(log_dir, "running_logs.log")  # Full file path for the log file

os.makedirs(log_dir, exist_ok=True)  # Create the log directory if it doesn't exist

# Configure the logging module
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # Log messages will be written to the specified file
        logging.StreamHandler(sys.stdout)  # Log messages will also be printed to the console
    ]
)

logger = logging.getLogger("mlprojectLogger")  # Create a logger object with the name "mlprojectLogger"