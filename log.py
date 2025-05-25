# Just logger factories

from rites.logger import get_logger, get_sec_logger, Logger


def p_logger(name) -> Logger:
    l = get_logger(log_path="logs", log_name=name, max_logs=2)

    l.add_custom("event", "EVT", 164, 247, 96)
    return l


def s_logger(name) -> Logger:
    l = get_sec_logger(log_path="logs", log_name=name)

    l.add_custom("event", "EVT", 164, 247, 96)
    return l
