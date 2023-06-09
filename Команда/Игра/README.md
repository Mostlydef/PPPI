# Описание проекта

Игра – 2D платформер с открытым миром, песочница с элементами выживания со следующим функционалом:

- Модуль "Главное меню":
  - создание персонажа;
  - создание нового мира;
  - изменение настроек:
    - языка;
    - графики;
    - звука;
    - управления;
    - курсора;
  - выбор персонажа;
  - выбор мира.
- Модуль "Игра":
  - в игре присутствует система достижений;
  - игровой мир состоит из блоков;
    - блоки имеют различную прочность;
  - в игре предусмотрена смена дня и ночи;
  - игрок управляет персонажем:
      - у персонажа есть показатели здоровья, маны, защиты;
      - при получении урона игрок становится неуязвим на короткое время;
      - передвижение происходит при помощи нажатия клавиш A, D, Space(по умолчанию);
  - у персонажа есть инвентарь:
    - в инвентарь можно класть предметы;
    - из инвентаря можно доставать предметы;
  - можно выбрать один из предметов инвентаря для взаимодействия:
    - если это инструмент, то им можно ломать блоки;
      - существует 4 вида инструментов(кирка, лопата, топор, универсальный);
      - некоторые блоки эффективнее добываются определённым инструментом;
    - если это блок, то его можно поставить;
    - если это оружие, то им можно наносить урон;
      - основные показатели оружия: скорость атаки, урон, шанс крита, множитель критической атаки;
      - существует 4 вида оружия:
        - оружие ближнего боя. Наносит урон в ближнем бою;
        - оружие дальнего боя. Наносит урон в дальнем бою. Требует боеприпасы;
        - магическое оружие. Наносит урон магией, требует ману;
        - оружие призывателя. Призывает существо, которое будет сражаться на стороне призывателя;
  - игрок может использовать броню:
    - броня повышает защиту;
    - для брони предусмотрены специальные слоты в инвентаре;
  - игрок может использовать аксессуары:
    - аксессуары повышают различные характеристики(здоровье, урон, ...);
    - для аксессуаров предусмотрены специальные слоты в инвентаре;
  - игрок может взаимодействовать с NPC:
    - ночью с NPC взаимодействовать нельзя;
  - в мире появляются различные существа:
    - существуют как враждебные, так и дружественные существа;
    - враждебные существа чаще появляются ночью;
    - как и игрок, существа обладают механикой неуязвимости при получении урона;
    - в случае смерти, из существ выпадают специальные вещи;
  - в игре присутствует система крафта:
    - у некоторых предметов есть тег "Материал", позволяющий узнать, в каких рецептах он участвует.

# Шаги разработки игры

- Идея и концептуальное планирование: определение целей, идеи, жанра, аудитории и визуального стиля игры;
- Разработка механик игры;
- Создание дизайна игры: разработка геймплея, уровней, графики и звука;
- Проектирование программных модулей игры;
- Реализация программных модулей;
- Тестирование игры;
- Релиз игры;
- Поддержка и обновление игры.