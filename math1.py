import math
x=21
y=9
z=-3622
math.ceil(1.6) #ondalıklı sayıyı, üst tam sayıya yuvarlar

math.copysign(x,y) #aldığı iki değerin ikincisinin işaretini birinciye verir

math.fabs(z) #parametre olarak verilen sayının mutlak değerini alır. sonucu float olarak döndürür

math.factorial(x) #bir değerin faktöriyelini alır. değer pozitif olmak zorundadır

math.floor(1.4) #bir ondalıklı tam sayıyı en yakın alt tam sayıya yuvarlar

math.fmod(x,y) #ilk parametrenin ikinci parametreden bölümünden kalanı vermektedir

math.frexp(x) # bu fonksiyon "x=m*2**e" işleminin m ve e parametrelerini bulmaya yarıyor

math.fsum([1.55,1.45]) #bu fonksiyon sum() gibi verilen değerlerin toplamını buluyor fakat sum fonksiyonu ondalıklı sayılarda işlem yaparken fsum fonksiyonu virgülden sonraki tek haneyi alıyor

math.gcd(x,y) #parametre olarak verilen 2 sayının ebobunu bulur

math.isclose(x,y) #parametre olarak verilen 2 sayının birbirine yakın olup olmadığını kontrol eder

math.modf(x) #parametre olarak verilen değerin kesirli ve tam sayı kısımlarını döndürür

math.trunc(1.6) #sadece tam sayıyı döndürür

#SABİTLER

math.pi #pi sayısını döndürür

math.e #euler sayısını döndürür

math.tau #tau sayısının değerini verir. tau sayısı pi sayısının 2 katıdır

#üslü sayılar ve logaritmik fonksiyonlar
math.exp(y) #euler sayısının y üssünü alır

math.expm1(y) #exp fonksiyonun aynısı, sadece sonuçtan 1 çıkarır

math.log(x,y) #parametre olarak verilen ilk değerin, ikinci değere göre logaritmasını hesaplar

math.log1p(x) #parametre olarak verilen sayıyı 1 ile toplayıp e tabanına göre logaritmasını hesaplar 1+x(taban e)'nin logaritması

math.log2(y) #parametre olarak verilen sayının 2 tabanına göre logaritmasını hesaplar

math.log10(y) #parametre olarak verilen sayının 10 tabanına göre logaritmasını hesaplar

math.pow(x,y) #ilk sayının ikinci sayıya göre kuvvetini (üssünü) alır

math.sqrt(9) #verilen değerin karekökünü alır

#Açısal dönüşümler
math.degrees(x) #parametre olarak verilen radyan açısını, dereceye çevirir

math.radians(85.94) #parametre olarak verilen dereceyi, radyan açısına çevirir

#Trigonometrik fonksiyonlar
math.acos(x) #parametre olarak verilen değerin ark kosinüsünü verir

math.asin(y) #parametre olarak verilen değerin ark sinüsünü verir

math.atan(x) #parametre olarak verilen değerin ark tanjantını verir

math.atan2(y,x) #parametre olarak atanan ilk değerin ikinciye göre ark tanjantını verir atan(y/x)

math.cos(x) #parametre olarak verilen değerin kosinüsünü hesaplar

math.hypot(x,y) # sqrt(x*x+y*y) sonucunu verir

math.sin(y) #parametre olarak verilen değerin sinüsünü hesaplar

math.tan(x) #parametre olarak verilen değerin tanjantını hesaplar

#hiperbolik fonksiyonlar
math.acosh(x) #parametre olarak verilen değerin ters hiperbolik kosinüs fonksiyonunu verir

math.asinh(x) #parametre olarak verilen değerin ters hiperbolik sinüs fonksiyonunu verir

math.tanh(x) #parametre olarak verilen değerin ters hiperbolik tanjant fonksiyonunu verir

math.acosh(x) #parametre olarak verilen değerin hiperbolik kosinüs fonksiyonunu verir

math.sinh(x) #parametre olarak verilen değerin hiperbolik sinüs fonksiyonunu verir

math.tanh(x) #parametre olarak verilen değerin hiperbolik tanjant fonksiyonunu verir

#özel fonksiyonlar
math.gamma(x) #parametre olarak verilen sayının 1 eksiğinin faktöriyelini hesaplar

math.lgamma(x) #parametre olarak verile sayının önce gamma() fonksiyonu ile değerini hesaplayıp daha sonra log() ile logaritmasının hesaplanmış halini ekrana verir

