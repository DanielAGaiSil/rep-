import os
import time
import logging
import shutil
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

class FileOrganizerHandler(LoggingEventHandler):
    """Custom event handler for file organization."""

    # Expanded file categories and their extensions
    FILE_CATEGORIES = {
        "Documents": 
        [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".xls", ".csv", 
        ".pptx", ".ppt", ".odt", ".ods", ".rtf"],
        "Images": 
        [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", 
        ".tiff", ".webp", ".ico"],
        "Videos": 
        [".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv", 
        ".webm", ".mpeg", ".mpg"],
        "Others": []
    }

    def __init__(self, source_dir):
        super().__init__()
        self.source_dir = source_dir
        self.extension_map = self._create_extension_map()
        self.processed_files = set()

    def _create_extension_map(self):
        """Create reverse mapping from extensions to categories."""
        mapping = {}
        for category, exts in self.FILE_CATEGORIES.items():
            for ext in exts:
                mapping[ext.lower()] = category
        return mapping

    def on_created(self, event):
        """Handle file creation event with safety checks."""
        if event.is_directory:
            return

        file_path = event.src_path
        time.sleep(5)  # Allow time for file transfers to complete

        if file_path not in self.processed_files:
            self.processed_files.add(file_path)
            self._organize_file(file_path)

    def _get_unique_path(self, destination, filename):
        """Handle duplicate filenames by adding suffixes."""
        base, ext = os.path.splitext(filename)
        counter = 1
        new_name = filename

        while os.path.exists(os.path.join(destination, new_name)):
            new_name = f"{base} ({counter}){ext}"
            counter += 1

        return os.path.join(destination, new_name)

    def _organize_file(self, file_path):
        """Organize file into appropriate category directory."""
        try:
            if not os.path.isfile(file_path):
                return

            filename = os.path.basename(file_path)
            _, ext = os.path.splitext(filename)
            category = self.extension_map.get(ext.lower(), "Outros")

            dest_dir = os.path.join(self.source_dir, category)
            os.makedirs(dest_dir, exist_ok=True)

            dest_path = self._get_unique_path(dest_dir, filename)
            shutil.move(file_path, dest_path)

            logging.info(f"Arquivo '{filename}' movido para {category}")

        except Exception as e:
            logging.error(f"Erro ao processar {file_path}: {str(e)}")


def main():
    source_directory = "C:/Users/Daniel/Downloads"

    event_handler = FileOrganizerHandler(source_directory)
    observer = Observer()
    observer.schedule(event_handler, source_directory, recursive=False)

    try:
        observer.start()
        logging.info(f"Monitoramento iniciado em {source_directory}")
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
        logging.info("Monitoramento encerrado pelo usuário")
    finally:
        observer.join()


if __name__ == "__main__":
    main()
