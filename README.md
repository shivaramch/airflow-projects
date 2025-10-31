# Airflow Setup - Quick Start Guide

## Current Status
✅ **Airflow 3.0.6** is installed and running
✅ **API Server** is running on http://localhost:8080
✅ **Scheduler** is running in the background
✅ **Database** is initialized (SQLite)

## Important Notes about Airflow 3.0.6

This version of Airflow has significant changes:
- **No traditional web UI**: The classic Airflow webserver has been replaced with an API-first architecture
- **API-only interface**: You interact with Airflow primarily through REST API calls
- **New architecture**: This is a major architectural shift from previous versions

## How to Access Airflow

### 1. API Documentation
Open your browser to: **http://localhost:8080**
This will show you the FastAPI documentation where you can:
- View all available API endpoints
- Test API calls directly from the browser
- See API schemas and examples

### 2. Basic API Usage Examples

```bash
# List all DAGs
curl http://localhost:8080/public/dags

# Get DAG details
curl http://localhost:8080/public/dags/{dag_id}

# Trigger a DAG run
curl -X POST http://localhost:8080/public/dags/{dag_id}/dagRuns \
  -H "Content-Type: application/json" \
  -d '{"dag_run_id": "manual_run", "logical_date": "2025-10-30T00:00:00Z"}'
```

## Directory Structure
```
/Users/shivaram.chennapragada/Documents/GitHub/airflow-projects/
├── airflow.cfg          # Airflow configuration
├── airflow.db           # SQLite database
├── dags/                # Put your DAG files here (create this folder)
├── logs/                # Airflow logs (auto-created)
└── plugins/             # Custom plugins (create if needed)
```

## Creating Your First DAG

1. Create a `dags` folder:
```bash
mkdir dags
```

2. Create a simple DAG file in `dags/hello_world.py`:
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def hello_world():
    print("Hello, World from Airflow!")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'hello_world_dag',
    default_args=default_args,
    description='A simple Hello World DAG',
    schedule_interval=timedelta(days=1),
    catchup=False,
)

hello_task = PythonOperator(
    task_id='hello_world_task',
    python_callable=hello_world,
    dag=dag,
)
```

## Managing Airflow

### Start Services
```bash
# API Server (already running)
/Users/shivaram.chennapragada/Documents/GitHub/airflow-projects/.venv/bin/python -m airflow api-server --port 8080

# Scheduler (already running)
/Users/shivaram.chennapragada/Documents/GitHub/airflow-projects/.venv/bin/python -m airflow scheduler
```

### Stop Services
Press `Ctrl+C` in each terminal where the services are running.

## Environment Variables
Make sure to set this in each new terminal session:
```bash
export AIRFLOW_HOME=/Users/shivaram.chennapragada/Documents/GitHub/airflow-projects
```

## Alternative: Traditional Airflow Web UI

If you need the traditional web interface, you might want to consider:
1. **Downgrading to Airflow 2.x** (not recommended for new projects)
2. **Using a third-party UI** that works with Airflow 3.x APIs
3. **Building a custom dashboard** using the API endpoints

## Next Steps
1. Create the `dags` folder and add your first DAG
2. Use the API documentation at http://localhost:8080 to explore available endpoints
3. Consider setting up authentication if needed for production use

---
**Need help?** Check the API documentation or ask for assistance with specific DAG creation!