import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# --- GENEL AYARLAR ---
st.set_page_config(page_title="Yapay Zeka Tahmin Motoru", layout="vertical")

# ==========================================
# 🔑 API ANAHTARLARINI BURAYA YAPIŞTIR
# ==========================================
API_FOOTBALL_KEY = "d4be5781f43029d921541da6ad9e8c2f"
THE_ODDS_API_KEY = "5221541f38aa190acd130e139dd67026"
OPENWEATHER_KEY = "5d9c4ce7342462761d635f8ddfb1f4d8"
# ==========================================

# --- MARKET VE API EŞLEŞTİRME SÖZLÜĞÜ (DATA DICTIONARY) ---
market_dict = {
    "h2h": {"isim": "Maç Sonucu", "kategori": "Ana"},
    "team_shots_on_target": {"isim": "Takım İsabetli Şut", "kategori": "Aksiyon"},
    "team_total_corners": {"isim": "Takım Toplam Korner", "kategori": "Aksiyon"},
    "player_shots_on_target": {"isim": "Oyuncu İsabetli Şut", "kategori": "Oyuncu"}
}

# --- YAPAY ZEKA RAPOR OLUŞTURUCU ---
def generate_ai_report(mac_verisi, secilen_bahis, oyuncu_verisi, taktik_verisi):
    market_adi = market_dict[secilen_bahis['anahtar']]['isim']
    rapor_metni = f"""
    ### 🤖 YAPAY ZEKA KARAR GEREKÇESİ
    **Neden {mac_verisi['takim']} {market_adi} Bareminde Değer (Value) Görüldü?**
    
    Bu yatırım kararı, {mac_verisi['rakip_takim']} takımının {taktik_verisi['zayif_bolge']} bölgesindeki savunma zaafiyetleri ile {mac_verisi['takim']} takımının hücum xG (Beklenen Gol) verilerinin çarpıştırılmasıyla alınmıştır.
    
    * **Oyuncu/Bölge Eşleşmesi:** {oyuncu_verisi['isim']} performans göstergesi {oyuncu_verisi['istatistik']} seviyesindedir. Rakibin yüksek PPDA (ön alan baskısı) uygulaması, bu alanda geniş koridorlar açacaktır.
    * **Piyasa Oran Dalgalanması:** Asya piyasalarında açılış oranı {secilen_bahis['acilis_oran']} seviyesindeyken, akıllı para girişiyle ana bürolarda oran {secilen_bahis['kapanis_oran']} seviyesine düşmüştür. Modelimiz, bu matematiksel açıklığı **%{secilen_bahis['guven_skoru']} güven skoruyla** sisteme kilitlemiştir.
    """
    return rapor_metni

# --- ARAYÜZ (FRONT-END) ---
st.title("🏆 Dünya Kupası Yapay Zeka Analiz Paneli")
st.subheader("Maç Öncesi (T-60) Gelişmiş Raporlama Ekranı")

if st.button("🔄 BÜLTENİ VE ANALİZLERİ GÜNCELLE"):
    with st.spinner("Mikro istatistikler işleniyor, Asya piyasası taranıyor..."):
        
        # Gelecekte API'lerden gelecek verilerin Demo Simülasyonu
        ornek_mac = {"takim": "İngiltere", "rakip_takim": "Brezilya"}
        ornek_bahis = {"anahtar": "player_shots_on_target", "acilis_oran": 2.10, "kapanis_oran": 1.75, "guven_skoru": 88}
        ornek_oyuncu = {"isim": "Jude Bellingham (10 Numara Pozisyonu)", "istatistik": "maç başına 2.1 isabetli şut"}
        ornek_taktik = {"zayif_bolge": "sol bek savunma arkası"}
        
        rapor = generate_ai_report(ornek_mac, ornek_bahis, ornek_oyuncu, ornek_taktik)
        
        # Çıktıyı Ekrana Basma
        st.success("📊 Veri Madenciliği Tamamlandı! Güncel Liste Filtrelendi.")
        
        st.info("🟢 **[GÜVEN: %88]** İngiltere - Brezilya | Önerilen Bahis: **İngiltere Toplam İsabetli Şut 4.5 Üst** (Sınıf 1 Fırsat)")
        
        # Detaylı raporu genişletilebilir bir kutu içine alıyoruz
        with st.expander("📝 Detaylı Yapay Zeka Analiz Raporunu Oku", expanded=True):
            st.markdown(rapor)
        
        st.warning("🟡 **[GÜVEN: %74]** Arjantin - Fransa | Önerilen Bahis: **İlk Yarı 4.5 Korner Üst** (Sınıf 2 Dengeli)")
else:
    st.write("Sistemi çalıştırmak için yukarıdaki 'Güncelle' butonuna basın.")
