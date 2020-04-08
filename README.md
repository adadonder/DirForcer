# DirForcer 
DirForcer is a Python tool that brute forces websites to find directories or files on it.

### Installation
````
$ python3 setup.py install
````
or
````
$ pip install .
````

### Usage
Be sure to run with ``python3``.
```
python3 DirForcer.py [-h] [-t TARGET] [-w WORDLIST] [-e]

  -h, --help                   show this help message and exit
  -t, --target TARGET          Target URL
  -w, --wordlist WORDLIST      Path to the wordlist.
  -e, --extension              An extension list to use while brute forcing. OPTIONAL
                               default: [ .php , .bak .orig, .inc ]
```
#### There is a wordlist included with DirForcer (dirforcer_wordlist.txt). If you want to, feel free to use your own wordlist.

### License
DirForcer is released under the Apache 2.0 license. See [LICENSE](https://github.com/adadonder/DirForcer/blob/master/LICENSE) for details.

### Contact
Feel free to contact me via e-mail: adadonderr@gmail.com
