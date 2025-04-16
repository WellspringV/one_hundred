<div align="center">
<h1>СОТКА<br>[ ... version ]</h1>
<img src="https://kartinki.pics/uploads/posts/2022-12/1671801345_kartinkin-net-p-shtanga-kartinka-krasivo-7.png" align="center" style="width: 100%" />
</div>

------

<div align="center">
<h1><b>О репозитории?</b></h1>
</div>
В этом проекте автоматизируем ведение статистику по здоровому образу жизни


<div align="center">
<h1><b>Больше информации и ссылки</b></h1>
</div>
<p>
<b>Наполняется .</b>  
---------

<div align="center"> 
<h1><b>Скриншоты</b></h1>
</div>
Наполняется

<div align="center"> 
<h1><b>Установка и использование </b></h1>
<p><b>( VPS or Local hosting )</b></p>
</div>
Наполняется
  
<div align="center">
<h1><img src="https://telegra.ph/file/c182d98c9d2bc0295bc86.png" width="45"><b>  
Структура <b></h1>
</div>



```

├── Dockerfile                          
├── LICENSE
├── README.md
├── config.env                         ( For storing all the  environment variables)
├── requirements.txt                   ( For keeping all the library name wich project is using)
├── TelegramBot
│   │
│   ├── __init__.py                   ( Initializing the bot from here.)
│   ├── __main__.py                   ( Starting the bot from here.)
│   ├── config.py                     ( Importing and storing all envireonment variables from config.env)
│   ├── logging.py                    ( Help in logging and get log file)
│   │
│   ├── assets                        ( An assets folder to keep all type of assets like thumbnail, font, constants, etc.)
│   │   └── __init__.py
│   │   ├── font.ttf
│   │   └── template.png
│   │
│   ├── database                      (Sperate folder to manage database related stuff for bigger projects.)
│   │   ├── __init__.py
│   │   ├── database.py              (contain functions related to handle database operations all over the bor)
│   │   └── MongoDb.py               (Contain a MongoDB class to handle CRUD operations on MongoDB collection )
│   │  
│   ├── helpers                       ( Contain all the file wich is imported and  used all over the code. It act as backbone of code.)
│   │   ├── __init__.py
│   │   ├── filters.py 
│   │   ├── decorators.py            ( Contain all the python decorators)
│   │   ├── ratelimiter.py           (Contain RateLimiter class that handle ratelimiting part of the bot.)
│   │   └── functions.py             ( Contain all the functions wich is used all over the code. )
│   │
│   ├── plugins                       ( plugins folder contain all the plugins commands via wich user interact)  
│   │   ├── __init__.py 
│   │   ├── developer
│   │   │   ├── __init__.py
│   │   │   ├── terminal.py
│   │   │   └── updater.py
│   │   │
│   │   ├── sudo
│   │   │   ├── __init__.py
│   │   │   ├── speedtest.py
│   │   │   ├── dbstats.py
│   │   │   └── serverstats.py
│   │   │   
│   │   └── users
│   │       ├── __init__.py
│   │       ├── alive.py
│   │       └── start.py
│   │      
│   └── version.py         
└── start                             ( A start file containing bash script to start the bot using bash start)

```    

