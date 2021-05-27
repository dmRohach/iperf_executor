import json


class BaseParser:
    def __init__(self, executor_result, sys_error=None):
        if not sys_error:
            self.error = executor_result['error']
            self.result = executor_result['result']
            self.status = executor_result['status']
        else:
            self.error = sys_error
            self.result = None
            self.status = "Failure"

    def print_json(self):
        final = {
            "status": self.status,
            "error": self.error,
            "result": self.result
        }
        print(json.dumps(final, sort_keys=True, indent=4))


from .rising_error_argparse import *
from .iperf_parser import *
