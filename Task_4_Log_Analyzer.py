import logging
import datetime as dt

today = dt.datetime.today()
filename = f"{today.month:02d}-{today.day:02d}-{today.year}.log"

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("SYSTEM_LOG")

file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.WARNING)

formatter = logging.Formatter("%(asctime)s: %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.debug("Debug")
logger.info("info")
logger.warning("Warning")
logger.error("Error")
logger.critical("Critical")

file = open('09-09-2023.log','r')
file_content = file.read()
print(file_content)

