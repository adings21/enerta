def cleanse_data(df):
    # Mapping kategori yang valid
    valid_categories = [
        "2 TRANSPORTAION MATERIAL EXPENSE",
        "2 LABOUR DAILY WAGES EXPENSE",
        "2 LABOUR TRANSPORTAION PROJECT EXPENSE",
        "2 LABOUR ACCOMODATION EXPENSE",
        "2 MEAL LABOUR EXPENSE",
        "2 SUPPLIES PROJECT EXPENSE",
        "2 GENERAL ADMINISTRATION EXPENSE",
        "2 RAW MATERIAL",
        "1 BEBAN BANK",
        "2 ENTERTAINMENT PROJECT EXPENSE",
        "2 MEDICAL EXPENSE",
    ]
    
    # Filter data yang sesuai dengan kategori valid
    cleansed_data = df[df['Kategori'].isin(valid_categories)]
    
    # Filter data yang tidak sesuai dengan kategori valid
    out_of_category = df[~df['Kategori'].isin(valid_categories)]
    
    return cleansed_data, out_of_category
