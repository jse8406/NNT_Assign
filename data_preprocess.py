import pandas as pd

# CSV 파일 로드 (메모리 경고 방지)
df = pd.read_csv("Data/appsflyer.csv", low_memory=False)

# "Install", "Complete Registration", "Purchase" 계산
install_df = df[df["Event Name"] == "install"]
registered_users = install_df["Customer User ID"].dropna().nunique()
non_registered_users = install_df.loc[install_df["Customer User ID"].isna(), "AppsFlyer ID"].nunique()
install_users = registered_users + non_registered_users

complete_registration_count = (df["Event Name"] == "af_complete_registration").sum()

purchase_count = (df["Event Name"] == "af_purchase").sum()

# "Purchase한 유저 수" 계산
purchase_users = df.loc[df["Event Name"] == "af_purchase", "Customer User ID"].nunique()

# print(f"Install Count: {install_users}")
# print(f"Complete Registration Count: {complete_registration_count}")
# print(f"Purchase Count: {purchase_count}")
# print(f"Purchase User Count: {purchase_users}")  # 구매한 유저 수


# 광고 비용에 해당하는 컬럼 : cost, bidAmount, billed_charge, mobile_conversion_spendt_credits, localSpend


ad_channel = ["apple_adchannel", "moloco_adchannel", "twitter_adchannel"]
cost_sum = 0

for channel in ad_channel:
    df = pd.read_csv(f"Data/{channel}.csv", low_memory=False)    
    for col in ["cost", "bidAmount", "billed_charge", "localSpend", "mobile_conversion_spent_credits"]:
        if col in df.columns: 
            cost_sum += df[col].sum()
            # print(cost_sum)
            
        
CVR_I2CR = complete_registration_count / install_users
CPA = cost_sum / purchase_count
CVR_CR2P = purchase_users / complete_registration_count
CAC_signup = cost_sum / complete_registration_count
CAC_install = cost_sum / install_users
CAC_purchase = cost_sum / purchase_users

print(f"CVR : {CVR_I2CR:.3f}")
print(f"CPA : {CPA:.3f}")
print(f"CVR : {CVR_CR2P:.3f}")
print(f"CAC_signup : {CAC_signup:.3f}")
print(f"CAC_install : {CAC_install:.3f}")
print(f"CAC_purchase : {CAC_purchase:.3f}")
