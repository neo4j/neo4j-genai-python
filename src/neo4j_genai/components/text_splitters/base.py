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
from __future__ import annotations

from abc import abstractmethod
from typing import Any, Optional

from neo4j_genai.pipeline.component import Component, DataModel
from pydantic import BaseModel


class TextChunk(BaseModel):
    """A chunk of text split from a document by a text splitter.

    Attributes:
        text (str): The raw chunk text.
        metadata (Optional[dict[str, Any]]): Metadata associated with this chunk such as the id of the next chunk in the original document.
    """

    text: str
    metadata: Optional[dict[str, Any]] = None


class TextChunks(DataModel):
    """A collection of text chunks returned from a text splitter.

    Attributes:
        chunks (list[TextChunk]): A list of text chunks.
    """

    chunks: list[TextChunk]


class TextSplitter(Component):
    """Interface for a text splitter."""

    @abstractmethod
    async def run(self, text: str) -> TextChunks:
        pass
