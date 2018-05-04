"""

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
  
"""
import docopt
import hide_msg

if __name__=='__main__':
	args = docopt.docopt(__doc__, version='1.0')
	img_loc = args["--in"]
	out_file = args["--out"]
		
	if args["encode"] :
		try:
			msg = open(args["--message"], 'r').read()
		except:
			msg = args["--message"]
		hide_msg.encode_image(msg, img_loc) if out_file is None else hide_msg.encode_image(msg, img_loc, out_loc=out_file)
	elif args["decode"] :
		ret = hide_msg.decode_image(img_loc)
		if ret is not False:
			print(ret) if out_file is None else open(out_file, 'w').write(ret)