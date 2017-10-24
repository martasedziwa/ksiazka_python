from time import time, localtime, strftime
czas_w_sekundach = time()
czas_w_minutach = czas_w_sekundach/60
czas_w_godzinach = czas_w_minutach/60
czas_w_dniach = czas_w_godzinach/24
czas_w_miesiacach = czas_w_dniach/31 # czas przyblizony
czas_w_latach = czas_w_miesiacach/12
print ('Od poczatku epoki upłuneły ', int(czas_w_dniach), ' dni')
print (localtime())
print('bieżący czas: ',strftime('%H:%M:%S'))
