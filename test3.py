from PIL import Image
import numpy as np
te = np.array(Image.open("./fcity.jpg").convert('L'))
print(te.shape, te.dtype)
te2 = (100/255)*te+100
im2 = Image.fromarray(te2.astype("uint8"))
im2.save("./fcity5.jpg")
