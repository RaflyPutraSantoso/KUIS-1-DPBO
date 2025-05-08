from StockIlustrasi import StockIlustrasi
from StockFoto import StockFoto
from Microstocker import Microstocker
from StockerPlatform import StockerPlatform
from Stockreviewer import Stockreviewer

def main():
    # Create StockIlustrasi object
    ilustrasi1 = StockIlustrasi(
        kodeIlustrasi="IL001",
        judul="Pattern Floral",
        deskripsi="Ilustrasi pattern floral seamless",
        tanggalUpload="2023-10-01",
        jenisIlustrasi="seamless"
    )

    # Create StockFoto object
    foto1 = StockFoto(
        kodeFoto="F001",
        judul="Sunset Landscape",
        deskripsi="Foto landscape sunset",
        tanggalUpload="2023-10-03",
        jenis="landscape"
    )

    # Create Microstocker object and add stocks
    microstocker1 = Microstocker(
        kodeMicrostocker="M001",
        Nama="John Doe",
        Username="johndoe",
        TanggalLahir="1990-01-01",
        negara="Indonesia",
        ListStock=[]
    )
    microstocker1.tambah_stock(ilustrasi1)
    microstocker1.tambah_stock(foto1)

    # Create StockerPlatform object and add microstocker
    stockerPlatform1 = StockerPlatform(
        kodeStocker="SP001",
        namaPlatform="Microstock Platform",
        listFile=["png", "jpeg", "jpg"],
        hakPerjanjian="eksklusif",
        listMicrostocker=[]
    )
    stockerPlatform1.tambah_microstocker(microstocker1)

    # Create StockReviewer object and add reviews
    reviewer1 = Stockreviewer(
        kodeReviewer="R001",
        Nama="Alice",
        Username="alice123",
        Statuspegawai="senior",
        Stockreview="ilustrasi",
        listStock=[],
        reviewlist=[]
    )
    reviewer1.tambah_stock_review(ilustrasi1)
    reviewer1.tambah_stock_review(foto1)

    # Display information
    print("=== Informasi Microstocker ===")
    microstocker1.display_info()

    print("\n=== Informasi Stocker Platform ===")
    stockerPlatform1.display_info()

    print("\n=== Informasi Stock Reviewer ===")
    reviewer1.display_info()

if __name__ == "__main__":
    main()