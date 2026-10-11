import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1" 

import customtkinter as ctk
from tkinter import filedialog
import threading
from faster_whisper import WhisperModel
import time

class KolayCeviriUygulamasi(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("650x700") 
        self.title("Kolay Çeviri Asistanı")
        ctk.set_appearance_mode("System") 
        
        self.secili_dosya = None
        
        self.sayac_aktif = False
        self.baslangic_zamani = 0
        
        self.diller = {
            "Otomatik Algıla": None,
            "Türkçe": "tr",
            "İngilizce": "en",
            "Almanca": "de",
            "Fransızca": "fr",
            "İspanyolca": "es",
            "Rusça": "ru",
            "Arapça": "ar"
        }
        
        self.title_label = ctk.CTkLabel(self, text="Ses ve Videoları Metne Çevirin", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=20)
        
        self.btn_select = ctk.CTkButton(self, text="📁 Dosya Seç", width=250, height=40, command=self.dosya_sec)
        self.btn_select.pack(pady=5)
        
        self.dosya_label = ctk.CTkLabel(self, text="Henüz dosya seçilmedi", text_color="gray")
        self.dosya_label.pack(pady=5)
        
        self.kalite_secim = ctk.CTkSegmentedButton(self, values=["Hızlı (Base)", "Dengeli (Small)", "İyi (Medium)", "Maksimum (Large)"])
        self.kalite_secim.set("Dengeli (Small)")
        self.kalite_secim.pack(pady=15)
        
        self.dil_label = ctk.CTkLabel(self, text="Konuşulan Dil:")
        self.dil_label.pack(pady=(5, 0))
        
        self.dil_secim = ctk.CTkOptionMenu(self, values=list(self.diller.keys()), width=200)
        self.dil_secim.set("Türkçe")
        self.dil_secim.pack(pady=5)
        
        self.btn_start = ctk.CTkButton(self, text="✨ Çeviriyi Başlat", fg_color="green", hover_color="darkgreen", command=self.ceviri_baslat)
        self.btn_start.pack(pady=15)
        
        self.sayac_label = ctk.CTkLabel(self, text="Geçen Süre: 00:00", font=("Arial", 14, "bold"), text_color="yellow")
        self.sayac_label.pack(pady=2)
        
        self.durum_label = ctk.CTkLabel(self, text="", font=("Arial", 12))
        self.durum_label.pack(pady=5)
        
        self.progress = ctk.CTkProgressBar(self, width=400, mode="indeterminate")
        self.progress.pack(pady=5)
        self.progress.set(0)
        
        self.sonuc_kutusu = ctk.CTkTextbox(self, width=550, height=150)
        self.sonuc_kutusu.pack(pady=10)
        self.sonuc_kutusu.configure(state="disabled")
        
        self.btn_save = ctk.CTkButton(self, text="💾 Sonucu .txt Olarak Kaydet", width=200, height=40, fg_color="#1f538d", command=self.metni_kaydet)
        self.footer_label = ctk.CTkLabel(self, text="Made By: ©VodeAn", font=("Arial", 18, "italic"), text_color="gray")
        self.footer_label.pack(side="bottom", pady=10)

    def dosya_sec(self):
        dosya_yolu = filedialog.askopenfilename(
            title="Medya seçin",
            filetypes=[("Medya Dosyaları", "*.mp3 *.wav *.mp4 *.m4a *.avi")]
        )
        if dosya_yolu:
            self.secili_dosya = dosya_yolu
            self.dosya_label.configure(text=f"Seçilen: {os.path.basename(dosya_yolu)}", text_color="white")

    def sayaci_guncelle(self):
        if self.sayac_aktif:
            gecen_saniye = int(time.time() - self.baslangic_zamani)
            dakika = gecen_saniye // 60
            saniye = gecen_saniye % 60
            
            self.sayac_label.configure(text=f"Geçen Süre: {dakika:02d}:{saniye:02d}")
            self.after(1000, self.sayaci_guncelle)

    def ceviri_baslat(self):
        if not self.secili_dosya:
            self.durum_label.configure(text="Lütfen önce bir dosya seçin!", text_color="red")
            return
            
        self.btn_start.configure(state="disabled")
        self.btn_select.configure(state="disabled")
        self.kalite_secim.configure(state="disabled")
        self.dil_secim.configure(state="disabled")
        
        self.btn_save.pack_forget() 
        
        self.sonuc_kutusu.configure(state="normal")
        self.sonuc_kutusu.delete("1.0", "end")
        self.sonuc_kutusu.configure(state="disabled")
        
        self.sayac_aktif = True
        self.baslangic_zamani = time.time()
        self.sayaci_guncelle()
        
        threading.Thread(target=self.arkaplan_ceviri, daemon=True).start()

    def saniye_cevir(self, saniye_degeri):
        saat = int(saniye_degeri // 3600)
        dakika = int((saniye_degeri % 3600) // 60)
        saniye = int(saniye_degeri % 60)
        return f"{saat:02d}:{dakika:02d}:{saniye:02d}"

    def arkaplan_ceviri(self):
        try:
            secim = self.kalite_secim.get()
            
            if "Base" in secim:
                model_boyutu = "base"
            elif "Small" in secim:
                model_boyutu = "small"
            elif "Medium" in secim:
                model_boyutu = "medium"
            else:
                model_boyutu = "large-v3"
            
            secilen_dil = self.dil_secim.get()
            dil_kodu = self.diller[secilen_dil]
            
            self.durum_label.configure(text="Yapay zeka motoru hazırlanıyor (İşlemci Modu)...", text_color="orange")
            self.progress.start()
            
            model = WhisperModel(model_boyutu, device="cpu", compute_type="int8")
            
            self.durum_label.configure(text=f"Ses işleniyor... (Dil: {secilen_dil})", text_color="lightblue")
            
            segments, info = model.transcribe(self.secili_dosya, beam_size=5, language=dil_kodu)
            
            if dil_kodu is None:
                self.sonuc_kutusu.configure(state="normal")
                self.sonuc_kutusu.insert("end", f"--- {info.language} dili tespit edildi ---\n\n")
                self.sonuc_kutusu.configure(state="disabled")
            
            for segment in segments:
                zaman = self.saniye_cevir(segment.start)
                metin = f"[{zaman}] {segment.text}\n"
                
                self.sonuc_kutusu.configure(state="normal")
                self.sonuc_kutusu.insert("end", metin)
                self.sonuc_kutusu.see("end")
                self.sonuc_kutusu.configure(state="disabled")
            
            self.durum_label.configure(text="Çeviri başarıyla tamamlandı!", text_color="green")
            self.btn_save.pack(pady=10)
            
        except Exception as e:
            self.durum_label.configure(text=f"Hata: {str(e)}", text_color="red")
        finally:
            self.progress.stop()
            self.btn_start.configure(state="normal")
            self.btn_select.configure(state="normal")
            self.kalite_secim.configure(state="normal")
            self.dil_secim.configure(state="normal")
            self.sayac_aktif = False

    def metni_kaydet(self):
        dosya_yolu = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Metin Dosyası", "*.txt")],
            title="Çeviriyi Kaydet",
            initialfile="Ceviri_Sonucu.txt"
        )
        
        if dosya_yolu:
            try:
                tum_metin = self.sonuc_kutusu.get("1.0", "end-1c")
                
                with open(dosya_yolu, "w", encoding="utf-8") as dosya:
                    dosya.write(tum_metin)
                    
                self.durum_label.configure(text="Dosya başarıyla bilgisayarınıza kaydedildi!", text_color="green")
            except Exception as e:
                self.durum_label.configure(text=f"Kaydetme Hatası: {str(e)}", text_color="red")

if __name__ == "__main__":
    app = KolayCeviriUygulamasi()
    app.mainloop()