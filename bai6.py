#  Viết hàm cắt chuỗi họ tên thành chuỗi họ lót và chuỗi tên.
def chuoi_ho_ten(ho_ten):
    list=ho_ten.split()
    chuoi_ten=list[-1]
    ho_lot = " ".join(list[:-1])
    return ho_lot, chuoi_ten
ho_ten = input("Nhập họ và tên: ")
ho_lot, ten = chuoi_ho_ten(ho_ten)
print('''Họ lót:''', ho_lot)
print('''Tên:''', ten)



