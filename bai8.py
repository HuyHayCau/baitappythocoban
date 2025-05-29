#  Viết chương trình đổi chữ xen kẽ: một chữ hoa và một chữ thường.
chuoi = input('''Nhập chương trình muốn đổi chữ xen kẻ : ''')
chuoi_xen_ke = []
for i in range(len(chuoi)):
    if i % 2 == 0:
        chuoi_xen_ke.append(chuoi[i].upper())
    else:
        chuoi_xen_ke.append(chuoi[i].lower())
        ket_qua = "".join(chuoi_xen_ke)
        print('''Chuỗi sau khi đổi:''', ket_qua)
