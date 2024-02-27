from bot_messages.bot_answer_text import who_i_am_text as gg


def insert_backslashes(s, chars):
    result = ''
    for char in s:
        if char in chars:
            result += '\\' + char
        else:
            result += char
    return result


if __name__ == '__main__':
    print(insert_backslashes(gg, '-.!()'))