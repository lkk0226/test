import logging


# logging.basicConfig(filename="F:\\pythonPjo\\testExcelCase\\log\\test.log", filemode="w", format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)
# logging.warning('this is warning')
# logging.info('this is info')

def get_logger(filename):
    logger_obj = logging.getLogger("mylogger")  #创建logger对象
    logger_obj.setLevel(logging.DEBUG)  #设置日志级别

    fh = logging.FileHandler(filename, encoding="UTF-8")  #创建handler输出到日志
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()  #创建handler输出到控制台
    ch.setLevel(logging.DEBUG)

    # 定义输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 给logger对象添加handler
    logger_obj.addHandler(fh)
    logger_obj.addHandler(ch)
    return logger_obj

# logger_obj=get_logger("F:\\pythonPjo\\testExcelCase\\log\\logtest.txt")
# logger_obj.info("info")
# logger_obj.error("error")
# logger_obj.warning("warning")
# logger_obj.debug("debug")
# logger_obj.critical("critical")
