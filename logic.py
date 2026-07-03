from datetime import datetime

def sahkan_input(nama, nokp):
    if nama.strip() == "":
        return False, "Nama tidak boleh kosong."
    if len(nokp) != 12 or not nokp.isdigit():
        return False, "Nombor kad pengenalan mestilah 12 digit angka."
    tarikh = nokp[:6]
    try:
        datetime.strptime(tarikh,"%y%m%d")
    except ValueError:
        return False, "6 digit pertama No.KP mestilah tarikh yang sah (YYMMDD)."
    return True, ""

def dapatkan_nama_berformat(nama,nokp):
    digit = int(nokp[-1])
    if digit % 2 == 1:
        return "Encik " + nama
    else:
        return "Cik " + nama

def kira_umur(nokp):
    yy = int(nokp[:2])
    mm = int(nokp[2:4])

    today = datetime.now()
    tahun_semasa = today.year
    bulan_semasa = today.month
    tahun_dua_digit = tahun_semasa % 100

    if yy <= tahun_dua_digit:
        tahun_lahir = 2000 + yy
    else:
        tahun_lahir = 1900 + yy
    
    jumlah_bulan_semasa = tahun_semasa * 12 + bulan_semasa
    jumlah_bulan_lahir = tahun_lahir * 12 + mm
    jumlah_bulan = jumlah_bulan_semasa - jumlah_bulan_lahir
    tahun = jumlah_bulan // 12
    bulan = jumlah_bulan % 12

    return f"Anda berumur {tahun} tahun {bulan} bulan."