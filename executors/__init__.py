import subprocess


class SSHExecutor:
    def __init__(self, args, command=None):
        self.args = ["sshpass", "-p", args.p, "ssh", args.host]
        if command:
            self.args.append(command)
        if args.f:
            self.args[1], self.args[2] = "-f", args.f

    def give_result(self):
        sub = subprocess.Popen(self.args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = map(lambda x: x, sub.communicate())
        final = {
            "status": sub.returncode,
            "error": err.decode("utf-8"),
            "result": out.decode("utf-8")
        }
        return final


from .iperf_executor import IperfExecutor