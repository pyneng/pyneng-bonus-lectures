## Ссылки

* [libtmux](https://github.com/tmux-python/libtmux)
* [How to start tmux with several panes open at the same time?](https://askubuntu.com/a/832465)
* [tmux cheat sheet](https://gist.github.com/andreyvit/2921703)
* [Update your tmux to latest version](http://witkowskibartosz.com/blog/update-your-tmux-to-latest-version.html)


## отправка команд на обрудование с управляющей консоли через tmux 

Переделать мой вариант со screen на tmux.


```
$ tmux -2 -f tmux_session_basics.conf attach
```

# [Терминология](https://github.com/tmux/tmux/wiki/Getting-Started#summary-of-terms)

* Сессия (session)
* Окно (window)
* Панель (pane)
* Схема окна (window layout)


![alt text](https://raw.githubusercontent.com/wiki/tmux/tmux/images/tmux_pane_diagram.png)

## cheat sheet

### sessions

```
$ tmux new -s mysession
```

Отключиться от сессии: `prefix d`.

Подключиться к сессии:
```
$ tmux attach -t mysession
```

Список сессий:
```
$ tmux ls
```

### windows

Создать окно `prefix c`.

Создать новое окно и выполнить в окне top:
```
:neww top
```

Передвижение между окнами:

* `prefix 0`
* `prefix '` - запрашивает индекс окна
* `prefix n` - следующее окно по индексу
* `prefix p` - предыдущее окно по индексу
* `prefix l` - вернуться на предыдущее открытое окно

### Разделение окна на панели

* Разделить горизонтально `prefix %`
* Разделить вертикально `prefix "`

Или использовать команду `split-window`

Передвижение между панелями:

* `prefix стрелки`
* `prefix q` - показать номер панели
* `prefix q 2` - переключиться на панель 2


Разделить окно вертикально на все окно
```
:split-window -h -f
```

### tree mode

* `prefix s` - сессии
* `prefix w` - окна
* Стрелка вправо разворачивает меню 
* `q` выход из режима
* `x` - закрыть выбранный элемент
* `X` - закрыть отмеченные элементы
* `t` - отметить элемент
* `T` - удалить отметки

### Предопределенные схемы окна

* `prefix space` - toggl layout
* `prefix Alt 1-5` - выбрать конкретный

Схемы:

1. even-horizontal
2. even-vertical
3. main-horizontal
4. main-vertical
5. tiled
