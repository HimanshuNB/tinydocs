import os

def save_uploaded_image(uploaded_image, save_dir="data/original"):
     if uploaded_image is not None:
          os.makedirs(save_dir, exist_ok=True)
          image_path = os.path.join(save_dir, uploaded_image.name)
          with open(image_path, "wb") as f:
               f.write(uploaded_image.getbuffer())
          return image_path
     return None

def get_file_size(file_path):
    size_bytes = os.path.getsize(file_path)
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024**2:
        return f"{size_bytes / 1024:.2f} KB"
    else:
        return f"{size_bytes / (1024**2):.2f} MB"