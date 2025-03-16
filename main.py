from fastapi import FastAPI, status, HTTPException

from schemas import CreateShortenURL, UpdateShortenURL
from controller import shorten_url

app = FastAPI()


@app.post("/shorten", status_code=status.HTTP_201_CREATED)
async def post_router(data: CreateShortenURL):
    try:
        return await shorten_url.create_shorten_url_model_in_database(dict(data))
    except HTTPException as error:
        raise HTTPException(detail=error, status_code=error.status_code)


@app.get("/shorten/{shorten_code}", status_code=status.HTTP_200_OK)
async def get_router(shorten_code: str):
    try:
        return await shorten_url.get_shorten_url_by_short_code(shorten_code)
    except HTTPException as error:
        raise HTTPException(detail=error, status_code=error.status_code)


@app.get("/shorten/{shorten_code}/stats", status_code=status.HTTP_200_OK)
async def get_stats_router(shorten_code: str):
    try:
        return await shorten_url.get_shorten_url_stats_by_short_code(shorten_code)
    except HTTPException as error:
        raise HTTPException(detail=error, status_code=error.status_code)


@app.put("/shorten/{shorten_code}", status_code=status.HTTP_204_NO_CONTENT)
async def put_router(short_code: str, put_data: UpdateShortenURL):
    await shorten_url.update_model_in_database_by_short_code(short_code, dict(put_data))
    return


@app.delete("/shorten/{shorten_code}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_router(shorten_code: str):
    await shorten_url.delete_model_in_database_by_short_code(shorten_code)
    return


if __name__ == "__main__":
    from database import create_db
    from asyncio import run

    run(create_db())
