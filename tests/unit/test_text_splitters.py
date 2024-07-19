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
import pytest
from langchain_text_splitters import RecursiveCharacterTextSplitter
from llama_index.core.node_parser.text.sentence import SentenceSplitter
from neo4j_genai.generation.text_splitters import TextSplitterAdapter

pytest_plugins = ("pytest_asyncio",)


text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
In cursus erat quis ornare condimentum. Ut sollicitudin libero nec quam vestibulum, non tristique augue tempor.
Nulla fringilla, augue ac fermentum ultricies, mauris tellus tempor orci, at tincidunt purus arcu vitae nisl.
Nunc suscipit neque vitae ipsum viverra, eu interdum tortor iaculis.
Suspendisse sit amet quam non ipsum molestie euismod finibus eu nisi. Quisque sit amet aliquet leo, vel auctor dolor.
Sed auctor enim at tempus eleifend. Suspendisse potenti. Suspendisse congue tellus id justo bibendum, at commodo sapien porta.
Nam sagittis nisl vitae nibh pellentesque, et convallis turpis ultrices.
"""


@pytest.mark.asyncio
async def test_langchain_adapter() -> None:
    text_splitter = TextSplitterAdapter(RecursiveCharacterTextSplitter())
    text_chunks = await text_splitter.run(text)

    assert list(text_chunks.keys()) == ["text_chunks"]
    assert isinstance(text_chunks["text_chunks"], list)
    for text_chunk in text_chunks["text_chunks"]:
        assert isinstance(text_chunk, str)
        assert text_chunk in text


@pytest.mark.asyncio
async def test_llamaindex_adapter() -> None:
    text_splitter = TextSplitterAdapter(SentenceSplitter())
    text_chunks = await text_splitter.run(text)

    assert list(text_chunks.keys()) == ["text_chunks"]
    assert isinstance(text_chunks["text_chunks"], list)
    for text_chunk in text_chunks["text_chunks"]:
        assert isinstance(text_chunk, str)
        assert text_chunk in text
