# Nama  : Wanda Septiananta Heryadi Putra
# NRP   : 5220600047
# Kelas : GT B

# pembuatan fungsi PassByReference dengan 1 parameter
def PassByReference(list) :
  # mengubah nilai di dalam variable list dengan menambahkan angka 47
  list.append(47)
  # mengembalikan nilai berupa isi dari list
  return list

# pembuatan fungsi PassByValue dengan 1 parameter
def PassByValue(list) :
  # mengubah nilai di dalam variable list dengan angka 47
  list = 47
  # mengembalikan nilai berupa isi dari list
  return list

# pembuatan fungsi Main dengan 1 parameter
def Main() :
  # menggunakan tipe data list (array)
  list = [52206000]
  # menampilkan nilai awal list
  print("List : ", list)
  # menampilkan nilai list saat di ubah menggunakan pass by value
  print("pass by value : ", PassByValue(list)) # manjalankan fungsi PassByValue dengan parameter list

  # menampilkan pemisah
  print("--------------------------------------")
  
  # menampilkan nilai list setelah di ubah
  print("List : ", list)
  # memanggil perintah pass by reference
  PassByReference(list) # manjalankan fungsi PassByReference dengan parameter list
  # menampilkan nilai list setelah di ubah menggunakan pass by reference
  print("pass by reference x : ", list)


# untuk mengizinkan atau mencegah bagian kode dijalankan saat modul diimpor
# jika file dijalankan variabel __name__ ditetapkan sebagai __main__ 
if __name__ == "__main__" :
  # memanggil fungsi main
  Main()
