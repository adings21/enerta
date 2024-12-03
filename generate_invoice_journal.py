import pandas as pd

def generate_invoice_journal(df, account, start_number):
    # Mapping akun kas ke project code
    project_codes = {
        "KAS PT BOILER": "24_52_BTS_IS",
        "BASUKI HALMAHERA II": "24_51_BSK(HLM)_IS",
        "KAS HCI": "24_53_HCI_IS",
        "KAS BHIRAWA STEEL": "24_55_BRS_IS",
        "KAS SWIF ASIA": "24_56_SAF_IS",
        "PROJECT UNL TANK": "24_58_UNL_IS",
        "KAS KOBE": "24_59_KOB_IS",
        "RAMLAN BSRNS": "24_60_BSR_IS",
        "KAS PETRODRILL": "24_62_PTR_IS",
        "PROJECT BMP": "24_64_BMP_IS",
        "KAS POCARI": "24_66_PCR_IS",
        "PROJECT INDOPELITA": "24_68_IND_IS",
        "MASERAYA": "24_70_MRY_IS",
        "ARTOMORO": "24_72_ART_IS"
    }
    
    # Mapping kategori ke *Customer
    customer_mapping = {
        "2 TRANSPORTAION MATERIAL EXPENSE": "Overhead",
        "2 LABOUR DAILY WAGES EXPENSE": "BTKL",
        "2 LABOUR TRANSPORTAION PROJECT EXPENSE": "BTKL",
        "2 LABOUR ACCOMODATION EXPENSE": "BTKL",
        "2 MEAL LABOUR EXPENSE": "BTKL",
        "2 SUPPLIES PROJECT EXPENSE": "Overhead",
        "2 GENERAL ADMINISTRATION EXPENSE": "Overhead",
        "2 RAW MATERIAL": "BB",
        "1 BEBAN BANK": "Overhead",
        "2 ENTERTAINMENT PROJECT EXPENSE": "Overhead",
        "2 MEDICAL EXPENSE": "BTKL",
    }

    # Tentukan project code berdasarkan akun kas yang dipilih
    project_code = project_codes.get(account, "")
    
    # Ekstrak kode project untuk *InvoiceNumber
    extracted_code = "".join(project_code.split("_")[2:3] + project_code.split("_")[1:2])
    
    # Format tanggal
    df['*InvoiceDate'] = pd.to_datetime(df['Tanggal'], format='%d %b %Y, %H.%M', errors='coerce').dt.strftime('%d/%m/%Y')
    df['*DueDate'] = pd.to_datetime(df['Tanggal'], format='%d %b %Y, %H.%M', errors='coerce').dt.strftime('%d/%m/%Y')
    
    # Tambahkan kolom lainnya
    df['*Customer'] = df['Kategori'].map(customer_mapping)
    df['Email'] = ''
    df['BillingAddress'] = ''
    df['ShippingAddress'] = ''
    df['ShippingDate'] = ''
    df['ShipVia'] = ''
    df['TrackingNo'] = ''
    df['CustomerRefNo'] = ''
    df['*InvoiceNumber'] = [f"SA-{extracted_code}-{i+start_number}-24" for i in range(len(df))]
    df['Message'] = ''
    df['Memo'] = ''
    df['*ProductName'] = project_code
    df['Description'] = df['Deskripsi']
    df['*Quantity'] = 1
    df['*UnitPrice'] = df['Pengeluaran']
    df['ProductDiscountRate(%)'] = ''
    df['InvoiceDiscountRate(%)'] = ''
    df['TaxName'] = ''
    df['TaxRate(%)'] = ''
    df['ShippingFee'] = ''
    df['WitholdingAccountCode'] = ''
    df['WitholdingAmount(value or %)'] = ''
    df['#paid?(yes/no)'] = ''
    df['#PaymentMethod'] = ''
    df['#PaidToAccountCode'] = ''
    df['Tags (use'] = f"{project_code},Project In Process"

    # Pilih kolom untuk output
    output_columns = [
        '*Customer', 'Email', 'BillingAddress', 'ShippingAddress', '*InvoiceDate', '*DueDate',
        'ShippingDate', 'ShipVia', 'TrackingNo', 'CustomerRefNo', '*InvoiceNumber', 'Message', 
        'Memo', '*ProductName', 'Description', '*Quantity', '*UnitPrice', 'ProductDiscountRate(%)',
        'InvoiceDiscountRate(%)', 'TaxName', 'TaxRate(%)', 'ShippingFee', 'WitholdingAccountCode',
        'WitholdingAmount(value or %)', '#paid?(yes/no)', '#PaymentMethod', '#PaidToAccountCode', 
        'Tags (use'
    ]

    return df[output_columns]
