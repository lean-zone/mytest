# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["HealthyResource", "AsyncHealthyResource"]


class HealthyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HealthyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/diting-python#accessing-raw-response-data-eg-headers
        """
        return HealthyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HealthyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/diting-python#with_streaming_response
        """
        return HealthyResourceWithStreamingResponse(self)

    def check(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """**健康检查**"""
        return self._get(
            "/healthy",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncHealthyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHealthyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/diting-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHealthyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHealthyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/diting-python#with_streaming_response
        """
        return AsyncHealthyResourceWithStreamingResponse(self)

    async def check(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """**健康检查**"""
        return await self._get(
            "/healthy",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class HealthyResourceWithRawResponse:
    def __init__(self, healthy: HealthyResource) -> None:
        self._healthy = healthy

        self.check = to_raw_response_wrapper(
            healthy.check,
        )


class AsyncHealthyResourceWithRawResponse:
    def __init__(self, healthy: AsyncHealthyResource) -> None:
        self._healthy = healthy

        self.check = async_to_raw_response_wrapper(
            healthy.check,
        )


class HealthyResourceWithStreamingResponse:
    def __init__(self, healthy: HealthyResource) -> None:
        self._healthy = healthy

        self.check = to_streamed_response_wrapper(
            healthy.check,
        )


class AsyncHealthyResourceWithStreamingResponse:
    def __init__(self, healthy: AsyncHealthyResource) -> None:
        self._healthy = healthy

        self.check = async_to_streamed_response_wrapper(
            healthy.check,
        )
