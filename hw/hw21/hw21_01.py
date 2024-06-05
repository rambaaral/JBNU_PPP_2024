
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


id = 7492385762

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('안녕하세요! 우마정보봇입니다. 위키, 극장판, 애니, 게임 등의 단어를 인식합니다.')


def handle_keyword(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id == id:
        if '위키' in update.message.text:
            update.message.reply_text('우마무스메 나무위키: https://namu.wiki/w/%EC%9A%B0%EB%A7%88%EB%AC%B4%EC%8A%A4%EB%A9%94%20%ED%94%84%EB%A6%AC%ED%8B%B0%20%EB%8D%94%EB%B9%84')
        if '극장판' in update.message.text:
            update.message.reply_text('우마무스메 극장판: https://movie-umamusume.jp/\n극장판 나무위키: https://namu.wiki/w/%EC%9A%B0%EB%A7%88%EB%AC%B4%EC%8A%A4%EB%A9%94%20%ED%94%84%EB%A6%AC%ED%8B%B0%20%EB%8D%94%EB%B9%84%20%EC%83%88%EB%A1%9C%EC%9A%B4%20%EC%8B%9C%EB%8C%80%EC%9D%98%20%EB%AC%B8')
        if '애니' or '1기' or '2기' or '3기' in update.message.text:
            update.message.reply_text('애니메이션 나무위키: https://namu.wiki/w/%EC%9A%B0%EB%A7%88%EB%AC%B4%EC%8A%A4%EB%A9%94%20%ED%94%84%EB%A6%AC%ED%8B%B0%20%EB%8D%94%EB%B9%84/%EC%95%A0%EB%8B%88%EB%A9%94%EC%9D%B4%EC%85%98')
        if '게임' in update.message.text:
            update.message.reply_text('열혈말딸: https://hachamecha-umamusume.jp/ko/\n나무위키: https://namu.wiki/w/%EC%9A%B0%EB%A7%88%EB%AC%B4%EC%8A%A4%EB%A9%94%20%ED%94%84%EB%A6%AC%ED%8B%B0%20%EB%8D%94%EB%B9%84%20%EC%97%B4%ED%98%88%20%EC%9A%B0%EB%8B%B9%ED%83%95%ED%83%95%20%EB%8C%80%EA%B0%90%EC%82%AC%EC%A0%9C!')
    else:
        update.message.reply_text('이 기능을 사용할 권한이 없습니다.')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main():
    token = "7165925531:AAEgHTKBt5Pi31Iu3Bm8eiMXz-yJTBULFAg"
    
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(MessageHandler(Filters.text & Filters.regex('위키'), handle_keyword))
    dispatcher.add_handler(MessageHandler(Filters.text & Filters.regex('극장판'), handle_keyword))
    dispatcher.add_handler(MessageHandler(Filters.text & Filters.regex(r'(1기|2기|3기|애니)'), handle_keyword))
    dispatcher.add_handler(MessageHandler(Filters.text & Filters.regex('게임'), handle_keyword))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
