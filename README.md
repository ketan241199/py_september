# 📘 Project: Data Scraping, Analysis, and REST API with SQL

## 📖 Overview
This project is designed to **learn and practice end-to-end data engineering concepts**:  
1. **Scraping data** from open sources using **Scrapy**.  
2. **Analyzing and cleaning** data using Python.  
3. **Storing data** in a SQL database for structured access.  
4. **Serving data** through a REST API.  

The project helps in building skills around **data pipelines, Scrapy, SQL integration, REST API design, and data analysis.**

---

## 📂 Project Structur
```txt
  data-scraping-analysis-api/
  │── README.md
  │── requirements.txt
  │── scrape/ # Scrapy project (spiders, pipelines, middlewares)
  │ └── scrapy.cfg
  │── analysis/ # Data cleaning, processing, and visualization
  │── database/ # SQL schema and models
  │── api/ # REST API (FastAPI/Flask)
  │── tests/ # Unit tests
  │── docs/ # Documentation & reports
  │── dataset/ # Raw + processed data
```

  
---

## 📊 Dataset
We will use an **open-source dataset with lakhs of records**, scraped or bulk-downloaded. 
- [https://books.toscrape.com/](https://books.toscrape.com/)


## 🚀 Features
- ✅ **Scraping with Scrapy spiders** (crawl pages, extract structured data).  
- ✅ **Data pipelines** (Scrapy item pipelines for cleaning + saving to CSV/SQL).  
- ✅ **Data Cleaning & Preprocessing** (using pandas).  
- ✅ **Exploratory Data Analysis (EDA)** (visualizations & statistics).  
- ✅ **SQL Storage** (PostgreSQL/MySQL/SQLite).  
- ✅ **REST API** with FastAPI to query data.  
- ✅ **Unit Tests** for spiders, pipelines, DB, and API.  

---

## 📦 Requirements
Create a `requirements.txt`:

```txt
# Core
pandas
numpy
matplotlib
seaborn

# Scraping
scrapy
lxml

# Database
sqlalchemy
psycopg2-binary   # PostgreSQL (or mysqlclient for MySQL)

# API
fastapi
uvicorn

# Testing
pytest
```

# Installation
## Clone repo
git clone https://github.com/your-username/data-scraping-analysis-api.git
cd data-scraping-analysis-api

## Create virtual environment
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate     # (Windows)

## Install requirements
pip install -r requirements.txt

## Start Scrapy crawl
cd scrape
scrapy crawl imdb_spider -o ../dataset/imdb_data.json

## Run FastAPI server
uvicorn api.main:app --reload


# 🔗 REST API Endpoints (Example)
Method	Endpoint	Description
GET	/	Health check
GET	/movies	Fetch all movies (paginated)
GET	/movies/{id}	Fetch a single movie by ID
GET	/movies/search?genre=Action&rating>8	Filter movies
POST	/movies	Insert a new movie
PUT	/movies/{id}	Update movie details
DELETE	/movies/{id}	Delete a movie

#📋 Task Checklist & Progress

 Project setup (repo, structure, README, requirements).

 Dataset selection (IMDb / NYC Taxi / Census).

 Scrapy project setup (scrape/ folder, settings, pipelines).

 Write Scrapy spider (e.g., IMDb movies crawler).

 Scrapy pipelines to export data → JSON/CSV.

 Data ingestion into Pandas for cleaning.

 Data preprocessing & transformation.

 EDA with visualizations.

 SQL schema creation (movies, ratings, etc.).

 Load cleaned data into SQL.

 REST API implementation with FastAPI.

 API integration with SQLAlchemy models.

 Unit tests (spider, pipeline, DB, API).

 Docs: EDA report, API docs.

 Dockerize application for deployment.
