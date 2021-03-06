import functools

from typing import Optional, Sequence
from sentry_asgi import SentryMiddleware

from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware

from fastapi import Request, Response

from {{cookiecutter.repo_name}}.api import api_router
from {{cookiecutter.repo_name}}.database.core import engine, sessionmaker


@functools.lru_cache()
def get_middlewares() -> Optional[Sequence[Middleware]]:
    middlewares = [
        Middleware(BaseHTTPMiddleware, dispatch=db_session_middleware),
        Middleware(BaseHTTPMiddleware, dispatch=add_security_headers),
        Middleware(SentryMiddleware),
    ]

    return middlewares


async def db_session_middleware(request: Request, call_next):
    response = Response("Internal Server Error", status_code=500)
    try:
        session = sessionmaker(bind=engine)

        if not session:
            return response

        request.state.db = session()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["Strict-Transport-Security"] = "max-age=31536000 ; includeSubDomains"
    return response
