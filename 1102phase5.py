# try:
#     number = int(input("Enter a number: "))
# except ValueError:
#     print("That's not a valid number. Please enter an integer.")
# else:
#     print(f"You entered the number: {number}")
# finally:
#     print("Execution completed.")

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    encoding="utf-8",
    format="%(asctime)s %(levelname)s %(message)s",
    force=True,
)

logging.info("Logging setup complete.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")

print("Logging messages have been written to app.log.")