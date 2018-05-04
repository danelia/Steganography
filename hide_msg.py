from PIL import Image

def to_bin(msg):
    return ''.join(format(ord(c), "08b") for c in msg) + "10"

def to_ascii(msg):
    return ''.join(chr(int(msg[i:i+8], 2)) for i in range(0, len(msg), 8))


def encode_image(msg, img_loc, out_loc="encoded_image.png"):
	try :
		img = Image.open(img_loc)
	except :
		print("Wrong destination or file name")
		return False
		
	if img.mode != 'RGB':
		print("image mode needs to be RGB")
		return False
    
	msg_b = to_bin(msg)
    
	encoded = img.copy()
	width, height = img.size
	for row in range(height):
		for col in range(width):
			if len(msg_b) is 0:
				encoded.save(out_loc)
				return encoded
            
			r, g, b = img.getpixel((col, row))
			r = int(format(r, "08b")[:-2] + msg_b[:2], 2)
			msg_b = msg_b[2:]
			encoded.putpixel((col, row), (r, g , b))
    
    # we will almost never get to this line,
    # but its here just to be safe
	encoded.save(out_loc)
	return encoded

def decode_image(img_loc):
	try :
		img = Image.open(img_loc)
	except:
		print("Wrong destination or file name")
		return False
	
	width, height = img.size
	msg = ""
	index = 0
	for row in range(height):
		for col in range(width):
			try:
				r, g, b = img.getpixel((col, row))
			except ValueError:
				r, g, b, a = img.getpixel((col, row))
            
			last_two = format(r, "08b")[-2:]
			if index % 8 is 0 and last_two[0] is '1':
				return to_ascii(msg)
			msg += last_two
			index += 2
    
    # we will almost never get to this line,
    # but its here just to be safe
	return to_ascii(msg)