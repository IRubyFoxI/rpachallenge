<p align="center">
   <img src="https://i.ibb.co/9hXHPh7/2024-11-26-005055.png" alt="Сайт RpaChallange">
</p>

## Мой проект - 
Привет, меня зовут Егор. Данный проект сделан в целях вбивания Excel-данных на сайт [RpaChallenge](https://www.rpachallenge.com/).

Этот код, который сделан на PyCharm Community Edition 2023.3.5, написанный на Python. Там используется библиотеки, что будут указаны снизу

## Как работает?

Выполнение кода берёт драйвер microsoft Edge, обращается, и запускает чистый браузер, после чего забирает с Excel данные, находит строчки по X.Path и вводит на сайте данные с Excel-файла. Примерное выполнения кода ~0.785 миллисекунд  

## Использованные библиотеки:
Также в терминале Pycharm можно удобно установить через pip install библиотеки (советую, ибо это удобнее и практичнее). Вебдравер ставится отдельно с соотвествием версией Microsoft Edge
 
[Edge webdriver](https://developer.microsoft.com/ru-ru/microsoft-edge/tools/webdriver/?form=MA13LH)


[Selenium:](https://github.com/SeleniumHQ/selenium) 
````
pip install selenium
````
[Pandas:](https://github.com/pandas-dev/pandas) 
````
pip install pandas
````
Сразу обе библиотеки:
````
pip install selenium pandas 
````

## Установка   
1. Скачать все файлы
2. Установить все библиотеки 
3. Загрузить в PyCharm код
4. Запустить код
