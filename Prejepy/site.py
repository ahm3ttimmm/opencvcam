from flask import Flask, render_template, jsonify
import os
import random

app = Flask(__name__)

C_KLASORU = r"C:\Users\User\Desktop\Prejepy\C"
UPLOADED_FILE = "uploaded.txt"

def get_uploaded_images():
    if not os.path.exists(UPLOADED_FILE):
        return set()
    with open(UPLOADED_FILE, "r") as f:
        return set(line.strip() for line in f.readlines())

def save_uploaded_image(filename):
    with open(UPLOADED_FILE, "a") as f:
        f.write(filename + "\n")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/random-image")
def random_image():
    all_images = [f for f in os.listdir(C_KLASORU) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    uploaded = get_uploaded_images()
    not_uploaded = [img for img in all_images if img not in uploaded]

    if not not_uploaded:
        return jsonify({"status": "empty", "message": "Gösterilecek resim kalmadı."})

    chosen = random.choice(not_uploaded)
    save_uploaded_image(chosen)

    img_url = f"/static/C/{chosen}"
    return jsonify({"status": "ok", "image_url": img_url})

if __name__ == "__main__":
    app.run(debug=True)
