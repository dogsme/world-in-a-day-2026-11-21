import base64
import os

# Decodes the front-page image (image.b64) and writes it to /output/entry.png.
# Paths resolve from this file's own directory, not the working directory.
HERE = os.path.dirname(os.path.abspath(__file__))
os.makedirs("/output", exist_ok=True)
with open(os.path.join(HERE, "image.b64"), "rb") as f:
    data = base64.b64decode(f.read())
with open("/output/entry.png", "wb") as f:
    f.write(data)
