"""Script for logger
"""
import os
import logging
from datetime import datetime

class Logger:
    """Logger class for multipurposes log
    """
    def __init__(self, script_file: str, log_dir: str = "../activity_log", level: str = "INFO"):
        """
        Args:
            script_file (str): __file__ of the calling script
            log_dir (str): Directory to store the log files
            level (str): Log level as string: INFO, DEBUG, WARNING, ERROR, CRITICAL
        """
        self.start_time = datetime.now().strftime("%Y%m%d%H%M%S")
        script_name = os.path.basename(script_file)
        os.makedirs(log_dir, exist_ok=True)
        log_filename = f"{self.start_time}-{script_name}.log"
        self.log_path = os.path.join(log_dir, log_filename)

        self.logger = logging.getLogger(script_name)
        self.logger.setLevel(getattr(logging, level.upper(), logging.INFO))

        # Prevent duplicate handlers
        if not self.logger.handlers:

            handler = logging.FileHandler(self.log_path)
            formatter = logging.Formatter(
                fmt="%(asctime)s,%(msecs)03d - %(levelname)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)


    def info(self, message: str, *args, **kwargs):
        """Log level information
        Args:
            message (str):
                message of the log
        """
        self.logger.info(message)
        print(f"{datetime.now().strftime('%Y%m%d%H%M%S')} - INFO - {message % args if args else message}")

    def debug(self, message: str):
        """Log level debug
        Args:
            message (str):
                message of the log
        """
        self.logger.debug(message)
        print(f"{datetime.now().strftime('%Y%m%d%H%M%S')} - DEBUG - {message}")

    def warning(self, message: str):
        """Log level warning
        Args:
            message (str):
                message of the log
        """
        self.logger.warning(message)
        print(f"{datetime.now().strftime('%Y%m%d%H%M%S')} - WARNING - {message}")

    def error(self, message: str):
        """Log level error
        Args:
            message (str):
                message of the log
        """
        self.logger.error(message)
        print(f"{datetime.now().strftime('%Y%m%d%H%M%S')} - ERROR - {message}")

    def critical(self, message: str):
        """Log level critical
        Args:
            message (str):
                message of the log
        """
        self.logger.critical(message)
        print(f"{datetime.now().strftime('%Y%m%d%H%M%S')} - CRITICAL - {message}")

    def get_log_path(self):
        """Get log path file
        """
        return self.log_path