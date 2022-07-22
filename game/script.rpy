define she = Character("Вона")
define me = Character("Я")

define audio.romantic = audio.mixkit_a_love_affair_1050
define audio.sad = audio.pixabay_lofi_study_112191
define audio.tragic = audio.mixkit_silent_descent_614

define audio.door = audio.pixabay_dorm_door_opening_6038
define audio.sliding_door = audio.mixkit_lightweight_sliding_door_close_182
define audio.shower = audio.pixabay_shower_14461
define audio.bottle = audio.pixabay_bottle_open_14895
define audio.pour = audio.pixabay_pouring_coffee_6743
define audio.message = audio.mixkit_page_forward_single_chime_1107

image bg black = "#000"
image bg room = "room_evening_light_on.jpg"

image she = im.FactorScale("idle.png", 0.7)
image she sad = im.FactorScale("sad.png", 0.7)
image she sceptical = im.FactorScale("idle.png", 0.7)
image she smiling = im.FactorScale("idle.png", 0.7)
image she surprised = im.FactorScale("idle.png", 0.7)
image she dissapointed = im.FactorScale("sad.png", 0.7)
image she crying = im.FactorScale("sad.png", 0.7)

default itsOkToEscape = False
label start:

    scene bg black
    with fade
    play music romantic
    "Замок впізнав ключ-карту і радісно пропищав. Двері в номер відкрилися"
    play sound door
    "Номер був в суцільній темряві. Я намацав вимикач."
    scene bg room
    with fade
    show me
    "Швиденько оглянув номер - чи все прибрано і охайно, поки є ще час щоб покликати покоївку."
    "Люкс був в ідеальному стані"
    "Час прийняти душ. Я добре знаю що вона це любить. Вона постійний клієнт."
    play sound shower
    scene bg room
    with fade
    show me

    "Застібаючи свіжу сорочку я відсунув скляні двері на балкон."
    play sound sliding_door
    scene bg balcony
    with fade
    show me
    "Зорі на небі, приглушені ліхтарями міста, ледь мерегтіли."
    "Огорожа за низька для мого комфорту, особливо якщо врахувати що це дев'ятий поверх!"
    "Пропищав замок і відкрилися вхідні двері."
    play sound door
    scene bg room
    with fade
    show she at left
    show me at right

    me "Добрий вечір!"
    she "Добрий, добрий"
    "Вона причепила табличку не турбувати на ручку і закрила двері"
    "Вона одягнена в сукню, прикраси і з макіяжем - вона з вечірки"
    she "Як справи?"
    me "Чудово. Як вечірка?"
    she "Світлана передавала привіт."
    me "Давно з нею не зустрічався, сподіваюся в неї все добре?"
    she "О так, вона була на вечірці з новим бойфрендом, то твої послуги їй найближчим часом не знадобляться!"
    me "Та невже"
    she "Геймер, постійно у віар зависає."
    me "Її завжди тянуло на пригоди."
    she "Це точно. Вона розповіла що в них навіть було побачення в віарі!"
    menu:
        "Я вважаю що:"
        "Це їхні проблеми. Якщо вони нікому не заважають, нехай собі що хочуть то і роблять":
            $ itsOkToEscape = True
            show me laughin
            me "Ха ха. Треба з цією темою познайомитися по ближче."
            me "Може мені не треба буди нікуди їздити?"
            show she sceptical
            she "Мені ніяково стає поруч з людьми що сидяь у віарі. Що вони роблять і що від них чекати не зрозуміло, начебто вони якісь навіжені."
            me "Якщо вони нікому не заважають, нехай собі що хочуть то і роблять"
            show she sad
            she "Напевно ти правий..."
        "Йому потрібна допомога. Він хворий, навіть якщо сам цьго не усвідомлює":
            $ itsOkToEscape = False
            show me sceptical
            me "Світлана як завжди. Знайшла чегову жертву яка потребує допомоги!" 
            me "Хоч би не довелося потім її саму рятувати."
            show she sceptical
            she "Ти перебільшуєш, то лише ігри."
            me "Бігти від реальності не має сенсу. Вона тебе наздожене. Навіть у віарі."
            me "Люди які цьго не розуміють, вони як діти, і потребують допомоги."
            show she sad
            she "Напевно ти правий..."
    play music sad fadeout 2.0 fadein 2.0
    "Вона зітхає."
    she "Є вино?"
    play sound [bottle, pour]
    me "Що тебе гризе?"
    she """
    Робота задовбала. Раніше... Раніше я любила свою роботу.

    В нас був малий коллектив. Ми працювали зарди ідеї, не зважаючи чи принесе ця ідея гроші чи ні.

    А тепер я лише сиджу на мітингах і папірці перекладаю... Спочатку успіх приніс нам гроші. 

    Не встигла і блимнути - все стало обертатися лише навколо них.
        
    Ти напевно не знаєшь, але в мене був чоловік ми разом створили цю команію. Але він загинув.
    """
    me "Він був, напевно дуже гарною людиною"
    show she smiling
    she "О так! Він був найкращім!"
    she "Звідки ти знаєшь?"
    me "Бо я тепер розумію чтому ти відмовляєшь усім чоловікам! Вони не дотягують до його рівня!"
    show she sceptical
    she "Не знаю. Я вже не дівчинка. Відносини то складно, на це потрібно багато часу... Я не бачу чоловіків на яких його варто витрачати."
    me "Ну на мене ти витрачаєшь не тільки час, та ще й гроші!"
    she "То я навпаки бережу свій час."

    "Вона ініціює секс"
    scene bg black
    with fade
    scene bg room
    with fade
    show me at right
    play sound shower
    "Вона повертаэться з душу"
    show she at left
    with moveinleft

    "Ви сидите в обіймах на дивані"
    me "Можна задати особисте питання?"
    show she surprised
    she "Ти якийсь дивний. Ну питай"
    me "Нащо я тобі?"
    she "Ти часом не захворів? З такими питанями ти багато грошей не заробиш!"
    me """До біса гроші. На зовні ти завжди веслеа, впевнена і вправна. Все можеш. Алеж я знаю що ти насправді нещасна.
        І я лише тимчасова розвага. """
    show she sad
    she "До чого ти ведеш"
    me "Я не зможу замінити твого чоловіка"
    me "Твоя справа буди зручним"
    hide she
    "Вона вийшла на балкон"
    play sound sliding_door
    "Раптово задзеленчав її телефон"
    play sound message
    "Я взяв його і пішов з ним на балкон"
    play sound sliding_door
    scene bg balcony
    with fade
    show me at right
    show she at left
    "Телефон був старий, навіть без сенсорногу єкрану"
    me "Вибач"
    "Я віддав їй телефон."
    she "Пробачений."
    "Вона мовчки переглянула повідомлення на телефоні"
    me "Чому ти не придбаєшь новий?"
    "Вона поклала телефон на долонь і болісно посміхнулась."
    show she sad
    she """
    Цей телефон його подарунок.

    На ньму багато фото і відео де ми разом...

    Треба їх скачати, десь має бути кабель...

    В його кімнаті...
    """
    show she crying

    she "Бо зазвичай він цим займався..."

    "Ти її обійняв"

    show she sad
    play music tragic fadeout 2.0 fadein 2.0
    "Правду ти казав... Я біжу від реальності..."
    "Вона підішла до краю балкона"
    she "Можна покінчити з цим тут і зараз..."
    "Вона перехилилася через огорожу"
    "Схопивши її сзаду ти відягнув її від огорожі. Вона не чинила опіру."

    menu:
        "Ти кажеш:"
        "Я не хочу сісти в тюрму, це не входить в мій бізнес план":
            me "Я не хочу сісти в тюрму, це не входить в мій бізнес план"
            if itsOkToEscape:
                she "Будь ласка. Дозволь мені це зробити."
                "Ти її відпускаєш."
                show she smiling
                jump free
            else:
                show she dissapointed
                stop music fadeout 2.0
                she "Тиж казав що бігати від реальності не має сенсу!"
                she "Хоча, що я кажу. Вибач, то був жарт. На сьгодні досить."
                jump fail
        "Не треба здаватися!":
            me "Так, що ти таке кажешь! Я не дозволю тобі це зробити!"
            if itsOkToEscape:
                show she dissapointed
                stop music fadeout 2.0
                she "Тиж казав що кожна людина має право жити я хоче?"
                she "Хоча, що я кажу. Вибач, то був жарт. На сьгодні досить."
                jump fail
            else:
                show she smiling
                she "Дякую... Будьласка залишься зі мною до ранку"
                me "Звичайно"
                jump sleep

    return

label fail:
    scene bg black
    with fade
    "З тобою вона більше не зв'язувалася." 
    "Через декілька років вона таки вчинила самогубство."
    return

label free:
    scene bg black
    with fade
    "Ти одразу викликав поліцю і швидку."
    "Вона померла."
    "Ти був підозрюванним у вбивстві, але зясувалося що вона ввімкнула запис на телефоні, і твоє алібі було підтверджено."
    return

label sleep:
    scene bg black
    with fade
    "Вона й далі продовжувала користуватися твоїми послугами."
    "Ви білше не поверталися до цієї теми."
    return
   


