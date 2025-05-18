import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent
from typing import Callable, List
import os
import logging
from src.core import env
import yaml

logger = logging.getLogger(__name__)


class CortexEventHandler(FileSystemEventHandler):
    def __init__(self, callback: Callable[[FileSystemEvent], None]):
        self.callback = callback

    def on_created(self, event: FileSystemEvent):
        self.callback(event)

    def on_modified(self, event: FileSystemEvent):
        self.callback(event)

    def on_deleted(self, event: FileSystemEvent):
        self.callback(event)


class FileWatcherDaemon:
    def __init__(
        self, cortex_paths: List[str], callback: Callable[[FileSystemEvent], None]
    ):
        self.cortex_paths = cortex_paths
        self.callback = callback
        self.observer = Observer()

    def start(self):
        for path in self.cortex_paths:
            if os.path.exists(path):
                event_handler = CortexEventHandler(self.callback)
                self.observer.schedule(event_handler, path=path, recursive=True)
            else:
                print(f"[FileWatcher] Path does not exist: {path}")
        self.observer.start()
        print("[FileWatcher] Started watching cortices...")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.observer.stop()
        self.observer.join()
        print("[FileWatcher] Stopped.")


# Example callback
def handle_file_event(event: FileSystemEvent):
    print(f"[FileWatcher] Event: {event.event_type} - {event.src_path}")


# Example usage
if __name__ == "__main__":
    cortex_file = env.CORTICES_FILE
    with open(cortex_file, "r") as f:
        cortices = yaml.safe_load(f)
    print(cortices)
    watcher = FileWatcherDaemon(cortex_paths=cortices, callback=handle_file_event)
    watcher.start()
