import pandas as pd

# CSV 파일 로드 (메모리 경고 방지)
df = pd.read_csv("Data/appsflyer.csv", low_memory=False)

# 'Event Name'이 Install, Complete Registration, Purchase인 행 필터링 후 개수 계산
install_count = (df["Event Name"] == "install").sum()
complete_registration_count = (df["Event Name"] == "af_complete_registration").sum()
purchase_count = (df["Event Name"] == "af_purchase").sum()

# 총합 출력
print(f"Install Count: {install_count}")
print(f"Complete Registration Count: {complete_registration_count}")
print(f"Purchase Count: {purchase_count}")

# result : 
# Install Count: 85121
# Complete Registration Count: 33810
# Purchase Count: 168695


