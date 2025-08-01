# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from diting import Diting, AsyncDiting
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHTTP:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_cancel_stream_chat(self, client: Diting) -> None:
        http = client.http.cancel_stream_chat()
        assert_matches_type(object, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cancel_stream_chat(self, client: Diting) -> None:
        response = client.http.with_raw_response.cancel_stream_chat()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = response.parse()
        assert_matches_type(object, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cancel_stream_chat(self, client: Diting) -> None:
        with client.http.with_streaming_response.cancel_stream_chat() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = response.parse()
            assert_matches_type(object, http, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_stream_chat(self, client: Diting) -> None:
        http = client.http.create_stream_chat(
            body={"foo": "bar"},
        )
        assert_matches_type(object, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_stream_chat(self, client: Diting) -> None:
        response = client.http.with_raw_response.create_stream_chat(
            body={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = response.parse()
        assert_matches_type(object, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_stream_chat(self, client: Diting) -> None:
        with client.http.with_streaming_response.create_stream_chat(
            body={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = response.parse()
            assert_matches_type(object, http, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_stream_chat2(self, client: Diting) -> None:
        http = client.http.create_stream_chat2(
            body={"foo": "bar"},
        )
        assert_matches_type(object, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_stream_chat2(self, client: Diting) -> None:
        response = client.http.with_raw_response.create_stream_chat2(
            body={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = response.parse()
        assert_matches_type(object, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_stream_chat2(self, client: Diting) -> None:
        with client.http.with_streaming_response.create_stream_chat2(
            body={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = response.parse()
            assert_matches_type(object, http, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_chat(self, client: Diting) -> None:
        http = client.http.retrieve_chat()
        assert_matches_type(object, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_chat(self, client: Diting) -> None:
        response = client.http.with_raw_response.retrieve_chat()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = response.parse()
        assert_matches_type(object, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_chat(self, client: Diting) -> None:
        with client.http.with_streaming_response.retrieve_chat() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = response.parse()
            assert_matches_type(object, http, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHTTP:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_cancel_stream_chat(self, async_client: AsyncDiting) -> None:
        http = await async_client.http.cancel_stream_chat()
        assert_matches_type(object, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cancel_stream_chat(self, async_client: AsyncDiting) -> None:
        response = await async_client.http.with_raw_response.cancel_stream_chat()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = await response.parse()
        assert_matches_type(object, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cancel_stream_chat(self, async_client: AsyncDiting) -> None:
        async with async_client.http.with_streaming_response.cancel_stream_chat() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = await response.parse()
            assert_matches_type(object, http, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_stream_chat(self, async_client: AsyncDiting) -> None:
        http = await async_client.http.create_stream_chat(
            body={"foo": "bar"},
        )
        assert_matches_type(object, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_stream_chat(self, async_client: AsyncDiting) -> None:
        response = await async_client.http.with_raw_response.create_stream_chat(
            body={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = await response.parse()
        assert_matches_type(object, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_stream_chat(self, async_client: AsyncDiting) -> None:
        async with async_client.http.with_streaming_response.create_stream_chat(
            body={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = await response.parse()
            assert_matches_type(object, http, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_stream_chat2(self, async_client: AsyncDiting) -> None:
        http = await async_client.http.create_stream_chat2(
            body={"foo": "bar"},
        )
        assert_matches_type(object, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_stream_chat2(self, async_client: AsyncDiting) -> None:
        response = await async_client.http.with_raw_response.create_stream_chat2(
            body={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = await response.parse()
        assert_matches_type(object, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_stream_chat2(self, async_client: AsyncDiting) -> None:
        async with async_client.http.with_streaming_response.create_stream_chat2(
            body={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = await response.parse()
            assert_matches_type(object, http, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_chat(self, async_client: AsyncDiting) -> None:
        http = await async_client.http.retrieve_chat()
        assert_matches_type(object, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_chat(self, async_client: AsyncDiting) -> None:
        response = await async_client.http.with_raw_response.retrieve_chat()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = await response.parse()
        assert_matches_type(object, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_chat(self, async_client: AsyncDiting) -> None:
        async with async_client.http.with_streaming_response.retrieve_chat() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = await response.parse()
            assert_matches_type(object, http, path=["response"])

        assert cast(Any, response.is_closed) is True
