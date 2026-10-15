#cek kelulusan mahasiswa
nama = input("Masukkan Nama Mahasiswa: ") #string
nilai = float(input("Masukkan Nilai Akhir: ")) #float

if nilai >= 60:
    status = "LULUS"
else:
    status ="Tidak Lulus"

if nilai >= 90:
    grade ="A"
elif nilai >= 75:
    grade ="B"
elif nilai >= 60:
    grade ="C"
elif nilai >= 50:
    grade ="D"

print (f"{nama} dengan nilai akhir {nilai} mendapatkan grade {grade} dan dinyatakan {status}")