import inspect
import logging

class LogGenerate():

    @staticmethod
    def loggen():
        classname = inspect.stack()[1][3]
        logger = logging.getLogger(classname)
        file = logging.FileHandler(r"C:\Users\Admin\PycharmProjects\nopCommerse\logs\logFile.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(message)s")
        file.setFormatter(format)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger

# This code defines a class called LogGenerate that contains a static method loggen() for generating a logger object.
# Here's a summary of what the code does:
#
# 1) It imports the inspect and logging modules, which are used for obtaining information about the calling function
# and setting up logging functionality, respectively.
#
# 2) The loggen() method is defined as a static method, which means it can be accessed without creating an instance of the LogGenerate class.
#
# 3) Within the loggen() method, inspect.stack()[1][3] is used to retrieve the name of the calling function.
# This information is stored in the classname variable.
#
# 4) A logger object is created using logging.getLogger(classname), where classname is passed as the name of the logger.
#
# 5) A FileHandler object is created with the path to the log file as an argument, specifying where the log messages will be written.

# 6) A Formatter object is created to define the format of the log messages, including the timestamp, log level,
# logger name, calling function name, and the log message itself.
#
# 7) The Formatter object is associated with the FileHandler using file.setFormatter(format).
#
# 8) The FileHandler is added to the logger using logger.addHandler(file).
#
# 9) The logging level is set to logging.INFO using logger.setLevel(logging.INFO).
#
# 10) Finally, the logger object is returned from the loggen() method.

