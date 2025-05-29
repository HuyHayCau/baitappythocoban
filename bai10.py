so_chu = {
    0: "không", 1: "một", 2: "hai", 3: "ba", 4: "bốn",
    5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín"
}
# Nhập số
so = input("Nhập số: ")
tram = int(so[0])
chuc = int(so[1])
don_vi = int(so[2])
doc = so_chu[tram] + " trăm"
if chuc == 0 and don_vi != 0:
    doc += " lẻ"
elif chuc == 1:
    doc += " mười"
elif chuc > 1:
    doc += " " + so_chu[chuc] + " mươi"
if don_vi != 0:
    if don_vi == 5 and chuc > 0:
        doc += " lăm"
    elif don_vi == 1 and chuc > 1:
        doc += " mốt"
    else:
        doc += " " + so_chu[don_vi]
print('''Đọc là:''', doc)
