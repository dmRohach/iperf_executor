from executors import *
from parsers import RisingErrorArgparse, BaseParser, IperfParser


parser = RisingErrorArgparse()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-p', help='keyword password')
group.add_argument('-f', help='password from file')
parser.add_argument('host', type=str, help='connection address')
parser.add_argument('client', type=str, help='client address (whom to listen)')

try:
    args = parser.parse_args()
    executor = IperfExecutor(args).give_result()
    parser = IperfParser(executor, args)
    parser.print_json()
except Exception as e:
    parser = BaseParser(None, sys_error=str(e))
    parser.print_json()
