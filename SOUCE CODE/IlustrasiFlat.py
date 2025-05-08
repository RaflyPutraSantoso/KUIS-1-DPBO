from StockIlustrasi import StockIlustrasi

class IlustrasiFlat :
    #Private Atribut
    __kodeIlustrasi = ""
    __judul = ""
    __deskripsi = ""
    __tanggalUpload = ""
    __jenisIlustrasi = ""
    __Tema = ""

    #Constructor
    def __init__(self, kodeIlustrasi, judul, deskripsi, tanggalUpload, jenisIlustrasi, tema):
        self.__kodeIlustrasi = kodeIlustrasi
        self.__judul = judul
        self.__deskripsi = deskripsi
        self.__tanggalUpload = tanggalUpload
        self.__jenisIlustrasi = jenisIlustrasi
        self.__Tema = tema

    #Setter
    def set__Tema(self, tema):
        self.__Tema = tema

    #Getter
    def get__Tema(self):
        return self.__Tema