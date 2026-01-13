nama_pegawai = input("nama  pegawai : ")
golongan_darah = input("Golonga darah: ")
status_nikah = input("Status nikah:")
mempunyai_anak = ""
gender_anak = ""

if status_nikah.upper() == "M" :
    mempunyai_anak = input("mempunyai  anak Y/N: ")
    if mempunyai_anak.upper() == "Y" :
        gender_anak = input("gender anak: ")
    else :
        print("no child ")


golongan_jabatan = {
     "A" : 1000000,
     "B" : 750000,
     "C" : 500000,
}

golongan_salary = {
    "A" : 5000000,
    "B" : 2000000, 
    "C" : 1000000,
}

benefits = {
    'M' : 0.25,
    'B' : 0,
}

gender_anak_benefit  = {
    'L' : 0.10,
    'P' : 0.7,
}

status_nikah_upper = status_nikah.upper()

status_nikah_benefit = 0
if status_nikah.upper == "M" :
    status_nikah = [status_nikah.upper()]

if mempunyai_anak.upper() ==  "Y" :
    anak_benefit =+ (2000000 * gender_anak_benefit[gender_anak.upper()])
else:
    anak_benefit = 0

salary = golongan_salary[golongan_darah.upper()]

