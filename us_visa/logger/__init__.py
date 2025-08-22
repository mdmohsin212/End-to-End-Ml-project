import logging
import os
from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

dir = "logs"

logs_path = os.path.join(from_root(), dir, LOG_FILE)

os.makedirs(dir, exist_ok=True)

logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level = logging.DEBUG,
)