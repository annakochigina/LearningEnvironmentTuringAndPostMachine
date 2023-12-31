import os

CONST_BRIEF_REFERENCE_TURING = """      Машина Тьюринга - это универсальный исполнитель (абстрактная
вычислительная машина), предложенный английским математиком
Аланом Тьюрингом в 1936 году как уточнения понятия алгоритма.

        Абстрактность алгоритма заключается в том, что он представляет собой
логическую вычислительную конструкцию, а не реальную вычислительную 
машину.

        Термин «универсальный исполнитель» говорит о том, что данный
исполнитель может имитировать любой другой исполнитель. Согласно тезису
Тьюринга, любой алгоритм может быть записан в виде программы
для машины Тьюринга."""

CONST_BRIEF_REFERENCE_TURING_TWO = """      
        В последствие, придуманная Тьюрингом вычислительная конструкция
была названа машиной Тьюринга. Кроме того, предполагается, что
универсальный исполнитель должен уметь доказывать существование
или отсутствие алгоритма для той или иной задачи."""

CONST_DESCRIPTION_ALGORITHM_TURING_ONE = """        Машина Тьюринга состоит из бесконечной в обе стороны ленты, разделенной на ячейки, и каретки (головки),
которая управляется программой. Выражение состоит из набора символов, который называют алфавитом."""

CONST_DESCRIPTION_ALGORITHM_TURING_TWO = """        Программы для машины Тьюринга записываются в виде таблицы, где первые столбец и строка содержат
символы алфавита и возможные внутренние состояния каретки. 

        Содержимое таблицы представляет собой команды для машины Тьюринга.
Символ, над которым находится каретка в данный момент, и внутренне состояние головки определяют,
какую команду нужно выполнить.
"""

CONST_BRIEF_REFERENCE_POST = """        Машина Поста – это абстрактная вычислительная машина,
созданная для уточнения понятия алгоритма.
Представляет собой универсальный исполнитель, позволяющий
вводить начальные данные и читать результат выполнения программы.

        Она была создана независимо от машины Тьюринга, но сообщение
о машине Поста опубликовано на несколько месяцев позднее.
Отличается от машины Тьюринга большей простотой, притом обе машины
алгоритмически «эквивалентны» и обе разработаны для формализации
понятия алгоритма и решения задач об алгоритмической разрешимости.
"""

CONST_BRIEF_REFERENCE_POST_TWO = """
        В 1936 г. американский математик Эмиль Пост
в статье описал систему, обладающую алгоритмической простотой
и способную определять, является ли та или иная задача
алгоритмически разрешимой. Если задача имеет алгоритмическое
решение, то она представима в форме команд для машины Поста."""

CONST_DESCRIPTION_ALGORITHM_POST_ONE = """      Машина Поста состоит из ...
    1.	бесконечной ленты, поделенной на одинаковые ячейки. Ячейка может быть пустой (0 или пустота) или 
содержать метку (1 или любой другой знак).
    2.	каретки, способной передвигаться по ленте на одну ячейку в ту или иную сторону, а также
способной проверять наличие метки, стирать и записывать метку.
    Текущее состояние машины Поста описывается состоянием ленты и положением каретки.
    Состояние ленты – информация о том, какие секции пусты, а какие отмечены. 
    Шаг – это движение каретки на одну ячейку влево или вправо.
"""

CONST_DESCRIPTION_ALGORITHM_POST_TWO = """      Кареткой управляет программа, состоящая из строк команд.
Каждая команда имеет следующий синтаксис: i,K,j, где i - номер команды, K – действие каретки (команда),
j - номер следующей команды
Всего для машины Поста существует шесть типов команд:
    •	поставить метку
    •	стереть метку
    •	сдвинуться влево
    •	сдвинуться вправо
    •	если в ячейке нет метки, то перейти к j1-й строке программы,
иначе перейти к j2-й строке программы.
    •	конец программы (стоп).
"""

CONST_CONTROL_START = """Контроль представляет собой 5 заданий разного уровня сложности.
За правильный ответ на задания №1,2,3,4 вам начисляется 1 балл,
за задание №5 - 2 балла.
После прохождения теста вы сможете узнать,
какое количество баллов вы набрали"""

CONST_TRAINER_TUR = """     В верхней части программы находится  поле, в которое можно ввести
условие задачи.

    Бесконечная лента перемещается влево и вправо с помощью кнопок,
расположенных слева и справа от нее. Каждая ячейка представляет собой меню,
состоящее из символов алфавита. Нажатием левой кнопки мыши можно выбрать символ.

    В поле "Алфавит" задаются символы алфавита. Пустой символ добавлять не нужно.
Он добавится автоматически.

    В таблице в нижней части окна набирается программа. В первом столбце
записаны символы алфавита. В первой строке перечисляются все возможные состояния. 
Добавить и удалить столбцы таблицы
(состояния) можно с помощью соответствующих кнопок, расположенных над таблицей.
    При вводе команды в ячейку таблицы сначала нужно ввести символ 
(на который следует заменять), затем направление перехода и номер состояния.
Если символ пропущен, по умолчанию, он не изменяется.
    Во время выполнения алгоритма справа в поле "Комментарии" появляются
объяснения к текущему правилу.
    Программа может выполняться непрерывно или по шагам. Команда, которая
будет выполняться, подсвечивается зеленым фоно м.

    С помощью меню "Лента" можно запомнить состояние ленты и восстановить её.
Если вы не сохраняете ленту, то по умолчанию она восстанавливается пустой.
    Лабораторная работа подразумевает выполнение 5 заданий на написание программы.
К каждому заданию есть тесты, на которых можно проверить правильность кода. Все
задания генерируются.
    В меню "Файл" вы можете создать новый, открыть файл или сохранить.
Сохраняется условие задачи, алфавит, таблица и начальное состояние ленты."""

CONST_TRAINER_POST = """    В верхней части программы находится поле текста, в которое можно ввести
условие задачи в свободной форме.

    Бесконечная лента перемещается влево и вправо с помощью кнопок,
расположенных слева и справа от нее.  Каждая ячейка представляет собой меню,
состоящее из символов алфавита. Нажатием левой кнопки мыши можно открыть меню.

     В меню "Алфавит" есть два алфавита. Двузначный алфавит представляет собой
набор из двух элементов: галочка и пустота. Трехзначный алфавит состоит из
0, 1 и пустоый символ. Вы можете сменить алфавит в верхнем меню в соотвутствующем поле.

    В таблице в нижней части окна набирается программа. В первом столбце записаны
номера строк, он заполняется автоматически. Во втором столбце из списка выбирается
нужная команда, а в третьем вводится номер строки для перехода (если это необходимо).
Четвертый столбец может содержать комментарий к каждой строчке программы.
    Добавить и удалить строки таблицы можно с помощью кнопок, расположенных
слева от таблицы.
    
    Лабораторная работа подразумевает выполнение 5 заданий на написание программы.
К каждому заданию есть тесты, на которых можно проверить правильность кода. Все
задания генерируются.

    Программа может выполняться непрерывно или по шагам. Команда, которая сейчас
будет выполняться, подсвечивается зеленым фоном.

    С помощью меню "Лента" можно запомнить состояние ленты и восстановить её.
Если вы не сохраняете ленту, то по умолчанию она восстанавливается пустой. 
    В меню "Файл" вы можете создать новый, открыть файл или сохранить.
Сохраняется условие задачи, алфавит, таблица и начальное состояние ленты."""

CONST_LEARN_TURING = """ В данном разделе вы можете отработать, полученные
теоретические знания.
    Перед тем, как приступить к обучению, рекомендуется ознакомиться с 
теорией, которая представлена в разделе "Алгоритм" """

CONST_LEARN_FIRST_TASK_TURING = """Ответьте на вопросы, согласно представленному правилу"""

CONST_LEARN_SECOND_TASK_TURING = """Запишите правило в ячейку, согласно описанию:"""