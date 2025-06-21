import random
import string


def random_string(length=8):
    """Генерирует случайную строку из букв и цифр."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
