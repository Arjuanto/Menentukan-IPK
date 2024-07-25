def menghitung_nilai_akhir(absen,tugas,uts,uas):
    return 0.1 * absen + 0.2 * tugas + 0.3 * uts + 0.4 * uas


def grade(absen,tugas,uts,uas):
    if absen >= 70:
        nilai_akhir = menghitung_nilai_akhir(absen, tugas, uts, uas)
        if nilai_akhir >= 86:
            return 'A'
        elif nilai_akhir >= 76:
            return 'B'
        elif nilai_akhir >= 66:
            return 'C'
        elif nilai_akhir >= 56:
            return 'D'
        else:
            return 'E'
    return 'E'


class kuliah:
    nm_matkul: str
    sks: int
    absen: int
    tugas: int
    uts: int
    uas: int
    mutu: int
    grade: str


grade_bobot = {
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 1,
    'E': 0
}


jml_matkul = int(input("Jumlah mata kuliah yang diambil semester ini: "))
kuliah = [kuliah() for _ in range(jml_matkul)]

total_mutu = 0
total_sks = 0

for i in range(jml_matkul):
    print(f"\nMATA KULIAH #{i+1}")
    kuliah[i].nm_matkul = str(input("Nama mata kuliah: "))
    kuliah[i].sks = int(input("SKS: "))
    kuliah[i].absen = int(input("Nilai absen: "))
    kuliah[i].tugas = int(input("Nilai tugas: "))
    kuliah[i].uts = int(input("Nilai UTS: "))
    kuliah[i].uas = int(input("Nilai UAS: "))
    kuliah[i].grade = grade(kuliah[i].absen, kuliah[i].tugas, kuliah[i].uts, kuliah[i].uas)
    kuliah[i].mutu = grade_bobot[kuliah[i].grade] * kuliah[i].sks

    total_mutu += kuliah[i].mutu
    total_sks += kuliah[i].sks

    total_nilai_akhir = int(menghitung_nilai_akhir(kuliah[i].absen, kuliah[i].tugas, kuliah[i].uts, kuliah[i].uas))
    print(f"Nilai akhir untuk mata kuliah {kuliah[i].nm_matkul}: {total_nilai_akhir}")
    print(f"Grade: {kuliah[i].grade}")

ipk = total_mutu / total_sks
print(f"\nIndeks Prestasi: {ipk:.2f}")