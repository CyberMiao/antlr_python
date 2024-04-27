from types import TracebackType


class SyntaxException(BaseException):
    def __init__(self, line, info):
        self.line = line
        self.info = info



