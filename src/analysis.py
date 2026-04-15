import pandas as pd

def calculate_covid_impact(df):
    pre_covid = df[df['Date'] < '2020-03-01']['Estimated Unemployment Rate (%)'].mean()
    post_covid = df[df['Date'] >= '2020-03-01']['Estimated Unemployment Rate (%)'].mean()
    
    print("\n" + "="*50)
    print("🦠 Impact of COVID-19 on Unemployment:")
    print("="*50)
    print(f"📉 Average Unemployment Rate Before COVID-19: {pre_covid:.2f}%")
    print(f"📈 Average Unemployment Rate During/After COVID-19: {post_covid:.2f}%")
    print(f"⚠️ Percentage Increase: {(post_covid/pre_covid - 1)*100:.1f}%")
    
    return {"pre_covid": pre_covid, "post_covid": post_covid}

def get_top5_unemployment_regions(df):
    unemp_by_region = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean()
    top5 = unemp_by_region.nlargest(5)
    bottom5 = unemp_by_region.nsmallest(5)
    
    print("\n" + "="*50)
    print("🏆 Top 5 Most Affected Regions by Unemployment:")
    print("="*50)
    print(top5)
    
    print("\n" + "="*50)
    print("🍃 Top 5 Least Affected Regions by Unemployment:")
    print("="*50)
    print(bottom5)
    
    return top5, bottom5

def area_comparison(df):
    unemp_by_area = df.groupby('Area')['Estimated Unemployment Rate (%)'].mean()
    
    print("\n" + "="*50)
    print("🏙️  Unemployment Comparison: Urban vs Rural Areas")
    print("="*50)
    print(f"🏙️  Urban: {unemp_by_area.get('Urban', 0):.2f}%")
    print(f"🌾 Rural: {unemp_by_area.get('Rural', 0):.2f}%")
    
    return unemp_by_area

def monthly_analysis(df):
    monthly_unemp = df.groupby('Month')['Estimated Unemployment Rate (%)'].mean()
    print("\n" + "="*50)
    print("📅 Average Unemployment Rate by Month:")
    print("="*50)
    print(monthly_unemp)
    return monthly_unemp