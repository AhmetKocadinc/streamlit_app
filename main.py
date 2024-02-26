import streamlit as st
import pickle
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


with open('data.pickle', 'rb') as file1:
    h_model = pickle.load(file1)

with open('price.pickle', 'rb') as file2:
    p_model = pickle.load(file2)

st.set_page_config(page_title='Ahmet Kocadinç Projeler')
tabs = ['Kalp Krizi Risk Tahmini',  'Ev Fiyat Tahmini', 'Hakkımda']

page = st.sidebar.radio('Ana Menü', tabs)

if page == 'Kalp Krizi Risk Tahmini':
    st.title('Kalp Krizi Risk Tahmini')
    st.write("""Bu sayfada istenen hasta bilgilerini girerek hastanın kalp krizi riski durumunu gözlemleyebilirsiniz""")
    col1, col2 = st.columns(2)
    with col1:
        age = st.text_input('Hastanın Yaşını Giriniz')
        cholesterol = st.text_input('Kolestrol Değerini Giriniz')
        chest = st.selectbox('Göğüs Ağrı Tipini Seçiniz', ['ATA', 'NAP', 'ASY', 'TA'])
        rest = st.text_input('Dinlenik Nabız Değerini Giriniz')

    with col2:
        sex = st.selectbox('Cinsiyet Seçiniz', ['Kadın', 'Erkek'])
        ekg = st.selectbox('EKG Sonuç Durumunu Giriniz', ['Normal', 'ST', 'LVH'])
        max_hr = st.text_input('Maksimum Nabız Değerini Giriniz.')
        st_slope = st.selectbox('Egzersiz Nabzının Durumu', ['Yukarı', 'Stabil', 'Aşağı'])
    buton = st.button('Sonucu Göster')

    if buton:
        def cins(deger):
            if deger == 'Erkek':
                return 1
            else:
                return 2


        def chest(deger):
            if deger == 'ATA':
                return 1
            elif deger == 'NAP':
                return 2
            elif deger == 'ASY':
                return 3
            else:
                return 4


        def kg(deger):
            if deger == 'Normal':
                return 1
            elif deger == 'ST':
                return 2
            else:
                return 3


        def slp(deger):
            if deger == 'Yukarı':
                return 1
            elif deger == 'Stabil':
                return 2
            else:
                return 3


        sex_num = cins(sex)
        chest_num = chest(chest)
        ekg_num = kg(ekg)
        slope_num = slp(st_slope)

        input_data = {
            'Age': [int(age)],
            'Sex': [int(sex_num)],
            'ChestPainType': [int(chest_num)],
            'RestingBP': [int(rest)],
            'Cholesterol': [int(cholesterol)],
            'RestingECG': [int(ekg_num)],
            'MaxHR': [int(max_hr)],
            'ST_Slope': [int(slope_num)]
        }

        input_df = pd.DataFrame(input_data)

        prediction = h_model.predict(input_df)

        if prediction[0] == 1:
            st.error('Hastada Kalp Krizi Riski Bulunmaktadır')
        else:
            st.success('Hastada Kalp Krizi Riski Bulunmuyor')


if page == 'Ev Fiyat Tahmini':
    st.title("Ev Fiyat Tahmini")
    st.write("""Bu sayfada evin özelliklerini ilgili yerlere girerek fiyat tahmini yapabilirsiniz""")

    col1, col2, col3 = st.columns(3)

    tip = st.selectbox('Satış tipini seçiniz', ['Condo for sale', 'House for sale' ,'Townhouse for sale', 'Co-op for sale'
                                                'Multi-family home for sale' ,'For sale', 'Contingent', 'Land for sale'
                                                'Foreclosure', 'Pending' ,'Coming Soon', 'Mobile house for sale'
                                                'Condop for sale'])
    beds = st.slider('Yatak odası sayısını giriniz', 0,10,0)
    baths = st.slider('Banyo sayısını giriniz', 0, 10, 0)
    location = st.selectbox('Lütfen Lokasyon Seçiniz', ['New York' ,'New York County', 'The Bronx' ,'Kings County' ,'Bronx County',
                                                        'Queens County' ,'Richmond County', 'United States' ,'Brooklyn', 'Queens', 'Flatbush'])

    sublocation = st.selectbox('Lütfen Alt Lokasyon Seçiniz',
                            ['Manhattan' ,'New York County','Richmond County', 'Kings County', 'New York',
                             'East Bronx' 'Brooklyn' 'The Bronx' 'Queens' 'Staten Island'
                             'Queens County' ,'Bronx County', 'Coney Island', 'Brooklyn Heights',
                             'Jackson Heights' ,'Riverdale' ,'Rego Park', 'Fort Hamilton', 'Flushing',
                             'Dumbo', 'Snyder Avenue'])

    metre = st.text_input('Lütfen Evin Metrekaresini giriniz.')
    butons = st.button('Ev Fiyatını Hesapla')

    if butons:

        def piss(deger):
            if deger == 'Condo for sale':
                return 1
            elif deger == 'House for sale':
                return 2
            elif deger == 'Townhouse for sale':
                return 3
            elif deger == 'Co-op for sale':
                return 4
            elif deger == 'Multi-family home for sale':
                return 5
            elif deger == 'For sale':
                return 6
            elif deger == 'Contingent':
                return 7
            elif deger == 'Land for sale':
                return 8
            elif deger == 'Foreclosure':
                return 9
            elif deger == 'Pending':
                return 10
            elif deger == 'Coming Soon':
                return 11
            elif deger == 'Mobile house for sale':
                return 12
            else:
                return 13

        def loc(deger):
            if deger == 'New York':
                return 1
            elif deger == 'New York County':
                return 2
            elif deger == 'The Bronx':
                return 3
            elif deger == 'Kings County':
                return 4
            elif deger == 'Bronx County':
                return 5
            elif deger == 'Queens County':
                return 6
            elif deger == 'Richmond County':
                return 7
            elif deger == 'United States':
                return 8
            elif deger == 'United States':
                return 9
            elif deger == 'Brooklyn':
                return 10
            elif deger == 'Queens':
                return 11
            else:
                return 12

        def subloc(deger):
            if deger == 'Manhattan':
                return 1
            elif deger == 'New York County':
                return 2
            elif deger == 'Richmond County':
                return 3
            elif deger == 'Kings County':
                return 4
            elif deger == 'New York':
                return 5
            elif deger == 'East Bronx':
                return 6
            elif deger == 'Brooklyn':
                return 7
            elif deger == 'The Bronx':
                return 8
            elif deger == 'The Bronx':
                return 9
            elif deger == 'Queens':
                return 10
            elif deger == 'Staten Island':
                return 11
            elif deger == 'Queens County':
                return 12
            elif deger == 'Bronx County':
                return 13
            elif deger == 'Coney Island':
                return 14
            elif deger == 'Brooklyn Heights':
                return 15
            elif deger == 'Jackson Heights':
                return 16
            elif deger == 'Riverdale':
                return 17
            elif deger == 'Riverdale':
                return 18
            elif deger == 'Rego Park':
                return 19
            elif deger == 'Fort Hamilton':
                return 20
            elif deger == 'Flushing':
                return 21
            elif deger == 'Dumbo':
                return 22
            else:
                return 23

        num_tip = piss(tip)
        num_location = loc(location)
        num_sub = subloc(sublocation)

        inputs = {
            'type' : [int(num_tip)],
            'beds' : [int(beds)],
            'bath' : [int(baths)],
            'location' : [int(num_location)],
            'sublocation': [int(num_sub)],
            'property': [int(metre)]
        }

        inputs_df = pd.DataFrame(inputs)

        ev_predict = p_model.predict(inputs_df)

        st.success(f'Evin tahmini fiyatı {ev_predict}')


if page == 'Hakkımda':
    st.header('Ahmet KOCADİNÇ')
    st.subheader('Veri Analisti / Veri Bilimci')

    st.image("vesika.jpg", use_column_width=True, width=300)

    st.write("""
    Merhaba, ben Ahmet Kocadinç.
    """)
    st.write("""
    Veri Analizi pozisyonuna olan ilgimle birlikte İstanbul Bilgi Üniversitesi Yönetim Bilişim Sistemleri bölümünde yüksek lisansımı büyük veri ile üretimin geliştirilmesi konusunda yaptığım proje ile tamamladım. Şu anda da Kodlasam Akademi de veri analizi sertifikasyon eğitimine devam ediyorum. Ayrıca veri analizi ve veri bilimi alanlarında kalitelerini kanıtlamış olan miuul, udemy ve Turkcell geleceği yazanlar gibi kurumların sağlamış olduğu eğitimleri de alarak ve sürekli projeler yaparak kendimi en iyi şekilde geliştiriyorum. Veri analizine olan tutkum beni çok hızlı ve sürekli öğrenmeye itiyor.
        """)
    st.write("""
    ## Eğitim

    - Lisans: İşletme Fakültesi- Eskişehir Anadolu Üniversitesi- 2016
    - Yüksek Lisans: Yönetim Bilişim Sistemleri - 2018

    ## Yetenekler

    - Python programlama
    - Veri analizi
    - Veri Görselleştirme
    - Makine Öğrenmesi
    - Yapay Zeka
    - Tahmin üretme
    - SQL ile veri analizi
    - SQL ile veri sorgulama

    ## Sosyal Medya ve Portfolyo
    Yaptığım tüm projelere kaggle ve github linklerinden ulaşabilirsiniz.

    - [Linkedin](https://www.linkedin.com/in/ahmet-kocadin%C3%A7-500673174/)
    - [GitHub](https://github.com/AhmetKocadinc)
    - [Kaggle](https://www.kaggle.com/ahmetkocadinc)

    """)
