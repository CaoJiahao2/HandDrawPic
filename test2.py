from PIL import Image
import numpy as np
te = np.array(Image.open("./fcity.jpg").convert("L"))
print(te.shape, te.dtype)
im = Image.fromarray(te.astype("uint8"))
im.save("./fcity3.jpg")
te2 = 255 - te
im2 = Image.fromarray(te2.astype("uint8"))
im2.save("./fcity4.jpg")
