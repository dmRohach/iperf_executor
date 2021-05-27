## Usage
`iperf_executor` is a command line program, executing and parsing linux system command `df`.

 you shold run it with following argumens:
 
- `-p/-f` (setting password as an argument / password should be taken from the file)
- `password / filename`
- `result`

    $ python3 app.py
    
 will return you `JSON dict` with following keys:
 
- `status`
- `error`
- `result`

You could add argument `--human` or `--inode` to execute 

`df -h` and `df -i` respectively 
