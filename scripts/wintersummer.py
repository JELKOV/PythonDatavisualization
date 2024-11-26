import csv
import matplotlib.pyplot as plt
import os
from collections import defaultdict

# 데이터를 저장할 딕셔너리
seasonal_data = defaultdict(lambda: {"Winter": None, "Summer": None})

# CSV 파일 경로 설정
file_path = os.path.join(os.path.dirname(__file__), "test.csv")

# CSV 파일 읽기
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # 헤더 건너뛰기

    for row in reader:
        if len(row) < 8:  # 데이터가 충분하지 않으면 건너뛰기
            continue

        # 마지막 컬럼에서 날짜 추출
        try:
            year_month_day = row[-1]  # 마지막 컬럼에서 날짜 문자열 가져오기
            year, month = year_month_day.split("-")[:2]  # 연도와 월 추출
            year = int(year)  # 연도를 정수로 변환
            month = int(month)  # 월을 정수로 변환
        except (ValueError, IndexError):
            continue

        min_temp = row[7]  # 최저 기온
        max_temp = row[4]  # 최고 기온

        # 데이터 필터링: 숫자인지 확인
        try:
            min_temp = float(min_temp)
            max_temp = float(max_temp)
        except ValueError:
            continue

        # 겨울(12월, 1월, 2월)과 여름(7월, 8월, 9월) 데이터 저장
        if month in [12, 1, 2]:
            seasonal_data[year]["Winter"] = min_temp
        elif month in [7, 8, 9]:
            seasonal_data[year]["Summer"] = max_temp

# 연도별 데이터를 정렬하여 추출
years = sorted(seasonal_data.keys())

# 동기화된 데이터 리스트 생성
filtered_years = []
filtered_winter_temps = []
filtered_summer_temps = []

for year in years:
    if seasonal_data[year]["Winter"] is not None and seasonal_data[year]["Summer"] is not None:
        filtered_years.append(year)
        filtered_winter_temps.append(seasonal_data[year]["Winter"])
        filtered_summer_temps.append(seasonal_data[year]["Summer"])

# 디버깅용 출력
print("Filtered Years:", filtered_years)
print("Winter Temps:", filtered_winter_temps)
print("Summer Temps:", filtered_summer_temps)

# 시각화
plt.figure(figsize=(12, 6))
plt.plot(filtered_years, filtered_winter_temps, label="Winter Min Temp", color="blue", marker="o", linestyle="-")
plt.plot(filtered_years, filtered_summer_temps, label="Summer Max Temp", color="red", marker="o", linestyle="-")

plt.title("Winter (Dec-Feb) vs Summer (Jul-Sep) Temperatures by Year", fontsize=15)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)
plt.legend()

# x축 레이블 설정
plt.xticks(ticks=filtered_years, labels=[str(year) for year in filtered_years], rotation=45)
plt.tight_layout()
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()
