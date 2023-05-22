# kindle-clippy

Converting your Kindle clippings into a searchable vector database.

You will need an OpenAI account with an API-KEY (see below for setup).

## Usage
Paste your "My Clippings.txt" file into the root directory of this project.

Then in a Python interpreter in a virtual environment with the requirements installed:
```python
from logic.processing.text_parsing import parse_clippings_file_to_dataframe
from logic.processing.token_analysis import calculate_cost_of_embeddings
from logic.processing.embeddings import add_embeddings_to_dataframe
df = parse_clippings_file_to_dataframe("My Clippings.txt")
cost = calculate_cost_of_embeddings(df); print(cost)
df_with_embeddings = add_embeddings_to_dataframe(df)
```

Or if you are happy without a cost estimate:
```python
from logic import get_dataframe_with_embeddings
df_with_embeddings = get_dataframe_with_embeddings("My Clippings.txt")
```

## Pickle Backup

When processing large files, the function periodically saves a backup to a pickle file - `progress_temp.pkl`. 
This is to avoid losing progress if the process is interrupted. If you want to start again, delete this file.

## Setting Up OpenAI API Key

The OpenAI API is a REST API that uses JSON for serialization. The API is rate limited to 5 requests per second.

Generate an API Key from the OpenAI dashboard. You can add it to your environment variables as `OPENAI_API_KEY`.

You can either add using:
```commandline
export OPENAI_API_KEY=<your-api-key>
```
or by adding the above line to the activate script of your virtual environment - typically found at `venv/bin/activate`.

It's advisable to create a new API Key for each application, 
so you can revoke access to the API for a specific application if needed.

You can also load and pass to functions, e.g.:
```python
from logic import get_dataframe_with_embeddings
api_key = "your-api-key"
df_with_embeddings = get_dataframe_with_embeddings("My Clippings.txt", api_key)
```

# General Guide

There are five main steps to the process:

## Obtaining Your Clippings

Clippings are stored on the Kindle device in a text file called "My Clippings.txt". This can be big if you read a lot (mind is 10.6MB).

## Clippings to Dataframe

Parse each clipping and add as a row to a pandas data frame.

## Costing Embeddings

Calculate the cost of obtaining embeddings by counting the number of tokens.

## Adding Embeddings to the Dataframe

Calling on the OpenAI API to convert the text of each clipping.

## Running Queries

Running similarity searches against your vector database of clippings.


```


