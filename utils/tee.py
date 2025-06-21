"""Tee class to duplicate
   log in console to data log
"""
import sys
from typing import TextIO, Optional
from datetime import datetime
from contextlib import contextmanager

class Tee:
    """Class for duplicating the 
       stdout writing log to files
    """
    def __init__(self, *streams: TextIO) -> None:
        """class initialization
        """
        self.streams = streams
    def write(self, data: str) -> None:
        """method to write log
        Args:
            data (_type_): _description_
        """
        for s in self.streams:
            s.write(data)

    def flush(self) -> None:
        """method to flush std out
        """
        for s in self.streams:
            s.flush()

@contextmanager
def tee_logger(log_filename: Optional[str] = None) -> None:
    """
    Context manager that logs stdout and stderr to both console and a log file.

    Args:
        log_filename (Optional[str]): Log file name. If None, generates a timestamped filename.

    Yields:
        None
    """
    if log_filename is None:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        log_filename = f"{timestamp}-RoboflowData.log"

    with open(log_filename, "w", encoding='utf-8') as f:
        original_stdout = sys.stdout
        original_stderr = sys.stderr
        sys.stdout = Tee(sys.stdout, f)
        sys.stderr = Tee(sys.stderr, f)

        try:
            yield
        finally:
            sys.stdout = original_stdout
            sys.stderr = original_stderr
            print(f"\n✅ Output also saved to: {log_filename}")