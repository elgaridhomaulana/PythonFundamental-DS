input_user = input('Masukan (1) Hari atau (2) Detik = ')
while input_user != '1' and input_user != '2':
	print('1 atau 2 saja!')
	input_user = input('Masukan (1) Hari atau (2) Detik= ')

if input_user == '1':
	jumlah_hari = int(input('Berapa Hari ? '))

	tahun = jumlah_hari // 360
	sisa_hari = jumlah_hari % 360
	bulan = sisa_hari // 30
	sisa_hari = sisa_hari % 30
	hari = sisa_hari

	print(f'{tahun} tahun, {bulan} bulan, {hari} hari')

elif input_user == '2':
	jumlah_detik = int(input('Jumlah Detik ? '))

	menit = jumlah_detik // 60
	detik = jumlah_detik % 60
	jam = menit // 60
	menit %= 60
	hari = jam // 24
	jam %= 24
	bulan = hari // 30
	hari %= 30
	tahun = bulan // 12
	bulan %= 12

	print(f'{tahun} tahun {bulan} bulan {hari} hari {jam} jam {menit} menit {detik} detik')

