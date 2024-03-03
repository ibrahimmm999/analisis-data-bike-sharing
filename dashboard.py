import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

st. set_page_config(layout="wide")

st.title('Analisis Data Bike Sharing')
st.write('oleh Imam Rusydi Ibrahim')

df_1 = pd.read_csv("total_penyewaan_per_musim.csv")
df_2 = pd.read_csv("penyewaan_tiap_jam_per_musim.csv")


tab1, tab2, tab3 = st.tabs(["Analisis 1", "Analisis 2", "Hasil"])

with tab1:
    df_1.set_index('season', inplace=True)
    plt.figure(figsize=(8, 6))
    df_1.plot(kind='bar', color='skyblue')
    plt.title('Total Jumlah Peminjaman Sepeda Berdasarkan Musim (Harian)')
    plt.xlabel('Musim')
    plt.ylabel('Total Jumlah Peminjaman')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt)
with tab2:
    season_labels = {1: 'Springer', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

    pivot_table_sorted = df_2.sort_values(by=['season', 'cnt'], ascending=[True, False])

    top_hours_per_season = pivot_table_sorted.groupby('season').head(4)
    # Iterasi melalui setiap musim
    for ax, (season, data) in zip(axes.flat, top_hours_per_season.groupby('season')):
        data.reset_index().plot(kind='bar', x='hr', y='cnt', ax=ax, color='skyblue', legend=False)
        ax.set_title(f'Top 4 Jam Peminjaman Sepeda Tertinggi di Musim {season_labels[season]}')
        ax.set_xlabel('Jam')
        ax.set_ylabel('Jumlah rata-rata Peminjaman')
        ax.set_xticklabels(data.reset_index()['hr'], rotation=0)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt)
with tab3:
    st.subheader('Conclusion:')
    st.write('''
- Analisis 1 : Musim fall/gugur adalah musim dengan jumlah peminjaman sepeda tertinggi
- Analisis 2 : Pada tiap musim, rata-rata peminjaman sepeda terbanyak terjadi pada jam 17.00 (5 sore)
'''
)
