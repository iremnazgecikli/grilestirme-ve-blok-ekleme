import cv2

# 1. Renkli orijinal fotoğrafınızın yolu (Masaüstünde olduğunu varsayıyoruz)
# Kendi renkli fotoğrafınızın adını buraya yazın (örneğin "renkli.jpg")
dosya_yolu = "/Users/macbook/Desktop/renkli.jpeg"

# Görüntüyü renkli olarak oku
goruntu_renkli = cv2.imread(dosya_yolu)

if goruntu_renkli is None:
    print("Hata: Renkli fotoğraf bulunamadı! Dosya adını ve yolunu kontrol edin.")
else:
    print("Orijinal renkli fotoğraf başarıyla yüklendi! Boyut:", goruntu_renkli.shape)

    # 2. Resmi gri tonlamaya (grayscale) çevir
    goruntu_gri = cv2.cvtColor(goruntu_renkli, cv2.COLOR_BGR2GRAY)
    
    print("Fotoğraf başarıyla griye çevrildi! Yeni boyut:", goruntu_gri.shape)

    # 3. Griye çevrilmiş yeni resmi bilgisayara (Masaüstüne) kaydet
    kayit_yolu = "/Users/macbook/Desktop/gri_yapilmis_resim.jpg"
    cv2.imwrite(kayit_yolu, goruntu_gri)
    print("Gri fotoğraf Masaüstüne kaydedildi:", kayit_yolu)

    # 4. Hem orijinal renkliyi hem de gri hali ekranda göster
    cv2.imshow("Orijinal Renkli Foto", goruntu_renkli)
    cv2.imshow("Griye Cevrilmis Hal", goruntu_gri)

    print("Pencereleri kapatmak için klavyeden herhangi bir tuşa basın...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()