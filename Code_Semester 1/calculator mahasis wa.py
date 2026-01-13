nama_mahasiswa = (input("nama_mahasiswa: "))

nilai_akhir=PTS=float(input("PTS: "))
nilai_akhir=TTS=float(input("TTS: "))
nilai_akhir=QTS=float(input("QTS: "))
nilai_akhir=UTS=float(input("UTS: "))
nilai_akhir=PAS=float(input("PAS: "))
nilai_akhir=TAS=float(input("TAS: "))
nilai_akhir=OAS=float(input("QAS: "))
nilai_akhir=UAS=float(input("UAS: "))


int = 0.40 *((PTS * 0.10)+(TTS *  0.20)+(QTS * 0.20)+(UTS * 0.50)) + 0.60 * ((PAS * 0.10) +  (TAS * 0.20) + (OAS * 0.20) +  (UAS * 0.50))

if nilai_akhir  >90 and  nilai_akhir <= 100 :
    grade = "A"
elif nilai_akhir   >80 and  nilai_akhir <= 90 :
    grade = "B"
elif  nilai_akhir   >70 and  nilai_akhir <= 80 :
    grade =  "C"

elif nilai_akhir    >60 and  nilai_akhir <= 70 :
    grade = "D"
elif nilai_akhir    >0 and  nilai_akhir <= 60 :
    grade = "E"


    print("Sangat Memuaskan")
print("Nama Mahasiswa:", nama_mahasiswa)
print("Nilai Akhir:", nilai_akhir)
print("garde" , grade )