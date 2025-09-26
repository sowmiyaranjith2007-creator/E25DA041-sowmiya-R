import pandas as pd
df = pd.DataFrame({
    "ID": [1, 2, 3, 4, 5],
    "Age": [25, None, 30, 22, None],
    "Salary": [50000, 60000, None, 45000, 70000],
    "Department": ["HR", "Finance", None, "IT", None]
})
print("Original DataFrame:")
print(df)
num_cols = df.select_dtypes(include=['number']).columns
cat_cols = df.select_dtypes(include=['object']).columns
for col in num_cols:
    df[col] = df[col].fillna(df[col].mean())
for col in cat_cols:
    if not df[col].mode().empty:
        df[col] = df[col].fillna(df[col].mode()[0])
print("\nCleaned DataFrame:")
print(df)