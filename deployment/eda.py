import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(
    page_title = 'OUTCOME CAR INSURANCE DATA - EDA',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    #membuat title
    st.title('CAR INSURANCE DATA PREDICTION')
    
    
    #membuat subheader
    st.subheader('LINDUNGI MOBIL MU SEBELUM AKU MELINDUNGIMU')
    
    #menambahkan gambar
    st.image('https://hondapasuruan.co.id/wp-content/uploads/2021/10/Tips-Asuransi-Mobil-Yang-Paling-Sesuai-Kebutuhan-Honda-Pasuruan.jpg')
    caption= ('Car Insurance Data')  
    
    #menambahkan deskripsi
    st.write('# Page ini dibuat oleh Salman Hamka De Qais Untuk Menampilkan Exploratory Data Analis')
        
    
    #membuat garis
    st.markdown('---')
    
    
    #magicsyntax
    '''
    pada page ini, penuis akan melakukan explorasi sederhana, dataset yang digunakan adalah dataset Car Insurance Data. dataset ini berasa dari bigquery.com.
    
    '''    
    
    #showdatabase
    df = pd.read_csv('Car_Insurance_Claim.csv')
    st.dataframe(df)


    # Streamlit app
    st.title('Exploratory Data Analysis: Distribusi Usia')
    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df['AGE'], kde=True, ax=ax)
    ax.set_title('Distribusi Usia')
    ax.set_xlabel('Usia')
    ax.set_ylabel('Frekuensi')
    # Display the plot in the Streamlit app
    st.pyplot(fig)
    
    
    
    
    # Gender Distribution Pie Chart
    st.subheader('Distribusi Jenis Kelamin')
    gender_counts = df['GENDER'].value_counts()
    fig2, ax2 = plt.subplots(figsize=(5, 5))
    ax2.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff'])
    ax2.set_title('Distribusi Jenis Kelamin')
    st.pyplot(fig2)
    
    # Outcome Distribution Plot
    st.subheader('Distribution of Insurance Claims')
    fig3, ax3 = plt.subplots(figsize=(5, 6))
    sns.countplot(x='OUTCOME', data=df, palette='viridis', ax=ax3)
    ax3.set_title('Distribution of Insurance Claims')
    ax3.set_xlabel('Outcome (0: No Claim, 1: Claim)')
    ax3.set_ylabel('Count')
    st.pyplot(fig3)


    # Driving Experience vs Speeding Violations
    st.subheader('Perbandingan Pengalaman Mengemudi dengan Pelanggaran Kecepatan')
    fig4, ax4 = plt.subplots(figsize=(6, 6))
    sns.scatterplot(x='DRIVING_EXPERIENCE', y='SPEEDING_VIOLATIONS', data=df, hue='GENDER', ax=ax4)
    ax4.set_title('Pengalaman Mengemudi vs Pelanggaran Kecepatan')
    ax4.set_xlabel('Pengalaman Mengemudi (tahun)')
    ax4.set_ylabel('Pelanggaran Kecepatan')
    st.pyplot(fig4)

    # Credit Score vs Outcome
    st.subheader('Credit Score vs Outcome')
    fig5, ax5 = plt.subplots(figsize=(12, 10))
    sns.boxplot(x='OUTCOME', y='CREDIT_SCORE', data=df, palette='viridis', ax=ax5)
    ax5.set_title('Credit Score vs Outcome')
    ax5.set_xlabel('Outcome')
    ax5.set_ylabel('Credit Score')
    st.pyplot(fig5)

    # Vehicle Type Count Plot
    st.subheader('Jumlah Kendaraan berdasarkan Jenis')
    fig6, ax6 = plt.subplots(figsize=(10, 6))
    sns.countplot(x='VEHICLE_TYPE', data=df, ax=ax6)
    ax6.set_title('Jumlah Kendaraan berdasarkan Jenis')
    ax6.set_xlabel('Jenis Kendaraan')
    ax6.set_ylabel('Jumlah')
    st.pyplot(fig6)


    # Annual Mileage vs Outcome
    st.subheader('Annual Mileage vs Outcome')
    fig7, ax7 = plt.subplots(figsize=(14, 10))
    sns.boxplot(x='OUTCOME', y='ANNUAL_MILEAGE', data=df, palette='viridis', ax=ax7)
    ax7.set_title('Annual Mileage vs Outcome')
    ax7.set_xlabel('Outcome')
    ax7.set_ylabel('Annual Mileage')
    st.pyplot(fig7)

    # Driving Experience by Outcome
    st.subheader('Driving Experience by Outcome')
    fig8, ax8 = plt.subplots(figsize=(14, 10))
    sns.boxplot(x='OUTCOME', y='DRIVING_EXPERIENCE', data=df, palette='viridis', ax=ax8)
    ax8.set_title('Driving Experience by Outcome')
    ax8.set_xlabel('Outcome')
    ax8.set_ylabel('Driving Experience')
    st.pyplot(fig8)

      
        
if __name__ == '__main__':
    run()
    
