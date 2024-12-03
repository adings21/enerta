import streamlit as st
import pandas as pd
import io
from cleanse_data import cleanse_data
from generate_invoice_journal import generate_invoice_journal
from generate_PurchasesSales_journal import generate_purchase_journal
from generate_payment_journal import generate_payment_journal

# Sidebar Menu
st.sidebar.title("Menu")
menu = st.sidebar.selectbox(
    "Pilih Menu",
    ["Cleansing Data", "Generate Template Jurnal"]
)

if menu == "Cleansing Data":
    st.title("Cleansing Data")
    uploaded_file = st.file_uploader("Upload File", type=["xlsx"])
    
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        st.write("Data Asli:")
        st.dataframe(df)

        # Menggunakan fungsi cleansing data
        cleansed_data, out_of_category = cleanse_data(df)
        
        st.write("Data Setelah Cleansing:")
        st.dataframe(cleansed_data)
        
        # Save cleansed data to a BytesIO object
        cleansed_data_bytes = io.BytesIO()
        cleansed_data.to_excel(cleansed_data_bytes, index=False)
        cleansed_data_bytes.seek(0)  # Rewind the BytesIO object
        
        st.download_button("Download Cleansed Data", cleansed_data_bytes, file_name="cleansed_data.xlsx")
        
        st.write("Data Out of Category:")
        st.dataframe(out_of_category)
        
        # Save out_of_category data to a BytesIO object
        out_of_category_bytes = io.BytesIO()
        out_of_category.to_excel(out_of_category_bytes, index=False)
        out_of_category_bytes.seek(0)
        
        st.download_button("Download Out of Category Data", out_of_category_bytes, file_name="out_of_category.xlsx")

elif menu == "Generate Template Jurnal":
    st.title("Generate Template Jurnal")
    sub_menu = st.selectbox(
        "Pilih Sub Menu",
        ["Generate Invoice Jurnal", "Generate Sales Invoice Jurnal", "Generate Payment Jurnal"]
    )
    account = st.selectbox(
        "Pilih Akun Kas Biz",
        [
            "KAS PT BOILER", "BASUKI HALMAHERA II", "KAS HCI", "KAS BHIRAWA STEEL",
            "KAS SWIF ASIA", "PROJECT UNL TANK", "KAS KOBE", "RAMLAN BSRNS",
            "KAS PETRODRILL", "PROJECT BMP", "KAS POCARI", "PROJECT INDOPELITA",
            "MASERAYA", "ARTOMORO"
        ]
    )

    uploaded_file = st.file_uploader("Upload File", type=["xlsx"])
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        st.write("Data Asli:")
        st.dataframe(df)

        if sub_menu == "Generate Invoice Jurnal":
            start_number = st.number_input("Mulai Nomor Urut", min_value=1, step=1)
            invoice_data = generate_invoice_journal(df, account, start_number)
            st.write("Hasil Generate Invoice Jurnal:")
            st.dataframe(invoice_data)
            
            # Save invoice_data to a BytesIO object
            invoice_data_bytes = io.BytesIO()
            invoice_data.to_excel(invoice_data_bytes, index=False)
            invoice_data_bytes.seek(0)
            
            st.download_button("Download Invoice Jurnal", invoice_data_bytes, file_name="invoice_journal.xlsx")

        elif sub_menu == "Generate Sales Invoice Jurnal":
            start_number = st.number_input("Mulai Nomor Urut", min_value=1, step=1)
            sales_data = generate_purchase_journal(df, account, start_number)
            st.write("Hasil Generate Sales Invoice Jurnal:")
            st.dataframe(sales_data)
            
            # Save sales_data to a BytesIO object
            sales_data_bytes = io.BytesIO()
            sales_data.to_excel(sales_data_bytes, index=False)
            sales_data_bytes.seek(0)
            
            st.download_button("Download Sales Invoice Jurnal", sales_data_bytes, file_name="sales_journal.xlsx")

        elif sub_menu == "Generate Payment Jurnal":
            start_number = st.number_input("Mulai Nomor Urut", min_value=1, step=1)
            payment_data = generate_payment_journal(df, account, start_number)
            st.write("Hasil Generate Payment Jurnal:")
            st.dataframe(payment_data)
            
            # Save payment_data to a BytesIO object
            payment_data_bytes = io.BytesIO()
            payment_data.to_excel(payment_data_bytes, index=False)
            payment_data_bytes.seek(0)
            
            st.download_button("Download Payment Jurnal", payment_data_bytes, file_name="payment_journal.xlsx")
