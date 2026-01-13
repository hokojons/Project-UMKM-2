while True:
    nilai_akhir = int(input("nilai_akhir: "))

    if nilai_akhir < 0  or nilai_akhir > 100:
        print("Invalid score. Please enter a value between 0 and 100.")
    else:
        if nilai_akhir == 0:
            print("Invalid score. Please enter a value between 1 and 100.")
        
        elif nilai_akhir   >79 and  nilai_akhir <= 89 :
            grade = "B"
           
        elif  nilai_akhir  >89 and  nilai_akhir <= 100 :
            grade = "A"
        elif  nilai_akhir   >69 and  nilai_akhir <= 79 :
             grade =  "C"
        elif nilai_akhir    >59 and  nilai_akhir <= 69 :
            grade = "D"
        else:
            grade = "E"
        print("Your grade is:", grade)
        break