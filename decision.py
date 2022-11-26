
import keras
import numpy as np
from PIL import Image
from skimage import io

img = []
model = keras.models.load_model('./models/model_myCNN.h5')
ad = "forrest"#input("resim adı ")
try:
    image1 = Image.open(ad+'.jpg')
    asa= image1.size
    if image1.size!=(250, 250):

        im2= image1.resize((250, 250))
        im2.save(ad+'.jpg')
    image = io.imread(ad+".jpg")
    img.append(image)
    x = np.array(img)

    y = model.predict(x)
    print(y)
    y= np.argmax(y, axis=1)
    if y ==0:
        print("yangın yok")
    elif y == 1:
        print("yangın var")
except FileNotFoundError :
    print(" dosya bulunamadı hata!")
