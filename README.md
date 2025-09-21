# RedditScrapper

RedditScrapper is an ETL pipeline for extracting, transforming, and loading Reddit post data, orchestrated using Apache Airflow.

## Features

- **Reddit Data Extraction:** Uses PRAW to connect to Reddit and extract posts from specified subreddits.
- **Data Transformation:** Cleans and normalizes post data using pandas and numpy.
- **CSV Export:** Saves processed data to CSV files.
- **Airflow Integration:** Schedules and manages ETL jobs via Airflow DAGs.
- **Docker Support:** Easily deployable with Docker and docker-compose.

## Project Structure

```
.
├── dags/                  # Airflow DAG definitions
│   └── reddit_dag.py
├── etls/                  # ETL logic
│   └── reddit_etl.py
├── pipelines/             # Pipeline orchestration
│   └── reddit_pipeline.py
├── utils/                 # Utility modules
│   └── constants.py
├── config/                # Configuration files
│   └── config.conf
├── data/                  # Data storage
│   ├── input/
│   └── output/
├── logs/                  # Airflow and pipeline logs
├── redditscrapperaws/     # Python virtual environment
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker build file
├── docker-compose.yml     # Docker Compose configuration
├── airflow.env            # Airflow environment variables
└── README.md              # Project documentation
```

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Configuration

Edit `config/config.conf` to set your Reddit API credentials and file paths.  
See [`utils/constants.py`](utils/constants.py) for expected config keys.

### Build and Run

1. **Build Docker Image:**
   ```sh
   docker-compose build
   ```

2. **Start Airflow & Pipeline:**
   ```sh
   docker-compose up
   ```

3. **Trigger DAG:**
   - Access Airflow UI at `localhost:8080`
   - Trigger the `etl_reddit_pipeline` DAG

### ETL Pipeline

- Extraction: [`etls.reddit_etl.extract_post`](etls/reddit_etl.py)
- Transformation: [`etls.reddit_etl.transform_data`](etls/reddit_etl.py)
- Loading: [`etls.reddit_etl.load_data_to_csv`](etls/reddit_etl.py)
- Orchestration: [`pipelines.reddit_pipeline.redditpipeline`](pipelines/reddit_pipeline.py)
- Scheduling: [`dags/reddit_dag.py`](dags/reddit_dag.py)

## Customization

- Change subreddit, time filter, or output filename in the DAG definition ([`dags/reddit_dag.py`](dags/reddit_dag.py)).
- Update transformation logic in [`etls/reddit_etl.py`](etls/reddit_etl.py).

## Logs & Output

- Logs: `logs/`
- Output CSVs: `data/output/`

## License

See individual files for license details.

## Authors

- Shasank Periwal

---

For more details, see the code in [`dags/reddit_dag.py`](dags/reddit_dag.py), [`etls/reddit_etl.py`](etls/reddit_etl.py), and [`pipelines/reddit_pipeline.py`](pipelines/reddit_pipeline.py).