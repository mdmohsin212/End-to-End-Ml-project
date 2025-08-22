from us_visa.logger import logging
from us_visa.exception import HandleException
import sys

try:
    n = 3 / 0
    print(n)

except Exception as e:
    logging.error(e)
    raise HandleException(e, sys)