import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_loader import load_and_clean_data
from src.analysis import calculate_covid_impact, get_top5_unemployment_regions, area_comparison

st.set_page_config(page_title="Unemployment Analysis India", page_icon="📊", layout="wide")

st.title("📊 Unemployment Analysis in India - COVID-19 Impact")
st.markdown("---")

@st.cache_data
def load_data():
    return load_and_clean_data()

df = load_data()

# Sidebar
st.sidebar.header("🔍 Filters")
selected_region = st.sidebar.selectbox("Select Region", ["All"] + sorted(df['Region'].unique()))
selected_area = st.sidebar.selectbox("Select Area", ["All"] + sorted(df['Area'].unique()))

filtered_df = df.copy()
if selected_region != "All":
    filtered_df = filtered_df[filtered_df['Region'] == selected_region]
if selected_area != "All":
    filtered_df = filtered_df[filtered_df['Area'] == selected_area]

# Key Metrics
st.subheader("📈 Key Metrics")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Avg Unemployment Rate", f"{filtered_df['Estimated Unemployment Rate (%)'].mean():.1f}%")
with col2:
    st.metric("Avg Employed", f"{filtered_df['Estimated Employed'].mean():,.0f}")
with col3:
    st.metric("Labour Participation", f"{filtered_df['Estimated Labour Participation Rate (%)'].mean():.1f}%")
with col4:
    pre, post = calculate_covid_impact(df).values()
    st.metric("COVID Impact", f"+{(post/pre - 1)*100:.0f}%", delta="Increase")

st.markdown("---")

# ============= الصورة 1 =============
st.subheader("📈 1. Unemployment Rate Over Time")
fig1, ax1 = plt.subplots(figsize=(12, 5))
unemp_time = filtered_df.groupby('Date')['Estimated Unemployment Rate (%)'].mean()
sns.lineplot(x=unemp_time.index, y=unemp_time.values, ax=ax1, color='red')
ax1.set_xlabel("Date")
ax1.set_ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
st.pyplot(fig1)

# ============= الصورة 2 =============
st.subheader("📉 2. Employment Over Time")
fig2, ax2 = plt.subplots(figsize=(12, 5))
employed_time = filtered_df.groupby('Date')['Estimated Employed'].mean()
sns.lineplot(x=employed_time.index, y=employed_time.values, ax=ax2, color='green')
ax2.set_xlabel("Date")
ax2.set_ylabel("Estimated Employed")
plt.xticks(rotation=45)
st.pyplot(fig2)

# ============= الصورتين جنب بعض (3 و 4) =============
col5, col6 = st.columns(2)

with col5:
    st.subheader("🏆 3. Top 5 Most Affected Regions")
    top5 = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().nlargest(5)
    fig3, ax3 = plt.subplots()
    sns.barplot(x=top5.values, y=top5.index, ax=ax3, palette='Reds_r')
    ax3.set_xlabel("Unemployment Rate (%)")
    st.pyplot(fig3)

with col6:
    st.subheader("🗺️ 4. Unemployment by Region (All)")
    unemp_region = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values()
    fig4, ax4 = plt.subplots(figsize=(8, 10))
    sns.barplot(x=unemp_region.values, y=unemp_region.index, ax=ax4, palette='coolwarm')
    ax4.set_xlabel("Unemployment Rate (%)")
    st.pyplot(fig4)

st.markdown("---")

# ============= الصورتين جنب بعض (5 و 6) =============
col7, col8 = st.columns(2)

with col7:
    st.subheader("🏙️ vs 🌾 5. Urban vs Rural (Pie)")
    area_comp = df.groupby('Area')['Estimated Unemployment Rate (%)'].mean()
    fig5, ax5 = plt.subplots()
    ax5.pie(area_comp.values, labels=area_comp.index, autopct='%1.1f%%', colors=['#ff9999','#66b3ff'])
    st.pyplot(fig5)

with col8:
    st.subheader("📊 6. Urban vs Rural Over Time")
    df_copy = df.copy()
    df_copy['YearMonth'] = df_copy['Date'].dt.to_period('M')
    area_time = df_copy.groupby(['YearMonth', 'Area'])['Estimated Unemployment Rate (%)'].mean().unstack()
    fig6, ax6 = plt.subplots(figsize=(10, 5))
    area_time.plot(ax=ax6, marker='o', linewidth=2)
    ax6.set_xlabel("Date")
    ax6.set_ylabel("Unemployment Rate (%)")
    ax6.legend(title='Area')
    plt.xticks(rotation=45)
    st.pyplot(fig6)

st.markdown("---")

# ============= الصورتين جنب بعض (7 و 8) =============
col9, col10 = st.columns(2)

with col9:
    st.subheader("🔥 7. Correlation Heatmap")
    numeric_cols = ['Estimated Unemployment Rate (%)', 'Estimated Employed', 'Estimated Labour Participation Rate (%)']
    fig7, ax7 = plt.subplots()
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', center=0, fmt='.2f', ax=ax7)
    st.pyplot(fig7)

with col10:
    st.subheader("📅 8. Monthly Unemployment Pattern")
    monthly = filtered_df.groupby('Month')['Estimated Unemployment Rate (%)'].mean()
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fig8, ax8 = plt.subplots()
    sns.barplot(x=months[:len(monthly)], y=monthly.values, ax=ax8, palette='viridis')
    ax8.set_xlabel("Month")
    ax8.set_ylabel("Unemployment Rate (%)")
    plt.xticks(rotation=45)
    st.pyplot(fig8)

# Raw Data
st.markdown("---")
st.subheader("📄 Raw Data")
st.dataframe(filtered_df.head(100))

st.markdown("---")
st.caption("Built with ❤️ using Streamlit | 8 Visualizations | Data: May 2019 - June 2020")