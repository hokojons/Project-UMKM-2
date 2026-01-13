# library_management_system.py
"""Sistem manajemen perpustakaan dengan antarmuka pengguna."""

class Book:
    """Class untuk merepresentasikan buku dalam perpustakaan."""
    
    def __init__(self, book_id, title, author, is_available=True):
        """Inisialisasi objek buku."""
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = is_available
    
    def __str__(self):
        """Representasi string dari objek buku."""
        status = "Tersedia" if self.is_available else "Dipinjam"
        return f"ID: {self.book_id} | Judul: {self.title} | Penulis: {self.author} | Status: {status}"


class Library:
    """Class untuk manajemen koleksi perpustakaan."""
    
    def __init__(self):
        """Inisialisasi perpustakaan dengan koleksi kosong."""
        self.book_collection = {}
    
    def add_book(self, book):
        """Menambahkan buku baru ke koleksi."""
        if book.book_id in self.book_collection:
            raise ValueError("Buku dengan ID tersebut sudah ada")
        self.book_collection[book.book_id] = book
    
    def find_book(self, search_term):
        """Mencari buku berdasarkan ID atau judul."""
        # Cari berdasarkan ID
        if search_term in self.book_collection:
            return self.book_collection[search_term]
        
        # Cari berdasarkan judul
        for book in self.book_collection.values():
            if search_term.lower() in book.title.lower():
                return book
        
        return None
    
    def borrow_book(self, book_id):
        """Meminjam buku dari perpustakaan."""
        book = self.book_collection.get(book_id)
        if book and book.is_available:
            book.is_available = False
            return True
        return False
    
    def return_book(self, book_id):
        """Mengembalikan buku ke perpustakaan."""
        book = self.book_collection.get(book_id)
        if book and not book.is_available:
            book.is_available = True
            return True
        return False
    
    def display_all_books(self):
        """Menampilkan semua buku dalam koleksi."""
        if not self.book_collection:
            print("Belum ada buku dalam koleksi.")
            return
        
        print("\nDaftar Buku:")
        for book in self.book_collection.values():
            print(book)


def display_menu():
    """Menampilkan menu pilihan untuk pengguna."""
    print("\n=== Sistem Manajemen Perpustakaan ===")
    print("1. Tambah Buku Baru")
    print("2. Cari Buku")
    print("3. Pinjam Buku")
    print("4. Kembalikan Buku")
    print("5. Tampilkan Semua Buku")
    print("6. Keluar")


def get_user_input(prompt, input_type=str):
    """Mendapatkan input dari pengguna dengan validasi dasar."""
    while True:
        try:
            user_input = input(prompt)
            if input_type == str and user_input.strip() == "":
                print("Input tidak boleh kosong!")
                continue
            return input_type(user_input.strip())
        except ValueError:
            print(f"Input harus bertipe {input_type.__name__}")


def main():
    """Fungsi utama untuk menjalankan sistem."""
    library = Library()
    
    # Data contoh
    library.add_book(Book("B001", "Python Programming", "Guido van Rossum"))
    library.add_book(Book("B002", "Clean Code", "Robert C. Martin"))
    
    while True:
        display_menu()
        choice = get_user_input("Pilih menu (1-6): ", int)
        
        if choice == 1:
            # Tambah buku baru
            print("\nTambah Buku Baru")
            book_id = get_user_input("Masukkan ID buku: ")
            title = get_user_input("Masukkan judul buku: ")
            author = get_user_input("Masukkan nama penulis: ")
            
            try:
                library.add_book(Book(book_id, title, author))
                print("Buku berhasil ditambahkan!")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == 2:
            # Cari buku
            print("\nCari Buku")
            search_term = get_user_input("Masukkan ID atau judul buku: ")
            book = library.find_book(search_term)
            
            if book:
                print("\nBuku ditemukan:")
                print(book)
            else:
                print("Buku tidak ditemukan.")
        
        elif choice == 3:
            # Pinjam buku
            print("\nPinjam Buku")
            book_id = get_user_input("Masukkan ID buku yang ingin dipinjam: ")
            
            if library.borrow_book(book_id):
                print("Buku berhasil dipinjam!")
            else:
                print("Gagal meminjam buku. Buku tidak tersedia atau tidak ditemukan.")
        
        elif choice == 4:
            # Kembalikan buku
            print("\nKembalikan Buku")
            book_id = get_user_input("Masukkan ID buku yang ingin dikembalikan: ")
            
            if library.return_book(book_id):
                print("Buku berhasil dikembalikan!")
            else:
                print("Gagal mengembalikan buku. Buku tidak sedang dipinjam atau tidak ditemukan.")
        
        elif choice == 5:
            # Tampilkan semua buku
            library.display_all_books()
        
        elif choice == 6:
            print("Terima kasih telah menggunakan sistem perpustakaan.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih 1-6.")


if __name__ == "__main__":
    main()