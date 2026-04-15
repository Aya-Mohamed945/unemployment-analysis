import matplotlib.pyplot as plt
import seaborn as sns
from src.config import OUTPUT_DIR, FIGURE_SIZE, FIGURE_DPI

sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = FIGURE_SIZE

def save_figure(filename):
    plt.savefig(f"{OUTPUT_DIR}/{filename}", dpi=FIGURE_DPI, bbox_inches='tight')
    print(f"✅ Figure saved: {filename}")

def plot_unemployment_over_time(df):
    unemp_by_date = df.groupby('Date')['Estimated Unemployment Rate (%)'].mean()
    
    plt.figure()
    sns.lineplot(x=unemp_by_date.index, y=unemp_by_date.values)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Unemployment Rate (%)', fontsize=12)
    plt.title('📈 Unemployment Rate Trend in India Over Time', fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    save_figure("unemployment_over_time.png")
    plt.show()

def plot_employed_over_time(df):
    employed_by_date = df.groupby('Date')['Estimated Employed'].mean()
    
    plt.figure()
    sns.lineplot(x=employed_by_date.index, y=employed_by_date.values, color='green')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('No of employed', fontsize=12)
    plt.title('📊 Employment Trend Over Time', fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    save_figure("employed_over_time.png")
    plt.show()

def plot_unemployment_by_region(df):
    unemp_by_region = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values()
    
    plt.figure(figsize=(14, 8))
    bars = plt.barh(range(len(unemp_by_region)), unemp_by_region.values, color='coral')
    plt.yticks(range(len(unemp_by_region)), unemp_by_region.index, fontsize=8)
    plt.xlabel('Unemployment Rate (%)', fontsize=12)
    plt.title('🏭 Unemployment Rate by Region', fontsize=14)
    plt.tight_layout()
    save_figure("unemployment_by_region.png")
    plt.show()

def plot_top5_regions(top5):
    plt.figure()
    sns.barplot(x=top5.values, y=top5.index, palette='Reds_r')
    plt.xlabel('Unemployment Rate (%)', fontsize=12)
    plt.title('⚠️ Top 5 Regions Most Affected by COVID-19', fontsize=14)
    plt.tight_layout()
    save_figure("top5_regions.png")
    plt.show()

def plot_area_pie(unemp_by_area):
    plt.figure()
    plt.pie(unemp_by_area.values, labels=unemp_by_area.index, autopct='%1.1f%%', 
            colors=['#ff9999','#66b3ff'], explode=(0.05, 0), shadow=True)
    plt.title('🏙️ vs 🌾 Unemployment Distribution: Urban vs Rural', fontsize=14)
    plt.tight_layout()
    save_figure("urban_vs_rural_pie.png")
    plt.show()

def plot_area_time_series(df):
    df['YearMonth'] = df['Date'].dt.to_period('M')
    area_time = df.groupby(['YearMonth', 'Area'])['Estimated Unemployment Rate (%)'].mean().unstack()
    
    plt.figure(figsize=(14, 7))
    area_time.plot(marker='o', linewidth=2, markersize=4)
    plt.xlabel('Date (Monthly)', fontsize=12)
    plt.ylabel('Unemployment Rate (%)', fontsize=12)
    plt.title('📉 Unemployment Comparison Between Urban and Rural Areas Over Time', fontsize=14)
    plt.legend(title='Area')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    save_figure("urban_vs_rural_timeseries.png")
    plt.show()

def plot_correlation_heatmap(df):
    numeric_cols = ['Estimated Unemployment Rate (%)', 'Estimated Employed', 'Estimated Labour Participation Rate (%)']
    
    plt.figure()
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', center=0, 
                fmt='.2f', square=True, linewidths=1)
    plt.title('🔥 Correlation Matrix of Unemployment Variables', fontsize=14)
    plt.tight_layout()
    save_figure("correlation_heatmap.png")
    plt.show()

def plot_monthly_bar(monthly_unemp):
    months = ['January', 'February', 'March', 'April', 'May', 'June',
 'July', 'August', 'September', 'October', 'November', 'December']
    
    plt.figure()
    sns.barplot(x=months[:len(monthly_unemp)], y=monthly_unemp.values, palette='viridis')
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Average Unemployment Rate (%)', fontsize=12)
    plt.title('📅 Average Unemployment Rate by Month (Aggregated Across Years)', fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    save_figure("monthly_unemployment.png")
    plt.show()