import logging

def setup_logger(logger_name="bot_logger", log_file="bot.log", level= logging.INFO):
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    if logger.hasHandlers():
        return logger

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(log_file)

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    
    return logger
