import cv2
import os

def compress_default(input_path, output_dir="data/compressed", quality=50):
     os.makedirs(output_dir, exist_ok=True)

     image = cv2.imread(input_path)

     filename = os.path.basename(input_path)
     filename = os.path.splitext(filename)[0] + "_compressed.jpg"
     output_path = os.path.join(output_dir, filename)

     cv2.imwrite(output_path, image, [cv2.IMWRITE_JPEG_QUALITY, quality])

     return output_path