def hitung_waris():
    print("=" * 45)
    print("   🤖 KALKULATOR FARAID SEDERHANA 🤖   ")
    print("=" * 45)

    try:
        total_harta = float(input("💰 Masukkan total harta warisan (Rp): "))
    except ValueError:
        print("❌ Masukkan angka yang bener dong, Wak! 💀")
        return

    print("\n👥 Pilih Kondisi Pasangan yang Ditinggalkan:")
    print("1. Meninggalkan Suami")
    print("2. Meninggalkan Istri")
    print("3. Tidak ada pasangan (Duda/Janda/Lajang)")
    pilihan_pasangan = input("👉 Pilih (1/2/3): ")

    try:
        anak_lk = int(input("\n👦 Jumlah Anak Laki-laki: "))
        anak_pr = int(input("👧 Jumlah Anak Perempuan: "))
    except ValueError:
        print("❌ Masukkan angka yang bener buat jumlah anak! 😱")
        return

    harta_tersisa = total_harta
    punya_anak = (anak_lk > 0 or anak_pr > 0)
    
    # Inisialisasi hasil
    bagian_pasangan = 0
    nama_pasangan = ""

    # 1. Hitung Bagian Suami/Istri
    if pilihan_pasangan == "1":
        nama_pasangan = "Suami"
        if punya_anak:
            bagian_pasangan = total_harta * (1 / 4)  # Dapet 1/4 kalau ada anak
        else:
            bagian_pasangan = total_harta * (1 / 2)  # Dapet 1/2 kalau nggak ada anak
    elif pilihan_pasangan == "2":
        nama_pasangan = "Istri"
        if punya_anak:
            bagian_pasangan = total_harta * (1 / 8)  # Dapet 1/8 kalau ada anak
        else:
            bagian_pasangan = total_harta * (1 / 4)  # Dapet 1/4 kalau nggak ada anak

    harta_tersisa -= bagian_pasangan

    # 2. Hitung Bagian Anak (Ashabah - Sisa)
    bagian_anak_lk = 0
    bagian_anak_pr = 0

    if punya_anak:
        # Rumus Islam: Bagian anak laki-laki = 2x anak perempuan
        total_bagian_anak = (anak_lk * 2) + anak_pr
        harta_per_bagian_anak = harta_tersisa / total_bagian_anak

        if anak_lk > 0:
            bagian_anak_lk = harta_per_bagian_anak * 2
        if anak_pr > 0:
            bagian_anak_pr = harta_per_bagian_anak

    # 3. Cetak Output Hasil Pembagian
    print("\n" + "=" * 45)
    print("📜 HASIL PEMBAGIAN WARIS 📜")
    print("=" * 45)
    print(f"💵 Total Harta Awal : Rp {total_harta:,.2f}")
    
    if nama_pasangan:
        print(f"👤 Bagian {nama_pasangan} : Rp {bagian_pasangan:,.2f}")
    
    if anak_lk > 0:
        print(f"👦 Bagian per Anak Laki-laki : Rp {bagian_anak_lk:,.2f} (Total {anak_lk} anak)")
    if anak_pr > 0:
        print(f"👧 Bagian per Anak Perempuan : Rp {bagian_anak_pr:,.2f} (Total {anak_pr} anak)")
        
    print("=" * 45)
    print("🫡 Semoga berkah dan tidak terjadi baku hantam keluarga! 😈")

# Jalankan programnya
if __name__ == "__main__":
    hitung_waris()