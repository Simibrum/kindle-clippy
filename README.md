# kindle-clippy

Converting your Kindle clippings into a searchable vector database.

You will need an OpenAI account with an API-KEY.

## Obtaining Your Clippings

Clippings are stored on the Kindle device in a text file called "My Clippings.txt". This can be big if you read a lot (mind is 10.6MB).

## Clippings to Dataframe

Parse each clipping and add as a row to a pandas data frame.

## Costing Embeddings

Calculate the cost of obtaining embeddings by counting the numnber of tokens.

## Adding Embeddings to the Dataframe

Calling on the OpenAI API to convert the text of each clipping.

### OpenAI API

The OpenAI API is a REST API that uses JSON for serialization. The API is rate limited to 5 requests per second.

Generate an API Key from the OpenAI dashboard. You can add it to your environment variables as `OPENAI_API_KEY`.

You can either add using:
```commandline
export OPENAI_API_KEY=<your-api-key>
```
or by adding the above line to the activate script of your virtual environment - typically found at `venv/bin/activate`.

It's advisable to create a new API Key for each application, 
so you can revoke access to the API for a specific application if needed.

## Running Queries

Running similarity searches against your vector database of clippings.
