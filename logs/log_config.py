import logging
from sys import stdout

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=stdout,
)

logger = logging.getLogger("SZPN")
