import xmlrpc.server
from xmlrpc.server import SimpleXMLRPCRequestHandler
from datetime import datetime, timedelta

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# inisialisasi server
with xmlrpc.server.SimpleXMLRPCServer(('localhost', 1337),
                                      requestHandler=RequestHandler) as server:

    def check(nikPelapor):
        with open('nik.txt') as f:
            datafile = f.readlines()
        found = False 
        for line in datafile:
            if nikPelapor in line:
                return True
        return False 

    # Fungsi untuk memvalidasi laporan
    def validate_report(nikPelapor, namaPelapor, namaTerdugaCovid, alamatTerdugaCovid, gejalaTerdugaCovid):
        if not (nikPelapor and namaPelapor and namaTerdugaCovid and alamatTerdugaCovid and gejalaTerdugaCovid):
            return {'error': 'Data tidak lengkap'}

        if check(nikPelapor):
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

            return response
        else:
            return {'error': 'NIK tidak valid'}

    # add fungsi ke server
    server.register_function(validate_report, 'validate_report')

    # run server
    print('Server siap menerima panggilan RPC...')
    server.serve_forever()
