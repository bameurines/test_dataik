# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku
from dataiku import pandasutils as pdu
import pandas as pd
from to_xlsx import dataframe_to_xlsx

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Example: load a DSS dataset as a Pandas dataframe
transactions_filtered = dataiku.Dataset("online_retail_dataset_filtered")
transactions_filtered_df = transactions_filtered.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
#dataframe_to_xlsx(input dataframe, folder where output file will be written, name of the output file)
dataframe_to_xlsx(transactions_filtered_df,'output_test', 'Transactions')
