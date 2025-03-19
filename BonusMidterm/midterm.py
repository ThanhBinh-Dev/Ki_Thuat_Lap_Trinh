import pandas as pd
import plotly.express as px


def load_and_process_data(file_path):
    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name=xls.sheet_names[0])
    df.columns = df.columns.str.strip()
    df_cleaned = df.dropna(subset=["Mã HP"]).copy()
    df_cleaned["Học Kỳ Gốc"] = df_cleaned["Học Kỳ"]
    df_cleaned["Học Kỳ Hiển Thị"] = "Học kỳ " + df_cleaned["Học Kỳ Gốc"].astype(str)
    if "Loại môn học" not in df_cleaned.columns:
        df_cleaned["Loại môn học"] = "Không xác định"
    df_cleaned["Tên học phần"] = df_cleaned["Tên học phần"].fillna(" ")
    df_cleaned["Giá trị Học Kỳ"] = 1
    hoc_ky_bo_sung = [1, 9, 10]
    for hk in hoc_ky_bo_sung:
        df_cleaned = pd.concat([
            df_cleaned,
            pd.DataFrame({
                "Học Kỳ Hiển Thị": [f"Học kỳ {hk}"] * 1,
                "Loại môn học": ["Bắt buộc"],
                "Tên học phần": [" "],
                "Giá trị Học Kỳ": [1]
            })
        ], ignore_index=True)
    return df_cleaned
def create_sunburst_chart(df_cleaned, output_html_path):
    fig = px.sunburst(df_cleaned,
                      path=["Học Kỳ Hiển Thị", "Loại môn học", "Tên học phần"],
                      values="Giá trị Học Kỳ",
                      title="Biểu đồ tròn chương trình đào tạo của 406H",
                      branchvalues="total")
    fig.update_traces(marker=dict(line=dict(width=1)))
    fig.write_html(output_html_path, include_plotlyjs="cdn")
    print(f"Biểu đồ đã được lưu tại: {output_html_path}")
if __name__ == "__main__":
    file_path = "dataset-406H.xlsx"
    output_html_path = "406H_10K.html"
    df_cleaned = load_and_process_data(file_path)
    create_sunburst_chart(df_cleaned, output_html_path)
