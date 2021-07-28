import json

from typing import List

from fastapi import Depends, Query
from fastapi.logger import logger

from sqlalchemy import or_, orm, func, desc
from sqlalchemy_filters import apply_pagination, apply_sort, apply_filters


from .core import (
    Base,
    get_class_by_tablename,
    get_model_name_by_tablename,
    get_db,
)

def common_parameters(
    db_session: orm.Session = Depends(get_db),
    page: int = 1,
    items_per_page: int = Query(5, alias="itemsPerPage"),
    query_str: str = Query(None, alias="q"),
    filter_spec: str = Query([], alias="filter"),
    sort_by: List[str] = Query([], alias="sortBy[]"),
    descending: List[bool] = Query([], alias="descending[]"),
):
    if filter_spec:
        filter_spec = json.loads(filter_spec)

    return {
        "db_session": db_session,
        "page": page,
        "items_per_page": items_per_page,
        "query_str": query_str,
        "filter_spec": filter_spec,
        "sort_by": sort_by,
        "descending": descending,
    }

