from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="automated_data_pipeline",
    start_date=datetime(2026, 6, 27),
    schedule=None,
    catchup=False,
    tags=["Data Engineering", "Automation"],
) as dag:

    # -----------------------------
    # Start
    # -----------------------------
    start = EmptyOperator(
        task_id="start"
    )

    # -----------------------------
    # Read Input Files
    # -----------------------------
    read_customers = EmptyOperator(
        task_id="read_customers"
    )

    read_orders = EmptyOperator(
        task_id="read_orders"
    )

    read_payments = EmptyOperator(
        task_id="read_payments"
    )

    # -----------------------------
    # NiFi Pipeline
    # -----------------------------
    run_nifi = EmptyOperator(
        task_id="run_nifi"
    )

    # -----------------------------
    # Store Data in MinIO
    # -----------------------------
    store_in_minio = EmptyOperator(
        task_id="store_in_minio"
    )

    # -----------------------------
    # Data Cleaning
    # -----------------------------
    run_data_cleaning = BashOperator(
        task_id="run_data_cleaning",
        bash_command="python /opt/airflow/dags/data_cleaning.py"
    )

    # -----------------------------
    # Merge Data
    # -----------------------------
    run_merge_data = BashOperator(
        task_id="run_merge_data",
        bash_command="python /opt/airflow/dags/merge_data.py"
    )

    # -----------------------------
    # Business Analysis
    # -----------------------------
    run_business_analysis = BashOperator(
        task_id="run_business_analysis",
        bash_command="python /opt/airflow/dags/business_analysis.py"
    )

    # -----------------------------
    # Visualization
    # -----------------------------
    run_visualization = BashOperator(
        task_id="run_visualization",
        bash_command="python /opt/airflow/dags/visualization.py"
    )

    # -----------------------------
    # End
    # -----------------------------
    end = EmptyOperator(
        task_id="end"
    )

    # -----------------------------
    # Workflow
    # -----------------------------
    (
        start
        >> read_customers
        >> read_orders
        >> read_payments
        >> run_nifi
        >> store_in_minio
        >> run_data_cleaning
        >> run_merge_data
        >> run_business_analysis
        >> run_visualization
        >> end
    )
