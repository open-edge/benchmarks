from openalpr import Alpr

alpr = Alpr("us","/etc/openalpr/openalpr.conf", "/usr/share/openalpr/runtime_data")
print(alpr.is_loaded())

results = alpr.recognize_file("/home/ubuntu/ea7the.jpg")
print(results)

with open("/home/ubuntu/ea7the.jpg", 'rb') as im_file:
	im_bytes = im_file.read()
	results = alpr.recognize_array(im_bytes)
	print(results)

