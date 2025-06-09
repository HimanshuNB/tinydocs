# 📄 TinyDocs – Smart Compression for Document Images
**TinyDocs** compresses scanned document images like certificates, academic records, legal files, forms, personal identity cards — while keeping them readable. It is a simple and light weight web app that built with **streamlit** for speed, simplicity, and space-saving!

---

## 🚀 Features
- 📤 Upload scanned document images (JPG, JPEG, PNG)
- 🗜️ Automatically compress with default settings
- 🖼️ View original vs compressed image side-by-side
- 📉 Compare file sizes instantly
- 📥 Download the compressed image

---

## 🛠️ Built With
- Python 3.11.0
- Streamlit – for interactive UI
- OpenCV – for image compression
- os and PIL – for file handling and image saving

---

## 📂 Folder Structure
TinyDocs/
|-- app.py                  # Main app
|-- src/
|    compression.py         # Image compression logic
|    utils.py               # Helper functions
|-- data/
     original/              # Uploaded original images
     compressed/            # Compressed output images

---

## How to Run Locally

Clone the Repository
`git clone https://github.com/your-username/tinydocs.git`
`cd tinydocs`

Create a Virtual Environment (Optional but Recommended)
`python -m venv venv`
`source venv/bin/activate`  # On Windows: venv\Scripts\activate

Install Dependencies
`pip install -r requirements.txt`

Run the App
`streamlit run app.py`

---

## 🖼️ Demo
<video></video>

---

## 📌 Whats Upcoming
- 🔧 Add a compression quality slider
- 📂 Support batch/multiple image upload
- 📈 Show compression % and image metadata
- 🔐 Add privacy messaging and secure file handling

---

## 📃 License
This project is open-source and free to use under the MIT License.