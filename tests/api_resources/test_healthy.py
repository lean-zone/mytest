# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from diting import Diting, AsyncDiting
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHealthy:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_check(self, client: Diting) -> None:
        healthy = client.healthy.check()
        assert_matches_type(object, healthy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_check(self, client: Diting) -> None:
        response = client.healthy.with_raw_response.check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        healthy = response.parse()
        assert_matches_type(object, healthy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_check(self, client: Diting) -> None:
        with client.healthy.with_streaming_response.check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            healthy = response.parse()
            assert_matches_type(object, healthy, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHealthy:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_check(self, async_client: AsyncDiting) -> None:
        healthy = await async_client.healthy.check()
        assert_matches_type(object, healthy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_check(self, async_client: AsyncDiting) -> None:
        response = await async_client.healthy.with_raw_response.check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        healthy = await response.parse()
        assert_matches_type(object, healthy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_check(self, async_client: AsyncDiting) -> None:
        async with async_client.healthy.with_streaming_response.check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            healthy = await response.parse()
            assert_matches_type(object, healthy, path=["response"])

        assert cast(Any, response.is_closed) is True
