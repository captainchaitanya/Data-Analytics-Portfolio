
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

RECORDS = 500
CHANNELS = ['Facebook Ads', 'Google Ads', 'LinkedIn Ads', 'TikTok Ads']
CAMPAIGN_TYPES = ['Brand Awareness', 'Lead Gen', 'Conversion']
START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2023, 12, 31)

data = []
for _ in range(RECORDS):
    channel = random.choice(CHANNELS)
    campaign = f"{random.choice(CAMPAIGN_TYPES)}_{random.randint(100, 999)}"
    date = START_DATE + timedelta(days=random.randint(0, (END_DATE - START_DATE).days))
    
   
    if channel == 'Facebook Ads':
        impressions = np.random.randint(5000, 20000)
        clicks = int(impressions * np.random.uniform(0.02, 0.05)) # Higher CTR
        cost = clicks * np.random.uniform(0.5, 1.5)
        conversions = int(clicks * np.random.uniform(0.04, 0.08)) # Higher Conversion Rate
    elif channel == 'LinkedIn Ads':
        impressions = np.random.randint(2000, 8000)
        clicks = int(impressions * np.random.uniform(0.005, 0.015)) # Lower CTR
        cost = clicks * np.random.uniform(2.5, 5.0) # Higher CPC
        conversions = int(clicks * np.random.uniform(0.01, 0.03))
    else:
        impressions = np.random.randint(3000, 15000)
        clicks = int(impressions * np.random.uniform(0.01, 0.03))
        cost = clicks * np.random.uniform(1.0, 2.5)
        conversions = int(clicks * np.random.uniform(0.02, 0.05))
        
    revenue = conversions * np.random.uniform(50, 150)
    
    data.append([date, channel, campaign, cost, impressions, clicks, conversions, revenue])

df = pd.DataFrame(data, columns=['Date', 'Channel', 'Campaign', 'Cost', 'Impressions', 'Clicks', 'Conversions', 'Revenue'])
df.to_csv('marketing_data.csv', index=False)

print("Synthetic marketing data ('marketing_data.csv') generated successfully!")
    