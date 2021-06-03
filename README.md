## Usage
`iperf_executor` is a command line program, that connects to the remote server and measures network bandwidth with linux system command `iperf3`.

 you shold run it with following argumens:
 
- `-p/-f` (setting password as an argument / password should be taken from the file)
- `password / filename`
- `servername@serverip`
- `clientip`

For example:

    $ python3 app.py -p 1234 username@192.168.1.1 192.168.1.2
    
 will return you `JSON dict` with following keys:
 
- `status`
- `error`
- `result`
