import pandas as pd

# CSV 파일 로드 (메모리 경고 방지)

ad_channel = ["apple_adchannel", "moloco_adchannel", "twitter_adchannel"]
cost_sum = 0


for channel in ad_channel:
    df = pd.read_csv(f"Data/{channel}.csv", low_memory=False)    
    for col in ["cost", "bidAmount", "billed_charge", "localSpend", "mobile_conversion_spent_credits"]:
        if col in df.columns: 
            cost_sum += df[col].sum()
            print(cost_sum)

# 최종 광고 비용 출력
print(f"Total Cost: {cost_sum}")