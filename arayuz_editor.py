import tkinter as tk
from tkinter import filedialog, ttk
import cv2
import numpy as np

class GoruntuEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Görüntü İşleme Proje Editörü")
        self.root.geometry("450x420")
        
        self.secilen_dosya_yolu = None
        self.orijinal_resim = None

        # Ana Başlık 
        self.lbl_bilgi = tk.Label(root, text="Lütfen önce '1. Görüntü Oku' butonuna basın", fg="#d32f2f", font=("Arial", 10, "bold"))
        self.lbl_bilgi.pack(pady=10)

        # Sekme (Notebook) Yapısı Oluşturma
        notebook = ttk.Notebook(root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # İşlem Sekmesi
        self.islem_sekmesi = ttk.Frame(notebook)
        notebook.add(self.islem_sekmesi, text="İşlemler")

        # --- SEKME İÇİNDEKİ BUTONLAR ---

        self.btn_oku = tk.Button(self.islem_sekmesi, text="1. Görüntü Oku", command=self.goruntu_oku, bg="#d4edda", fg="#152457", font=("Arial", 11, "bold"), relief="raised", bd=2)
        self.btn_oku.pack(pady=15, fill="x", padx=30)

        self.btn_gri = tk.Button(self.islem_sekmesi, text="2. Griye Dönüştür", command=self.griye_cevir, bg="#d1ecf1", fg="#17899d", font=("Arial", 11, "bold"), relief="raised", bd=2)
        self.btn_gri.pack(pady=15, fill="x", padx=30)

        self.btn_blok = tk.Button(self.islem_sekmesi, text="3. Sol Üst & Sağ Alt 10x10 Blok", command=self.blok_ekle, bg="#fff3cd", fg="#048513", font=("Arial", 11, "bold"), relief="raised", bd=2)
        self.btn_blok.pack(pady=15, fill="x", padx=30)

    def goruntu_oku(self):
        dosya = filedialog.askopenfilename(title="Bir Görüntü Seçin", filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        
        if dosya:
            self.secilen_dosya_yolu = dosya
            self.orijinal_resim = cv2.imread(self.secilen_dosya_yolu)
            
            if self.orijinal_resim is not None:
                self.lbl_bilgi.config(text=f"Seçilen Dosya: {dosya.split('/')[-1]}", fg="#155724")
                print(f"Başarıyla okundu: {self.secilen_dosya_yolu}")
                
                cv2.imshow("Secilen Orijinal Goruntu", self.orijinal_resim)
                cv2.waitKey(1)
            else:
                self.lbl_bilgi.config(text="Hata: Resim okunamadı!", fg="#d32f2f")
        else:
            print("Dosya seçme işlemi iptal edildi.")

    def griye_cevir(self):
        if self.orijinal_resim is None:
            self.lbl_bilgi.config(text="Önce 1. butona basıp görüntü seçmelisiniz!", fg="#d32f2f")
            print("Uyarı: Önce bir görüntü okumalısınız!")
            return
        
        gri_resim = cv2.cvtColor(self.orijinal_resim, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("/Users/macbook/Desktop/arayuz_gri_resim.jpg", gri_resim)
        print("Gri resim masaüstüne kaydedildi.")
        
        cv2.imshow("Griye Donusturulmus", gri_resim)
        cv2.waitKey(1)

    def blok_ekle(self):
        if self.orijinal_resim is None:
            self.lbl_bilgi.config(text="Önce 1. butona basıp görüntü seçmelisiniz!", fg="#d32f2f")
            print("Uyarı: Önce bir görüntü okumalısınız!")
            return
        
        # Orijinal resmi bozmamak için kopyasını alalım
        yeni_goruntu = self.orijinal_resim.copy()
        h, w, _ = yeni_goruntu.shape
        
        # Sol üst tarafa doğru 10x10'luk beyaz kare
        yeni_goruntu[50:60, 50:60] = [255, 255, 255] 
        
        # Sağ alt tarafa doğru 10x10'luk beyaz kare
        yeni_goruntu[h-70:h-60, w-70:w-60] = [255, 255, 255]
        
        # Masaüstüne kaydedelim 
        cv2.imwrite("/Users/macbook/Desktop/arayuz_kose_bloklu.jpg", yeni_goruntu)
        print("Fotoğrafın içine 2 adet 10x10 beyaz blok eklendi.")
        
        # Yeni ekranda göster
        cv2.imshow("Ic Kisimda 10x10 Beyaz Bloklar", yeni_goruntu)
        cv2.waitKey(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = GoruntuEditorApp(root)
    root.mainloop()

    