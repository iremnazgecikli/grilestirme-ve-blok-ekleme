import cv2

# Dosya yolu (Kendi masaüstünüzdeki resim adı ile aynı olduğundan emin olun)
dosya_yolu = "/Users/macbook/Desktop/renkli.jpeg"

# Görüntüyü oku
renkli_resim = cv2.imread(dosya_yolu)

if renkli_resim is None:
    print("Hata: Fotoğraf bulunamadı!")
else:
    # Fonksiyon kullanmadan doğrudan OpenCV ile griye çevir
    gri_resim = cv2.cvtColor(renkli_resim, cv2.COLOR_BGR2GRAY)
    
    # Masaüstüne kaydet
    cv2.imwrite("/Users/macbook/Desktop/gri_yapilmis_resim.jpeg", gri_resim)
    print("Gri fotoğraf başarıyla oluşturuldu ve kaydedildi!")

    # Ekranda göster
    cv2.imshow("Fonksiyonsuz Gri Hali", gri_resim)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
