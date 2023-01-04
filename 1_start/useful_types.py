from typing import Union
from datetime import datetime, date, time, timedelta
from uuid import UUID
from fastapi import Body, FastAPI


app = FastAPI()


@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Union[datetime, None] = Body(default=None),
    end_date: Union[date, None] = Body(default=None),
    repeat_at: Union[time, None] = Body(default=None),
    process_after: Union[timedelta, None] = Body(default=None),
):
    """
    ### there is many useful parameter types that can be converted to python datatypes
    """

    start_process = start_datetime + process_after
    duration = end_date - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_date": end_date,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }
