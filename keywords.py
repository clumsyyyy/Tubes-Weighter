keywords_dict = {
    1: ['laporan', 'dokumen', 'README', 'bonus', 'berkas', 
        'demo', 'video', 'penjelasan', 'anggota', 'pembagian'],
    2: ['komentar', 'kode', 'code',
        'executable', 'modular', 'repository', 'folder', 'debugging', 
        'bugtesting', 'instalasi', 'pemasangan', 'tahapan', 'pengaturan', 'belajar', 
        'mempelajari'],
    3: ['algoritma', 'konsep', 'implementasi', 'penerapan', 'solusi', 'pengujian',
        'cara', 'kesesuaian', 'sesuai', 'materi', 'dataset', 'data', 'kreativitas', 'tutorial', 
        'referensi', 'dokumentasi', 'pemakaian', 'penggunaan', 
        'pengembangan', 'akses', 'desain'],
    4: ['bahasa', 'pustaka', 'library', 'CLI', 'GUI', 'web', 'desktop'
        'waktu', 'eksekusi', 'program', 'opsi', 'deploy', 'fitur', 
        'buat', 'hasil', 'jenis', 'memakai', 'menggunakan', 'groundwork'],
    5: ['frontend', 'backend', 'framework', 'basis data', 'database', 'analisis', 
        'aplikasi', 'pengujian', 'menguji', 'visualisasi', 'eksplorasi', 'perbaikan', 'wajib', 'benar', 
        'interface'],
}

def bfMatch(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        j = 0
        # melakukan iterasi selama j < len(pattern) dan kata-katanya cocok
        while (j < len(pattern) and pattern[j] == text[i + j]):
            j += 1
        
        # return True apabila iterasi berhasil dilakukan sampai habis
        if (j == len(pattern)):
            return True
        
    # default, return False apabila tidak ditemukan kecocokan
    return False

def calculateWeight(query):
    weight = 0
    
    # membagi query menjadi kata-kata
    split_query = [word.lower() for word in query.split(" ")]
    
    for word in split_query:
        temp = 0
        for i in range(len(keywords_dict.keys())):
            for j in range(len(keywords_dict[i + 1])):
                # melakukan pencocokan kata-kata dengan keyword tertentu
                if (len(word) >= len(keywords_dict[i + 1][j]) and bfMatch(word, keywords_dict[i + 1][j])):
                    if (i + 1 > temp):
                        # mengubah nilai weight sementara, apabila
                        # ditemukan kata yang lebih "cocok"
                        temp = i + 1
                        
        # menambahkan bobot total
        weight += temp
        
    # apabila kebutuhan termasuk bonus,
    # kembalikan weight // 2 (bonus diprioritaskan terakhir)
    if "bonus" in split_query:
        return weight // 2
    
    # default, return weight biasa
    return weight
