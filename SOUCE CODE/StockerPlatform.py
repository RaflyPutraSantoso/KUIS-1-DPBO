from Microstocker import Microstocker

#deklarasi
class StockerPlatform :
    #privat atribut
    __KodeStocker = ""
    __NamaPlatform = ""
    __ListFile = ""
    __HakPerjanjian = ""
    __ListMicrostocker = ""

    #constructor
    def __init__(self, kodeStocker, namaPlatform, listFile, hakPerjanjian, listMicrostocker):
        self.__KodeStocker = kodeStocker
        self.__NamaPlatform = namaPlatform
        self.__ListFile = listFile
        self.__HakPerjanjian = hakPerjanjian
        self.__ListMicrostocker = []

    # Method to add a microstocker
    def tambah_microstocker(self, microstocker):
        self.__ListMicrostocker.append(microstocker)

     # Method to display information
    def display_info(self):
        print("List of Microstockers:")
        for microstocker in self.__ListMicrostocker:
            microstocker.display_info()  # Assuming Microstocker has a display_info method

    #setter
    def set_kodeStocker(self, kodeStocker):
        self.__KodeStocker = kodeStocker

    def set_namaPlatform(self, namaPlatform):
        self.__NamaPlatform = namaPlatform

    def set_listFile(self, listFile):
        self.__ListFile = listFile

    def set_hakPerjanjian(self, hakPerjanjian):
        self.__HakPerjanjian = hakPerjanjian

    def set_listMicrostocker(self, listMicrostocker):
        self.__ListMicrostocker = listMicrostocker

    #getter
    def get_kodeStocker(self):
        return self.__KodeStocker
    
    def get_namaPlatform(self):
        return self.__NamaPlatform
    
    def get_listFile(self):
        return self.__ListFile
    
    def get_hakPerjanjian(self):
        return self.__HakPerjanjian
    
    def get_listMicrostocker(self):
        return self.__ListMicrostocker
    
    