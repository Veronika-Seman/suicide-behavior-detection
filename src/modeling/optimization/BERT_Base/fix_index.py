import pandas as pd
"""
# טען את הקובץ
df = pd.read_csv("train_val.csv")

# הפוך את עמודת 'index' לאינדקס
df.set_index('index', inplace=True)

# שמור מחדש עם אותו שם (או חדש)
df.to_csv("train_val_fixed.csv")
"""
"""
# טען את הקבצים
folds_df = pd.read_csv("fold_assignments.csv")
train_val_df = pd.read_csv("train_val_fixed.csv", index_col=0)

# סינון רק למה שקיים ב-train_val
valid_folds_df = folds_df[folds_df['index'].isin(train_val_df.index)]

# שמירה לקובץ חדש
valid_folds_df.to_csv("fold_assignments_fixed.csv", index=False)
"""

# שלב 1: טען את הקבצים
folds_df = pd.read_csv("fold_assignments_fixed.csv")
train_val_df = pd.read_csv("train_val.csv")

# שלב 2: שמור רק את התצפיות שיש להן אינדקסים בקובץ הקיפולים
filtered_df = train_val_df.loc[train_val_df.index.isin(folds_df['index'])].copy()

# שלב 3: מחק עמודת 'Unnamed: 0' אם קיימת
if 'Unnamed: 0' in filtered_df.columns:
    filtered_df.drop(columns=['Unnamed: 0'], inplace=True)

# שלב 4: שמור לקובץ חדש
filtered_df.to_csv("train_val_fixed.csv", index=False)

print("✔️ train_val_fixed.csv נשמר בהצלחה.")
