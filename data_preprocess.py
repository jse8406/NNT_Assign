import pandas as pd

# CSV 파일 로드 (메모리 경고 방지)
df = pd.read_csv("Data/appsflyer.csv", low_memory=False)

# "Install", "Complete Registration", "Purchase" 수 계산
install_count = (df["Event Name"] == "install").sum()
complete_registration_count = (df["Event Name"] == "af_complete_registration").sum()
purchase_count = (df["Event Name"] == "af_purchase").sum()

# "Purchase한 유저 수" 계산 (중복 제거)
purchase_users = df.loc[df["Event Name"] == "af_purchase", "Customer User ID"].nunique()

# 만약 'Customer User ID'가 NaN인 경우 'AppsFlyer ID'를 사용하여 유저 수 계산
if purchase_users == 0:  
    purchase_users = df.loc[df["Event Name"] == "af_purchase", "AppsFlyer ID"].nunique()

# 결과 출력
print(f"Install Count: {install_count}")
print(f"Complete Registration Count: {complete_registration_count}")
print(f"Purchase Count: {purchase_count}")
print(f"Purchase User Count: {purchase_users}")  # 구매한 유저 수


# 광고 비용에 해당하는 컬럼 : cost, bidAmount, billed_charge, mobile_conversion_spendt_credits, localSpend