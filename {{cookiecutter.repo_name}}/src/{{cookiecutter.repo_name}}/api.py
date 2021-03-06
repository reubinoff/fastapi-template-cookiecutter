from fastapi import APIRouter
from fastapi import Depends
from fastapi.openapi.docs import get_redoc_html
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse

from {{cookiecutter.repo_name}}.auth.services import get_current_user
from {{cookiecutter.repo_name}}.item.views import router as items_router


api_router = APIRouter(
    default_response_class=JSONResponse
)  # WARNING: Don't use this unless you want unauthenticated routes
authenticated_api_router = APIRouter()


# NOTE: All api routes should be authenticated by default

"""
Example: How to use routing 
Secured:
authenticated_api_router.include_router(
    items_router, prefix="/items", tags=["items"]
)
Unsecured:
@api_router.get("/healthcheck", include_in_schema=False)
def healthcheck():
    return {"status": "ok"}
"""

api_router.include_router(authenticated_api_router, dependencies=[Depends(get_current_user)])
