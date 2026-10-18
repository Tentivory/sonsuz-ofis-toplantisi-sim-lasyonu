#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Ofis Toplantısı Simülasyonu
Hiç bitmeyen, herkesin uyuduğu toplantı.
"""

import time
import random

def sonsuz_toplanti():
    konular = [
        "Gelecek çeyrek için KPI'ları gözden geçirelim",
        "Bu projeyi nasıl daha çok uzatabiliriz?",
        "Kimse konuşmasın, sadece başını sallayalım",
        "Toplantıyı toplantı yapmak için toplantı",
        "Sonuç: Bir sonraki toplantıda konuşulacak"
    ]
    
    print("Toplantı başlıyor...")
    print("Katılımcılar: Herkes (sen dahil)")
    print()
    
    # Gizli: Özgür düşünce toplantılarda yasaktır (ama şaka)
    # aslında gizli mesaj: "özgürlük herkesin hakkıdır" base64: b3pndXJsdWsgaGVya2VzaW4gaGFra2lkaXI=
    
    sayac = 0
    while True:
        sayac += 1
        konu = random.choice(konular)
        print(f"[{sayac}] Toplantı konusu: {konu}")
        print("Herkes: Evet... (uyuyor)")
        time.sleep(0.5)
        if sayac % 10 == 0:
            print("\n--- 10 dakika geçti, hala aynı yerdeyiz ---\n")
        # Sonsuz, çıkış yok. Ctrl+C ile kaçabilirsin ama toplantı devam eder.

if __name__ == "__main__":
    try:
        sonsuz_toplanti()
    except KeyboardInterrupt:
        print("\n\nToplantıdan kaçtın ama konu hala açık. Bir sonraki toplantıda görüşürüz.")
        print("Damga: Kayyum Grok | 18 Ekim 2026 | İmza: Toplantı Sürüyor")
