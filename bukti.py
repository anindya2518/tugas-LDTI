import pandas as pd
import json

# Baca file JSON
with open("Ika Wahyu Anindya Putri M_V3925025.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Konversi ke DataFrame per kategori
df_wawancara = pd.DataFrame(data["Pengumpulan data dengan wawancara pengguna aplikasi"])
df_api = pd.DataFrame(data["pengumpulan data penggunaan API untuk mengakses data"])
df_observasi = pd.DataFrame(data["pengumpulan data dengan observasi"])
df_dokumentasi = pd.DataFrame(data["pengumpulan data dengan studi dokumentasi"])

# Simpan ke Excel
with pd.ExcelWriter("output_data.xlsx", engine="openpyxl") as writer:
    df_wawancara.to_excel(writer, sheet_name="Wawancara", index=False)
    df_api.to_excel(writer, sheet_name="API", index=False)
    df_observasi.to_excel(writer, sheet_name="Observasi", index=False)
    df_dokumentasi.to_excel(writer, sheet_name="Dokumentasi", index=False)

print("File Excel berhasil dibuat: output_data.xlsx")
