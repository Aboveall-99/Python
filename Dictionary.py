
import pandas as pd
import matplotlib.pyplot as plt


advert_data = {
    "tv": [23000, 44000, 17000, 15000, 18000, 87000,
           57000],
    "radio": [37000, 39000, 45000, 41000, 36000, 28000,
              42000],
    "sales": [221000, 304000, 197000, 188000, 215000, 450000,
              365000]
}
df = pd.DataFrame(advert_data)
df.to_csv('cleaned_data.csv', index=False)