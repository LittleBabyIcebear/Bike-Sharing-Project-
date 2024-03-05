import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

day_df = pd.read_csv("https://raw.githubusercontent.com/LittleBabyIcebear/Bike-Sharing-Project-/main/day.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/LittleBabyIcebear/Bike-Sharing-Project-/main/hour.csv")

columns_rename = {
    'dteday': 'date',
    'mnth': 'month', 
    'yr': 'year', 
    'temp': 'temperature', 
    'hum': 'humidity',
    'cnt': 'total'
}

day_df.rename(columns=columns_rename, inplace="True")

columns_rename_hour = {
    'dteday': 'date',
    'mnth': 'month', 
    'hr': 'hour',
    'yr': 'year', 
    'temp': 'temperature', 
    'hum': 'humidity',
    'cnt': 'total'
}

hour_df.rename(columns=columns_rename_hour, inplace="True")

day_df['date'] = pd.to_datetime(day_df["date"])
hour_df['date'] = pd.to_datetime(hour_df["date"])

#Data Day
day_df['season'] = day_df['season'].astype('category')
day_df['season'] = day_df['season'].cat.rename_categories({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})

#Data hour
hour_df['season'] = hour_df['season'].astype('category')
hour_df['season'] = hour_df['season'].cat.rename_categories({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})

#Data Day
day_df['holiday'] = day_df['holiday'].astype('category')
day_df['holiday'] = day_df['holiday'].cat.rename_categories({1: 'holiday', 0: 'not'})

#Data hour
hour_df['holiday'] = hour_df['holiday'].astype('category')
hour_df['holiday'] = hour_df['holiday'].cat.rename_categories({1: 'holiday', 0: 'not'})

#Hubungan antara jumlah pesepeda dengan musim 
total_by_season=day_df.groupby('season')['total'].sum().sort_values(ascending=False)
spring_hour_df = hour_df[hour_df['season'] == 'Spring'].groupby('hour')['total'].sum()
summer_hour_df = hour_df[hour_df['season'] == 'Summer'].groupby('hour')['total'].sum()
fall_hour_df = hour_df[hour_df['season'] == 'Fall'].groupby('hour')['total'].sum()
winter_hour_df = hour_df[hour_df['season'] == 'Winter'].groupby('hour')['total'].sum()

#Jumlah Peminjam Pesepeda dengan Cuaca di setiap Musim 

#Pengauh cuaca terhadap jumlah pesepeda saat holiday di setiap musim 
holiday_spring=hour_df[(hour_df['holiday']=='holiday') & (hour_df['season'] == 'Spring')].groupby('hour')['total'].sum()
holiday_summer=hour_df[(hour_df['holiday']=='holiday') & (hour_df['season'] == 'Summer')].groupby('hour')['total'].sum()
holiday_fall=hour_df[(hour_df['holiday']=='holiday') & (hour_df['season'] == 'Fall')].groupby('hour')['total'].sum()
holiday_winter=hour_df[(hour_df['holiday']=='holiday') & (hour_df['season'] == 'Winter')].groupby('hour')['total'].sum()

#Bagaimana Windspeed mempengaruhi jumlah pesepeda di setiap musim 
#all
windspeed_all_df = day_df.groupby('windspeed')['total'].sum().reset_index()
sns.regplot(x='windspeed', y='total', data=windspeed_all_df, line_kws={'color': 'red'})
max_total_row = windspeed_all_df.loc[windspeed_all_df['total'].idxmax()]
windspeed_at_max_total = max_total_row['windspeed']

# Memilih baris yang sesuai dengan musim 'Spring'
windspeed_spring_df = day_df[day_df['season'] == 'Spring'].groupby('windspeed')['total'].sum().reset_index()
sns.regplot(x='windspeed', y='total', data=windspeed_spring_df, line_kws={'color': 'red'})
max_total_row = windspeed_spring_df.loc[windspeed_spring_df['total'].idxmax()]
windspeed_at_max_total = max_total_row['windspeed']

# Memilih baris yang sesuai dengan musim 'Summer'
windspeed_summer_df = day_df[day_df['season'] == 'Summer'].groupby('windspeed')['total'].sum().reset_index()
sns.regplot(x='windspeed', y='total', data=windspeed_summer_df, line_kws={'color': 'red'})
max_total_row = windspeed_summer_df.loc[windspeed_summer_df['total'].idxmax()]
windspeed_at_max_total = max_total_row['windspeed']

# Memilih baris yang sesuai dengan musim 'Fall'
windspeed_fall_df = day_df[day_df['season'] == 'Fall'].groupby('windspeed')['total'].sum().reset_index()
sns.regplot(x='windspeed', y='total', data=windspeed_fall_df, line_kws={'color': 'red'})
max_total_row = windspeed_fall_df.loc[windspeed_fall_df['total'].idxmax()]
windspeed_at_max_total = max_total_row['windspeed']

# Memilih baris yang sesuai dengan musim 'Winter'
windspeed_winter_df = day_df[day_df['season'] == 'Winter'].groupby('windspeed')['total'].sum().reset_index()
sns.regplot(x='windspeed', y='total', data=windspeed_winter_df, line_kws={'color': 'red'})
max_total_row = windspeed_winter_df.loc[windspeed_winter_df['total'].idxmax()]
windspeed_at_max_total = max_total_row['windspeed']



st.title("Bike Sharing Analysis")

selected_analysis=st.sidebar.selectbox(
    label="Pilih Hasil Analisis",
    options=('home','Peminjam Sepeda terhadap Musim', 'Peminjam Sepeda terhadap Cuaca', 'Peminjam Sepeda terhadap Cuaca saat Holiday', 'Peminjam Sepeda saat Windspeed Berbeda')
)

# Logika untuk menampilkan plot berdasarkan pilihan
if selected_analysis== 'home':
    st.markdown(
    """
    Program ini dianalisis dengan menggunakan Python yang dibantu 
    menggunkana library Pandas dengan memanfaatkan Seaborn dan Matplotlib
    Program ini menganalisis beberapa pertanyaan yang terkait jumlah peminjam sepeda
    serta hubungannya dengan musim
    """
)
elif selected_analysis == "Peminjam Sepeda terhadap Musim":
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(spring_hour_df.index, spring_hour_df.values, label='Spring')
    ax.plot(summer_hour_df.index, summer_hour_df.values, label='Summer')
    ax.plot(fall_hour_df.index, fall_hour_df.values, label='Fall')
    ax.plot(winter_hour_df.index, winter_hour_df.values, label='Winter')
    st.subheader("Jumlah Peminjam Sepeda Berdasarkan Waktu di Setiap Musim")
    ax.legend()
    ax.grid()
    st.pyplot(fig)

elif selected_analysis == 'Peminjam Sepeda terhadap Cuaca':
    st.subheader("Jumlah Peminjam Sepeda terhadap Cuaca di Setiap Musim")

    fig, axs = plt.subplots(1, 4, figsize=(20, 5))
    season_data = {
        'Spring': day_df[day_df['season'] == 'Spring']['weathersit'].value_counts(),
        'Summer': hour_df[hour_df['season'] == 'Summer']['weathersit'].value_counts(),
        'Fall': hour_df[hour_df['season'] == 'Fall']['weathersit'].value_counts(),
        'Winter': hour_df[hour_df['season'] == 'Winter']['weathersit'].value_counts()
    }

    # Plotting untuk setiap musim
    for i, (season, data) in enumerate(season_data.items()):
        ax = axs[i]
        ax.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140)
        ax.set_title(season)

    # Menampilkan plot
    plt.tight_layout()
    st.pyplot(fig)

elif selected_analysis == 'Peminjam Sepeda terhadap Cuaca saat Holiday':
    st.subheader("Jumlah Peminjam Sepeda saat Holiday Berdasarkan Waktu di Setiap Musim")
    fig, ax = plt.subplots(figsize=(15, 5))

    ax.plot(holiday_spring.index, holiday_spring.values, label='Spring')
    ax.plot(holiday_summer.index, holiday_summer.values, label='Summer')
    ax.plot(holiday_fall.index, holiday_fall.values, label='Fall')
    ax.plot(holiday_winter.index, holiday_winter.values, label='Winter')

    ax.legend()
    ax.grid()
    st.pyplot(fig)

elif selected_analysis == 'Peminjam Sepeda saat Windspeed Berbeda':
    fig, axs = plt.subplots(4, 1, figsize=(15, 20))
    
    # Plot untuk keseluruhan tahun
    windspeed_all_df['wind_category'] = pd.cut(windspeed_all_df['windspeed'],
                                                bins=[-float('inf'), 0.25, 0.5, float('inf')],
                                                labels=['Sejuk', 'Sedikit Kencang', 'Kencang'])
    sns.scatterplot(x='windspeed', y='total', hue='wind_category', data=windspeed_all_df, ax=axs[0])
    sns.regplot(x='windspeed', y='total', data=windspeed_all_df, scatter=False, line_kws={'color': 'red'}, ci=None, ax=axs[0])
    axs[0].set_title("Jumlah Pesepeda Berdasarkan Windspeed Secara Keseluruhan")

    # Plot untuk musim panas
    windspeed_summer_df['wind_category'] = pd.cut(windspeed_summer_df['windspeed'],
                                                   bins=[-float('inf'), 0.25, 0.5, float('inf')],
                                                   labels=['Sejuk', 'Sedikit Kencang', 'Kencang'])
    sns.scatterplot(x='windspeed', y='total', hue='wind_category', data=windspeed_summer_df, ax=axs[1])
    sns.regplot(x='windspeed', y='total', data=windspeed_summer_df, scatter=False, line_kws={'color': 'red'}, ci=None, ax=axs[1])
    axs[1].set_title("Jumlah Pesepeda Berdasarkan Windspeed pada Musim Panas")

    # Plot untuk musim gugur
    windspeed_fall_df['wind_category'] = pd.cut(windspeed_fall_df['windspeed'],
                                                 bins=[-float('inf'), 0.25, 0.5, float('inf')],
                                                 labels=['Sejuk', 'Sedikit Kencang', 'Kencang'])
    sns.scatterplot(x='windspeed', y='total', hue='wind_category', data=windspeed_fall_df, ax=axs[2])
    sns.regplot(x='windspeed', y='total', data=windspeed_fall_df, scatter=False, line_kws={'color': 'red'}, ci=None, ax=axs[2])
    axs[2].set_title("Jumlah Pesepeda Berdasarkan Windspeed pada Musim Gugur")

    # Plot untuk musim dingin
    windspeed_winter_df['wind_category'] = pd.cut(windspeed_winter_df['windspeed'],
                                                   bins=[-float('inf'), 0.25, 0.5, float('inf')],
                                                   labels=['Sejuk', 'Sedikit Kencang', 'Kencang'])
    sns.scatterplot(x='windspeed', y='total', hue='wind_category', data=windspeed_winter_df, ax=axs[3])
    sns.regplot(x='windspeed', y='total', data=windspeed_winter_df, scatter=False, line_kws={'color': 'red'}, ci=None, ax=axs[3])
    axs[3].set_title("Jumlah Pesepeda Berdasarkan Windspeed pada Musim Dingin")

    plt.tight_layout()
    st.pyplot(fig)


