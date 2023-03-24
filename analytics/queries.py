import requests
import pandas as pd
import io

res = requests.get("https://raw.githubusercontent.com/pedrohgoncalvess/jobanalytics/master/datasets/tecnologies_jsa.csv").content
rawData = pd.read_csv(io.StringIO(res.decode('utf-8')),on_bad_lines='skip')
print(rawData)