import logging

# Create a logger instance
logger = logging.getLogger(__name__)

def hello_world():
    return "Hello, world!"

if __name__ == "__main__":
    # Configure the logger
    logging.basicConfig(level=logging.INFO)

    # Get the message from the function
    message = hello_world()

    # Log the message at the INFO level
    logger.info(message)