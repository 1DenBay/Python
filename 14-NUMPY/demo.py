import numpy as np

result = np.array([10,15,30,45]) #dizi
result = np.arange(5,15) #aralıkta dizi oluşturma
result = np.arange(5,15,3) #3er 3er giderek aralıkta
result = np.zeros(10) #sıfırlardan 10 elemanlk
result = np.ones(5) #1lerden oluşan
result = np.linspace(0,100,5) #5 eşit parçalı dizi
result = np.random.randint(10,30,5) #5 adet aralıkta rastgele sayı
result = np.random.randn(10) #-1 1 arası rastgele sayılar
result = np.random.randint(10,50,15).reshape(3,5) #10-50 arası 3,5lik matris için 15 eleman lazım olduğundan önce elemanları oluştur sonra matrise çevir

matris = np.random.randint(10,50,15).reshape(3,5) #3x5lik matrisimiz
rowtotal = matris.sum(axis=1) #satır toplamları
coltotal = matris.sum(axis=0) #sütun toplamları
result = matris.max() #max eleman
result = matris.min() #min elaman
result = matris.mean() #ortalama
result = matris.argmax() #max elemanın indeksi "arg" ile bulunur

arr = np.arange(10,20)
result = arr[0:3] #dizinin ilk 3 elemanını seçme

result = matris[0] #matrisin ilk satırı seçer
result = matris[1,2] #2.satırın üçüncü sütunu seçilir
result = matris[:,0] #tüm satırdaki ilk elemanları seçer
result = matris ** 2 #tüm elemanların karesini alır



print(result)