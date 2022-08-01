# import logging
# logging.basicConfig(level=logging.INFO, filename='datacamp.log', filemode='a')
#
# logging.info("=")

# logging.debug("A debug Logging Message")
# logging.info("A INFO Logging Message")
# logging.warning("A Warning logging Message")
# logging.error("An Error Logging Message")
# logging.critical("A critical Logging Message")


import logging
logging.basicConfig(format='Date-Time : %(asctime)s : Line No. :%(lineno)d - %(message)s', level = logging.DEBUG)

logging.debug("A debug Logging Message")
logging.info("A INFO Logging Message")
logging.warning("A Warning logging Message")
logging.error("An Error Logging Message")
logging.critical("A critical Logging Message")

