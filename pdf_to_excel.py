import numpy as np
import tabula

df = tabula.read_pdf("table.pdf", pages=1)[0]

cols = list(df.iloc[:6].apply(lambda x: " ".join([str(i) for i in x if i is not np.NAN])))

df1 = df.iloc[6:]
df1.columns = cols
df1.fillna(method='ffill', inplace=True)

df1.to_excel('demo_pdf.xlsx', index=False)

