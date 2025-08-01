# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import http_create_stream_chat_params, http_create_stream_chat2_params
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

__all__ = ["HTTPResource", "AsyncHTTPResource"]


class HTTPResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HTTPResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/diting-python#accessing-raw-response-data-eg-headers
        """
        return HTTPResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HTTPResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/diting-python#with_streaming_response
        """
        return HTTPResourceWithStreamingResponse(self)

    def cancel_stream_chat(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Stream Chat"""
        return self._post(
            "/http/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def create_stream_chat(
        self,
        *,
        body: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Stream Chat

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/http/stream-chat",
            body=maybe_transform(body, http_create_stream_chat_params.HTTPCreateStreamChatParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def create_stream_chat2(
        self,
        *,
        body: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Stream Chat2

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/http/stream-chat2",
            body=maybe_transform(body, http_create_stream_chat2_params.HTTPCreateStreamChat2Params),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retrieve_chat(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Chat"""
        return self._get(
            "/http/chat",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncHTTPResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHTTPResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/diting-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHTTPResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHTTPResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/diting-python#with_streaming_response
        """
        return AsyncHTTPResourceWithStreamingResponse(self)

    async def cancel_stream_chat(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Stream Chat"""
        return await self._post(
            "/http/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def create_stream_chat(
        self,
        *,
        body: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Stream Chat

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/http/stream-chat",
            body=await async_maybe_transform(body, http_create_stream_chat_params.HTTPCreateStreamChatParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def create_stream_chat2(
        self,
        *,
        body: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Stream Chat2

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/http/stream-chat2",
            body=await async_maybe_transform(body, http_create_stream_chat2_params.HTTPCreateStreamChat2Params),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retrieve_chat(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Chat"""
        return await self._get(
            "/http/chat",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class HTTPResourceWithRawResponse:
    def __init__(self, http: HTTPResource) -> None:
        self._http = http

        self.cancel_stream_chat = to_raw_response_wrapper(
            http.cancel_stream_chat,
        )
        self.create_stream_chat = to_raw_response_wrapper(
            http.create_stream_chat,
        )
        self.create_stream_chat2 = to_raw_response_wrapper(
            http.create_stream_chat2,
        )
        self.retrieve_chat = to_raw_response_wrapper(
            http.retrieve_chat,
        )


class AsyncHTTPResourceWithRawResponse:
    def __init__(self, http: AsyncHTTPResource) -> None:
        self._http = http

        self.cancel_stream_chat = async_to_raw_response_wrapper(
            http.cancel_stream_chat,
        )
        self.create_stream_chat = async_to_raw_response_wrapper(
            http.create_stream_chat,
        )
        self.create_stream_chat2 = async_to_raw_response_wrapper(
            http.create_stream_chat2,
        )
        self.retrieve_chat = async_to_raw_response_wrapper(
            http.retrieve_chat,
        )


class HTTPResourceWithStreamingResponse:
    def __init__(self, http: HTTPResource) -> None:
        self._http = http

        self.cancel_stream_chat = to_streamed_response_wrapper(
            http.cancel_stream_chat,
        )
        self.create_stream_chat = to_streamed_response_wrapper(
            http.create_stream_chat,
        )
        self.create_stream_chat2 = to_streamed_response_wrapper(
            http.create_stream_chat2,
        )
        self.retrieve_chat = to_streamed_response_wrapper(
            http.retrieve_chat,
        )


class AsyncHTTPResourceWithStreamingResponse:
    def __init__(self, http: AsyncHTTPResource) -> None:
        self._http = http

        self.cancel_stream_chat = async_to_streamed_response_wrapper(
            http.cancel_stream_chat,
        )
        self.create_stream_chat = async_to_streamed_response_wrapper(
            http.create_stream_chat,
        )
        self.create_stream_chat2 = async_to_streamed_response_wrapper(
            http.create_stream_chat2,
        )
        self.retrieve_chat = async_to_streamed_response_wrapper(
            http.retrieve_chat,
        )
