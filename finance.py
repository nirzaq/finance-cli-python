import sqlite3

def create_tables():
    """Creates essential database tables if they don't exist."""
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS income (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL NOT NULL,
                    description TEXT NOT NULL
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS expense (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL NOT NULL,
                    description TEXT NOT NULL
                )''')

    conn.commit()
    conn.close()

def add_income(amount, description):
    """Adds income data to the database."""
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()

    c.execute("INSERT INTO income (amount, description) VALUES (?, ?)", (amount, description))
    conn.commit()
    conn.close()

def show_income():
    """Show Total Income From Database"""
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()

    c.execute("SELECT SUM(amount) FROM income")
    total_income = c.fetchone()[0]

    print(f"Total Pemasukan: {total_income:.2f}")

    conn.close()

def show_income_list():
    """Show Income list From Database"""
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()

    c.execute("SELECT * FROM income ORDER BY id DESC")

    lists = c.fetchall()
    print("Daftar Pengeluaran")
    print("Jumlah   | Keterangan")
    for list in lists:
        jumlah = list[1]
        keterangan = list[2]

        print(f"{jumlah} | {keterangan}")
    
    conn.close()


def add_expense(amount, description):
    """Adds expense data to the database."""
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()

    c.execute("INSERT INTO expense (amount, description) VALUES (?, ?)", (amount, description))
    conn.commit()
    conn.close()

def show_expense():
    """Show Total Income From Database"""
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()

    c.execute("SELECT SUM(amount) FROM expense")
    total_income = c.fetchone()[0]

    print(f"Total Pengeluaran: {total_income:.2f}")

    conn.close()

def show_sums():
    """Calculates and displays total income and expenses."""
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()

    c.execute("SELECT SUM(amount) FROM income")
    total_income = c.fetchone()[0]

    c.execute("SELECT SUM(amount) FROM expense")
    total_expense = c.fetchone()[0]
    print("\n===========================================")
    print(f"Total Pemasukan\t: {total_income}")
    print(f"Total Pengeluaran\t: {total_expense}")
    print(f"Net\t: {total_income - total_expense}")
    print("===========================================")
    conn.close()

def main():
    create_tables()

    while True:
        print("\nData Keuangan")
        print("1. Tambah Pemasukan")
        print("2. Tambah Pengeluaran")
        print("3. List Pemasukan")
        print("4. List Pengeluaran")
        print("5. Total Pemasukan")
        print("6. Total Pengeluaran")
        print("7. Net")
        print("8. Keluar")

        choice = input("Masukkan Pilihan (1-8)")

        if choice == '1':
            amount = float(input("Input Pemasukan: "))
            description = input("Input Keterangan: ")
            add_income(amount, description)
            print("Pemasukan Berhasil diinput!")
            show_income_list()
        elif choice == '2':
            amount = float(input("Input Pengeluaran: "))
            description = input("Input Keterangan: ")
            add_expense(amount, description)
            print("Pengeluaran Berhasil diinput!")
        elif choice == '3':
            show_income_list()
        elif choice == '4':
            show_expense()
        elif choice == '5':
            show_sums()
        elif choice == '8':
            print("Keluar dari Aplikasi...")
            break
        else:
            print("Input Tidak Benar!")

if __name__ == "__main__":
    main()
