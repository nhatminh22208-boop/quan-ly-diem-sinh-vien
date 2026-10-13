import pandas as pd

ho_ten = [
    "Nguyen Van An",
    "Tran Minh Khoa",
    "Le Hoang Nam",
    "Pham Gia Bao",
    "Vo Than Long",
    "Dang Quoc Huy",
    "Bui Minh Tuan",
    "Hoang Anh Duc",
    "Doan Thanh Dat",
    "Nguyen Gia Huy"
]

chuyen_can = [8.5, 7.0, 9.0, 6.5, 8.0, 9.5, 7.5, 6.0, 8.5, 9.0]

giua_ki = [8.0, 7.0, 8.5, 6.0, 7.0, 9.0, 8.0, 6.5, 5.5, 7.0]

cuoi_ki = [9.0, 8.0, 9.5, 7.0, 8.0, 9.5, 7.5, 6.0, 9.0, 4.0]

df = pd.DataFrame({
    "Ho_ten": ho_ten,
    "Chuyen_can": chuyen_can,
    "Giua_ki": giua_ki,
    "cuoi_ki": cuoi_ki
})

# Hiển thị bảng dữ liệu 
display(df)

# #2. Tính điểm tổng kết 

df["Tong_ket"] = (
    + df["Chuyen_can"] * 0.2
    + df["Giua_ki"] * 0.3
    + df["cuoi_ki"] * 0.5
)

display(df)

# #3.Xếp loại sinh viên 

def xep_loai(diem):
  if diem >= 8.5:
    return "Giỏi"
  elif diem >= 7.0:
    return "Khá"
  elif diem >= 5.0:
    return "Cần cố gắng thêm"
  else:
    return "yếu"

df["xep_loai"] = df["Tong_ket"].apply(xep_loai)

display(df)

# #4 + #5. Thống kê và trực quan hóa 

import matplotlib.pyplot as plt

#===== Thống kê =====

#Điểm tổng kết trung bình 
diem_trung_binh = df["Tong_ket"].mean()

#Sinh viên có điểm cao nhất 
Sinh_vien_cao_nhat = df.loc[df["Tong_ket"].idxmax()]

#Sinh viên có điểm thấp nhất 
Sinh_vien_thap_nhat = df.loc[df["Tong_ket"].idxmin()]

# Số sinh viên đạt 
so_sinh_vien_dat = (df["Tong_ket"] >= 5).sum

print("Điểm tổng kết trung bình:", round(diem_trung_binh, 2))
print("Sinh viên cao điểm nhất:",
      Sinh_vien_cao_nhat["Ho_ten"],
      "-", Sinh_vien_cao_nhat["Tong_ket"])

print("Sinh viên có điểm thấp nhất:",
      Sinh_vien_thap_nhat["Ho_ten"],
      "-", Sinh_vien_thap_nhat["Tong_ket"])

print("số sinh viên đạt:", so_sinh_vien_dat)


#===== Trực quan hóa =====
plt.figure(figsize=(12, 6))

plt.bar(df["Ho_ten"], df["Tong_ket"])

plt.title("Điểm tổng kết của 10 sinh viên")
plt.xlabel("Họ và tên")
plt.ylabel("điểm tổng kết")
plt.xlabel("Họ và tên")
plt.ylabel("Điểm tổng kết")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# #6. Tạo Web App bằng Streamlit

import streamlit as st
import pandas as pd

# =========================
# 1. TẠO DỮ LIỆU
# =========================

ho_ten = [
    "Nguyen Van An",
    "Tran Minh Khoa",
    "Le Hoang Nam",
    "Pham Gia Bao",
    "Vo Thanh Long",
    "Dang Quoc Huy",
    "Bui Minh Tuan",
    "Hoang Anh Duc",
    "Doan Thanh Dat",
    "Nguyen Gia Huy"
]

chuyen_can = [8.5, 7.0, 9.0, 6.5, 8.0, 9.5, 7.5, 6.0, 8.5, 9.0]

giua_ki = [8.0, 7.0, 8.5, 6.0, 7.0, 9.0, 8.0, 6.5, 5.5, 7.0]

cuoi_ki = [9.0, 8.0, 9.5, 7.0, 8.0, 9.5, 7.5, 6.0, 9.0, 4.0]

df = pd.DataFrame({
    "Ho_ten": ho_ten,
    "Chuyen_can": chuyen_can,
    "Giua_ky": giua_ki,
    "Cuoi_ky": cuoi_ki
})

# =========================
# 2. TÍNH ĐIỂM TỔNG KẾT
# =========================

df["Tong_ket"] = (
    df["Chuyen_can"] * 0.2
    + df["Giua_ky"] * 0.3
    + df["Cuoi_ky"] * 0.5
)

# =========================
# 3. XẾP LOẠI
# =========================

def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# =========================
# 4. THỐNG KÊ
# =========================

diem_trung_binh = df["Tong_ket"].mean()

sinh_vien_cao_nhat = df.loc[df["Tong_ket"].idxmax()]

sinh_vien_thap_nhat = df.loc[df["Tong_ket"].idxmin()]

so_sinh_vien_dat = (df["Tong_ket"] >= 5).sum()

# =========================
# 5. GIAO DIỆN WEB
# =========================

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

st.subheader("Bảng điểm sinh viên")

st.dataframe(
    df[
        [
            "Ho_ten",
            "Chuyen_can",
            "Giua_ky",
            "Cuoi_ky",
            "Tong_ket",
            "Xep_loai"
        ]
    ],
    use_container_width=True
)

# =========================
# 6. THỐNG KÊ
# =========================

st.subheader("Thống kê")

st.write(
    "Điểm trung bình của lớp:",
    round(diem_trung_binh, 2)
)

st.write(
    "Sinh viên có điểm cao nhất:",
    sinh_vien_cao_nhat["Ho_ten"],
    "-",
    round(sinh_vien_cao_nhat["Tong_ket"], 2)
)

st.write(
    "Sinh viên có điểm thấp nhất:",
    sinh_vien_thap_nhat["Ho_ten"],
    "-",
    round(sinh_vien_thap_nhat["Tong_ket"], 2)
)

st.write(
    "Số sinh viên đạt:",
    so_sinh_vien_dat
)

# =========================
# 7. CHỌN SINH VIÊN
# =========================

st.subheader("Thông tin sinh viên")

sinh_vien_chon = st.selectbox(
    "Chọn sinh viên:",
    df["Ho_ten"]
)

sv = df[df["Ho_ten"] == sinh_vien_chon].iloc[0]

st.write("Chuyên cần:", sv["Chuyen_can"])
st.write("Giữa kỳ:", sv["Giua_ky"])
st.write("Cuối kỳ:", sv["Cuoi_ky"])
st.write("Điểm tổng kết:", round(sv["Tong_ket"], 2))
st.write("Xếp loại:", sv["Xep_loai"])

# =========================
# 8. BIỂU ĐỒ
# =========================

st.subheader("Biểu đồ điểm tổng kết")

st.bar_chart(
    df.set_index("Ho_ten")["Tong_ket"]
)

# =========================
# 9. THÔNG TIN NGƯỜI THỰC HIỆN
# =========================

st.markdown("---")

st.caption(
    "Người thực hiện: Huỳnh Nhật Minh - MSSV: 064208014398 "
)
