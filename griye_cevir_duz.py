import cv2

# Dosya yolu
dosya_yolu = "/Users/macbook/Desktop/renkli.jpeg"

# Görüntüyü oku
renkli_resim = cv2.imread(dosya_yolu)

if renkli_resim is None:
    print("Hata: Fotoğraf bulunamadı!")

else:
    # Görüntünün yüksekliğini ve genişliğini al
    yukseklik = renkli_resim.shape[0]
    genislik = renkli_resim.shape[1]

    # Gri görüntü için renkli görüntünün kopyasını oluştur
    gri_resim = renkli_resim.copy()

    # Bütün pikselleri tek tek dolaş
    for y in range(yukseklik):
        for x in range(genislik):

            # BGR değerlerini al
            B = renkli_resim[y, x][0]
            G = renkli_resim[y, x][1]
            R = renkli_resim[y, x][2]

            # Gri değeri kendimiz hesaplıyoruz
            gri = int(0.114 * B + 0.587 * G + 0.299 * R)

            # Pikseli gri yap
            gri_resim[y, x][0] = gri
            gri_resim[y, x][1] = gri
            gri_resim[y, x][2] = gri

    # Gri resmi kaydet
    cv2.imwrite(
        "/Users/macbook/Desktop/gri_yapilmis_resim.jpeg",
        gri_resim
    )

    print("Gri fotoğraf başarıyla oluşturuldu ve kaydedildi!")

    # Ekranda göster
    cv2.imshow("Gri Hali", gri_resim)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
