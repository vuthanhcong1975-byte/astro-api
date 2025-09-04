import swisseph as swe

# Trỏ đến thư mục ephemeris (thư mục chứa sepl_18.se1)
swe.set_ephe_path("./ephe")

# Ví dụ: tính vị trí Mặt Trời ngày 23/05/2011 lúc 02:00 UTC
jd = swe.julday(2011, 5, 23, 2.0)  # Julian Day
pos, _ = swe.calc_ut(jd, swe.SUN)

print("Kinh độ Mặt Trời:", pos[0])
