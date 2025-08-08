# fff
# pip install simple-image-download

from simple_image_download import simple_image_download as simp

responce = simp.simple_image_download

keywords = ["johny depp jack", "jack sparrow"]

for kw in keywords:
    responce().download(kw, 10)
    
