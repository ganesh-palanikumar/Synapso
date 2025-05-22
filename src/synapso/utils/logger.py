import loguru

def get_logger(name: str) -> loguru.Logger:
    return loguru.logger.bind(name=name)
