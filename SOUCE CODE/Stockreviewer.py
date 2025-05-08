from StockIlustrasi import StockIlustrasi
from StockFoto import StockFoto

class Stockreviewer:
    #private atribut
    __kodeReviewer = ""
    __Nama = ""
    __Username = ""
    __Statuspegawai = ""
    __Stockreview = ""
    __listStock = ""
    __reviewlist = ""

    #constructor
    def __init__(self, kodeReviewer, Nama, Username, Statuspegawai, Stockreview, listStock,reviewlist):
        self.__kodeReviewer = kodeReviewer
        self.__Nama = Nama
        self.__Username = Username
        self.__Statuspegawai = Statuspegawai
        self.__Stockreview = Stockreview
        self.__listStock = []
        self.__ListStockReviews = []
        self.__review_list = reviewlist

     # Method to add a stock review
    def tambah_stock_review(self, review):
        self.__ListStockReviews.append(review)

     # Method to display information
    def display_info(self):
        print(f"Reviewer ID: {self.__reviewer_id}")
        print(f"Name: {self.__name}")
        print(f"Username: {self.__username}")
        print(f"Reviews: {self.__review_list}")
    #setter
    def set_kodeReviewer(self, kodeReviewer):
        self.__kodeReviewer = kodeReviewer

    def set_Nama(self, Nama):
        self.__Nama = Nama

    def set_Username(self, Username):
        self.__Username = Username

    def set_Statuspegawai(self, Statuspegawai):
        self.__Statuspegawai = Statuspegawai

    def set_Stockreview(self, Stockreview):
        self.__Stockreview = Stockreview

    def set_listStock(self, listStock):
        self.__listStock = listStock

    #getter
    def get_kodeReviewer(self):
        return self.__kodeReviewer
    
    def get_Nama(self):
        return self.__Nama
    
    def get_Username(self):
        return self.__Username
    
    def get_Statuspegawai(self):
        return self.__Statuspegawai
    
    def get_Stockreview(self):
        return self.__Stockreview
    
    def get_listStock(self):
        return
    

