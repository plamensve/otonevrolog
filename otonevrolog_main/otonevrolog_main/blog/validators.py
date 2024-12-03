from django.core.exceptions import ValidationError

"""
Използвам два пъти една и съща функция за валидиране от гл. т. на това, че апликацията се старая да може да 
функционира самостоятелно. Заради това избягвам да обвързвам една апликация с валидатори от друга.
"""


def validate_image_size(value):
    max_size_mb = 5
    if value.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"The maximum allowed picture size is {max_size_mb} MB.")
