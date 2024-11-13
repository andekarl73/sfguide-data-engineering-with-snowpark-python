import sys
from pathlib import Path
root_dir = Path(__file__).resolve().parent.parent
print("A")
print(f'root_dir: {root_dir}')
sys.path.append(str(root_dir))

from snowflake.snowpark.session import Session
#sys.path.append("C:\\Projekt\\Python\\sfguide-data.engineering-with-snowpark-python\\steps\\05_fahrenheit_to_celsius_udf\\fahrenheit_to_celsius_udf")
#sys.path.append("C:\\Projekt\\Python\\sfguide-data.engineering-with-snowpark-python\\test")
#sys.path.append("C:\\Projekt\\Python\\sftutorial-snowpark-testing\\test")
# test/test_transformers.py

# test/test_transformers.py
from steps.fahrenheit_to_celsius_udf.fahrenheit_to_celsius_udf.function import main
from snowflake.snowpark.types import StructType, StructField, IntegerType, FloatType

def test_main(session: Session):
    expected = 0.0
    actual = main(32,'F','C')
    assert expected == actual