
import logging
import random
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    logger.info("### Invoked")
    logger.info(event)

    if random.randint(1, 100) < 10:
        logger.error('Random error')
        raise Exception("oh no")

    return
