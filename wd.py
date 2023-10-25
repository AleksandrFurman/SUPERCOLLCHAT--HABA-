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

            put_buttons(
                ['Ольга Бузова & DAVA - Мандаринка!', 'King Crimson - Epitaph', 'Cigarettes After Sex - Apocalypse',
                 'Frank Sinatra - Fly Me To The Moon', "Elvis Presley - Can't Help Falling In Love",
                 'Alex Clare - Too Close',
                 'Depeche Mode - Enjoy The Silence', 'Slowdive - altogether', 'Deftones - Sextape',
                 'Альянс - На заре!', 'Lil peep - Star shopping', 'DJ Snake and Lil Jon - Turn Down For What',
                 'Chase Atlantic - Swim', 'Laki bass - Deset Horse', 'Billie Eilish, Khalid - Lovely',
                 'Gotye - Somebody that I used to know', 'Кис-кис - Мелочь', 'Hozier - Would that I',
                 'The Weeknd (feat. Ed Sheeran) - Dark Times', 'Король и шут - Воспоминания о былой любви'], onclick=btn_click)

        if choice == "Скрыть музыку":
            clear('Music')

def btn_click(a):
    with use_scope('hobby', clear=True):
        put_text(f"Для вас играет: {a}")

        if a == "Ольга Бузова & DAVA - Мандаринка!":
            url = "https://moosic.my.mail.ru/file/04a18a20d10df0d8fdf0fc75de5ab285.mp3"
        elif a == "King Crimson - Epitaph":
            url = "https://moosic.my.mail.ru/file/bfeb583d7e9cee2741faf4b9dbfbe172.mp3"
        elif a == "Cigarettes After Sex - Apocalypse":
            url = "https://moosic.my.mail.ru/file/5cc1d3c447537e9480287dc30a9a773f.mp3"
        elif a == "Frank Sinatra - Fly Me To The Moon":
            url = "https://moosic.my.mail.ru/file/669c5b4d2f5409a2e4168bbad105d7cc.mp3"
        elif a == "Elvis Presley - Can't Help Falling In Love":
            url = "https://moosic.my.mail.ru/file/05811feb7583f71b42d74dd659428c39.mp3"
        elif a == "Depeche Mode - Enjoy The Silence":
            url = "https://moosic.my.mail.ru/file/01179e43e478e38e234213e6acb21a9a.mp3"
        elif a == "Alex Clare - Too Close":
            url = "https://moosic.my.mail.ru/file/fc5111d455346a0524f5ef662cf2116b.mp3"
        elif a == "Slowdive - altogether":
            url = "https://moosic.my.mail.ru/file/662350d39daadc1c0126f3514740f5a0.mp3"
        elif a == "Deftones - Sextape":
            url = "https://moosic.my.mail.ru/file/33c9d795aa363fd9071ef22c507959c9.mp3"
        elif a == "Альянс - На заре!":
            url = "https://moosic.my.mail.ru/file/6e43ce87382f3fdf23b1e46549875b6d.mp3"
        elif a == "Lil peep - Star shopping":
            url = "https://moosic.my.mail.ru/file/7a47d17c35e788b6f5422079f5b0a4f1.mp3"
        elif a == "DJ Snake and Lil Jon - Turn Down For What":
            url = "https://moosic.my.mail.ru/file/5d38f88f58c41a04f496479a5626f257.mp3"
        elif a == "Chase Atlantic - Swim":
            url = "https://moosic.my.mail.ru/file/7e5fecb577f00d3471c839c4a83f59b3.mp3"
        elif a == "Laki bass - Deset Horse":
            url = "https://moosic.my.mail.ru/file/261ecdde53187737bd346d54091bf99e.mp3"
        elif a == "Billie Eilish, Khalid - Lovely":
            url = "https://moosic.my.mail.ru/file/67d2f96bc9042240870d5eb2e4ed589a.mp3"
        elif a == "Gotye - Somebody that I used to know":
            url = "https://moosic.my.mail.ru/file/abd4d59f5a18e6edfca9dc0a1d07d6b6.mp3"
        elif a == "Кис-кис - Мелочь":
            url = "https://moosic.my.mail.ru/file/9bd5e31d4f3476d957a72d4aa641c8dd.mp3"
        elif a == "Hozier - Would that I":
            url = "https://moosic.my.mail.ru/file/798455c3545358b73e1293e207c4b774.mp3"
        elif a == "The Weeknd (feat. Ed Sheeran) - Dark Times":
            url = "https://moosic.my.mail.ru/file/abd14f8fb51b00bcc79611c87560cced.mp3"
        elif a == "Король и шут - Воспоминания о былой любви":
            url = "https://moosic.my.mail.ru/file/da2141c0ab0f32e13fb89fc7b3aa9ffa.mp3"


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
