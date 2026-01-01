# Import necessary modules
import logging  # For logging messages to files or console
import os  # For interacting with the operating system (like creating directories)
from datetime import datetime  # For working with current date and time
import time  # Imported but not used in this code (can be removed if not needed)


class LogGen:
    """
    LogGen class to generate and configure a logger for automation scripts.
    The logger writes log messages to a timestamped log file inside a 'logs' folder.
    """

    @staticmethod
    def loggen():
        """
        Static method to create and return a logger instance.
        Ensures that each log file has a unique name based on current timestamp.
        """

        # Define the directory where logs will be stored
        logs_dir = "logs"

        # If the logs directory does not exist, create it
        if not os.path.exists(logs_dir):
            os.mkdir(logs_dir)

        # Get current date and time in format YYYY-MM-DD_HH-MM-SS
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Define the full path for the log file with a timestamped filename
        log_file = os.path.join(logs_dir, f"automation_{current_time}.log")

        # Get the root logger instance
        logger = logging.getLogger()

        # Create a file handler to write log messages to the file
        file_handler = logging.FileHandler(log_file)

        # Define the log message format
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)  # Apply the formatter to the file handler

        # Add the file handler to the logger
        logger.addHandler(file_handler)

        # Set the logging level to INFO (can also be DEBUG, WARNING, ERROR, etc.)
        logger.setLevel(logging.INFO)

        # Return the configured logger instance
        return logger
