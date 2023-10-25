import asyncio

from functools import partial

from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio import start_server
from pywebio_battery import *

def show_music(choice):
    with use_scope('Music', clear=True):
        if choice == "Показать музыку":



        if choice == "Скрыть музыку":
            clear('Music')

def btn_click(a):
    with use_scope('hobby', clear=True):
        put_text(f"Для вас играет: {a}")



        put_audio(url)

 #
def edit_row(choice, row):
    put_text("You click %s button ar row %s" % (choice, row))





chat_msgs = []
online_users = set()

MAX_MESSAGES_COUNT = 100


async def main():
    global chat_msgs

    put_markdown(
        "## 🦄 Добро пожаловать в онлайн чат 'НАВА'\n🌈Только здесь вы в полной мере смжете насладиться общением в интернете."
        "\n✨Забудьте про всякий вк, тг, inst. 'НАВА' - выбор самых крутых ребят!")

    put_text("🎧 Ниже представлен список прекрасных произведений, которые обязательно скрасят переписку🤟🤟🤟")
    put_buttons(['Показать музыку', 'Скрыть музыку'], onclick=show_music)



    msg_box = output()
    put_scrollable(msg_box, height=300, keep_bottom=True)

    nickname = await input("Войти в чат", required=True, placeholder="Ваше имя",
                           validate=lambda n: "Такой ник уже используется!" if n in online_users or n == '📢' else None)
    online_users.add(nickname)

    chat_msgs.append(('📢', f'`{nickname}` присоединился к чату!'))
    msg_box.append(put_markdown(f'📢 `{nickname}` присоединился к чату'))

    refresh_task = run_async(refresh_msg(nickname, msg_box))

    while True:
        data = await input_group("💭 Новое сообщение", [
            input(placeholder="Текст сообщения ...", name="msg"),
            actions(name="cmd", buttons=["Отправить", {'label': "Выйти из чата", 'type': 'cancel'}])
        ], validate=lambda m: ('msg', "Введите текст сообщения!") if m["cmd"] == "Отправить" and not m['msg']  else None)

        if data is None:
            break

        msg_box.append(put_markdown(f"`{nickname}`: {data['msg']}"))
        chat_msgs.append((nickname, data['msg']))

    refresh_task.close()

    online_users.remove(nickname)
    toast("Вы вышли из чата!")
    msg_box.append(put_markdown(f'📢 Пользователь `{nickname}` покинул чат!'))
    chat_msgs.append(('📢', f'Пользователь `{nickname}` покинул чат!'))

    put_buttons(['Перезайти'], onclick=lambda btn: run_js('window.location.reload()'))



async def refresh_msg(nickname, msg_box):
    global chat_msgs
    last_idx = len(chat_msgs)

    while True:
        await asyncio.sleep(1)

        for m in chat_msgs[last_idx:]:
            if m[0] != nickname:  # if not a message from current user
                msg_box.append(put_markdown(f"`{m[0]}`: {m[1]}"))

        # remove expired
        if len(chat_msgs) > MAX_MESSAGES_COUNT:
            chat_msgs = chat_msgs[len(chat_msgs) // 2:]

        last_idx = len(chat_msgs)


if __name__ == "__main__":
    start_server(main, debug=True, port=8080, cdn=False)