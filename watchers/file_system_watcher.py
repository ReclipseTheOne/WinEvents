"""
Simple and reliable file system watcher using polling method.
"""

import os
import time
from log import s_logger
from events import CreateFolderEvent

from utils.paths import sanitize

WATCH_PATHS = [
    os.path.expanduser("~\\Desktop\\Dev")
]


class SimpleFileSystemWatcher:
    """Simple polling-based file system watcher."""
    
    def __init__(self):
        self.logger = s_logger("FileSystemWatcher")
        self.known_directories = set()
        self._populate_initial_directories()
    
    def _populate_initial_directories(self):
        """Populate the initial set of directories."""
        try:
            for WATCH_PATH in WATCH_PATHS:
                if os.path.exists(WATCH_PATH):
                    for item in os.listdir(WATCH_PATH):
                        item_path = os.path.join(WATCH_PATH, item)
                        if os.path.isdir(item_path):
                            self.known_directories.add(sanitize(item_path))
                    self.logger.info(f"Monitoring {len(self.known_directories)} initial " + ("directory" if len(self.known_directories) == 1 else "directories") + f" in {WATCH_PATH}")
        except Exception as e:
            self.logger.error(f"Failed to populate initial directories: {e}")
    
    def _check_for_new_directories(self, dispatch):
        """Check for new directories and dispatch events."""
        try:
            for WATCH_PATH in WATCH_PATHS:
                if not os.path.exists(WATCH_PATH):
                    return
                
                current_directories = set()
                for item in os.listdir(WATCH_PATH):
                    item_path = os.path.join(WATCH_PATH, item)
                    if os.path.isdir(item_path):
                        current_directories.add(sanitize(item_path))
            
                # Find new directories
                new_directories = current_directories - self.known_directories
                
                for new_dir in new_directories:
                    self.logger.custom("event", f"Folder created: {new_dir}")
                    dispatch(CreateFolderEvent(new_dir))
                
                # Update known directories
                self.known_directories = current_directories
            
        except Exception as e:
            self.logger.error(f"Error checking for new directories: {e}")
    
    def run(self, dispatch, poll_interval=0.5):
        """
        Run the file system watcher.
        
        Args:
            dispatch: The dispatch function to call when events occur
            poll_interval: How often to check for changes (in seconds)
        """
        self.logger.info(f"Starting file system monitoring on {WATCH_PATHS} (polling every {poll_interval}s)")
        
        try:
            while True:
                self._check_for_new_directories(dispatch)
                time.sleep(poll_interval)
        except KeyboardInterrupt:
            self.logger.info("File system monitoring stopped")


def run_simple_fs_watcher(dispatch, poll_interval=0.5):
    """
    Convenience function to run the simple file system watcher.
    
    Args:
        dispatch: The dispatch function to call when events occur
        poll_interval: How often to check for changes (in seconds)
    """
    watcher = SimpleFileSystemWatcher()
    watcher.run(dispatch, poll_interval)
