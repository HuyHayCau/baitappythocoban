# Viết chương trình nhập một chuỗi bất kỳ, liệt kê số lần xuất hiện của mỗi ký tự.
from collections import*
chuoi=input("Nhập 1 chuỗi bất kì:")
so_lan_xuat_hien= Counter(chuoi)
print("số lần xuất hiện của mỗi kí tự:")
#sorted sắp xếp các phần tử
for ky_tu, so_lan in sorted(so_lan_xuat_hien.items()):
    print("'" + ky_tu + "': " + str(so_lan))


