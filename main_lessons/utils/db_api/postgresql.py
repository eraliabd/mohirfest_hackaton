from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(self, command, *args,
                      # qanday command-da ekanligiga qarab pastdagi o'zgaruvchilar (True) ga o'zgaradi
                      fetch: bool = False,  # bazadan barcha ma'lumotlarni olish
                      fetchval: bool = False,  # bazadan bitta ma'lumot olish (masalan: users soni)
                      fetchrow: bool = False,  # bazadan bitta qator olish ya'ni (1 ta user ni barcha ma'lumotlari)
                      execute: bool = False  # bazaga ma'lumot yozish (masalan: ro'yxatdan o'tayotgan user ma'lumotlari)
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    # async def create_table_users(self):
    #     sql = """
    #     CREATE TABLE IF NOT EXISTS shareit_shareit_receiveruseruser (
    #     id SERIAL PRIMARY KEY,
    #     full_name VARCHAR(255) NOT NULL,
    #     age BIGINT NULL,
    #     phone_number VARCHAR(255) NOT NULL,
    #     address VARCHAR(255)  NOT NULL,
    #     job VARCHAR(255) NULL,
    #     purpose VARCHAR(255) NULL
    #     );
    #     """
    #     await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        print(sql)
        return sql, tuple(parameters.values())

    async def add_user(self, full_name, age, phone_number, address, job, purpose):
        sql = "INSERT INTO shareit_receiveruser (full_name, age, phone_number, address, job, purpose) VALUES($1, $2, $3, $4, $5, $6) returning *"
        return await self.execute(sql, full_name, age, phone_number, address, job, purpose, fetchrow=True)

    async def add_user1(self, full_name, phone_number, job, address, photo_id, compute_info):
        sql = "INSERT INTO shareit_charityuser (full_name, phone_number, job, address, photo_id, compute_info) VALUES($1, $2, $3, $4, $5, $6) returning *"
        return await self.execute(sql, full_name, phone_number, job, address, photo_id, compute_info, fetchrow=True)

    # async def select_all_users(self):
    #     sql = "SELECT * FROM shareit_receiveruser"
    #     return await self.execute(sql, fetch=True)
    #
    # async def select_user(self, **kwargs):
    #     sql = "SELECT * FROM shareit_receiveruser WHERE "
    #     sql, parameters = self.format_args(sql, parameters=kwargs)
    #     return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM shareit_receiveruser"
        return await self.execute(sql, fetchval=True)
