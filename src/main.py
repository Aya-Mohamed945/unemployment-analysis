import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_loader import load_and_clean_data, get_data_info
from src.analysis import (
    calculate_covid_impact, 
    get_top5_unemployment_regions, 
    area_comparison,
    monthly_analysis
)
from src.visualizations import (
    plot_unemployment_over_time,
    plot_employed_over_time,
    plot_unemployment_by_region,
    plot_top5_regions,
    plot_area_pie,
    plot_area_time_series,
    plot_correlation_heatmap,
    plot_monthly_bar
)

def main():
    print("🚀 Starting analysis of unemployment data in India...")
    print("="*50)
    
    df = load_and_clean_data()
    get_data_info(df)
    
    calculate_covid_impact(df)
    top5, bottom5 = get_top5_unemployment_regions(df)
    unemp_by_area = area_comparison(df)
    monthly_unemp = monthly_analysis(df)
    
    print("\n" + "="*50)
    print("🎨 Starting visualization creation...")
    print("="*50)
    
    plot_unemployment_over_time(df)
    plot_employed_over_time(df)
    plot_unemployment_by_region(df)
    plot_top5_regions(top5)
    plot_area_pie(unemp_by_area)
    plot_area_time_series(df)
    plot_correlation_heatmap(df)
    plot_monthly_bar(monthly_unemp)
    
    print("\n" + "="*50)
    print("✅ Analysis completed! All figures have been saved in the outputs/figures/ folder")
    print("="*50)

if __name__ == "__main__":
    main()
