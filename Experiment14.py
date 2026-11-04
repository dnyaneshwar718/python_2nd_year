import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

logging.debug("This is a debug message")
logging.info("Program started")
logging.warning("This is a warning")
logging.error("An error occurred")
logging.critical("This is a critical message")

try:
    a = 10
    b = 0
    result = a / b
except ZeroDivisionError:
    logging.exception("Cannot divide by zero")

print("Program completed")