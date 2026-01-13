nama_pegawai = input("Nama Pegawai: ")
golongan_pegawai = input("Golongan A/B/C: ")
status_nikah = input("Status Nikah M/S: ")
mempunyai_anak = ""
gender_anak = ""

if status_nikah.upper() == "M":
    mempunyai_anak = input("Mempunyai Anak Y/N: ")
    if mempunyai_anak.upper() == 'Y':
        gender_anak = input("Gender anak  L/P: ")

golongan_jabatan = {
    'A': 1000000,
    'B': 750000,
    'C': 500000
}

golongan_salary = {
    'A': 5000000,
    'B': 2000000,
    'C': 1000000
}

benefits = {
    'M': 0.25,
    'S': 0
}
gender_anak_benefit = {
    'L':0.10,
    "P": 0.7
}

status_nikah_benefit = 0
if  status_nikah.upper() ==  "M":
    status_nikah_benefit = benefits[status_nikah.upper()]

anak_benefit = 0
if mempunyai_anak.upper() == 'Y':
    anak_benefit = 200000 + (200000 * gender_anak_benefit[gender_anak.upper()])

# Calculate salary and benefits
salary = golongan_salary[golongan_pegawai.upper()]
total_benefit = status_nikah_benefit + anak_benefit
total_salary = salary + total_benefit

# Print payroll details
print("Payroll Details:")
print(f"Nama Pegawai: {nama_pegawai}")
print(f"Golongan: {golongan_pegawai}")
print(f"Status Nikah: {status_nikah}")
if status_nikah.upper() == "M":
    print(f"Mempunyai Anak: {mempunyai_anak}")
    if mempunyai_anak.upper() == 'Y':
        print(f"Gender Anak : {gender_anak}")
print(f"Salary: Rp {salary:,}")
print(f"Benefit Nikah: Rp {status_nikah_benefit*salary:,}")
print(f"Benefit Anak: Rp {anak_benefit:,}")
print(f"Total Benefit: Rp {total_benefit*salary:,}")
print(f"Total Salary: Rp {total_salary:,}")