#deklarasi
class StockIlustrasi:
    #private atribut
    __KodeIlustrasi = ""
    __Judul = ""
    __Deskripsi = ""
    __TanggalUpload = ""
    __JenisIlustrasi = ""
    
    #constructor
    def __init__(self, kodeIlustrasi, judul, deskripsi, tanggalUpload, jenisIlustrasi):
        self.__KodeIlustrasi = kodeIlustrasi
        self.__Judul = judul
        self.__Deskripsi = deskripsi
        self.__TanggalUpload = tanggalUpload
        self.__JenisIlustrasi = jenisIlustrasi

    #setter
    def set_kodeIlustrasi(self, kodeIlustrasi):
        self.__KodeIlustrasi = kodeIlustrasi

    def set_judul(self, judul):
        self.__Judul = judul

    def set_deskripsi(self, deskripsi):
        self.__Deskripsi = deskripsi

    def set_tanggalUpload(self, tanggalUpload):
        self.__TanggalUpload = tanggalUpload

    def set_jenisIlustrasi(self, jenisIlustrasi):
        self.__JenisIlustrasi = jenisIlustrasi

    #getter
    def get_kodeIlustrasi(self):
        return self.__KodeIlustrasi
    
    def get_judul(self):
        return self.__Judul
    
    def get_deskripsi(self):
        return self.__Deskripsi
    
    def get_tanggalUpload(self):
        return self.__TanggalUpload
    
    def get_jenisIlustrasi(self):
        return self.__JenisIlustrasi
    