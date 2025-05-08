#deklarasi
class Microstocker:
    #privat atribut
    __kodeMicrostocker = ""
    __Nama = ""
    __Username = ""
    __TanggalLahir = ""
    __negara = ""
    __ListStock = ""

     # Method to display information
    def display_info(self):
        print(f"Kode Microstocker: {self.__kodeMicrostocker}")
        print(f"Nama: {self.__Nama}")
        print(f"Username: {self.__Username}")
        print(f"Tanggal Lahir: {self.__TanggalLahir}")
        print(f"Negara: {self.__negara}")
        print(f"List Stock: {self.__ListStock}")

    #constructor
    def __init__(self, kodeMicrostocker, Nama, Username, TanggalLahir, negara, ListStock):
        self.__kodeMicrostocker = kodeMicrostocker
        self.__Nama = Nama
        self.__Username = Username
        self.__TanggalLahir = TanggalLahir
        self.__negara = negara
        self.__ListStock = ListStock


      # method to add stock
    def tambah_stock(self, stock):
        self.__ListStock.append(stock)

    #setter
    def set_kodeMicrostocker(self, kodeMicrostocker):
        self.__kodeMicrostocker = kodeMicrostocker

    def set_Nama(self, Nama):
        self.__Nama = Nama

    def set_Username(self, Username):
        self.__Username = Username

    def set_TanggalLahir(self, TanggalLahir):
        self.__TanggalLahir = TanggalLahir

    def set_negara(self, negara):
        self.__negara = negara

    def set_ListStock(self, ListStock):
        self.__ListStock = ListStock

    #getter
    def get_kodeMicrostocker(self):
        return self.__kodeMicrostocker
    
    def get_Nama(self):
        return self.__Nama
    
    def get_Username(self):
        return self.__Username
    
    def get_TanggalLahir(self):
        return self.__TanggalLahir
    
    def get_negara(self):
        return self.__negara
    
    def get_ListStock(self):
        return self.__ListStock