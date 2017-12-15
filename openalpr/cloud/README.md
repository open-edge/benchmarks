# Setup cloud server (Ubuntu 16.04)
- Install OpenALPR binary: http://doc.openalpr.com/opensource.html#id1
- Install python binding:
  - Method 1: Python2 only: Install python-openalpr: apt install python-openalpr
  - Method 2: 
    - Clone github.com/openalpr/openalpr
    - cd openalpr/src/bindings/python
    - python setup.py install
    - python test.py /path/to/test/image

# Python usage

Steps:
- Load Alpr object by specifying country, config file, and `runtime_data` directory
- Use `alpr.recognize_file()` to process image files, or `alpr.recognize_array()`
  to recognize bytes

See more at:
https://github.com/openalpr/openalpr/blob/master/src/bindings/python/openalpr/openalpr.py

```
from openalpr import Alpr

alpr = Alpr("us", "/etc/openalpr/openalpr.conf",
"/usr/share/openalpr/runtime_data)

print(alpr.is_loaded())

results = alpr.recognize_file("/home/ubuntu/ea7the.jpg")
print(results)

with open("/home/ubuntu/ae7the.jpg", "rb") as im_file:
    im_bytes = im_file.read()
    results = alpr_recognize_array(im_bytes)
    print results
```
