from models import ShortenURL


async def get_no_sensitive_data(model: ShortenURL) -> dict:
    return {
        "url": model.url,
        "short_code": model.short_code,
        "create_at": model.create_at,
        "update_at": model.update_at,
        "total_access": model.total_access,
    }


async def create_model(data: dict) -> ShortenURL:
    model = ShortenURL()
    model.url = data["url"]
    model.short_code = data["short_code"]

    return model
