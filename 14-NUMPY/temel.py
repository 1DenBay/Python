#numpy , büyük listeleri daha hızlı ve kolay işlenmesini sağlar
#normal listelere göre daha hızlı ve kullanışlı olmasının sebebi :
#veriler tek tiptir (float yada int) , C ve Fortran gibi makine diline en yakın dillerde yazıldığından çok hızlıdır
#eleman bazında işlemleri doğrudan yapabilir toplama için filan döngülere gerek yok, bellekte kesintisiz bir blokta saklanır normal listelerde her eleman farklı yerlerde olabiliyordu
#numpy genellikle bi iş yaparken başlangıçta kullanılır verileri düzenleme , matrisleri oluşturup toplarlama gibi ön düzeni sağlamada kullanılır

import numpy as np

numbers = np.array([0,5,10,15,20,25,40])

result = numbers[::] #herkesi yazdırır
result = numbers [3:] #3 dahil indeksten sona kadar yazdırır

numbers2 = np.array([5,10,15],[20,25,30],[35,40,45]) #içeride ki her bir köşeli satır olarak adlandırılır ve kendi indeksleri vardır
#matriks
result = numbers2[0,2] #0. satırdaki 2. indeks elemanı
result = numbers2[:,2] #tüm satırlardaki 2. indeks elemanları
result = numbers2[:,0:2] #tüm satırlardaki 0dahil ile 2hariç indeks elemanları

