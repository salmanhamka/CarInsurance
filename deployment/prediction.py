import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn

with open('gridsearch.pkl', 'rb') as file_1:
    grid_search_best = pickle.load(file_1)   


def run():
    with st.form("my_form"):
        dataid = st.number_input('Masukan Id', min_value=10,  max_value=10000, value=50, help='masukan Id berupa angka')
        Umur = st.selectbox('masukan umur', ('65+', '16-25', '26-39', '40-64'), index=1) 
        JenKelamin = st.selectbox('Masukan Jenis Kelamin', ('female', 'male'), index=1) 
        ras =  st.selectbox('masukan Ras', ('majority', 'minority'), index=1) 
        Expdrive = st.selectbox('Pilih Pengalaman Mengemudi', ('0-9y', '10-19y', '20-29y', '30y+'), index=1)
        pendidikan = st.selectbox('Pilih Pendidikan', ('none', 'high school', 'university'), index=1)
        pendapatan = st.selectbox('Masukan Pendapatan', ('upper class', 'poverty', 'working class', 'middle class'), index=1)
        skorkredit = st.number_input('Masukan Skor Kredit', min_value=0.0, max_value=3000.0, value=2.0) 
        statuskendaraan = st.selectbox('Status kepemilikan kendaraan', ('Milik Pribadi', 'Rental/Sewa'), index=1)
        tahunkendaraan = st.selectbox('Pilih Tahun Kendaraan', ('After 2015', 'Before 2015'), index=1)
        status = st.selectbox('Pilih Status Pernikahan', ('Sudah Menikah', 'Belum Menikah'), index=1)
        memilikiketurunan = st.selectbox('Memiliki Keturunan', ('Iya', 'Belum'), index=1)
        codepos = st.selectbox('Masukan kode pos', (10238, 32765, 92101, 21217), index=1)
        jaraktempuh = st.selectbox('Masukan jarak tempuh', (12000, 16000, 11000, 13000, 14000, 10000,8000,18000, 17000, 7000, 15000, 9000, 5000, 6000, 19000, 4000, 3000, 2000, 20000, 21000), index=1)
        jeniskendaraan = st.selectbox('Pilih Jenis Kendaraan', ('sedan', 'sports car'), index=1)
        pelanggaran = st.number_input('masukan berapa banyak pelanggaran', min_value=1.0, max_value=22.0, value=5.0)
        pengaruhobat = st.number_input('Seberapa kuat pengaruh obat-obatan', min_value=0.0, max_value=6.0, value=1.0, help='Indikator Seberapa kuat berpengaruh obat-obatan (masukan dengan angka)')
        historykecelakaan = st.number_input('Berapa Kali Kecelakaan Sebelum nya', min_value=0.0, max_value=15.0, value=1.0, help='Berapa sering mengalami kecelakaan')
       
        submitted = st.form_submit_button("Submit")

        st.write("Outside the form")

    #create new data 
    data_inf = {
        'id' : dataid,
        'age' : Umur,
        'gender' : JenKelamin,
        'race' :  ras,
        'driving_experience' : Expdrive,
        'education' : pendidikan,
        'income' : pendapatan,
        'credit_score' : skorkredit,
        'vehicle_ownership' : statuskendaraan,
        'vehicle_year' : tahunkendaraan ,
        'married' : status,
        'children' : memilikiketurunan,
        'postal_code' : codepos,
        'annual_mileage' : jaraktempuh,
        'vehicle_type' : jeniskendaraan,
        'speeding_violations' : pelanggaran,
        'duis' : pengaruhobat,
        'past_accidents' : historykecelakaan
        }
    
    data_inf = pd.DataFrame([data_inf])
    
    if submitted:
        result= grid_search_best.predict(data_inf)
        for i in result: 
            if i == 0:
                st.write("Tidak Claim Assuransi")
            else:
                st.write("Claim Assuransi")
    
if __name__ == '__main__':
 run()


