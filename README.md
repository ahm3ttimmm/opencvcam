# 🚀📸 ESP32 OpenCV Kamera ile Akıllı Arka Plan Değiştirici Projesi 🎨✨

> Bilgisayar CPU’sunu kullanan Python/OpenCV tabanlı arka plan değiştirme uygulamasının, ESP32’ye özel optimize edilmiş, gövdeyi gerçek zamanlı ayırıp arka planı değiştirmenizi sağlayan hafif versiyonu.

---

## 🔍 Proje Hakkında

### 🎯 Amaç  
ESP32 kamera modülü ile gerçek zamanlı görüntü yakalama, görüntüden kişiyi ayırma ve arka planı önceden belirlenmiş farklı arka planlarla dinamik şekilde değiştirme. Böylece gövde ve arka plan ayrı ayrı yönetilerek etkileyici görsel deneyimler oluşturuluyor.

### 💻 Orijinal Kod  
Python, OpenCV ve `rembg` kütüphanesi ile CPU tabanlı olarak geliştirilmiş, ESP32 için özel optimizasyonlarla hafifletilip gömülü ortama uyarlanmıştır.

---

## ⚙️ Özellikler

- 🎥 Gerçek zamanlı kamera görüntüsü yakalama  
- 📸 Fotoğraf çekip arka plan kaldırma  
- 🎨 Arka planı rastgele önceden yüklenmiş görseller arasından seçme  
- 🖼 Yeni arka plan ile görüntüyü kusursuz şekilde birleştirme ve kaydetme  
- ⚡ ESP32 için düşük güç tüketimli, performans optimize edilmiş hafif yapı  

---

## 🛠 Gereksinimler

### 🖥 Donanım  
- 📷 ESP32 Kamera Modülü (örn. ESP32-CAM)  
- 🔌 USB kablo ve PC bağlantısı  

### 🧑‍💻 Yazılım  
- 🛠 Arduino IDE veya PlatformIO (ESP32 destekli)  
- 🧩 OpenCV (geliştirme ve prototip için)  
- ⚙️ Hafif arka plan kaldırma algoritmaları (ESP32 için Python `rembg` çalışmaz)  
- 🐍 Python 3.x (orijinal CPU tabanlı kod için)  
- 🔄 ESP32 kodu C++ veya MicroPython ile yeniden yazılmalı  

---

## 🚀 Kurulum & Kullanım

1. **🛠 ESP32 Ortamını Hazırla**  
   Arduino IDE veya PlatformIO’da ESP32 kütüphanelerini kur.

2. **📝 Kod Uyarlaması**  
   Python’daki arka plan kaldırma algoritmasını, ESP32 uyumlu C++/MicroPython koduna dönüştür.  
   Kamera ve görüntü işleme fonksiyonları ESP32 donanımına göre optimize edilmeli.

3. **🖼 Arka Plan Görselleri**  
   Önceden ESP32 hafızasına veya SD karta yüklenmiş arka plan dosyaları kullanılacak.

4. **▶️ Çalıştır**  
   ESP32’yi programla ve canlı kamera görüntüsünde arka plan değiştirmeyi deneyimle.

---

## ⚠️ Dikkat Edilmesi Gerekenler

- 🧠 ESP32’nin sınırlı işlem gücü gerçek zamanlı karmaşık arka plan kaldırmayı zorlaştırır.  
- ⚡ Hafif ve basit algoritmalar (renk segmentasyonu, hareket farkı vb.) tercih edilmeli.  
- 🐍 `rembg` gibi Python bağımlı kütüphaneler ESP32’de çalışmaz; alternatif çözümler geliştirilmelidir.

---

## 🌟 Gelecek Planlar

- 🤖 TinyML ile model tabanlı gerçek zamanlı arka plan kaldırma  
- 🎞 Video akışı üzerinde arka plan değiştirme desteği  
- 🌐 Web arayüzü ile cihaz kontrolü ve görüntü yönetimi  

---

## 📚 Kaynaklar & Referanslar

- [📄 ESP32-CAM Resmi Dokümantasyon](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/camera.html)  
- [🐍 rembg GitHub](https://github.com/danielgatis/rembg)  
- 🖥 OpenCV Embedded Cihazlar İçin Eğitimler  
- 🐍 Python Arka Plan Kaldırma Örnekleri  

---

## 📬 İletişim

Proje, öneri ve sorularınız için:  
**Ahmet Şahin Özpınar- Bilişim Teknolojileri Öğrencisi** 🚀
