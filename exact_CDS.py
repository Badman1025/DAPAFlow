import pandas as pd
df = pd.read_csv("1.Homo_sapiens_TarBase-v9.tsv", sep='\t')
first_row = df.iloc[0:1]
filtered_df = df[df.iloc[:, 5] == 'CDS']
result_df = pd.concat([first_row, filtered_df], ignore_index=True)
result_df.to_csv('TarBase_CDS.tsv', sep='\t', index=False)
