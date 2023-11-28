from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


def optimize_image(image_field, max_size=(800, 600)):
    """
    Оптимизация изображений перед сохранением.
    """
    if not image_field:
        return None

    img = Image.open(image_field)

    # Проверка размера и изменение размера, если необходимо
    if img.size > max_size:
        img.thumbnail(max_size)

    # Создание буфера для сохранения оптимизированного изображения
    output_buffer = BytesIO()
    img.save(output_buffer, format="PNG")

    # Создание InMemoryUploadedFile
    optimized_image = InMemoryUploadedFile(
        output_buffer,
        "ImageField",
        f"{image_field.name.split('.')[0]}.png",
        "image/png",
        output_buffer.getbuffer().nbytes,
        None,
    )

    return optimized_image
