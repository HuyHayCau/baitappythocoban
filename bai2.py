# Nhập chuỗi từ bàn phím
chuoi=input("Nhập 1 chuỗi từ bàn phím:")
list_tu= chuoi.split()
list_tu.reverse()
ket_qua=" ".join(list_tu)
print("Kết quả là: ", ket_qua)