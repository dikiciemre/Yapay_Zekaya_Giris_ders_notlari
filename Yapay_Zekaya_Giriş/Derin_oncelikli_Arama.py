#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 23:09:44 2023

@author: emredikici
"""
def dfs(graf, baslangic, hedef, ziyaret_edilen=None, yol=None):
    if ziyaret_edilen is None:
        ziyaret_edilen = []
    if yol is None:
        yol = []

    ziyaret_edilen.append(baslangic)  # Düğümü ziyaret edilmiş olarak işaretle
    yol.append(baslangic)  # Yolu güncelle, şu anki düğümü ekleyin

    if baslangic == hedef:
        return yol  # Hedef düğüme ulaşıldıysa yolu döndür

    if baslangic not in graf:
        return None  # Başlangıç düğümü grafi içinde bulunmuyorsa, yol yok

    for komsu in graf[baslangic]:
        if komsu not in ziyaret_edilen:
            yeni_yol = dfs(graf, komsu, hedef, ziyaret_edilen.copy(), yol.copy())  # Yeni yol oluştur
            if yeni_yol:
                return yeni_yol  # Yolu bulduğumuzda dön

    return None  # Hedef düğüme ulaşılamadıysa, yol yok

# Başlangıç ve hedef düğümleri belirleyin
baslangic_dugumu = 'A'
hedef_dugumu = 'F'

# Örnek grafı tanımlayın
graf = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# DFS ile yolu bulun
ziyaret_edilen = []  # Ziyaret edilen düğümleri izlemek için liste
sonuc = dfs(graf, baslangic_dugumu, hedef_dugumu, ziyaret_edilen)

if sonuc:
    print(f"{baslangic_dugumu} ile {hedef_dugumu} arasındaki yol: {' -> '.join(sonuc)}")
else:
    print(f"{baslangic_dugumu} ile {hedef_dugumu} arasında yol bulunamadı.")
