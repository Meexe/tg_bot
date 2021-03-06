from simple_settings import settings

'''
Types of messages:

voice
photo
text
doc

message = {
    'type': ____,
    'payload': ____,
    'delay': ____,
}
'''


class Task:
    
    def __init__(self, start, end, tips=None):
        self.start_messages = start
        self.end_messages = end
        self.tips = tips


tasks = [
    # Памятник Пушкину
    Task(
        [
            {
                'type': 'text',
                'payload': 'Ваше путешествие начинается здесь',
                'delay': 2,
            },
            {
                'type': 'photo',
                'payload': open(settings.base + 'photos/UHtVwkUicKc.jpg', 'rb'),
                'delay': 5,
            },
            {
                'type': 'text',
                'payload': 'Ваше первое задание: найти со мной общий язык',
                'delay': 2,
            },
            {
                'type': 'text',
                'payload': '0JLQsdC70LjQt9C4INCi0LLQtdGA0YHQutC+0LPQviDQuCDQod' \
                           'GC0YDQsNGB0YLQvdC+0LPQviwK0JIg0LzQtdGC0YDQviDQt9C0' \
                           '0LXRgdGMINCf0YPRiNC60LjQvdGB0LrQsNGPINCy0YXQvtC0Lg' \
                           'rQmCDQsiDQutCw0LzQvdC1INC90LDRiCDQv9C+0Y3RgiDRgdGD' \
                           '0YDQvtCy0L4K0J3QsCDQv9C10YDQtdC60YDQtdGB0YLQstC1IN' \
                           'C30LTQtdGB0Ywg0LLQsNGBINC20LTQtdGCLg==',
                'delay': 0,
            },
        ],
        [
            {
                'type': 'text',
                'payload': 'Славное начало квеста!',
                'delay': 2,
            }
        ],
    ),
    Task(
        [
            {
                'type': 'text',
                'payload': 'Пусть весь мир видит как вы проводите время! Ну и лайки, само собой',
                'delay': 0,
            },
        ],
        [
            {
                'type': 'text',
                'payload': 'Жюри нужно немного времени посовещаться',
                'delay': 2,
            }
        ],
    ),
    # Гнездинский
    Task(
	    [
            {
             	'type': 'text',
                'payload': 'А тем временем нам пора в Гнездниковский переулок',
                'delay': 2,
            },
            {
             	'type': 'voice',
                'payload': open(settings.base + 'voices/nest.ogg', 'rb'),
                'delay': 30,
            },
            {
             	'type': 'photo',
                'payload': open(settings.base + 'photos/YByKiaC_fi8.jpg', 'rb'),
                'delay': 5,
            },
            {
             	'type': 'text',
                'payload': 'Этот человек утверждает, что где-то здесь водится очень редкая и гордая птица. ' \
                           'Вот бы поймать ее, хотя бы на камеру...',
                'delay': 0,
            },
	    ],
	    [
	        {
		        'type': 'text',
		        'payload': 'Отныне вы почетные орнитологи!',
		        'delay': 2,
	        },
            {
                'type': 'text',
                'payload': 'Кстати, тут неподалеку есть театр. Обожаю театры! Не хотите заглянуть?',
                'delay': 6,
            },
	    ],
    ),
    # МХАТ
    Task(
	    [
	        {
           	    'type': 'text',
                'payload':	'При входе висит большая золотая схема. ' \
			                'Сколько чисел... Но нам нужно всего лишь три. ' \
				            'Первое число - количество рядов в левой части первого яруса. ' \
				            'Второе - число мест в самом длинном ряду в партере + первое число. ' \
                            'И, наконец, третье - число рядов партера, названных не цифрами, а буквами',
                'delay': 0,
            },
        ],
        [
	        {
                'type': 'text',
                'payload':	'Эти числа, дорогие мои ведьмачки - точное указание на номер главы, абзаца и предложения в книге,' \
                            'которые вам укажут, куда двигаться дальше. Вперед, мессир уже ждет!',
                'delay': 2,
            },
        ],
    ),
    # Никитские Ворота
    Task(
        [
	        {
                'type': 'text',
                'payload':'Ах! Кажется, здесь неподалеку состоится свадьба! Так держать, Александр Серегевич! ' \
                          'Кажется молодожены не против сфотографироваться с вами!',
                'delay': 0,
            },
	    ],
        [
            {
                'type': 'text',
                'payload': 'Ох, ну и праздник!',
                'delay': 2,
            },
        ],
    ),
    # Перекус на Никитских Воротах
    Task(
	    [
            {
                'type': 'voice',
                'payload': open(settings.base + 'voices/nikitskie.ogg', 'rb'),
                'delay': 20,
            },
            {
             	'type': 'text',
                'payload': 'Устали? Тут на углу есть милое, уютное кафе, попейте чаю, вы заслужили. ' \
				           'Мой исполнительный друг заказал столик на имя Волонда. ' \
                           'Намекните, когда отдохнете',
                'delay': 2,
            },
            {
                'type': 'photo',
                'payload': open(settings.base + 'photos/rGGyr9x980Q.jpg', 'rb'),
                'delay': 0,
            },
	    ],
	    [
	        {
           	    'type': 'text',
               	'payload':	'Снова в путь! Мне бесконечно импонирует данное заведение, однако нам пора',
                'delay': 2,
            },
	    ],
    ),
    # Никитские ворота - уход
    Task(
        [
            {
                'type': 'text',
                'payload': 'На ул "лнимицопошта"! Понимаю, вам сложно понять эту тарабарщину, но вы же безопасницы, должны ' \
				           'понимать наш язык, справитесь',
                'delay': 0,
            }
        ],
        [
            {
                'type': 'text',
                'payload': 'Поблагодарим автора этой замечательной загадки и пойдем дальше',
                'delay': 2,
            }
        ],
    ),
    # Особняк Маргариты - барельеф
    Task(
	    [
            {
         	    'type': 'text',
                'payload':	'Направьте свои стопы по левой стороне улицы, найдите меня!',
                'delay': 4,
            },
	    {
          	'type': 'text',
                'payload': 'Подходите скорее, сфотографируемся',
                'delay': 0,
            },
        ],
        [
	    {
         	'type': 'voice',
                'payload': open(settings.base + 'voices/mansion.ogg', 'rb'),
                'delay': 20,
            },
        ],
    ),
    # Особняк Маргариты - птица
    Task(
        [
	    {
             	'type': 'text',
                'payload': 'Если ещё не устали, найдите на доме все ту же благородную ' \
                           'птицу. Но предупреждаю, сделать это будет слегка посложнее..',
                'delay': 0,
            },
        ],
	[
	    {
                'type': 'text',
                'payload': 'Хорошо сохранился домик. Но время не ждет, вперед, к Патриаршим!',
                'delay': 20,
	    },
        ],
    ),
    # Патриаршие - фашист
    Task(
	    [  
            {
             	'type': 'text',
                'payload': 'Присаживайтесь поудобнее на какую-нибудь лавочку, и осторожнее, тут ' \
                           'где-то бродит Аннушка!',
                'delay': 4,
            },
	        {
             	'type': 'voice',
                'payload': open(settings.base + 'voices/lakes.ogg', 'rb'),
                'delay': 20,
            },
	        {
             	'type': 'text',
                'payload': 'В одном из фрагментов книги я при помощи машинного обуч.. Тьфу, темной магии! ' \
				           'word2vec, заменил некоторые слова. Угадаете хотя бы одно? ... ' \
				           '"– Вы – фашист? – осведомился Безнадзорный. ' \
				           '– Я-то?.. – Переспросил доцент и вдруг задумался. – Да, пожалуй, фашист… – сказал он."',
                'delay': 0,
            },
	    ],
	    [
	        {
           	    'type': 'text',
               	'payload': 'Оригинальный отрывок звучит так: ' \
				           '"– Вы – немец? – осведомился Бездомный. '  \
				           '– Я-то?.. – Переспросил профессор и вдруг задумался. – Да, пожалуй, немец… – сказал он." ' \
				           'Что ж, таков черный юмор вашего покорного друга.',
                'delay': 2,
	        },
	    ],
    ),
    # Патриаршие - преподаватели
    Task(
	    [   
            {
             	'type': 'text',
                'payload': 'Пройдемте на другую сторону Патриарших, там стоят прекрасные скульптуры животных. ' \
				           'И выложить фотокарточку не забудьте, я их коллекционирую',
                'delay': 2,
            },
        ],
        [
        ],
    ),
    # Патриаршие - преподаватели 2
    Task(
        [
	        {
             	'type': 'text',
                'payload': 'Узнаете ваших профессоров? Тех, кто творит зло во имя добра каждый день? ' \
                           'Попробуйте угадать кто из них кто',
                'delay': 4,
            },
	    ],
	    [
	        {
           	    'type': 'text',
               	'payload': 'Жжуть жживотные. Мяу. Поскорее бы домой',
                'delay': 8,
	        },
	    ]
    ),
    # По дороге на нехорошую
    Task(
	    [
            {
             	'type': 'text',
                'payload': 'А пока вы идете-попробуйте угадать следующих персонажей:',
                'delay': 2,
            },
	        {
             	'type': 'text',
                'payload': 'Член свиты Воланда. Маленького роста, пламенно‑рыжий, кривоглазый, ' \
				           'с клыком во рту и разбойничей рожей.', #Азазелло - Дима Кондратьев
                'delay': 0,
            },
        ],
        [

        ],
    ),
    Task(
        [
	        {
             	'type': 'text',
                'payload': 'Сомнительный и страннный мужчина... В клетчатых брючонках, в треснутом пенсне и... ' \
				           'рожа совершенно невозможная! Волшебник с дребезжащим треснутым тенором. Всюду ходит с большим лохматым котом. ' \
				           'Одним словом - наглый гаер.', # Паша Пархомец/Саша Петраки
                'delay': 0,
            },
        ],
        [

        ],
    ),
    Task(
        [
	        {
             	'type': 'text',
                'payload': 'Почтительный с дамами, но похож на оборванца, ходит на задних лапах как человек, ' \
				'наглый, неугомонный весельчак, любящий безобразничать. Постоянно что-то починяет…', # Бегемот - Антон
                'delay': 0,
            },
        ],
        [

        ],
    ),
    Task(
        [
	        {
             	'type': 'text',
                'payload': 'Малообразованный, невежественный холостяк. Имеющий вредные привычки '\
				'и любящий выражаться вычурно и фигурально. Одним словом, поэт!', # однозначно
                'delay': 0,
            },
        ],
        [

        ],
    ),
    Task(
        [
	        {
             	'type': 'text',
                'payload': '«Я — часть той силы, что вечно хочет зла и вечно совершает благо.»', # Иваненыч
                'delay': 0,
            },
	    ],
	    [
	        {
           	    'type': 'text',
               	'payload': 'Вхух. Ну вы даете))',
                'delay': 2,
	        },
	    ],
    ),
    # дом Булгакова
    Task(
	    [   
            {
             	'type': 'text',
                'payload': 'В продолжении нашей культурной программы, предлагаю пройти в музей',	
                'delay': 6,
            },
	        {
             	'type': 'text',
                'payload': 'Перед моим изображением на лестнице прочтите выразительно самый любимый ' \
				           'отрывок из книги и выложите в истории instagram, И никаких отговорок!',
                'delay': 6,
            },
	    ],
	    [
	        {
             	'type': 'text',
                'payload': 'А сейчас спускайтесь на улицу, там вас ждет САМОЕ ВАЖНОЕ задание',
                'delay': 20,
            },
	    ]
    ),
    # приручи кота
    Task(
	    [
   	        {
             	'type': 'text',
                'payload': 'А слабо приручить Бегемота? Только не мухлевать, без доказательств задание вам не зачтется',
                'delay': 2,
            },
	        {
             	'type': 'text',
                'payload': 'Вы должны выложить story в instagram, мне льстит внимание людей', 
                'delay': 2
            },
	    ],
	    [
	        {
             	'type': 'text',
                'payload':	'Вы были великолепны! Так уж и быть, вот вам адрес, где пройдет НАСТОЯЩИЙ бал сатаны!',
                'delay': 2
            },
	        {
             	'type': 'text',
                'payload': 'антикафе', # TODO место антикафе
                'delay': 2
            },
	    ],
    ),
]
