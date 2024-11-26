# [데이터 시각화]

import csv
import matplotlib.pyplot as plt
import os

# 파일 경로 설정
file_path = os.path.join(os.path.dirname(__file__), "test.csv")

# 데이터 저장 리스트
dates = []
temps = []

# CSV 파일 읽기
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # 헤더 건너뛰기

    for row in reader:
        # 빈 행 또는 불완전한 데이터 건너뛰기
        if len(row) < 3:
            print("불완전한 데이터:", row)
            continue
        
        # 데이터 읽기
        a = row[2]  # 날짜
        b = row[-2]  # 온도
        if a.startswith("Dec"):  # "Dec"로 시작하는 데이터만 처리
            print(a, b)
            dates.append(a)
            temps.append(float(b))

# 선 그래프 출력
plt.plot(dates, temps, marker='o', color='r', linestyle=':', linewidth=2, markersize=5)
plt.title("Temperature in December", fontsize=15)
plt.xlabel("Date", fontsize=10)
plt.ylabel("Temperature", fontsize=10)
plt.show() 


# 막대 그래프 출력
plt.bar(dates, temps, color='blue')
plt.title("Temperature in December", fontsize=15)
plt.xlabel("Date", fontsize=10)
plt.ylabel("Temperature", fontsize=10)
plt.show()

# 겨울 최저기온 + 여름 최고기온 데이터
winter_dates = ["Dec 1", "Dec 2", "Dec 3", "Dec 4", "Dec 5"]
winter_temps = [-5, -3, -7, -2, -4]

summer_dates = ["Jul 1", "Jul 2", "Jul 3", "Jul 4", "Jul 5"]
summer_temps = [30, 32, 33, 31, 29]

# 두 개의 선 그래프 출력
plt.plot(winter_dates, winter_temps, label="Winter Min Temp", color='blue', marker='o')
plt.plot(summer_dates, summer_temps, label="Summer Max Temp", color='red', marker='x')
plt.title("Winter vs Summer Temperatures", fontsize=15)
plt.xlabel("Date", fontsize=10)
plt.ylabel("Temperature", fontsize=10)
plt.legend()
plt.show()



