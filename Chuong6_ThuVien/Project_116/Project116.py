import numpy as np

# Tạo mảng ngẫu nhiên gồm 10 phần tử trong khoảng [-100, 500]
arr = np.random.randint(-100, 501, 10)
print("Mảng ban đầu:", arr)
# 1
print("Toàn bộ mảng:", arr)
# 2
print("Phần tử từ vị trí 2 tới 5:", arr[2:6])
# 3
print("Các phần tử âm:", arr[arr < 0])
# 4
x, y = map(int, input("Nhập khoảng giá trị x y: ").split())
print(f"Phần tử từ {x} tới {y}:", arr[(arr >= x) & (arr <= y)])
# 5
arr_positive = arr[arr >= 0]
print("Mảng sau khi lọc số âm:", arr_positive)
# 6
sorted_arr_asc = np.sort(arr)
print("Mảng sắp xếp tăng dần:", sorted_arr_asc)
# 7
sorted_arr_desc = np.sort(arr)[::-1]
print("Mảng sắp xếp giảm dần:", sorted_arr_desc)
# 8
print("Giá trị nhỏ nhất:", np.min(arr))
print("Giá trị lớn nhất:", np.max(arr))
print("Giá trị trung bình:", np.mean(arr))
print("Giá trị trung vị:", np.median(arr))
print("Độ lệch chuẩn:", np.std(arr))
# 9
def is_perfect_square(n):
    return n >= 0 and int(np.sqrt(n)) ** 2 == n
arr_no_squares = arr[~np.array([is_perfect_square(num) for num in arr])]
print("Mảng sau khi loại bỏ số chính phương:", arr_no_squares)
# 10
X = int(input("Nhập giá trị X: "))
V = int(input("Nhập vị trí V: "))
arr_inserted = np.insert(arr, V, X)
print("Mảng sau khi chèn:", arr_inserted)
