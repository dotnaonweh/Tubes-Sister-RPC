import xmlrpc.client

# inisialisasi ke server
proxy = xmlrpc.client.ServerProxy('http://localhost:1337/RPC2')

# input data
nikPelapor = input("Masukkan NIK: ")
namaPelapor = input("Masukkan Nama Pelapor: ")
namaTerdugaCovid = input("Masukkan Nama Terduga: ")
alamatTerdugaCovid = input("Masukkan Alamat Terduga: ")
gejalaTerdugaCovid = input("Masukkan Gejala yang Dialami ")

# panggil fungsi RPC di server
result = proxy.validate_report(nikPelapor, namaPelapor, namaTerdugaCovid, alamatTerdugaCovid, gejalaTerdugaCovid)

if 'error' in result:
    print(f"\n{result['error']}")
else:
    # menampilkan respon dari server
    print("\nRespon dari server:")
    print(f"Waktu: {result['waktu']}")
    print(f"Petugas: {result['nama_petugas']}")
    print(f"Jumlah Orang: {result['jumlah_orang']}")
    print("\nDetail:")
    for key, value in result['detail'].items():
        print(f"{key}: {value}")
        

