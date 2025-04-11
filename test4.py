from PIL import Image, ImageFilter
import time

img = Image.new("RGB", (4000, 4000), color="red")

start = time.time()
for _ in range(500):
    img = img.filter(ImageFilter.GaussianBlur(2))
end = time.time()

print(f"20 Gaussian filters took {end - start:.2f} seconds")
