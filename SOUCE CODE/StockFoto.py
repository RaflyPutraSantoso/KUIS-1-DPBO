#deklarasi
class StockFoto:
    #private atribut
    __KodeFoto = ""
    __Judul = ""
    __Deskripsi = ""
    __TanggalUpload = ""
    __JenisFoto = ""

    #constructor
    def __init__(self, kodeFoto, judul, deskripsi, tanggalUpload, jenis):
        self.__KodeFoto = kodeFoto
        self.__Judul = judul
        self.__Deskripsi = deskripsi
        self.__TanggalUpload = tanggalUpload
        self.__JenisFoto = jenis

    #setter
    def set_kodeFoto(self, kodeFoto):
        self.__KodeFoto = kodeFoto

    def set_judul(self, judul):
        self.__Judul = judul

    def set_deskripsi(self, deskripsi):
        self.__Deskripsi = deskripsi

    def set_tanggalUpload(self, tanggalUpload):
        self.__TanggalUpload = tanggalUpload

    def set_jenisFoto(self, jenis):
        self.__JenisFoto = jenis

    #getter
    def get_kodeFoto(self):
        return self.__KodeFoto
    
    def get_judul(self):
        return self.__Judul
    
    def get_deskripsi(self):
        return self.__Deskripsi
    
    def get_tanggalUpload(self):
        return self.__TanggalUpload
    
    def get_jenisFoto(self):
        return self.__JenisFoto
    
    