# 🎵 SQL & Python Data Analytics: Digital Music Store Analysis

## 📌 Project Overview
This project demonstrates a full-stack data analysis workflow—from raw data ingestion to actionable business insights. Using the **Chinook Database** (a digital media store schema), I analyzed sales data to identify top-performing rock artists, helping the business optimize inventory and marketing strategies.

The project bridges the gap between **SQL** (for data extraction and complex joins) and **Python** (for statistical analysis and visualization).

## 🚀 Business Problem
The fictitious media store needed to identify **which Rock artists generate the highest revenue** to decide which albums to promote in the upcoming quarter. 
* **Challenge:** Data was scattered across 4 normalized tables (`Artist`, `Album`, `Track`, `Invoice_Line`).
* **Solution:** Designed a multi-table SQL JOIN query to aggregate sales and visualized the results in Python.

## 🛠️ Tech Stack & Tools
* **Database:** PostgreSQL 16 (Hosted locally via Postgres.app)
* **SQL Client:** pgAdmin 4
* **Language:** Python 3.11
* **Libraries:** `pandas`, `sqlalchemy`, `matplotlib`, `seaborn`
* **IDE:** VS Code

---

## 📊 Database Schema (Chinook)
I worked with a normalized relational schema including:
* **`artist`**: Artist names and IDs.
* **`album`**: Linked to artists.
* **`track`**: Linked to albums and genres.
* **`invoice_line`**: Transactional sales data.

*(The project involved handling schema inconsistencies, such as converting `TitleCase` legacy naming conventions to PostgreSQL standard `snake_case`.)*

---

## 📝 Key SQL Analysis
To extract the insights, I wrote a complex query joining **four tables**.

```sql
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
