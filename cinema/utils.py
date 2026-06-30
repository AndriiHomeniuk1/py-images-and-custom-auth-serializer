import pathlib
import uuid
from django.utils.text import slugify


def movie_image_path(
        instance: "Movie", filename: str) -> pathlib.Path:  # noqa: F821
    filename = (
        f"{slugify(instance.title)}-{uuid.uuid4()}"
        + pathlib.Path(filename).suffix
    )
    return pathlib.Path("uploads/movies/") / pathlib.Path(filename)
