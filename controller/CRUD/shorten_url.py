from sqlalchemy import select, update
from fastapi import HTTPException

from models import ShortenURL
from . import CRUD


class ShortenURLCRUD(CRUD):
    @classmethod
    async def get_model_by_id(cls, id: str) -> ShortenURL:
        async with cls.session_factory() as session:
            try:
                statement = select(ShortenURL).where(ShortenURL.id == id)
                result = await session.execute(statement)
                model = result.scalars().one()
                model.total_access += 1
                await session.commit()

                return model
            except HTTPException as error:
                raise HTTPException(status_code=error.status_code, detail=error)

    @classmethod
    async def get_model_by_short_code(cls, short_code: str) -> ShortenURL:
        async with cls.session_factory() as session:
            try:
                statement = select(ShortenURL).where(
                    ShortenURL.short_code == short_code
                )
                result = await session.execute(statement)
                model = result.scalars().one()
                model.total_access += 1
                await session.commit()

                return model
            except HTTPException as error:
                raise HTTPException(detail=error, status_code=error.status_code)

    @classmethod
    async def create_model(cls, model: ShortenURL) -> ShortenURL:
        async with cls.session_factory() as session:
            try:
                session.add(model)
                await session.commit()

                return model
            except HTTPException as error:
                raise HTTPException(detail=error, status_code=error.status_code)

    @classmethod
    async def delete_model_by_id(cls, id: str) -> ShortenURL:
        async with cls.session_factory() as session:
            try:
                model = await ShortenURLCRUD.get_model_by_id(id)
                await session.delete(model)
                await session.commit()

                return model
            except HTTPException as error:
                raise HTTPException(detail=error, status_code=error.status_code)

    @classmethod
    async def delete_model_by_short_code(cls, short_code: str) -> ShortenURL:
        async with cls.session_factory() as session:
            try:
                model = await ShortenURLCRUD.get_model_by_short_code(short_code)
                await session.delete(model)
                await session.commit()

                return model
            except HTTPException as error:
                raise HTTPException(detail=error, status_code=error.status_code)

    @classmethod
    async def update_model_by_id(cls, id: str, new_data: dict) -> ShortenURL:
        async with cls.session_factory() as session:
            try:
                statement = (
                    update(ShortenURL)
                    .where(ShortenURL.id == id)
                    .values(**new_data)
                    .returning(ShortenURL)
                )
                result = await session.execute(statement)
                await session.commit()

                return result.scalars().one()
            except HTTPException as error:
                raise HTTPException(detail=error, status_code=error.status_code)

    @classmethod
    async def update_model_by_short_code(
        cls, short_code: str, new_data: dict
    ) -> ShortenURL:
        async with cls.session_factory() as session:
            try:
                statement = (
                    update(ShortenURL)
                    .where(ShortenURL.short_code == short_code)
                    .values(**new_data)
                    .returning(ShortenURL)
                )
                result = await session.execute(statement)
                await session.commit()

                return result.scalars().one()
            except HTTPException as error:
                raise HTTPException(detail=error, status_code=error.status_code)
