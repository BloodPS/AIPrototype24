1. Ubuntu 📁

Ubuntu คือระบบปฏิบัติการที่ใช้พื้นฐานจาก Linux

สำหรับการติดตั้ง Ubuntu บน WSL (Windows Subsystem for Linux): Ubuntu WSL

📌 คำสั่งพื้นฐาน

'''bash
sudo apt update   # อัปเดตแหล่งข้อมูลแพ็คเกจ
sudo apt upgrade  # อัปเกรดแพ็คเกจทั้งหมด
sudo apt install <package_name>  # ติดตั้ง package
sudo apt-get install <application>  # ติดตั้งแอปพลิเคชัน
mkdir <directory_name>  # สร้างโฟลเดอร์
rm <file_name>  # ลบไฟล์
'''

🔍 ตรวจสอบเวอร์ชันของ Ubuntu

lsb_release -a

2. GitHub 🚀

GitHub เป็นแพลตฟอร์มสำหรับการจัดการโค้ดและการทำงานร่วมกันผ่าน Git

⚙️ การตั้งค่า Git และเชื่อมต่อกับ GitHub

git config --global user.name "Your Name"

git config --global user.email "your.email@example.com"

git clone https://github.com/username/repository.git

🔄 การอัปโหลดโค้ดไปยัง GitHub

git add .

git commit -m "Initial commit"

git push origin main

3. Miniconda 🐍

Miniconda เป็นเวอร์ชันที่เล็กกว่าของ Anaconda ที่ช่วยจัดการสภาพแวดล้อม Python

🔧 การติดตั้ง Miniconda

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

🏗️ การสร้างและใช้งาน environment

conda create -n myenv python=3.9 -y
conda activate myenv

4. Web Page 🌍

Web Page เป็นหน้าเว็บที่สามารถสร้างได้ด้วย HTML, CSS และ JavaScript

📜 ตัวอย่าง HTML พื้นฐาน

<!DOCTYPE html>
<html>
<head>
    <title>My Web Page</title>
</head>
<body>
    <h1>Welcome to My Web Page</h1>
</body>
</html>

5. Web Application 🖥️

Web Application เป็นแอปพลิเคชันที่ทำงานบนเว็บ โดยใช้ Flask

🔹 การติดตั้ง Flask

pip install flask

🚀 ตัวอย่าง Flask App

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)

6. Web Service ⚡

Web Service เป็น API ที่ให้บริการข้อมูลผ่าน HTTP

📡 ตัวอย่าง Flask API

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello, API!"})

if __name__ == '__main__':
    app.run(debug=True)

7. Deep Learning 🧠

Deep Learning เป็นเทคนิคของ Machine Learning ที่ใช้ Neural Networks

📥 การติดตั้ง TensorFlow

pip install tensorflow

📊 ตัวอย่างโมเดล Deep Learning
