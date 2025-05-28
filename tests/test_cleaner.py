import pandas as pd
from excel_cleaner import clean_xlsx

def test_clean_xlsx(tmp_path):
    sample = tmp_path / "demo.xlsx"
    pd.DataFrame({"A": [1, None]}).to_excel(sample, index=False)
    df = clean_xlsx(sample)
    assert df.iloc[0, 0] == 1
