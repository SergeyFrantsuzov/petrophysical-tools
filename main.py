# %%
import pandas as pd
from pathlib import Path
import time
import pyodbc
import numpy as np
from importlib import reload
import add_functions as addfun
# %%
reload(addfun)

# %%
connect_param = r'Driver={SQL Server};Server=SERGEYFRPC;Database=cpiDB;Trusted_Connection=yes;'
df_cpi_temp = addfun.data_from_mssql(connect_param, 'cpi_temp' )

# %%
