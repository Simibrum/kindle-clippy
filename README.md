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

## Running Queries

Running similarity searches against your vector database of clippings.
