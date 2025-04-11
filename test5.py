import gzip
import time
import os

data = b"A" * 1000000000  # 100 MB

start = time.time()
with gzip.open("test.gz", "wb") as f:
    f.write(data)
compress_time = time.time()

with gzip.open("test.gz", "rb") as f:
    _ = f.read()
decompress_time = time.time()

print(f"Compression took {compress_time - start:.2f} sec, Decompression took {decompress_time - compress_time:.2f} sec")
os.remove("test.gz")
