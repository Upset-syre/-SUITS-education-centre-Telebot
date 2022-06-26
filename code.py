import telebot
import requests
import json
#Hello there!\nWelcome to the official telegram-bot of\nSUITS ENGLISH EDUCATION CENTER


bot=telebot.TeleBot('1361993168:AAHtRhPW1g3yfGHAPZ66aP586TiOHKEgVyE')

mainmenu=telebot.types.InlineKeyboardMarkup()
telnomer=telebot.types.ReplyKeyboardMarkup(True,one_time_keyboard=True)
subjectlists=telebot.types.InlineKeyboardMarkup()
bosh_sahifa=telebot.types.ReplyKeyboardMarkup(True,one_time_keyboard=True)
bosh_shf_btn=telebot.types.KeyboardButton('Bosh sahifaga qaytish🔙'.upper())
bosh_sahifa.add(bosh_shf_btn)
gallereya=telebot.types.InlineKeyboardMarkup()
orqaga=telebot.types.InlineKeyboardMarkup()
orqagarpl=telebot.types.KeyboardButton('Orqaga qaytish⬅️'.upper())



Tiltanlash=telebot.types.ReplyKeyboardMarkup(True,True)

uzb=telebot.types.KeyboardButton("O'zbek tili🇺🇿".upper())
rus=telebot.types.KeyboardButton("Русский язык🇷🇺".upper())
Tiltanlash.row(uzb,rus)

mainmenurus=telebot.types.InlineKeyboardMarkup()
button1ru=telebot.types.InlineKeyboardButton('Оставить заявку✍️'.upper(),callback_data='registration')
button2ru=telebot.types.InlineKeyboardButton('сменить язык🌐'.upper(),callback_data='language')
button3ru=telebot.types.InlineKeyboardButton('Адрес📍'.upper(),callback_data='location')
button4ru=telebot.types.InlineKeyboardButton("О насℹ️".upper(),callback_data='bizhaqimizda')
button5ru=telebot.types.InlineKeyboardButton('Галлерея📸'.upper(),callback_data='gallery')
button6ru=telebot.types.InlineKeyboardButton('Акции💯'.upper(),callback_data='action')
button7ru=telebot.types.InlineKeyboardButton('админы👨‍💻'.upper(),callback_data='admin')

mainmenurus.add(button1ru)
mainmenurus.add(button2ru)
mainmenurus.add(button3ru)
mainmenurus.add(button4ru)
mainmenurus.add(button5ru)
mainmenurus.add(button6ru)
mainmenurus.add(button7ru)
subjectlists_rus=telebot.types.InlineKeyboardMarkup()

button_1=telebot.types.InlineKeyboardButton('Английский язык🇬🇧'.upper(),callback_data='en')
button_2=telebot.types.InlineKeyboardButton('Математика🔥'.upper(),callback_data='math')
button_3=telebot.types.InlineKeyboardButton('Ielts🇺🇸'.upper(),callback_data='ielts')
button_4=telebot.types.InlineKeyboardButton('Русский язык🇷🇺'.upper(),callback_data='rus')
button_5=telebot.types.InlineKeyboardButton('Главное меню🔙'.upper(),callback_data='mainmenu')

subjectlists_rus.add(button_1)
subjectlists_rus.add(button_2)
subjectlists_rus.add(button_3)
subjectlists_rus.add(button_4)
subjectlists_rus.add(button_5)

gallereya_rus=telebot.types.InlineKeyboardMarkup()

gallery_btn1=telebot.types.InlineKeyboardButton('Уроки👨‍🎓👩‍🎓'.upper(),callback_data='1dars')
gallery_btn2=telebot.types.InlineKeyboardButton("Достижения🔝🔥".upper(),callback_data='2natija')
gallery_btn3=telebot.types.InlineKeyboardButton('Мероприятия🎁🎈'.upper(),callback_data='3tadbirlar')

gallereya_rus.add(gallery_btn1)
gallereya_rus.add(gallery_btn2)
gallereya_rus.add(gallery_btn3)

telnomer_rus=telebot.types.ReplyKeyboardMarkup(True,True)

button__1_rus=telebot.types.KeyboardButton("Отправить номер телефона📲".upper(),request_contact=True)
orqagarpl_rus=telebot.types.KeyboardButton('Назад⬅️'.upper())

bosh_shf_btn_rus=telebot.types.KeyboardButton('Главное меню🔙'.upper())

bosh_sahifa_rus=telebot.types.ReplyKeyboardMarkup(True,one_time_keyboard=True)

bosh_sahifa_rus.add(bosh_shf_btn_rus)

telnomer_rus.add(button__1_rus)
telnomer_rus.add(orqagarpl_rus)
telnomer_rus.add(bosh_shf_btn_rus)

orqaga_rus=telebot.types.InlineKeyboardMarkup()

orqaga_rus.add(button_5)




button1=telebot.types.InlineKeyboardButton('Ariza qoldirish✍️'.upper(),callback_data='registration')
button2=telebot.types.InlineKeyboardButton('Tilni ozgartirish🌐'.upper(),callback_data='language')
button3=telebot.types.InlineKeyboardButton('Manzil📍'.upper(),callback_data='location')
button4=telebot.types.InlineKeyboardButton("Biz haqimizdaℹ️".upper(),callback_data='bizhaqimizda')
button5=telebot.types.InlineKeyboardButton('Gallereya📸'.upper(),callback_data='gallery')
button6=telebot.types.InlineKeyboardButton('Aksiyalar💯'.upper(),callback_data='action')
button7=telebot.types.InlineKeyboardButton('Adminlar👨‍💻'.upper(),callback_data='admin')


button_1=telebot.types.InlineKeyboardButton('Ingliz tili🇬🇧'.upper(),callback_data='en')
button_2=telebot.types.InlineKeyboardButton('Matematika🔥'.upper(),callback_data='math')
button_3=telebot.types.InlineKeyboardButton('Ielts🇺🇸'.upper(),callback_data='ielts')
button_4=telebot.types.InlineKeyboardButton('Rus tili🇷🇺'.upper(),callback_data='rus')
button_5=telebot.types.InlineKeyboardButton('bosh Sahifaga qaytish🔙'.upper(),callback_data='mainmenu')

gallery_btn1=telebot.types.InlineKeyboardButton('Dars jarayoni👨‍🎓👩‍🎓'.upper(),callback_data='1dars')
gallery_btn2=telebot.types.InlineKeyboardButton("Natijalar🔝🔥".upper(),callback_data='2natija')
gallery_btn3=telebot.types.InlineKeyboardButton('Tadbirlar🎁🎈'.upper(),callback_data='3tadbirlar')


gallereya.add(gallery_btn1)
gallereya.add(gallery_btn2)
gallereya.add(gallery_btn3)
gallereya.add(button_5)

orqaga.add(button_5)

subjectlists.add(button_1)
subjectlists.add(button_2)
subjectlists.add(button_3)
subjectlists.add(button_4)
subjectlists.add(button_5)

button__1=telebot.types.KeyboardButton("Telefon raqamni jo'natish📲".upper(),request_contact=True)
telnomer.add(button__1)
telnomer.add(orqagarpl)
telnomer.add(bosh_shf_btn)

mainmenu.add(button1)
mainmenu.add(button2)
mainmenu.add(button3)
mainmenu.add(button5)
mainmenu.add(button4)
mainmenu.add(button6)
mainmenu.add(button7)





povod=''
get_contact=False
global language
language=None


@bot.message_handler(commands=["start"])
def start(message):
    print(str(message.chat.id))
    global language
    if language==None:
        bot.send_message(message.chat.id,'Tilni tanlang  /  Выберите язык :'.upper(),reply_markup=Tiltanlash)
    else:
        if language:
            bot.send_message(message.chat.id,'Assalomu alaykum\n⚜️SUITS ENGLISH EDUCATION⚜️\nrasmiy telegram botiga hush kelibsiz🤖'.upper(),reply_markup=mainmenu)
        else:
            bot.send_message(message.chat.id,'Добро пожаловать \nв телеграмм-бот🤖 учебного центра\n⚜️SUITS ENGLISH EDUCATION⚜️'.upper(),reply_markup=mainmenurus)
@bot.message_handler(commands=["developer"])
def developer(message):
    bot.send_message(message.chat.id,"Developer👨‍💻:\n\n⚡️@Hornet_21⚡️".upper(),reply_markup=bosh_sahifa)


@bot.callback_query_handler(func=lambda call: True)
def mains(call):
    global povod
    if language:
        if call.message:
            if call.data == 'registration':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Kursni tanlang⬇️:".upper(),reply_markup=subjectlists)
            if call.data=='en':
                image1 = open('uzeng.png', 'rb')
                bot.send_photo(call.message.chat.id,image1)
                bot.send_message(call.message.chat.id,"Ariza qoldirish uchun telefon raqamingizni jo'nating📲".upper(),reply_markup=telnomer)
                povod='ingliz tili'
            if call.data=='math':
                bot.send_message(call.message.chat.id,"👨‍🎓Matematika Kursi👩‍🎓:\n\n✅Milliy OTM larga tayyarlov\n✅Chet el OTM larga tayyarlov\n✅Litseyga tayyorlov\n✅Boshlangich matematika(6-sinf)\n✅Oraliq testlar va sinovlar\n✅Haftasiga 3 martadan dars \n🔥Narhi 300 000 so'm\n\n🔝@suits_official_bot".upper())
                bot.send_message(call.message.chat.id,"Ariza qoldirish uchun telefon raqamingizni jo'nating📲".upper(),reply_markup=telnomer)
                povod='matematika'
            if call.data=='ielts':
                bot.send_message(call.message.chat.id,"🇺🇸Ielts Courses🇺🇸:\n\n✅Ielts Fondation 6+\n✅Ielts Graduation 7+\n⏳Muddati: 3 oy dan\n✅Haftasiga 4 martadan dars \n🔥Narxi: 450 000 so'm\n\n🔝@suits_official_bot".upper())
                bot.send_message(call.message.chat.id,"Ariza qoldirish uchun telefon raqamingizni jo'nating📲".upper(),reply_markup=telnomer)
                povod='ielts'
            if call.data=='rus':
                bot.send_message(call.message.chat.id,"🇷🇺Rus tili kurslari🇷🇺:\n\n✅Rus tili gramatikasi\n✅Og'zaki gaplashish\n⏳Muddati: 3 oy dan\n✅Haftasiga 3 martadan dars \n🔥Narxi: 300 000 so'm\n\n🔝@suits_official_bot".upper())
                bot.send_message(call.message.chat.id,"Ariza qoldirish uchun telefon raqamingizni jo'nating📲".upper(),reply_markup=telnomer)
                povod='rus tili'
            if call.data=='language':
                bot.send_message(call.message.chat.id,'Tilni tanlang  /  Выберите язык :'.upper(),reply_markup=Tiltanlash)
            if call.data=='location':
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='Bizning manzil📍:\n\n🏢Toshkent, uchtepa tumani, Farhod va Lutfiy kochalari kesishuvi, AZIZ Centre, 2 etaj, 57 xona'.upper())
                bot.send_location(call.message.chat.id,41.285738,69.186160,reply_markup=bosh_sahifa)
            if call.data=='mainmenu':
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='Assalomu alaykum\n⚜️SUITS ENGLISH EDUCATION⚜️\nrasmiy telegram botiga hush kelibsiz🤖'.upper(),reply_markup=mainmenu)
            if call.data=='gallery':
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Bo'limni tanlang😊:".upper(),reply_markup=gallereya)
            if call.data=='1dars':
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='📸 Dars jarayoni 📸:\n\n⏳ Iltimos kuting ⏳'.upper())
                n=1
                while n<11:
                    photo = open('1/'+str(n)+'.jpg', 'rb')
                    bot.send_document(call.message.chat.id,photo)
                    n=n+1
                    photo.close()
                bot.send_message(call.message.chat.id,str(n-1)+"/"+str(n-1)+" rasm ko'rsatildi😊".upper(),reply_markup=bosh_sahifa)
            if call.data=='2natija':
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='📸 Natijalar 📸:\n\n⏳ Iltimos kuting ⏳'.upper())
                n=1
                while n<10:
                    photo = open('2/'+str(n)+'.jpg', 'rb')
                    bot.send_document(call.message.chat.id,photo)
                    n=n+1
                    photo.close()
                bot.send_message(call.message.chat.id,str(n-1)+'/'+str(n-1)+" rasm ko'rsatildi😊".upper(),reply_markup=bosh_sahifa)
            if call.data=='3tadbirlar':
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='📸 Tadbirlar 📸:\n\n⏳ Iltimos kuting ⏳'.upper())
                n=1
                while n<6:
                    photo = open('3/'+str(n)+'.jpg', 'rb')
                    bot.send_document(call.message.chat.id,photo)
                    n=n+1
                    photo.close()
                bot.send_message(call.message.chat.id,str(n-1)+'/'+str(n-1)+" rasm ko'rsatildi😊".upper(),reply_markup=bosh_sahifa)
            if call.data=='action':
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Hozircha bo'limda ma'lumot yo'q🌝".upper(),reply_markup=orqaga)
            if call.data=='admin':
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="👩‍💻Admin blan bog'lanish👨‍💻:\n\n@SUITSENGLISHADMIN\n+998 97 775 37 44",reply_markup=orqaga)
            if call.data=="bizhaqimizda":
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="⚜️SUITS ENGLISH EDUCATION⚜️-bu innovatsion o'quv markazi. O'zimizning inqilobiy o'qitish uslubimiz bilan siz fanlarni tez va samarali o'rganishingiz mumkin!\n\n⚜️SUITS ENGLISH EDUCATION⚜️- bu:\n-👩‍🎓 Minglab mamnun talabalar\n-✅ Vaqt bilan sinalgan o'qituvchilar\n-📈 O'qish va zavqni birlashuvi\n-🔥 Muvaffaqiyatingiz kaliti\n-⚡️ Aqlli odamlarni tanlovi!\n\n-📞Tafsilotlar telefon orqali: +998 97 775 37 44 \n\n@SUITS_OFFICIAL_BOT".upper(),reply_markup=orqaga)
    else:
        if call.message:
            if call.data == 'registration':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите курс⬇️:".upper(),reply_markup=subjectlists_rus)
            if call.data=='en':
                image2 = open('rueng.png', 'rb')
                bot.send_photo(call.message.chat.id,image2)
                bot.send_message(call.message.chat.id,"отправьте номер для того чтобы оставить заявку📲".upper(),reply_markup=telnomer_rus)
                povod='ingliz tili'
            if call.data=='math':
                bot.send_message(call.message.chat.id,'👨‍🎓Курсы математики👩‍🎓:\n\n✅Подготовка на национальные ВУЗы\n✅Подготовка на Иностранные Вузы\n✅Подготовка к лицею\n✅Основы математики(6-класс)\n✅Промежуточные контрольные и тесты\n✅3 Занятий в неделю \n🔥Цена 300 000 сум\n\n🔝@suits_official_bot'.upper())
                bot.send_message(call.message.chat.id,"отправьте номер для того чтобы оставить заявку📲".upper(),reply_markup=telnomer_rus)
                povod='matematika'
            if call.data=='ielts':
                bot.send_message(call.message.chat.id,'🇺🇸Курсы Ielts🇺🇸:\n\n✅Ielts Fondation 6+\n✅Ielts Graduation 7+\n⏳Длительность: с 3 месяцов\n✅4 Занятий в неделю \n🔥Цена: 450 000 сум\n\n🔝@suits_official_bot'.upper())
                bot.send_message(call.message.chat.id,"отправьте номер для того чтобы оставить заявку📲".upper(),reply_markup=telnomer_rus)
                povod='ielts'
            if call.data=='rus':
                bot.send_message(call.message.chat.id,"🇷🇺Курсы русского языка🇷🇺:\n\n✅Грамматика\n✅Устная речь\n⏳Длительность: с 3 месяцов\n✅3 Занятий в неделю \n🔥Цена: 300 000 сум\n\n🔝@suits_official_bot".upper())
                bot.send_message(call.message.chat.id,"отправьте номер для того чтобы оставить заявку📲".upper(),reply_markup=telnomer_rus)
                povod='rus tili'
            if call.data=='language':
                bot.send_message(call.message.chat.id,'Tilni tanlang  /  Выберите язык :'.upper(),reply_markup=Tiltanlash)
            if call.data=='location':
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='Мы находимся в📍:\n\n🏢Ташкент, учтепинский район, Перекресток улиц фарход и лутфий, AZIZ Centre, 2 этаж, 57 комната'.upper())
                bot.send_location(call.message.chat.id,41.285738,69.186160,reply_markup=bosh_sahifa_rus)
            if call.data=='mainmenu':
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='Добро пожаловать \nв телеграмм-бот🤖 учебного центра\n⚜️SUITS ENGLISH EDUCATION⚜️'.upper(),reply_markup=mainmenurus)
            if call.data=='gallery':
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="выберите раздел😊:".upper(),reply_markup=gallereya_rus)
            if call.data=='1dars':
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='📸 Уроки 📸:\n\n⏳ Пожалуйста подождите ⏳'.upper())
                n=1
                while n<11:
                    photo = open('1/'+str(n)+'.jpg', 'rb')
                    bot.send_document(call.message.chat.id,photo)
                    n=n+1
                    photo.close()
                bot.send_message(call.message.chat.id,str(n-1)+"/"+str(n-1)+" Показано😊".upper(),reply_markup=bosh_sahifa_rus)
            if call.data=='2natija':
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='📸 Достижения 📸:\n\n⏳ Пожалуйста подождите ⏳'.upper())
                n=1
                while n<10:
                    photo = open('2/'+str(n)+'.jpg', 'rb')
                    bot.send_document(call.message.chat.id,photo)
                    n=n+1
                    photo.close()
                bot.send_message(call.message.chat.id,str(n-1)+'/'+str(n-1)+" Показано😊".upper(),reply_markup=bosh_sahifa_rus)
            if call.data=='3tadbirlar':
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='📸 Мероприятия 📸:\n\n⏳ Пожалуйста подождите ⏳'.upper())
                n=1
                while n<6:
                    photo = open('3/'+str(n)+'.jpg', 'rb')
                    bot.send_document(call.message.chat.id,photo)
                    n=n+1
                    photo.close()
                bot.send_message(call.message.chat.id,str(n-1)+'/'+str(n-1)+"Показано😊".upper(),reply_markup=bosh_sahifa_rus)
            if call.data=='action':
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Пока что нет акций🌝".upper(),reply_markup=orqaga_rus)
            if call.data=='admin':
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="👩‍💻Связаться с админом👨‍💻:\n\n@SUITSENGLISHADMIN\n+998 97 775 37 44",reply_markup=orqaga_rus)
            if call.data=="bizhaqimizda":
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="⚜️SUITS ENGLISH EDUCATION⚜️-это инновационный учебный центр. Благодаря нашему собственному революционному методу обучения вы сможете усвоить предметы быстро и эффектно!\n⚜️SUITS ENGLISH EDUCATION⚜️- это:\n-👩‍🎓 Тысячи довольных студентов\n-✅ Проверенные временем учителя\n-📈 Объединение обучения и удовольствия\n-🔥 Залог вашего успеха\n-⚡️ Выбор умных людей!\n-📞Подробности по телефону: +998 97 775 37 44\n@SUITS_OFFICIAL_BOT".upper(),reply_markup=orqaga_rus)






#bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Iltimos ismingizni kiriting⬇️")
            #get_number=True

@bot.message_handler(content_types=['text'])
def m1(message):
    global language
    if message.text=='Bosh sahifaga qaytish🔙'.upper():
        bot.send_message(message.chat.id,'Assalomu alaykum\n⚜️SUITS ENGLISH EDUCATION⚜️\nrasmiy telegram botiga hush kelibsiz🤖'.upper(),reply_markup=mainmenu)
    if message.text=='Orqaga qaytish⬅️'.upper():
        bot.send_message(message.chat.id, text="Kursni tanlang⬇️:".upper(),reply_markup=subjectlists)
        #bot.send_message(message.chat.id,'')
    if message.text=="Назад⬅️".upper():
        bot.send_message(message.chat.id, text="Выберите курс⬇️:".upper(),reply_markup=subjectlists_rus)
    if message.text=='главное меню🔙'.upper():
        bot.send_message(message.chat.id,'Добро пожаловать \nв телеграмм-бот🤖 учебного центра\n⚜️SUITS ENGLISH EDUCATION⚜️'.upper(),reply_markup=mainmenurus)
    if message.text=="O'zbek tili🇺🇿".upper():
        language=True
        bot.send_message(message.chat.id,'Assalomu alaykum\n⚜️SUITS ENGLISH EDUCATION⚜️\nrasmiy telegram botiga hush kelibsiz🤖'.upper(),reply_markup=mainmenu)
    if message.text=="Русский язык🇷🇺".upper():
        language=False
        bot.send_message(message.chat.id,'Добро пожаловать \nв телеграмм-бот🤖 учебного центра\n⚜️SUITS ENGLISH EDUCATION⚜️'.upper(),reply_markup=mainmenurus)

@bot.message_handler(content_types=['contact'])
def cntc(message):
    contact=message.contact.phone_number
    bot.send_message(201458407,contact+' - '+povod)
    bot.send_message(848994232,contact+' - '+povod)
    if language:
        bot.send_message(message.chat.id,'Arizangiz uchun rahmat, tez orada siz bilan aloqaga chiqamiz😊'.upper(),reply_markup=bosh_sahifa)
    else:
        bot.send_message(message.chat.id,'Спасибо за вашу заявку, в скором времени мы с вами свяжемся😊'.upper(),reply_markup=bosh_sahifa_rus)




bot.polling(none_stop=True, interval=0)