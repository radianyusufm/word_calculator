# Word Calculator
#### Video Demo:  https://www.youtube.com/watch?v=czxJyQ6J4Vg
#### Description: project ini memungkingkan pengguna untuk menghitung jumlah kata yang ada di file txt dan juga menghapus kata kata yang tidak diperlukan, penghapusan stop word dan penghitungan total kata bertujuan untuk memberikan teks yang lebih fokus dan relevan.

Dengan menggunakan fungsi penghapusan stop word, kita dapat menghilangkan kata-kata yang tidak memberikan kontribusi signifikan dalam pemahaman teks. Hal ini membantu kita fokus pada kata-kata yang lebih penting dan meningkatkan efisiensi dalam pemrosesan teks.

Sementara itu, penghitungan total kata memberikan informasi tentang jumlah kata dalam teks. Ini membantu kita memahami ukuran teks dan dapat digunakan sebagai langkah awal untuk analisis lebih lanjut.

Dengan demikian, kombinasi fungsi penghapusan stop word dan penghitungan total kata membantu kita memproses teks dengan lebih baik dan mendapatkan pemahaman yang lebih baik tentang kontennya


### Bahasa pemrograman yang digunakan :
Python

### Library:
re reguler expression

### Function:

def generate_stop_word():
ini menghasilkan kata apa yang harus dihilangkan ,stop word sering muncul secara sering dalam teks tetapi memberikan sedikit informasi tentang konten atau topik. Dengan menghapusnya, noise dalam teks dapat dikurangi, dan lebih banyak perhatian dapat difokuskan pada kata-kata atau frasa penting yang membawa inti dari teks.

def read_data():
ini digunakan untuk membaca isi dari artikel file txt

def replace_word(s, *stop_word):
ini akan menghapus semua kata yang ada di storp word

def list_word(s):
ini menghasilkan sebuah list yang bersih dari kata kata penting

def total_word(s):
ini akan menjumlahkan kata kata penting yang ada di list dan mengembalikanya dalam bentuk dictionary

def generate_file_txt(data):
ini akan membuat file result.txt yang isinya dari dictionary

