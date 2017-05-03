# Synopsis

Synopsis is a tool to quickly and efficiently encode strings from text files, supporting up to 15 different types of encodings.

Current Version: v.1.0.0

Author: ThanhMinh

## Requirements:
The computer was installed python 2.7

## Install
```
apt-get -y install git
git clone https://github.com/thanhminh6996/Synopsis.git
cd ./Synopsis
```

## Use
Command: python synopsis.py -i [input file] -o [output file] -f [type of encryption]

### Example:
I have a list.txt file and I want to encode it in md5 format and output it as list_encode.txt:

`python synopsis.py -i list.txt -o list_encode.txt -f md5`

![Alt](http://sv1.upsieutoc.com/2017/05/03/Screenshotfrom2017-05-0321-17-11.png)

