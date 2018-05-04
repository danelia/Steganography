# Steganography

Python program based on steganographical methods to hide files in images.

## Information

* `encode_image(msg, img_loc, out_loc)` takes message(`msg`) and hides it in image(`img_loc`) and saves in `out_loc`. default ouput file is "encoded_image.png". `msg` can be either file or string.
* `decode_image(img_loc)` takes image and finds hidden message. If output file isn't specified(see usage) hidden message will be displayed on terminal.

Note that, program only supports RGB images.

## Installation

```
pip install -r requirements.txt
```

## Usage and Options
```
Usage:
  main.py encode -i <input> -m <message/file> -o <output>
  main.py encode -i <input> -m <message/file>
  main.py decode -i <input> -o <output>
  main.py decode -i <input>
  
Options:
  -h, --help                	Show this help
  -V, --version                 Show the version
  -m,--message=<message/file>   File to hide
  -i,--in=<input>           	Input image
  -o,--out=<output>         	Output image/file for text (optional, default img is "encoded_image.png")
  
```
