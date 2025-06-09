import streamlit as st
from src.utils import save_uploaded_image, get_file_size
from src.compression import compress_default

st.set_page_config("Tiny Docs", page_icon=":boy:")

st.title("TinyDocs – Fast & Simple Image Compression")
st.divider()

uploaded_image = st.file_uploader("Select Image to be Compressed", type=["jpg", "jpeg", "png"], accept_multiple_files=False)
if uploaded_image is not None:
     saved_path = save_uploaded_image(uploaded_image)
     col1, col2 = st.columns(2)
     with col1:
          st.image(saved_path, caption="Uploaded Image", use_container_width=True)
          original_size = get_file_size(saved_path)
          st.write(f"Original File: {original_size}")

if uploaded_image:
     if st.button("Compress"):
          if saved_path:
               compressed_path = compress_default(saved_path)
               with col2:
                    st.image(compressed_path, caption="Compressed Image", use_container_width=True)
                    compressed_size = get_file_size(compressed_path)
                    st.write(f"Compressed Size: {compressed_size}")
                    with open(compressed_path, "rb") as f:
                         st.download_button("Download", f, file_name=compressed_path.split("/")[-1], icon=":material/download:")