from StockIlustrasi import StockIlustrasi

class IlustrasiPatternSeamles:
    #private atribut
    __kodePattern = ""
    __Nama = ""
    __Tema = ""

    #constructor
    def __init__(self, kodePattern, nama, tema):
        self.__kodePattern = kodePattern
        self.__Nama = nama
        self.__Tema = tema

    #setter
    def set_kodePattern(self, kodePattern):
        self.__kodePattern = kodePattern

    def set_nama(self, nama):
        self.__Nama = nama

    def set_tema(self, tema):
        self.__Tema = tema


    #getter
    def get_kodePattern(self):
        return self.__kodePattern
    
    def get_nama(self):
        return self.__Nama
    
    def get_tema(self):
        return self.__Tema