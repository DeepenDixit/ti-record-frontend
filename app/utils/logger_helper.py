import logging

from app.core.config import settings

app_logger = logging.getLogger(settings.APP_LOGGER_NAME)

handeler = logging.StreamHandler()
handeler.setLevel(settings.APP_LOG_LEVEL)
handeler.setFormatter(
    logging.Formatter(
        "%(asctime)s %(levelname)s [%(name)s] --- "
        "%(module)s::%(funcName)s::%(lineno)d : %(message)s"
    )
)
logging.basicConfig(level=settings.APP_LOG_LEVEL, handlers=[handeler])
