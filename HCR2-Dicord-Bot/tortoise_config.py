tortoise_config = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "database": "hcr2",
                "host": "localhost",
                "password": "12345",
                "port": 5432,
                "user": "postgres",
            },
        }
    },
    "apps": {
        "main": {"models": ["models", "aerich.models"], "default_connection": "default"}
    },
}