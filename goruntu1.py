import cv2

# Masaüstündeki fotoğrafın yolu
dosya_yolu = "/Users/macbook/Desktop/gri.jpeg"

goruntu = cv2.imread(dosya_yolu)

if goruntu is None:
    print("Hata: Fotoğraf bulunamadı! Dosya masaüstünde ve adı 'gri.jpeg' mi kontrol et.")
else:
    print("Harika! Fotoğraf başarıyla yüklendi. Boyutu:", goruntu.shape)

    # Fotoğrafı ekranda göster
    cv2.imshow("Gri Goruntu", goruntu)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()