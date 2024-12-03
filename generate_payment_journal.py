import pandas as pd

def generate_payment_journal(df, account, start_number):
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

    # Mapping akun kas ke kode akun
    account_codes = {
        "KAS PT BOILER": "1-11011-00063",
        "BASUKI HALMAHERA II": "1-11011-00059",
        "KAS HCI": "1-11011-00061",
        "KAS BHIRAWA STEEL": "1-11011-00065",
        "KAS SWIF ASIA": "1-11011-00043",
        "PROJECT UNL TANK": "1-11011-00040",
        "KAS KOBE": "1-11011-00060",
        "RAMLAN BSRNS": "1-110102",
        "KAS PETRODRILL": "1-11011-00058",
        "PROJECT BMP": "1-11011-00019",
        "KAS POCARI": "1-11011-00064",
        "PROJECT INDOPELITA": "1-11011-00050",
        "MASERAYA": "1-11011-00066",
        "ARTOMORO": "1-11011-00067"
    }

    # Tentukan project code berdasarkan akun kas yang dipilih
    project_code = project_codes.get(account, "")

    # Ekstrak huruf tengah dan angka kedua dari kode proyek
    project_short_code = "".join(project_code.split("_")[2:3] + project_code.split("_")[1:2])

    # Tambahkan kolom sesuai kebutuhan
    df['*Payment Number'] = [f"PP-{project_short_code}-{i+start_number}-24" for i in range(len(df))]
    df['*InvoiceNumber'] = [f"PI-{project_short_code}-{i+start_number}-24" for i in range(len(df))]
    df['*Pay from account(Code)'] = account_codes.get(account, "")
    df['*PaymentDate'] = pd.to_datetime(df['Tanggal'], format='%d %b %Y, %H.%M', errors='coerce').dt.strftime('%d/%m/%Y')
    df['*Amount'] = df['Pengeluaran']
    df['*PaymentMethod'] = "Cash"
    df['Tags (use'] = project_code  # Tags berdasarkan kode proyek

    # Pilih kolom untuk output
    output_columns = [
        '*Payment Number', '*InvoiceNumber', '*PaymentDate', '*Amount', '*PaymentMethod',
        '*Pay from account(Code)', 'Tags (use'
    ]

    return df[output_columns]
