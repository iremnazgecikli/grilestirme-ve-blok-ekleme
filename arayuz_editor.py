import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np

class GoruntuEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Görüntü İşleme Proje Editörü")
        self.root.geometry("450x600")
        
        self.root.attributes('-topmost', True)
        
        self.secilen_dosya_yolu = None
        self.orijinal_resim = None

        self.lbl_bilgi = tk.Label(root, text="Lütfen önce Görüntü Oku butonuna basın", fg="#d32f2f", font=("Arial", 10, "bold"))
        self.lbl_bilgi.pack(pady=10)

        self.btn_oku = tk.Button(root, text="1. Görüntü Oku", command=self.goruntu_oku, bg="#d4edda", fg="#152457", font=("Arial", 11, "bold"), relief="raised", bd=2)
        self.btn_oku.pack(pady=6, fill="x", padx=30)

        self.btn_gri = tk.Button(root, text="2. Griye Dönüştür", command=self.griye_cevir, bg="#d1ecf1", fg="#17899d", font=("Arial", 11, "bold"), relief="raised", bd=2)
        self.btn_gri.pack(pady=6, fill="x", padx=30)

        self.btn_blok = tk.Button(root, text="3. Sol Üst & Sağ Alt 10x10 Blok", command=self.blok_ekle, bg="#fff3cd", fg="#048513", font=("Arial", 11, "bold"), relief="raised", bd=2)
        self.btn_blok.pack(pady=6, fill="x", padx=30)

        self.btn_dpi = tk.Button(root, text="4. DPI / Çözünürlüğü Yarıya Düşür", command=self.dpi_dusur, bg="#f8d7da", fg="#721c24", font=("Arial", 11, "bold"), relief="raised", bd=2)
        self.btn_dpi.pack(pady=6, fill="x", padx=30)

        self.lbl_bit = tk.Label(root, text="Gri Seviye (Bit) Dönüşümleri", fg="#333333", font=("Arial", 9, "bold"))
        self.lbl_bit.pack(pady=(10, 2))

        frame_bit = tk.Frame(root)
        frame_bit.pack(pady=5)

        self.btn_256 = tk.Button(frame_bit, text="256 Bit", command=lambda: self.bit_donustur(256), bg="#e2e3e5", fg="#383d41", font=("Arial", 9, "bold"), width=8)
        self.btn_256.pack(side="left", padx=4)

        self.btn_64 = tk.Button(frame_bit, text="64 Bit", command=lambda: self.bit_donustur(64), bg="#e2e3e5", fg="#383d41", font=("Arial", 9, "bold"), width=8)
        self.btn_64.pack(side="left", padx=4)

        self.btn_16 = tk.Button(frame_bit, text="16 Bit", command=lambda: self.bit_donustur(16), bg="#e2e3e5", fg="#383d41", font=("Arial", 9, "bold"), width=8)
        self.btn_16.pack(side="left", padx=4)

        self.btn_2 = tk.Button(frame_bit, text="2 Bit", command=lambda: self.bit_donustur(2), bg="#e2e3e5", fg="#383d41", font=("Arial", 9, "bold"), width=8)
        self.btn_2.pack(side="left", padx=4)

    def goruntu_oku(self):
        dosya = filedialog.askopenfilename(title="Bir Görüntü Seçin", filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        if dosya:
            self.secilen_dosya_yolu = dosya
            self.orijinal_resim = cv2.imread(self.secilen_dosya_yolu)
            if self.orijinal_resim is not None:
                h, w, _ = self.orijinal_resim.shape
                self.lbl_bilgi.config(text=f"Seçilen dosya ({w}x{h})", fg="#155724")
                print(f"Basariyla okundu: {self.secilen_dosya_yolu} | Boyut: {w}x{h}")
                cv2.imshow("Secilen Orijinal Goruntu", self.orijinal_resim)
                cv2.waitKey(1)
            else:
                self.lbl_bilgi.config(text="Hata: Resim okunamadı!", fg="#d32f2f")
        else:
            print("Dosya secme islemi iptal edildi.")

    def griye_cevir(self):
        if self.orijinal_resim is None:
            self.lbl_bilgi.config(text="Önce görüntü seçmelisiniz!", fg="#d32f2f")
            print("Uyari: Once bir görüntü okumalisiniz!")
            return
        gri_resim = cv2.cvtColor(self.orijinal_resim, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("/Users/macbook/Desktop/arayuz_gri_resim.jpg", gri_resim)
        print("Gri resim masaüstüne kaydedildi.")
        cv2.imshow("Griye Donusturulmus", gri_resim)
        cv2.waitKey(1)

    def blok_ekle(self):
        if self.orijinal_resim is None:
            self.lbl_bilgi.config(text="Önce görüntü seçmelisiniz!", fg="#d32f2f")
            print("Uyari: Once bir görüntü okumalisiniz!")
            return
        yeni_goruntu = self.orijinal_resim.copy()
        h, w, _ = yeni_goruntu.shape
        yeni_goruntu[50:60, 50:60] = [255, 255, 255] 
        yeni_goruntu[h-70:h-60, w-70:w-60] = [255, 255, 255]
        cv2.imwrite("/Users/macbook/Desktop/arayuz_kose_bloklu.jpg", yeni_goruntu)
        print("Fotografa bloklar eklendi.")
        cv2.imshow("10x10 Beyaz Bloklar", yeni_goruntu)
        cv2.waitKey(1)

    def dpi_dusur(self):
        if self.orijinal_resim is None:
            self.lbl_bilgi.config(text="Önce görüntü seçmelisiniz!", fg="#d32f2f")
            print("Uyari: Once bir görüntü okumalisiniz!")
            return
        h_orijinal, w_orijinal, _ = self.orijinal_resim.shape
        yeni_genislik = w_orijinal // 2
        yeni_yukseklik = h_orijinal // 2
        dusuk_dpi_resim = cv2.resize(self.orijinal_resim, (yeni_genislik, yeni_yukseklik), interpolation=cv2.INTER_LINEAR)
        self.lbl_bilgi.config(text=f"DPI Dusuruldu: {yeni_genislik}x{yeni_yukseklik}", fg="#721c24")
        print(f"Yeni Çözünürlük: {yeni_genislik}x{yeni_yukseklik}")
        cv2.imwrite("/Users/macbook/Desktop/arayuz_dpi_dusuk.jpg", dusuk_dpi_resim)
        cv2.imshow("DPI Dusurulmus Goruntu", dusuk_dpi_resim)
        cv2.waitKey(1)

    def bit_donustur(self, seviye):
        if self.orijinal_resim is None:
            self.lbl_bilgi.config(text="Önce görüntü seçmelisiniz!", fg="#d32f2f")
            print("Uyari: Once bir görüntü okumalisiniz!")
            return
        
        gri = cv2.cvtColor(self.orijinal_resim, cv2.COLOR_BGR2GRAY)
        faktor = 256 // seviye
        yeni_gri = (gri // faktor) * faktor
        
        self.lbl_bilgi.config(text=f"Görüntü {seviye} Seviye Yapıldı", fg="#17899d")
        print(f"Goruntu {seviye} seviye gri tona dönüştürüldü.")
        
        dosya_adi = f"/Users/macbook/Desktop/arayuz_{seviye}_seviye.jpg"
        cv2.imwrite(dosya_adi, yeni_gri)
        
        cv2.imshow(f"Gri Seviye - {seviye} Bit", yeni_gri)
        cv2.waitKey(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = GoruntuEditorApp(root)
    root.mainloop()
    