#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 23:03:43 2023

@author: emredikici
"""
from collections import deque

def bfs(graf, baslangic, hedef):
    # Bir kuyruk (queue) oluşturun ve başlangıç noktasını ekleyin
    kuyruk = deque()
    kuyruk.append((baslangic, []))  # Düğüm ve yol listesi tuple'ı

    # Ziyaret edilen düğümleri takip etmek için bir küme oluşturun
    ziyaret_edilen = set()
    ziyaret_edilen.add(baslangic)

    # Hedefe ulaşana kadar BFS ile arama yapın
    while kuyruk:
        dugum, yol = kuyruk.popleft()  # Düğümü ve yol listesini al

        # Hedefe ulaşıldı mı?
        if dugum == hedef:
            return yol + [dugum]  # Yolu döndür

        # Düğümün komşularını incele
        for komsu in graf[dugum]:
            if komsu not in ziyaret_edilen:
                yeni_yol = yol + [dugum]  # Yeni yol listesini oluştur
                kuyruk.append((komsu, yeni_yol))  # Kuyruğa ekleyin
                ziyaret_edilen.add(komsu)  # Ziyaret edildi olarak işaretleyin

    # Hedefe ulaşılamadı
    return None

# Başlangıç ve hedef noktalarını belirleyin
baslangic_noktasi = 'A'
hedef_noktasi = 'F'

# Grafı tanımlayın (örnek graf)
graf = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# BFS ile en kısa yolu arayın
en_kisa_yol = bfs(graf, baslangic_noktasi, hedef_noktasi)

if en_kisa_yol:
    print(f"{baslangic_noktasi} ile {hedef_noktasi} arasındaki en kısa yol: {en_kisa_yol}")
else:
    print(f"{baslangic_noktasi} ile {hedef_noktasi} arasında yol bulunamadı.")
