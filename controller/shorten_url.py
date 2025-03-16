from .CRUD import ShortenURLCRUD
from utils.shorten_url import get_no_sensitive_data, create_model
from datetime import datetime


async def get_shorten_url_by_short_code(short_code: str) -> dict:
    model = await ShortenURLCRUD.get_model_by_short_code(short_code)
    return await get_no_sensitive_data(model)


async def get_shorten_url_stats_by_short_code(short_code: str) -> str:
    model = await ShortenURLCRUD.get_model_by_short_code(short_code)
    return model.total_access


async def create_shorten_url_model_in_database(data: dict) -> dict:
    model = await create_model(data)
    model = await ShortenURLCRUD.create_model(model)
    return await get_no_sensitive_data(model)


async def delete_model_in_database_by_short_code(short_code: str) -> None:
    model = await ShortenURLCRUD.delete_model_by_short_code(short_code)


async def update_model_in_database_by_short_code(short_code: str, data: dict) -> dict:
    data["update_at"] = datetime.now()
    model = await ShortenURLCRUD.update_model_by_short_code(short_code, data)
    return await get_no_sensitive_data(model)
