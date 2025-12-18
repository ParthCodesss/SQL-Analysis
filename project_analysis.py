import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# --- CONFIGURATION ---
db_user = 'parth'
db_password = '1234'
db_host = 'localhost'
db_port = '5478'
db_name = 'parth'

connection_str = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection_str)

# --- COMPLEX QUERY (Snake_Case Corrected) ---
# Changes: artistid -> artist_id, albumid -> album_id, etc.
sql_query = """
SELECT 
    ar.name as artist_name, 
    SUM(il.unit_price * il.quantity) AS total_sales
FROM artist ar
JOIN album al ON ar.artist_id = al.artist_id
JOIN track t ON al.album_id = t.album_id
JOIN invoice_line il ON t.track_id = il.track_id
JOIN genre g ON t.genre_id = g.genre_id
WHERE g.name = 'Rock'
GROUP BY ar.name
ORDER BY total_sales DESC
LIMIT 10;
"""

print("Extracting Music Store Data...")

try:
    df = pd.read_sql(sql_query, engine)
    print("✅ Data extracted successfully!")
    print(df)

    # --- VISUALIZATION ---
    plt.figure(figsize=(12, 6))

    # Bar Chart
    sns.barplot(x='total_sales', y='artist_name', data=df, palette='viridis')

    plt.title('Top 10 Rock Artists by Revenue', fontsize=16)
    plt.xlabel('Total Sales ($)', fontsize=12)
    plt.ylabel('Artist', fontsize=12)
    plt.grid(axis='x', linestyle='--', alpha=0.3)

    plt.tight_layout()
    plt.show()

except Exception as e:
    print("\n❌ Error:", e)