## Ссылки

* [libtmux](https://github.com/tmux-python/libtmux)
* [How to start tmux with several panes open at the same time?](https://askubuntu.com/a/832465)
* [Update your tmux to latest version](http://witkowskibartosz.com/blog/update-your-tmux-to-latest-version.html)
* [tmux cheat sheet](https://gist.github.com/andreyvit/2921703)
* [tmux shortcuts & cheatsheet](https://gist.github.com/MohamedAlaa/2961058)


## отправка команд на обрудование с управляющей консоли через tmux 

Переделать мой вариант со screen на tmux.


```
$ tmux -2 -f tmux_session_basics.conf attach
```

## [Терминология](https://github.com/tmux/tmux/wiki/Getting-Started#summary-of-terms)

* Сессия (session)
* Окно (window)
* Панель (pane)
* Схема окна (window layout)


![alt text](https://raw.githubusercontent.com/wiki/tmux/tmux/images/tmux_pane_diagram.png)


## sessions

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

## windows

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

## tree mode

* `prefix s` - сессии
* `prefix w` - окна
* Стрелка вправо разворачивает меню 
* `q` выход из режима
* `x` - закрыть выбранный элемент
* `X` - закрыть отмеченные элементы
* `t` - отметить элемент
* `T` - удалить отметки

## Панели (panes)

### Разделение окна на панели

* Разделить горизонтально `prefix %`
* Разделить вертикально `prefix "`

Или использовать команду `split-window`

Передвижение между панелями:

* `prefix стрелки`
* `prefix q` - показать номер панели
* `prefix q 2` - переключиться на панель 2

Работа с панелями:

* `prefix x` - закрыть текщую панель
* `prefix z` - развернуть панель на все окно, повторно вернуть раскладку
* `prefix }` - сдвинуть текщую панель вправо
* `prefix {` - сдвинуть текщую панель влево


Разделить окно вертикально на все окно
```
:split-window -h -f
```

### Предопределенные схемы окна

* `prefix space` - toggle layout
* `prefix Alt 1-5` - выбрать конкретный

Схемы:

1. even-horizontal
2. even-vertical
3. main-horizontal
4. main-vertical
5. tiled

### Изменение размера

`prefix Alt стрелки` - стрелки надо нажимать быстро

```
prefix : resize-pane -D (Resizes the current pane down)
prefix : resize-pane -U (Resizes the current pane upward)
prefix : resize-pane -L (Resizes the current pane left)
prefix : resize-pane -R (Resizes the current pane right)
prefix : resize-pane -D 20 (Resizes the current pane down by 20 cells)
prefix : resize-pane -U 20 (Resizes the current pane upward by 20 cells)
prefix : resize-pane -L 20 (Resizes the current pane left by 20 cells)
prefix : resize-pane -R 20 (Resizes the current pane right by 20 cells)
```

> Технически Meta, а не Alt

> [вариант настройки комбинации](https://superuser.com/a/863413)

### Синхронизация панелей

Синхронизация
```
:setw synchronize-panes
```

после этого набранная команда отправляется на все панели.


## Режим копирования

## Работа с мышкой


## Командный режим

Выход `Enter`.
