import json  # JSON formatında veri kaydetmek ve okumak için gerekli modül
import random  # Rastgele sayı üretmek için kullanılan modül
import pandas as pd  # Verileri işlemek ve analiz etmek için kullanılan kütüphane
import matplotlib.pyplot as plt  # Grafik çizmek için kullanılan kütüphane

# Sensör verisi oluşturma fonksiyonu
def sensör_verisi_olustur(num_records):
    """
    Bu fonksiyon belirtilen sayıda rastgele sensör verisi (sıcaklık ve nem) oluşturur.
    :param num_records: Üretilecek veri sayısı
    :return: Sensör verilerini içeren bir liste
    """
    sensör_verisi = []
    for _ in range(num_records):
        # Rastgele sıcaklık (20-40 derece arasında) ve nem (%30-%70 arasında) değerleri oluşturulur
        kayıt = {
            "sıcaklık": round(random.uniform(20, 40), 2),  # Sıcaklık değeri
            "nem": round(random.uniform(30, 70), 2)  # Nem değeri
        }
        sensör_verisi.append(kayıt)  # Her kaydı listeye ekle
    return sensör_verisi

# Verileri JSON dosyasına kaydetme fonksiyonu
def json_dosyasina_kaydet(veri, dosya_yolu):
    """
    Oluşturulan sensör verilerini bir JSON dosyasına kaydeder.
    :param veri: Kaydedilecek veri
    :param dosya_yolu: JSON dosyasının kaydedileceği dosya yolu
    """
    with open(dosya_yolu, "w") as json_dosya:
        json.dump(veri, json_dosya, indent=4)  # Verileri JSON formatında kaydet

# Verileri görselleştirme fonksiyonu
def sensör_verisini_gorsellestir(dosya_yolu):
    """
    JSON dosyasından sensör verilerini okuyarak grafiksel olarak görselleştirir.
    :param dosya_yolu: JSON dosyasının yolu
    """
    # JSON dosyasını oku ve bir DataFrame'e yükle
    sensör_verisi = pd.read_json(dosya_yolu)
    
    # Grafikler için çizim alanını ayarla
    plt.figure(figsize=(12, 6))
    
    # Sıcaklık verisi grafiği
    plt.subplot(2, 1, 1)  # İki grafik çizmek için 1. alt grafik
    plt.plot(sensör_verisi.index, sensör_verisi['sıcaklık'], label='Sıcaklık (°C)', color='red')
    plt.title('Sıcaklık Verileri')  # Grafiğin başlığı
    plt.xlabel('Kayıt İndeksi')  # X ekseni etiketi
    plt.ylabel('Sıcaklık (°C)')  # Y ekseni etiketi
    plt.legend()  # Etiketlerin görünmesi için
    plt.grid()  # Izgara çizgileri ekle

    # Nem verisi grafiği
    plt.subplot(2, 1, 2)  # İkinci alt grafik
    plt.plot(sensör_verisi.index, sensör_verisi['nem'], label='Nem (%)', color='blue')
    plt.title('Nem Verileri')  # Grafiğin başlığı
    plt.xlabel('Kayıt İndeksi')  # X ekseni etiketi
    plt.ylabel('Nem (%)')  # Y ekseni etiketi
    plt.legend()  # Etiketlerin görünmesi için
    plt.grid()  # Izgara çizgileri ekle

    # Grafiklerin daha iyi görünmesi için düzenleme
    plt.tight_layout()
    plt.show()

# Ana program bloğu
if __name__ == "__main__":
    # JSON dosyasının kaydedileceği dosya yolu
    json_dosya_yolu = "sensör_verisi.json"
    
    # 100 adet sensör verisi oluştur ve JSON dosyasına kaydet
    sensör_verisi = sensör_verisi_olustur(100)
    json_dosyasina_kaydet(sensör_verisi, json_dosya_yolu)
    
    # JSON dosyasından verileri oku ve görselleştir
    sensör_verisini_gorsellestir(json_dosya_yolu)