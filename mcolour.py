colour = {
    'red': '31m',
    'black': '30m',
    'green': '32m',
    'yellow': '33m',
    'blue': '34m',
    'purpure': '35m',
    'biruza': '36m',
    'white': '37m'
}


def color_text(text, colour_name):
    coloured_txt = '\033[' + colour_name + text + '\033[0m'
    return coloured_txt
    """
    Повертає текст із вказаним кольором.
    :param text: Текст, який необхідно виділити кольором.
    :param colour_name: Назва кольору зі словника 'colour'.
    :return: Рядок з кольорованим текстом.
    """

def styled(text, code="3m"):
    clean_style_code = '\033[0m'
    styled_txt = f'\033[{code}{text}{clean_style_code}'
    return styled_txt
    """
    Повертає текст із вказаним стилем.
    :param text: Текст, який необхідно стилізувати.
    :param code: Код стилю.
    :return: Рядок із стилізованим текстом.
    """


def error_message(message):
    status = "ERROR"
    error = color_text(f"{status:<8} ", colour['red'])
    _message = color_text(message, colour['yellow'])
    err_message = error + _message
    return err_message
    """
    Повертає повідомлення про помилку.
    :param message: Текст помилки.
    :return: Рядок із кольорованим повідомленням про помилку.
    """

def warning_message(message):
    status = "WARNING"
    warn = color_text(f"{status:<8} ", colour['yellow'])
    _message = color_text(message, colour['biruza'])
    warn_message = warn + _message
    return warn_message
    """
    Повертає предупреждення.
    :param message: Текст предупреждення.
    :return: Рядок із кольорованим предупрежденням.
    """

def info_message(message):
    status = "INFO"
    info = color_text(f"{status:<8} ", colour['purpure'])
    info_message = info + message
    return info_message
    """
    Повертає інформаційне повідомлення.
    :param message: Текст інформації.
    :return: Рядок із кольорованим інформаційним повідомленням.
    """



"""
Example:
s = "\033[3m"
c = "\033[33m"
f  = "\033[41m";
clean = "\033[0m"
pattern = f"{s}{c}{f}{txt}{clean}"
"""



if __name__ == "__main__":
    print(warning_message("ups i did sit again"))
    print(error_message("wrong way"))
    print(info_message("thanks for info"))

def custom_style_text(
    text: str,
    text_style: str = "0",  # Default style
    text_color: str = "37m",  # Default color (white)
    background_color: str = "45m"  # Default background color (pink)
) -> str:
    """
    Повертає текст із заданим стилем, кольором тексту та фону.
    :param text: Текст, який необхідно стилізувати.
    :param text_style: Код стилю (за замовчуванням - звичайний стиль).
    :param text_color: Код кольору тексту (за замовчуванням - білий).
    :param background_color: Код кольору фону (за замовчуванням - рожевий).
    :return: Рядок із стилізованим текстом.
    """
    styled_txt = f'\033[{text_style};{text_color};{background_color}{text}\033[0m'
    return styled_txt