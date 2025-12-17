def journalist_schema(journalist) -> dict:
    # El id en base de datos es _id
    return {
        "id": str(journalist["_id"]),
        "name": journalist["name"],
        "surname": journalist["surname"],
        "age": journalist["age"]
    }


def journalists_schema(journalists) -> list:
    return [journalist_schema(journalist) for journalist in journalists]
