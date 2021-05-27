from . import BaseParser


class IperfParser(BaseParser):
    def __init__(self, executor_result, args):
        super().__init__(executor_result)
        if not executor_result["error"]:
            self.executor_result_split = executor_result["result"].split('\n')[-5].split()  # Deleting unnecessary information
            self.result = {
                "IPs": str(args.host.split("@")[1] + ", " + args.client),
                "Hostname": str(args.host.split("@")[0]),
                "Interval": str(self.executor_result_split[2] + " " + self.executor_result_split[3]),
                "Transfer": str(self.executor_result_split[4] + " " + self.executor_result_split[5]),
                "Bandwidth": str(self.executor_result_split[6] + " " + self.executor_result_split[7])
            }
