# Product Review Analyzer (FastAPI, React, PostgreSQL, Gemini)

Proyek ini adalah implementasi dari **Product Review Analyzer** yang dirancang untuk menganalisis ulasan produk yang dimasukkan pengguna, menentukan sentimennya, dan mengekstrak poin-poin penting menggunakan teknologi AI/NLP.

## Informasi Pengumpulan Tugas
Nama   : Rafael Abimanyu Ratmoko

NIM    : 123140134

---

## Fitur Utama

Aplikasi ini menggabungkan layanan *backend* (FastAPI), *frontend* (React), dan *database* (PostgreSQL) yang dikoordinasikan oleh Docker Compose.

| Fitur | Teknologi yang Digunakan | Deskripsi |
| :--- | :--- | :--- |
| **Input Review** | React Frontend | Antarmuka pengguna untuk memasukkan teks ulasan produk. |
| **Sentiment Analysis** | Hugging Face Transformers | Menganalisis ulasan untuk klasifikasi sentimen (**Positive/Negative/Neutral**). |
| **Key Point Extraction** | Google Gemini API (gemini-2.5-flash) | Mengekstrak 3 hingga 5 poin-poin penting dari ulasan produk. |
| **Database Persistence** | PostgreSQL & SQLAlchemy | Menyimpan hasil analisis (ulasan, sentimen, dan poin kunci) secara permanen. |
| **API Backend** | FastAPI | Menyediakan dua endpoint RESTful untuk analisis dan pengambilan data. |

## Struktur Proyek

Struktur direktori mengikuti format yang ditentukan:

```

product-review-analyzer/
├── backend/
│   ├── app/
│   │   ├── services/
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── crud.py
│   │   ├── database.py
│   │   └── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env (Contoh/Templat)
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   └── (File React lainnya)
│   ├── Dockerfile
│   └── package.json
├── docker-compose.yml
└── README.md

````

## Persyaratan Sistem

Untuk menjalankan proyek ini, Anda membutuhkan:

* **Docker** (v20+ disarankan)
* **Docker Compose**
* **Gemini API Key** (diperlukan untuk layanan Key Point Extractor)

## Panduan Menjalankan Aplikasi

Ikuti langkah-langkah berikut untuk mengaktifkan dan menjalankan seluruh *stack* aplikasi:

### 1. Kloning Repositori

```bash
git clone [LINK REPO GITHUB ANDA]
cd product-review-analyzer
````

### 2\. Konfigurasi Environment (`.env`)

Buat file `.env` di direktori *root* (`product-review-analyzer/`) dan isi dengan *API Key* dan *credentials* database.

> **Penting:** Ganti `YOUR_GEMINI_API_KEY_HERE` dengan kunci API Gemini Anda yang valid.

```env
# .env

# API KEY GEMINI
GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE

# DATABASE CONFIG
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=review_db
DATABASE_URL=postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}

# FRONTEND CONFIG
VITE_API_URL=http://localhost:8000
```

### 3\. Bangun dan Jalankan Kontainer

Gunakan Docker Compose. Perintah ini akan membangun *image* (untuk backend dan frontend), membuat kontainer PostgreSQL, dan menjalankan semua layanan.

```bash
docker compose up --build
```

### 4\. Akses Aplikasi

Tunggu hingga semua layanan (terutama `db` dan `backend`) berstatus `Up`. Anda dapat mengakses aplikasi melalui *browser*:

  * **Aplikasi Web (Frontend React):** `http://localhost:3000`
  * **API Documentation (FastAPI Swagger UI):** `http://localhost:8000/docs`

### 5\. Endpoints API

| Metode | Endpoint | Deskripsi |
| :--- | :--- | :--- |
| **POST** | `/api/analyze-review` | Menganalisis teks ulasan baru (Hugging Face + Gemini), menyimpannya ke DB, dan mengembalikan hasil. |
| **GET** | `/api/reviews` | Mengambil daftar semua hasil analisis ulasan yang tersimpan. |

```
```
