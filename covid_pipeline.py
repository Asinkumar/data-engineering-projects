import requests
import json
import pandas as pd
url =  "https://disease.sh/v3/covid-19/countries"

response = requests.get(url)
data = response.json()

print(f"data fetched")
print(f"status_code {response.status_code}")
print(f"saving raw data to the file")
with open("cord.json" ,"w") as f:
  json.dump(data,f, indent = 4)
  print(f" data saved!")
df = pd.DataFrame(data)
print(f" loaded {df.shape[0]} countries" )
print(f" total columns { df.shape[1]},")



print(f"data cleaning ")
df = df[["country","cases","deaths","recovered","active","population"]]
before = len(df)
df.dropna()
after = len(df)
print(f"cleaned rows: {after}")


df["death_rate"] = (df["deaths"] / df["cases"] * 100).round(2)
df["recovery_rate"] = (df["recovered"] / df["cases"] * 100).round(2)
print("Added death_rate column")
print(" Added recovery_rate column")


print("STEP 6: Analysis Results")


print("\n Top 5 by Total Cases:")
top5 = df.nlargest(5, "cases")[["country","cases","deaths"]]
for _, row in top5.iterrows():
    print(f"  {row['country']:<15} {row['cases']:>12,} cases")

print("\n Top 5 Death Rate:")
top_death = df.nlargest(5, "death_rate")[["country","death_rate"]]
for _, row in top_death.iterrows():
    print(f"  {row['country']:<15} {row['death_rate']}%")
print("\n Top 5 Recovery Rate:")
top_rec = df.nlargest(5, "recovery_rate")[["country","recovery_rate"]]
for _, row in top_rec.iterrows():
    print(f"  {row['country']:<15} {row['recovery_rate']}%")


print("STEP 7: Saving clean data...")


df.to_csv("clean_covid.csv", index=False)
df.to_json("clean_covid.json", orient="records", indent=4)
print(" Saved clean_covid.csv")
print("Saved clean_covid.json")



print(" PIPELINE COMPLETE!")
print(f"   Countries processed : {len(df)}")
print(f"   Files created       : raw_covid.json,")
print(f"                         clean_covid.csv,")
print(f"                         clean_covid.json")
print("=" * 50)

