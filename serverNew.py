import xmlrpc.server
from xmlrpc.server import SimpleXMLRPCRequestHandler
from datetime import datetime, timedelta

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# inisialisasi server
with xmlrpc.server.SimpleXMLRPCServer(('localhost', 1337),
                                      requestHandler=RequestHandler) as server:

    valid_nik_set = {"123", "321"}

    # Fungsi untuk memvalidasi laporan
    def validate_report(nikPelapor, namaPelapor, namaTerdugaCovid, alamatTerdugaCovid, gejalaTerdugaCovid):
        if not (nikPelapor and namaPelapor and namaTerdugaCovid and alamatTerdugaCovid and gejalaTerdugaCovid):
            return {'error': 'Data tidak lengkap'}

        if nikPelapor in valid_nik_set:
            response = {
                'waktu': (datetime.now() + timedelta(minutes=15)).strftime('%Y-%m-%d %H:%M:%S'),
                'nama_petugas': 'Tim Penanganan COVID-19',
                'jumlah_orang': 2,
                'detail': {
                    'NIK_pelapor': nikPelapor,
                    'Nama_pelapor': namaPelapor,
                    'Alamat_terduga_Covid': alamatTerdugaCovid,
                    'Nama_terduga_Covid': namaTerdugaCovid,
                    'Gejala_dirasakan': gejalaTerdugaCovid
                }
            }

            # print("Laporan COVID-19 diterima. Respon:")
            # print("Waktu: ", response['waktu'])
            # print("Petugas: ", response['nama_petugas'])
            # print("Jumlah Orang: ", response['jumlah_orang'])
            # print("Detail:")
            # for key, value in response['detail'].items():
            #     print(f"{key}: {value}")

            return response
        else:
            return {'error': 'NIK tidak valid'}

    # add fungsi ke server
    server.register_function(validate_report, 'validate_report')

    # run server
    print('Server siap menerima panggilan RPC...')
    server.serve_forever()
