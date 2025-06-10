# 📄 TinyDocs – Smart Compression for Document Images
**TinyDocs** compresses document images like certificates, academic records, legal files, forms, personal identity cards — while keeping them readable. It is a simple and light weight web app that built with **streamlit** for speed, simplicity, and space-saving!

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
TinyDocs/<br>
|-- app.py                  # Main app<br>
|-- src/<br>
|    compression.py         # Image compression logic<br>
|    utils.py               # Helper functions<br>
|-- data/<br>
     original/              # Uploaded original images<br>
     compressed/            # Compressed output images<br>

---

## How to Run Locally

Clone the Repository
`git clone`<br>
`https://github.com/your-username/tinydocs.git`<br>
`cd tinydocs`<br>

Create a Virtual Environment (Optional but Recommended)
`python -m venv venv`<br>
`source venv/bin/activate`  `# On Windows: venv\Scripts\activate`<br>

Install Dependencies
`pip install -r requirements.txt`

Run the App
`streamlit run app.py`

---

## 🖼️ Demo


---

## 📌 Whats Upcoming
- 🔧 Add a compression quality slider
- 📂 Support batch/multiple image upload
- 📈 Show compression % and image metadata

---

## 📃 License
This project is open-source and free to use under the MIT License.
