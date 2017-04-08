# chapter 3. Neural Network - 예제 모음
#
# runnable 
# %run C:\Users\Administrator\Documents\workspace\deep_learing_for_scratch\chap3_6_mnist.py

import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
from mnist import load_mnist
from PIL import Image

def img_show(img):
	pil_img = Image.fromarray(np.uint8(img))
	pil_img.show()

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

img = x_train[0]
label = t_train[0]

print(label) # 5

print(img.shape)
img = img.reshape(28, 28)
print(img.shape)

img_show(img)