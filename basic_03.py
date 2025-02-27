
import smtplib
import os
from dotenv import load_dotenv
text_letter = ("""Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""")
website = "https://dvmn.org/profession-ref-program/2077647/d6NPX/"
frend_name = "Павел"
my_name = "Даниил"
text_letter = text_letter.replace("%friend_name%",(frend_name))
text_letter = text_letter.replace("%my_name%",(my_name))
text_letter = text_letter.replace("%website%",(website))
from_mail = "danik013@yandex.ru"
to_mail = "2077647@gmail.com"
subjest_mail = "Приглашение!"
headers_ = """\
From: {fr}
To: {to}
Subject: {sub}
Content-Type: text/plain; charset="UTF-8";""".format(fr=from_mail, to=to_mail, sub=subjest_mail)
letter = "{h}\n\n{t}".format(h=headers_, t=text_letter)
letter = letter.encode("UTF-8")
load_dotenv()
mail_login = os.getenv('LOGIN')
mail_pass = os.getenv('PASSWORD')
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(mail_login, mail_pass)
server.sendmail(from_mail, to_mail, letter)
server.quit()


