from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from horoscope_observatory.horoscope_application import HoroscopeApplication 
default_args = {
 
    'owner': 'horoscope_inc',
    'start_date': days_ago(1)
}
 
dag = DAG(dag_id = 'horoscope_observatory', default_args=default_args, schedule_interval=None)
 
 
def execute_horoscope_observatory_etl():
    horoscope_application = HoroscopeApplication()
    horoscope_application.process()
    print('Finished Operator')
 
with dag:
    run_horoscope_observatory_task = PythonOperator(
        task_id='run_this_first',
        python_callable = execute_horoscope_observatory_etl
    )
 
    run_horoscope_observatory_task