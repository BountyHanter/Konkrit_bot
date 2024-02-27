В библиотеке aiogram для создания телеграм-ботов действительно существует несколько способов регистрации обработчиков сообщений и команд. Вы можете использовать как декораторы, так и явную регистрацию через экземпляр `Dispatcher`. Вот краткое описание каждого из подходов:

### Использование декораторов
Декораторы в aiogram позволяют прямо над функцией-обработчиком указать, на какие сообщения или команды она должна реагировать. Это делает код более читаемым и понятным, особенно когда логика обработки небольшая. Например:

```python
from aiogram import Bot, Dispatcher, types

bot = Bot(token='YOUR_TOKEN_HERE')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!")

@dp.message_handler(lambda message: message.text == "Как дела?")
async def answer_question(message: types.Message):
    await message.reply("Все хорошо!")
```

### Явная регистрация через Dispatcher
В этом подходе вы явно указываете, какие обработчики должны быть связаны с какими сообщениями или командами, используя методы экземпляра `Dispatcher`. Это может быть полезно для более сложной логики регистрации, где требуется более тонкая настройка или когда обработчики определены в разных модулях. Пример:

```python
from aiogram import Bot, Dispatcher, types

async def send_welcome(message: types.Message):
    await message.reply("Привет!")

async def answer_question(message: types.Message):
    await message.reply("Все хорошо!")

bot = Bot(token='YOUR_TOKEN_HERE')
dp = Dispatcher(bot)

dp.register_message_handler(send_welcome, commands=['start'])
dp.register_message_handler(answer_question, lambda message: message.text == "Как дела?")
```

Оба подхода валидны и могут быть использованы в зависимости от предпочтений разработчика и специфики проекта. Вы можете выбирать между ними, исходя из удобства организации кода, читаемости и сложности логики обработки сообщений.