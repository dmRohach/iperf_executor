from . import SSHExecutor


class IperfExecutor(SSHExecutor):
    def __init__(self, args):
        super().__init__(args)
        self.args.append("iperf3 -c " + args.client)
