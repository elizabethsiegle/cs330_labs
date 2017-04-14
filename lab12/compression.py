import urllib.request

mode = 3

def compress(string):
    """string is an ascii string of text.
        Returns a LZW compression (a list of indexes).
    """
    # First, seed the dictionary with ASCII symbols
    print("The original text takes %s bytes." % len(string))
    codes = dict([(chr(x),x) for x in range(256)])
    next_code = 256
    s = string[0]
    if mode == 4:
    	s = chr(s)
    output = []
    for c in string[1:]:
    	if mode == 4:
    		c = chr(c)
    	sc = s+c
    	if sc in codes:
    		s = sc
    	else:
    		output.append(codes[s])
    		codes[sc] = next_code
    		next_code = next_code+1
    		s = c
    output.append(codes[s])
    print("Dictionary size: %s entries" % len(codes))
    len_bytes = 4*len(codes)
    print("The compressed text takes %s bytes." % len_bytes)
    return output

def decompress(indices):
    """ indices is a sequence of indices into a dictionary created by compress()
        Returns the original, uncopressed text
    """
    print("Decompressing...")
    # First, seed the dictionary with ASCII symbols
    codes = dict([(x, chr(x)) for x in range(256)])
    next_code = 256

    # output the string in dictionary for first index in indices
    result = codes[indices.pop(0)] # first character/string
    previous = result[0]
    for current in indices:
        if current in codes:        # dictionary contains the current index
            s = codes[current]
        else:       # if current == len(codes)???
            s = previous + previous[0]
        result = result + s       # output s

        codes[next_code] = previous + s[0]   #Add to the dictionary
        next_code = next_code + 1
        previous = s
    print("Dictionary size: %s entries" % len(codes))
    print("The decompressed text takes %s bytes." % len(result))
    return result

def main():
	if mode == 1:
		lines = "It was the best of times, it was the worst of times."
	elif mode == 2:
		lines = open("cheer.txt","r").read()
	elif mode == 3:
		f = urllib.request.urlopen("http://cs.brynmawr.edu/Courses/cs330/spring2017/moby10b.txt")
		lines = f.read().decode("utf-8")

	com = compress(lines)
	print()
	decom = decompress(com)
	print()
	if (len(com) <= 1000):
		print("The compressed test is:")
		print(com)

	if (len(decom) <= 1000):
		print("The decompressed test is:")
		print(decom)

if __name__ == "__main__":
    main()
