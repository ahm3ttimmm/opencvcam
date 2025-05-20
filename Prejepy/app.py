import os
import cv2
import random
from datetime import datetime
from tkinter import Tk, Button, Label, Frame, messagebox
from PIL import Image, ImageTk
from rembg import remove
import io

# Klasörler
A_KLASORU = r"C:\Users\User\Desktop\Prejepy\A"
B_KLASORU = r"C:\Users\User\Desktop\Prejepy\B"
C_KLASORU = r"C:\Users\User\Desktop\Prejepy\C"

for klasor in [A_KLASORU, B_KLASORU, C_KLASORU]:
    os.makedirs(klasor, exist_ok=True)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("CPU ile Arka Plan Değiştirici")
        self.root.geometry("1200x420")
        self.root.resizable(True, True)

        # Frame'ler
        self.left_frame = Frame(root, width=400, height=400)
        self.left_frame.grid(row=0, column=0)
        self.left_frame.grid_propagate(False)

        self.middle_frame = Frame(root, width=400, height=400)
        self.middle_frame.grid(row=0, column=1)
        self.middle_frame.grid_propagate(False)

        self.right_frame = Frame(root, width=400, height=400)
        self.right_frame.grid(row=0, column=2)
        self.right_frame.grid_propagate(False)

        # Kamera görüntüsü label
        self.cam_label = Label(self.left_frame)
        self.cam_label.pack(fill="both", expand=True)

        # Çekilen fotoğraf label
        self.captured_img_label = Label(self.left_frame)
        self.captured_img_label.pack(pady=5)

        # Buton
        self.snap_btn = Button(self.left_frame, text="📷 Fotoğraf Çek (R tuşu ile de)", command=self.fotograf_cek)
        self.snap_btn.pack(pady=10)

        # Arka plan kaldırılmış label ve image
        self.rembg_label = Label(self.middle_frame, text="Arka Plan Kaldırılmış", font=("Arial", 12))
        self.rembg_label.pack()
        self.rembg_img_label = Label(self.middle_frame)
        self.rembg_img_label.pack()

        # Yeni arka planla birleşmiş label ve image
        self.final_label = Label(self.right_frame, text="Yeni Arka Plan ile Birleşmiş", font=("Arial", 12))
        self.final_label.pack()
        self.final_img_label = Label(self.right_frame)
        self.final_img_label.pack()

        # Kamera aç
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            messagebox.showerror("Hata", "Kamera açılamadı! Kamera bağlı mı kontrol et.")
            root.destroy()
            return

        self.kamera_goruntusu()

        # Resim dosyaları için değişkenler
        self.kisi_resim_yolu = None
        self.rembg_img = None
        self.final_img = None

        # Klavye dinleme (R tuşu)
        self.root.bind("<r>", lambda event: self.fotograf_cek())
        self.root.bind("<R>", lambda event: self.fotograf_cek())

    def kamera_goruntusu(self):
        ret, frame = self.cap.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_rgb = cv2.resize(frame_rgb, (400, 400))
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)
            self.cam_label.imgtk = imgtk
            self.cam_label.configure(image=imgtk)
        self.root.after(15, self.kamera_goruntusu)

    def rastgele_arka_plan_sec(self):
        dosyalar = [f for f in os.listdir(B_KLASORU) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
        if not dosyalar:
            messagebox.showerror("Hata", f"{B_KLASORU} klasöründe arka plan yok!")
            return None
        return os.path.join(B_KLASORU, random.choice(dosyalar))

    def fotograf_cek(self):
        ret, frame = self.cap.read()
        if not ret:
            messagebox.showerror("Hata", "Kameradan görüntü alınamadı!")
            return

        filename = datetime.now().strftime("capture_%Y%m%d_%H%M%S.png")
        self.kisi_resim_yolu = os.path.join(A_KLASORU, filename)
        cv2.imwrite(self.kisi_resim_yolu, frame)

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb).resize((280, 280))
        imgtk = ImageTk.PhotoImage(image=img)
        self.captured_img_label.imgtk = imgtk
        self.captured_img_label.config(image=imgtk)

        messagebox.showinfo("Başarılı", "Resim çekildi, arka plan işlemi başlıyor...")

        self.arka_plan_islemleri()

        messagebox.showinfo("Bitti", "Resim oluştu ve kaydedildi!")

    def arka_plan_islemleri(self):
        arka_plan_path = self.rastgele_arka_plan_sec()
        if not arka_plan_path or not self.kisi_resim_yolu:
            return

        try:
            with open(self.kisi_resim_yolu, "rb") as f:
                input_image = f.read()

            output_image = remove(input_image)

            # Bytes -> PIL Image
            person = Image.open(io.BytesIO(output_image)).convert("RGBA")
            background = Image.open(arka_plan_path).convert("RGBA").resize(person.size)

            final = Image.alpha_composite(background, person)

            output_filename = datetime.now().strftime("output_%Y%m%d_%H%M%S.png")
            output_path = os.path.join(C_KLASORU, output_filename)
            final.save(output_path)

            self.rembg_img = ImageTk.PhotoImage(person.resize((280, 280)))
            self.rembg_img_label.config(image=self.rembg_img)

            self.final_img = ImageTk.PhotoImage(final.resize((280, 280)))
            self.final_img_label.config(image=self.final_img)
        

        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu:\n{e}")
        os.remove(self.kisi_resim_yolu)
        self.kisi_resim_yolu = None  # Silindikten sonra yol sıfırlansın


    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
