# 🎙️ Kolay Çeviri Asistanı

**Kolay Çeviri Asistanı**, herhangi bir teknik bilgiye ihtiyaç duymadan ses ve video dosyalarınızı yüksek doğrulukla metne dönüştürmenizi sağlayan, yapay zeka tabanlı bir masaüstü uygulamasıdır. 

Bu uygulama, özellikle **akademisyen arkadaşlarımın** mülakat, odak grup görüşmesi, ders veya toplantı kayıtlarını metne dökerken (deşifre/transkripsiyon) yaşadıkları zaman kaybını önlemek ve iş yüklerini hafifletmek amacıyla özel olarak tasarlanmıştır. **Şimdilik sadece Windows işletim sistemlerini desteklemektedir.**

Arka planda gücünü OpenAI'ın gelişmiş konuşma tanıma modeli olan Whisper'ın modernize edilmiş versiyonu **Faster-Whisper**'dan alır. Karmaşık terminal komutlarıyla uğraşmak istemeyen son kullanıcılar için özel olarak tasarlanmıştır. Tamamen çevrimdışı (internetsiz) çalışır.

---

## ✨ Öne Çıkan Özellikler

*   **Çoklu Format Desteği:** Popüler ses ve video formatlarını (.mp3, .wav, .mp4, .m4a, .avi) doğrudan okuyabilir.
*   **Esnek Yapay Zeka Modelleri:** İhtiyacınıza göre performansı ayarlayın. 
    *   *Hızlı (Base):* Anında sonuç almak için.
    *   *Dengeli (Small):* Günlük çeviriler için ideal.
    *   *İyi (Medium):* Yüksek doğruluk isteyenler için.
    *   *Maksimum (Large):* En zorlu sesleri bile kusursuz metne döken gelişmiş model.
*   **Akıllı Dil Tanıma:** Konuşulan dili (İngilizce, Türkçe, Almanca vb.) otomatik tespit edebilir veya dil menüsünden manuel seçim yapabilirsiniz.
*   **Dinamik Süre Takibi:** Çeviri sürecinde geçen süreyi (HH:MM:SS formatında) canlı olarak gösterir.
*   **Sonucu Dışa Aktarma:** Çeviri bittiğinde tek tıkla sonucu .txt dosyası olarak bilgisayarınıza kaydedebilirsiniz.
*   **Donanım Dostu:** Bilgisayarında ekran kartı olmayan (veya NVIDIA kullanmayan) kullanıcıların çökme yaşamaması için özel olarak optimize edilmiş İşlemci (CPU) çalışma moduna sahiptir.

---

## 🚀 Son Kullanıcılar İçin Kurulum (Tek Tıkla Çalıştır)

Eğer kodlarla uğraşmak istemiyor ve programı standart bir Windows uygulaması gibi bilgisayarınıza kurmak istiyorsanız, aşağıdaki bağlantıdan hazırladığım Setup dosyasını indirebilirsiniz:

📥 **[Programı İndirmek İçin Buraya Tıklayın]**

1. Linkten KolayCeviriSetup.exe dosyasını indirin.
2. Çift tıklayarak kurulum adımlarını izleyin.
3. Masaüstündeki kısayoldan uygulamayı başlatın ve çevirinin tadını çıkarın!

*(Not: Uygulama şimdilik sadece Windows cihazlarda çalışmaktadır. Mac kullanıcıları için henüz derlenmemiştir.)*

---

## 💻 Geliştiriciler İçin Çalıştırma Kılavuzu

Projeyi kendi bilgisayarınızda derlemek veya kodları incelemek isterseniz aşağıdaki adımları izleyebilirsiniz.

### Gereksinimler
*   Python 3.8 veya üzeri
*   FFmpeg (Sistem PATH'ine eklenmiş olmalıdır)

### Kurulum Adımları

**1. Depoyu Klonlayın:**
git clone https://github.com/VodeAn/Kolay-Ceviri-Asistani.git
cd Kolay-Ceviri-Asistani

**2. Sanal Ortam Oluşturun ve Aktif Edin:**
python -m venv venv
venv\Scripts\activate

**3. Gerekli Kütüphaneleri Yükleyin:**
pip install customtkinter faster-whisper

**4. Uygulamayı Başlatın:**
python main.py

> Geliştirici Notu: main.py içerisinde donanım uyumsuzluklarını önlemek adına os.environ["CUDA_VISIBLE_DEVICES"] = "-1" kullanılarak motor zorunlu CPU moduna alınmıştır. NVIDIA ekran kartına sahip bir geliştirici ortamındaysanız bu satırı kaldırıp model yükleme parametrelerini device="cuda" olarak güncelleyebilirsiniz.

---

## 🛠️ Kullanılan Teknolojiler
*   **Arayüz (GUI):** CustomTkinter
*   **Yapay Zeka Motoru:** Faster-Whisper (CTranslate2)
*   **Programlama Dili:** Python 3

---
*Made By: ©VodeAn*
