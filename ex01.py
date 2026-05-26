from datetime import datetime

current_year = datetime.now().year

name = input("Nhập tên bệnh nhân: ")
birth_year = int(input("Nhập năm sinh: "))
sick_days = int(input("Nhập số ngày bị bệnh: "))
temperature = float(input("Nhập nhiệt độ cơ thể: "))
fee = float(input("Nhập chi phí khám: "))

# Kiểm tra hợp lệ
if name == "":
    print("Lỗi: Tên không được để trống")
elif birth_year < 1900 or birth_year > current_year:
    print("Lỗi: Năm sinh không hợp lệ")
elif sick_days < 0:
    print("Lỗi: Số ngày bị bệnh không hợp lệ")
elif temperature < 30 or temperature > 45:
    print("Lỗi: Nhiệt độ không hợp lệ")
elif fee <= 0:
    print("Lỗi: Chi phí khám không hợp lệ")
else:
    # Tính toán
    age = current_year - birth_year
    extra_fee = fee * 0.1
    total_fee = fee + extra_fee

    # Phân loại sức khỏe
    if temperature > 38 and sick_days > 3:
        health_status = "Nguy hiểm"
    elif temperature > 38:
        health_status = "Sốt cao"
    elif temperature > 37.5:
        health_status = "Sốt nhẹ"
    else:
        health_status = "Bình thường"

    # Nested if đánh giá ưu tiên
    if health_status == "Nguy hiểm":
        if age > 60:
            priority = "Cấp cứu"
        else:
            priority = "Ưu tiên cao"
    else:
        priority = "Bình thường"

    # Toán tử 3 ngôi
    cost_level = "Cao" if total_fee > 500000 else "Thấp"

    # Kết quả
    print("\n===== KẾT QUẢ ĐÁNH GIÁ =====")
    print("Tên bệnh nhân:", name)
    print("Tuổi:", age)
    print("Số ngày bị bệnh:", sick_days)
    print("Nhiệt độ:", temperature, "°C")
    print("Chi phí khám:", fee)
    print("Phụ phí:", extra_fee)
    print("Tổng chi phí:", total_fee)
    print("Tình trạng sức khỏe:", health_status)
    print("Mức độ ưu tiên:", priority)
    print("Mức chi phí:", cost_level)