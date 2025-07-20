import logging
import os
from datetime import datetime

class LogGen:
    @staticmethod
    def loggen():
        logs_dir = "logs"
        if not os.path.exists(logs_dir):
            os.mkdir(logs_dir)

        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_file = os.path.join(logs_dir, f"automation_{current_time}.log")
        logger = logging.getLogger()
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger




