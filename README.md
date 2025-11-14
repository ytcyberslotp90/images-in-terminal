# Image Viewer (Chafa Auto-Installer)

This **Python script automatically checks whether Chafa is installed on your system**. If Chafa is missing, it installs it via **winget** and then displays the given image inside your terminal using **Sixel** graphics.

---

## ✨ Features

* **Auto-detects** if Chafa is installed
* Installs Chafa automatically using **winget** if missing
* Displays images in terminal using **Sixel**
* Checks if the image file exists
* Simple, lightweight, and **Beginner-friendly**

---

## 💡 Usage

1.  Install **Python 3.x**
2.  Keep your image in the same folder (default `image.jpg`)
3.  Run the script:
    ```bash
    python viewer.py
    ```

---

## 💖 How It Works

1.  Script tries:
    ```bash
    chafa --version
    ```
3.  If Chafa exists - Image is displayed
4.  If not installed:
    ```bash
    winget install chafa --silent
    ```
6.  After installation success:
    ```bash
    chafa --format sixel image.jpg
    ```

---

## 🖼️ Changing the Image

Edit the line in the script:
`image_file = 'image.jpg'`
Replace it with any other **image filename or path**.

---
## 📷 Screenshot:
![Screenshot](https://raw.githubusercontent.com/ytcyberslotp90/images-in-terminal/refs/heads/main/Screenshot.png)
---
## ⚙️ Requirements

* **Windows 10/11+**
* **Python 3.x**
* **winget** installed
* **Terminal that supports Sixel** (Windows Terminal recommended)

---

## 📜 License

Free to use, modify, and share.
Credits appreciated! 😊

---

YouTube: [Cyber Slot](https://www.youtube.com/@cyberslot-p90)
Discord: [Get Discord invite link](https://discord.gg/6bdpB4Bh)
WebSite: [Official WebSite](https://csp90.pages.dev)
App Store: [Cyber Slot App Store](https://apps-csp90.pages.dev)
