# 🧾 POS System Django - Real Implementation

Sistem backend **Point of Sale (POS)** berbasis **Django REST Framework** dengan fitur:

- Manajemen Produk
- Autentikasi JWT
- Sistem Transaksi otomatis (dengan pemotongan stok)

---

## 🚀 Prasyarat (Prerequisites)

Sebelum memulai, pastikan Anda telah menginstal:

- **Python 3.10+**
- **Laragon** (untuk MySQL Database)
- **Git**

---

## 🛠️ Langkah Instalasi

### 1. Persiapan Folder & Virtual Environment

Buka terminal (PowerShell/CMD) di folder proyek Anda:

```powershell
# Buat virtual environment
python -m venv venv

# Aktifkan venv
.\venv\Scripts\activate
```

### 2. Instalasi Library

Instal semua dependensi yang dibutuhkan:

```powershell
pip install django djangorestframework djangorestframework-simplejwt django-environ mysqlclient pymysql faker
```

### 3 Konfigurasi Database (MySQL Laragon)

1. Buka Laragon dan pastikan MySQL berjalan.

2. Buka HeidiSQL, buat database baru dengan nama pos_db.

3. Pastikan core/settings.py sudah terkonfigurasi untuk MySQL.

### 4 Migrasi Database

Jalankan perintah ini untuk membuat struktur tabel di MySQL:

```powershell
# Membuat file migrasi
python manage.py makemigrations

# Menerapkan migrasi ke MySQL
python manage.py migrate

# Membuat akun Superuser untuk akses admin
python manage.py createsuperuser
```

### 5 Membuat Akun Admin

```powershell
python manage.py createsuperuser
```

### 📦 Menjalankan Data Seeder

```powershell
python manage.py seed_products
```

### 🔌 Dokumentasi API Endpoints

Gunakan Postman untuk melakukan tes pada endpoint berikut:

#### 🔐 Autentikasi (JWT)

| Method | Endpoint           | Description                   |
| ------ | ------------------ | ----------------------------- |
| POST   | /api/auth/login/   | Login & Mendapatkan JWT Token |
| POST   | /api/auth/refresh/ | Memperbarui Token             |

#### 🍎 Produk (CRUD)

| Method | Endpoint            | Description                |
| ------ | ------------------- | -------------------------- |
| GET    | /api/products/      | List semua produk          |
| POST   | /api/products/      | Tambah produk baru (Admin) |
| PUT    | /api/products/{id}/ | Update produk              |
| DELETE | /api/products/{id}/ | Hapus produk               |

#### 🛒 Transaksi

| Method | Endpoint                    | Description                       |
| ------ | --------------------------- | --------------------------------- |
| POST   | /api/transactions/checkout/ | Melakukan transaksi & potong stok |

## Format Body Checkout (JSON):

```json
{
  "items": [
    { "product": 1, "quantity": 2 },
    { "product": 5, "quantity": 1 }
  ]
}
```

---

## 🧪 Menjalankan Unit Test

```powershell
python manage.py test
```

---

### 📂 Struktur Proyek

- core/: Pengaturan utama Django & Routing global.
- apps/users/: Custom User Model & Manajemen Role.
- apps/products/: Logika produk & Seeder.
- apps/transactions/: Logika transaksi & Service Layer.
