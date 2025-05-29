# Viết hàm kiểm tra xem trong chuỗi có ký tự số hay không. Nếu có, tách các số đó ra thành một mảng riêng.
def kiem_tra_so_va_tach_cac_so(chuoi):
    # Tạo danh sách rỗng để chứa số
    list = []  
    co_so = False   
    for ky_tu_so in chuoi:
        # Kiểm tra ký tự có phải là số không
        if ky_tu_so.isdigit():
            list.append(ky_tu_so)
            co_so = True 
    return co_so, list
chuoi = input('''Nhập chuỗi: ''')
co_so, list =  kiem_tra_so_va_tach_cac_so(chuoi)
if co_so:
    print('''Chuỗi có chứa ký tự số.''')
    print('''Các số được tách ra thành mảng riêng là:''', list)
else:
    print('''Chuỗi bạn đã nhập không có ký tự số.''')
