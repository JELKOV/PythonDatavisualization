import csv
import matplotlib.pyplot as plt
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(__file__), "test.csv")

# 데이터 저장 리스트
winter_dates = []
winter_temps = []
summer_dates = []
summer_temps = []

# CSV 파일 읽기
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # 헤더 건너뛰기

    for row in reader:
        if len(row) < 8:  # 데이터가 충분하지 않으면 건너뛰기
            print("불완전한 데이터:", row)
            continue
        
        date = row[2]  # 날짜 (예: "Dec-93" 또는 "Jul-93")
        min_temp = row[7]  # 최저 기온
        max_temp = row[4]  # 최고 기온

        # 데이터 필터링: 숫자인지 확인
        try:
            min_temp = float(min_temp)
            max_temp = float(max_temp)
        except ValueError:
            print(f"유효하지 않은 데이터: {row}")
            continue
        
        # 겨울 데이터 추출 (12월)
        if "Dec" in date:
            winter_dates.append(date)
            winter_temps.append(min_temp)
        
        # 여름 데이터 추출 (7월)
        elif "Jul" in date:
            summer_dates.append(date)
            summer_temps.append(max_temp)

# 두 개의 선 그래프 출력
plt.figure(figsize=(10, 5))
plt.plot(winter_dates, winter_temps, label="Winter Min Temp", color='blue', marker='o')
plt.plot(summer_dates, summer_temps, label="Summer Max Temp", color='red', marker='o')
plt.title("Winter vs Summer Temperatures", fontsize=15)
plt.xlabel("Date", fontsize=10)
plt.ylabel("Temperature (°C)", fontsize=10)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
