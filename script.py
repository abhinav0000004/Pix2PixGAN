import sys
from PIL import Image
# for multiple files
'''for i in range(100,102):
    if (i<10):
        s='0'+str(i)
    else:
        s=str(i)'''
#end multiple files
#change image name 
print("a")
images = [Image.open(x) for x in ['./uploads/1.jpg', './uploads/1.jpg']]
widths, heights = zip(*(i.size for i in images))
print("a")
total_width = sum(widths)
max_height = max(heights)
print("a")
new_im = Image.new('RGB', (total_width, max_height))
print("a")
x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]
print("a")
new_im.save('./datasets/facades/test/hel.jpg')
print("YA")
import os  
print("helo ")
os.system("python ./script3.py")
