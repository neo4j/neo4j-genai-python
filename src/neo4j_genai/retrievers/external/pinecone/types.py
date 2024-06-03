#  Copyright (c) "Neo4j"
#  Neo4j Sweden AB [https://neo4j.com]
#  #
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  #
#      https://www.apache.org/licenses/LICENSE-2.0
#  #
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
from typing import Any, Callable, Optional

import neo4j
from pinecone import Pinecone
from pydantic import (
    BaseModel,
    ConfigDict,
    field_validator,
)

from neo4j_genai.types import EmbedderModel, Neo4jDriverModel, VectorSearchModel


class PineconeSearchModel(VectorSearchModel):
    pinecone_filter: Optional[dict[str, Any]] = None


class PineconeClientModel(BaseModel):
    client: Pinecone
    model_config = ConfigDict(arbitrary_types_allowed=True)

    @field_validator("client")
    def check_client(cls, value):
        if not isinstance(value, Pinecone):
            raise ValueError("Provided client needs to be of type Pinecone")
        return value


class PineconeNeo4jRetrieverModel(BaseModel):
    driver_model: Neo4jDriverModel
    client_model: PineconeClientModel
    index_name: str
    id_property_neo4j: str
    embedder_model: Optional[EmbedderModel] = None
    return_properties: Optional[list[str]] = None
    retrieval_query: Optional[str] = None
    format_record_function: Optional[Callable[[neo4j.Record], str]] = None
