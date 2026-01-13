while True:
    print("      Payroll       ")
    nama_pegawai = input("Nama Pegawai: ")
    golongan_pegawai = input("Golongan A/B/C: ")
    status_nikah = input("Status Nikah M/S: ")
    mempunyai_anak = ""
    gender_anak = ""

    if status_nikah.upper() == "M":
        mempunyai_anak = input("Mempunyai Anak Y/N :  ")

    golongan_jabatan = {
        'A': 5000000,
        'B': 2000000,
        'C': 1000000
    }

    golongan_salary = {
        'A': 1000000,
        'B': 750000,
        'C': 500000
    }

    status_nikah_benefit = {
        'M': 0.25,
        'S': 0
    }
    gender_anak_benefit = {
        'L':0.10,
        "P":0.7
    }

    status_nikah_upper = status_nikah.upper()

    benefit_nikah = 0
    if status_nikah_upper == "M":
        benefit_nikah = golongan_jabatan[golongan_pegawai.upper()] * status_nikah_benefit[status_nikah_upper]

    anak_benefit = 0
    if mempunyai_anak.upper() == 'Y':
        gender_anak = input("Gender anak  L/P: ")
        if gender_anak.upper() == "L":
            anak_benefit = golongan_jabatan[golongan_pegawai.upper()] * 0.1
        elif gender_anak.upper() == "P":
            anak_benefit = golongan_jabatan[golongan_pegawai.upper()] * 0.07

    golongan_jabatan_value = 0
    if golongan_pegawai.upper() in ("A", "B", "C"):
        if golongan_pegawai.upper() == "A":
            golongan_jabatan_value = 5000000
        elif golongan_pegawai.upper() == "B":
            golongan_jabatan_value = 2000000
        elif golongan_pegawai.upper() == "C":
            golongan_jabatan_value = 1000000

    # Calculate salary and benefits
    salary = golongan_salary[golongan_pegawai.upper()]
    benefit_nikah = golongan_jabatan[golongan_pegawai.upper()] * status_nikah_benefit[status_nikah_upper]
    total_benefit = benefit_nikah + anak_benefit
    total_salary = salary + total_benefit + benefit_nikah + golongan_jabatan_value


    # Print payroll details
    print ("Payroll Details:")
    print(f"Nama Pegawai: {nama_pegawai}")
    print(f"Golongan: {golongan_pegawai}")
    print(f"Status Nikah: {status_nikah_upper}")
    print(f"Mempunyai Anak: {mempunyai_anak}")
    if mempunyai_anak.upper() == 'Y':
        print(f"Gender Anak : {gender_anak}")
    else:
        print("no child")

    print(f"Salary          : Rp {salary:,}")
    print(f"Benefit jabatan : Rp {golongan_jabatan_value:,}")
    print(f"Benefit Nikah   : Rp {benefit_nikah:,}")
    print(f"Benefit Anak    : Rp {anak_benefit:,}")
    print(f"Total Benefit   : Rp {total_benefit:,}")
    print(f"Total Salary    : Rp {total_salary:,}")

    
    response = input("Do you want to continue? (Y/N): ")
    if response.upper() != "Y":
        break