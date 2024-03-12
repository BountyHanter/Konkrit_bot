from bot_messages.bot_answer_text import send_request_text as gg

"""
Функция для экранирования символов
"""

def insert_backslashes(s, chars='-.!()'):
    result = ''
    for char in s:
        if char in chars:
            result += '\\' + char
        else:
            result += char
    return result


if __name__ == '__main__':
    print(insert_backslashes(gg))
