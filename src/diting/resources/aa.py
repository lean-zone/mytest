# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import aa_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["AaResource", "AsyncAaResource"]


class AaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lean-zone/mytest#accessing-raw-response-data-eg-headers
        """
        return AaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lean-zone/mytest#with_streaming_response
        """
        return AaResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        var_name: str,
        reload: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Aa

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/aa",
            body=maybe_transform(
                {
                    "name": name,
                    "var_name": var_name,
                    "reload": reload,
                },
                aa_create_params.AaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncAaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lean-zone/mytest#accessing-raw-response-data-eg-headers
        """
        return AsyncAaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lean-zone/mytest#with_streaming_response
        """
        return AsyncAaResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        var_name: str,
        reload: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Aa

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/aa",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "var_name": var_name,
                    "reload": reload,
                },
                aa_create_params.AaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AaResourceWithRawResponse:
    def __init__(self, aa: AaResource) -> None:
        self._aa = aa

        self.create = to_raw_response_wrapper(
            aa.create,
        )


class AsyncAaResourceWithRawResponse:
    def __init__(self, aa: AsyncAaResource) -> None:
        self._aa = aa

        self.create = async_to_raw_response_wrapper(
            aa.create,
        )


class AaResourceWithStreamingResponse:
    def __init__(self, aa: AaResource) -> None:
        self._aa = aa

        self.create = to_streamed_response_wrapper(
            aa.create,
        )


class AsyncAaResourceWithStreamingResponse:
    def __init__(self, aa: AsyncAaResource) -> None:
        self._aa = aa

        self.create = async_to_streamed_response_wrapper(
            aa.create,
        )
