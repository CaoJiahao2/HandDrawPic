from PIL import Image
import numpy as np
te = np.array(Image.open("./fcity.jpg"))
print(te.shape, te.dtype)
te2 = [255, 255, 255] - te
im2 = Image.fromarray(te2.astype("uint8"))
im2.save("./fcity2.jpg")
