import time
import sys
import os
import signal
import daemon
import daemon.pidfile
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import loguru

# Configure logging to write to a file
loguru.logger.remove()  # Remove default handler
loguru.logger.add(
    "cortex_watcher.log",
    rotation="1 day",
    retention="7 days",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO",
)
logger = loguru.logger.bind(name="cortex_watcher")


class CortexEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        logger.info(f"[CREATED] {event.src_path}")

    def on_deleted(self, event):
        logger.info(f"[DELETED] {event.src_path}")

    def on_modified(self, event):
        logger.info(f"[MODIFIED] {event.src_path}")

    def on_moved(self, event):
        logger.info(f"[MOVED] {event.src_path} -> {event.dest_path}")


def run_watcher(path_to_watch):
    event_handler = CortexEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=True)

    logger.info(f"Watching directory: {path_to_watch}")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    finally:
        observer.join()


def main():
    if len(sys.argv) != 2:
        logger.error(f"Usage: python {sys.argv[0]} /path/to/watch")
        sys.exit(1)

    path_to_watch = sys.argv[1]
    if not os.path.isdir(path_to_watch):
        logger.error(f"Error: {path_to_watch} is not a valid directory")
        sys.exit(1)

    pid_file = "/tmp/cortex_watcher.pid"
    log_file = "/tmp/cortex_watcher.log"

    context = daemon.DaemonContext(
        working_directory="/",
        umask=0o002,
        pidfile=daemon.pidfile.PIDLockFile(pid_file),
        signal_map={
            signal.SIGTERM: lambda signo, frame: sys.exit(0),
            signal.SIGINT: lambda signo, frame: sys.exit(0),
        },
        stdout=log_file,
        stderr=log_file,
    )

    with context:
        logger.info("Starting cortex watcher daemon")
        run_watcher(path_to_watch)


if __name__ == "__main__":
    main()
