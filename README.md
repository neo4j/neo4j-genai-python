# Neo4j GenAI package for Python

This repository contains the official Neo4j GenAI features for Python.

# Usage

## Installation

This package requires Python (>=3.8.1).

To install the latest stable version, use:

```shell
pip install neo4j-genai
```

## Example

After setting up a Neo4j database instance:

```python
from neo4j import GraphDatabase
from neo4j_genai import VectorRetriever

from random import random

from neo4j_genai.indexes import create_vector_index

URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "password")

INDEX_NAME = "embedding-name"
DIMENSION = 1536

# Connect to Neo4j database
driver = GraphDatabase.driver(URI, auth=AUTH)

# Creating the index
create_vector_index(
    driver,
    INDEX_NAME,
    label="Document",
    property="propertyKey",
    dimensions=DIMENSION,
    similarity_fn="euclidean",
)

# Initialize the retriever
retriever = VectorRetriever(driver, INDEX_NAME)

# Upsert the vector
vector = [random() for _ in range(DIMENSION)]
insert_query = (
    "MERGE (n:Document {id: $id})"
    "WITH n "
    "CALL db.create.setNodeVectorProperty(n, 'propertyKey', $vector)"
    "RETURN n"
)
parameters = {
    "id": 0,
    "vector": vector,
}
driver.execute_query(insert_query, parameters)

# Perform the similarity search for a vector query
query_vector = [random() for _ in range(DIMENSION)]
print(retriever.search(query_vector=query_vector, top_k=5))

```

# Development

## Install dependencies

```bash
poetry install
```


## Getting started

### Issues

If you have a bug to report or feature to request, first
[search to see if an issue already exists](https://docs.github.com/en/github/searching-for-information-on-github/searching-on-github/searching-issues-and-pull-requests#search-by-the-title-body-or-comments).
If a related issue doesn't exist, please raise a new issue using the relevant
[issue form](https://github.com/neo4j/neo4j-genai-python/issues/new/choose).

If you're a Neo4j Enterprise customer, you can also reach out to [Customer Support](http://support.neo4j.com/).

If you don't have a bug to report or feature request, but you need a hand with
the library; community support is available via [Neo4j Online Community](https://community.neo4j.com/)
and/or [Discord](https://discord.gg/neo4j).

### Make changes

1. Fork the respository.
2. Install Node.js and Yarn. For more information, see [the development guide](./docs/contributing/DEVELOPING.md).
3. Create a working branch from `dev` and start with your changes!

### Pull request

When you're finished with your changes, create a pull request, also known as a PR.

* Ensure that you have [signed the CLA](https://neo4j.com/developer/contributing-code/#sign-cla).
* Ensure that the base of your PR is set to `main`.
* Fill out the template so that we can easily review your PR. The template helps
reviewers understand your changes as well as the purpose of the pull request.
* Don't forget to [link your PR to an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue)
if you are solving one.
* Enable the checkbox to [allow maintainer edits](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/allowing-changes-to-a-pull-request-branch-created-from-a-fork)
so that maintainers can make any necessary tweaks and update your branch for merge.
* Reviewers may ask for changes to be made before a PR can be merged, either using
[suggested changes](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/incorporating-feedback-in-your-pull-request)
or normal pull request comments. You can apply suggested changes directly through
the UI, and any other changes can be made in your fork and committed to the PR branch.
* As you update your PR and apply changes, mark each conversation as [resolved](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/commenting-on-a-pull-request#resolving-conversations).


## Run tests

Open a new virtual environment and then run the tests.

```bash
poetry shell
pytest
```

## Further information

-   [The official Neo4j Python driver](https://github.com/neo4j/neo4j-python-driver)
-   [Neo4j GenAI integrations](https://neo4j.com/docs/cypher-manual/current/genai-integrations/)
