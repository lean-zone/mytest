# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from diting import Diting, AsyncDiting
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAa:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Diting) -> None:
        aa = client.aa.create(
            name="name",
            var_name="var_name",
        )
        assert_matches_type(object, aa, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Diting) -> None:
        aa = client.aa.create(
            name="name",
            var_name="var_name",
            reload=True,
        )
        assert_matches_type(object, aa, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Diting) -> None:
        response = client.aa.with_raw_response.create(
            name="name",
            var_name="var_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aa = response.parse()
        assert_matches_type(object, aa, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Diting) -> None:
        with client.aa.with_streaming_response.create(
            name="name",
            var_name="var_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aa = response.parse()
            assert_matches_type(object, aa, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAa:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDiting) -> None:
        aa = await async_client.aa.create(
            name="name",
            var_name="var_name",
        )
        assert_matches_type(object, aa, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDiting) -> None:
        aa = await async_client.aa.create(
            name="name",
            var_name="var_name",
            reload=True,
        )
        assert_matches_type(object, aa, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDiting) -> None:
        response = await async_client.aa.with_raw_response.create(
            name="name",
            var_name="var_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aa = await response.parse()
        assert_matches_type(object, aa, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDiting) -> None:
        async with async_client.aa.with_streaming_response.create(
            name="name",
            var_name="var_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aa = await response.parse()
            assert_matches_type(object, aa, path=["response"])

        assert cast(Any, response.is_closed) is True
