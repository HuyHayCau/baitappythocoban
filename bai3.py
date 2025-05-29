# Viết chương trình tìm kiếm ký tự xuất hiện nhiều nhất trong chuỗi.
list =["Huy", "Đạt","Huy","Việt", "Toàn", "Huy"]
from collections import Counter
# Đếm 
Dem = Counter(list)
# tìm tên xuất hiện nhiều nhất trong chuỗi
#most_common Trả về phần tử phổ biến nhất
name_max = Dem.most_common(1)[0]
print("Tên đã xuất hiện nhiều trong chuỗi:", name_max[0])
print("Số lần xuất hiện trong chuỗi:", name_max[1])


