define she = Character("Вона", image="she", who_color="#D15133")
define me = Character("Я", image="me", who_color="#1891C2")

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
image bg room = "rooms/bedroom 1.png"
image bg room after = "rooms/bedroom 2.png"
image bg balcony = "rooms/balcony.png"

image she dress sad = "lady/sad.png"
image she dress sceptical = "lady/sceptical.png"
image she dress smiling = "lady/smiling.png"
image she dress surprised = "lady/surprised.png"
image she dress neutral = "lady/neutral.png"

image she robe crying = "lady/crying 2.png"
image she robe disappointed = "lady/disappointed 2.png"
image she robe sad = "lady/sad 2.png"
image she robe smiling = "lady/smiling 2.png"
image she robe surprised = "lady/surprised 2.png"
image she robe neutral = "lady/neutral 2.png"
image she robe sceptical = "lady/sceptical 2.png"

image side me disturbed = "man/disturbed.png"
image side me neutral = "man/neutral.png"
image side me serious = "man/serious.png"
image side me smiling = "man/smiling.png"

default itsOkToEscapeFromReality = False
default isHobby = False

label start:

    scene bg black
    with fade
    play music romantic
    "Замок впізнав ключ-карту і радісно пропищав.\nДвері в номер відкрилися."
    play sound door
    "Номер був в суцільній темряві. Тож вона ще досі на вечірці."
    "Я звичним рухом, наосліп, намацав вимикач."
    scene bg room
    with fade

    "Люкс був в ідеальному стані, вочевидь покоївка прибирала в номері, поки хазяйки не було."

    me neutral "Час прийняти душ!"
    scene bg black
    with fade
    play sound shower
    "Вона дуже любить чистоту, це я швидко зрозумів."
    scene bg room
    with fade

    menu:
        "Я був в чудовому настрої, тому що:"
        "Чоловічий ескорт - то моє хоббі":
            $ isHobby = True
            "Хоч вона і мій клієнт, вона просто чудова людина, з якою приємно і поспілкуватися!"
            "А не тільки мати справи."
        "Чоловічий ескорт - то добрий заробіток":
            $ isHobby = False
            "Робота є робота.\nКлієнти бувають різні, далеко не завжди приємні."
            "Але вона чудовий клієнт!"
            "І гроші зароблю, і задоволення отримаю."

    "Застібаючи свіжу сорочку я відсунув скляні двері на балкон."
    play sound sliding_door
    scene bg balcony
    with fade
    "Зорі на небі, приглушені ліхтарями міста, ледь мерехтіли."
    "Я глянув вниз, на вулицях майже нікого не було, адже курортний сезон вже закінчився."
    me serious "Огорожа занизька для мого комфорту!"
    "Пропищав замок і відкрилися вхідні двері."
    me smiling "А ось і вона!"
    play sound door
    scene bg room
    with fade

    show she dress neutral
    with moveinleft

    me smiling "Добрий вечір!"
    she dress smiling "Капець, ледь втікла!"
    hide she dress neutral
    with moveoutleft
    show she dress neutral
    with moveinleft
    "Вона причепила табличку не турбувати на ручку і закрила двері."

    me neutral "Чудово. Як вечірка?"
    she dress sceptical "Світлана знову потягла мене до того бару!"
    me smiling "Сама винна, що погодилась. Ти ж її знаєш!"
    she dress neutral "Та я не могла відмовити."
    she dress smiling "В неї новий кавалер. Розумієш, вона хотіла, щоб я допомогла справити на нього враження."
    me "Яким чином??"
    she dress neutral "Цитую: \"ти - солідна дама, що вселяє довіру.\""
    me "Правду каже!"
    show she dress smiling
    "Вона позбулася сумочки."
    me neutral """
    Зачекай. 

    А де твій ноут? Загубила?
    """
    she dress sceptical "Я нічого не гублю."
    she dress neutral "Я залишила ноут у коворкінгу, нащо він мені на вечірці?"


    me smiling "Добре!"
    me neutral "Ну розповідай, чи вдалося їй справити враження на кавалера?"
    she dress smiling "О так, тому твої послуги їй найближчим часом не знадобляться!"
    if isHobby:
        show she dress surprised
        me smiling "Ну то й нехай. Головне, щоб людина була хороша."
        she dress sceptical "Ось це якраз не факт."
    else:
        me neutral "Шкода, втрачаю клієнтів!"
        she dress neutral "Гадаю незабаром вона знову до тебе повернеться!"
    me neutral "Чому?"
    she dress neutral "Він - геймер, постійно у віар зависає."
    she dress sceptical "Капець, весь час про ігри розказував!"
    me serious "Її завжди тягнуло на пригоди."
    she dress neutral "Це точно. В них навіть було побачення в віарі!"
    menu:
        "Я вважаю що:"
        "Це їхні проблеми.":
            $ itsOkToEscapeFromReality = True
            show she dress surprised
            me smiling "Ха ха. Треба з цією темою познайомитися ближче."
            me "Може мені не треба буде нікуди їздити?"
            she dress sceptical "Сподіваюсь ти жартуєш."
            show she dress neutral
            me smiling "Так, я жартую!"
            she dress sceptical """
            Мені ніяково стає поруч з людьми що сидять у віарі.
            
            Начебто вони якісь навіжені.
            """
            me "Але якщо вони нікому не заважають, нехай собі що хочуть то і роблять. Чи не так?"
            she dress sad "Напевно ти правий..."
        "Він хворий, навіть якщо сам цього не усвідомлює.":
            $ itsOkToEscapeFromReality = False
            me serious "Світлана як завжди. Знайшла чегову жертву яка потребує допомоги!"
            me "Хоч би не довелося потім її саму рятувати."
            she dress surprised "Капець, ти перебільшуєш, то лише ігри."
            me serious "Для всього є межа."
            me neutral """
            Бігти від реальності немає сенсу. 
            
            Вона тебе наздожене.
            
            І у віарі також.
            """
            me serious "Інколи люди цього не розуміють, вони як діти, і потребують допомоги."
            me neutral """
            Інколи вони навіть чинять спротив. Наприклад, наркомани. 
            
            Але їх все одно треба рятувати."""
            she dress sad "Напевно ти правий..."
    "Вона зітхає."

    "Треба змінити тему!"
    show she dress neutral
    if isHobby:
        me smiling "Чула про новий космічний телескоп?" 
        she dress surprised "Ні."
        me "Його мають запустити незабаром з космодрому Куру, я б дуже хотів подивитися на запуск!"
    else:
        me smiling """
        Ти коли небудь була в Діснейленді? 
        
        Я завжди мріяв туди потрапити."""
        she dress neutral """
        Ні, не була. 
        
        Та й мені не дуже цікаво.
        """
    me neutral "А є таке місце куди би ти хотіла поїхати?"
 
    play music sad fadeout 2.0 fadein 2.0
    she dress sad "Ні." 
    she dress neutral "Та й подорожувати я не люблю. Це завжди якісь проблеми."
    she dress smiling """
    Хоча, було якось ми з чоловіком поїхали на концерт відомого піаніста... Як його...

    Пітер Бенс, начебто.
    """
    she dress neutral """
    Ми прилетіли - а концерт, просто за годину до початку, відмінили!
   
    Уявляєш?
    """
    me neutral "Невдача!"
    she dress smiling """
    Однак то була найкраща подорож в моєму житті.
 
    Ми цілий день тинялися містом.

    Ходили по кафешках. Потрапили під дощ!

    Сходили в кіно.
    """

    show she dress neutral
    "Отакої. Вона вочевидь кохає свого чоловіка!"
    if isHobby:
        "Треба допомогти їм налагодити відносини!"
    else:
        "Якщо вони помиряться, я залишусь без клієнта!"

    me neutral """
    А чого це він відпускає таку гарну жінку у таке довге відрядження саму?
    
    Чи ви посварилися?
    """
    she dress sad "..."
    she "Він помер."
    me disturbed "..."
    me serious "Вибач."
    she dress neutral "О ні, не треба вибачатися!"
    she dress smiling "Я не хочу сумувати!"
    "Вона припала до мене всім тілом і поцілувала."
    "Я відчув ледь помітний присмак алкоголю."
    "Ми цілувалися в обіймах, i через тонку сукню я відчув, що вона десь вже зняла білизну."
    me smiling "Ти що цілий день ходила коммандо?"
    she dress smiling "Так, я капець як чекала на нашу зустріч!"

    scene bg black
    with fade
    "Після сексу вона пішла в душ."
    play sound shower
    scene bg room after
    with fade
    "Я тим часом одягнувся і поприбирав."
    "Тож її чоловік помер."
    "Не схоже щоб вона народжувала - цеб було помітно, тобто дітей у них немає."
    "Раніше я думав що її чоловік - то якийсь старий мішок грошей,\nа вона разважається за його рахунок."
    "Я відкрив вино."
    play sound [bottle, pour]
    "Потім зрозумів, що вона - директор компанії, тому і сама дуже гарно заробляє."
    "А тепер виявляється, що її чоловік помер."
    "Це якось дивно. В її оточенні має бути чимало чоловіків, які залюбки з нею зустрічались би."
    "Чому вона сидить тут?"
    play sound sliding_door
    show she robe neutral
    with moveinleft
    she "Обожнюю відчуття свіжості після душу!"
    "Я подав їй вино, а сам сів на диван."
    "Вона слідом примостилася до мене на дивані."
    me neutral "То коли твоє відрядження закінчується?"
    she robe surprised "Отакої, ти боїшся втратити клієнта?"
    she robe smiling "Не хвилюйся!"
    me serious "В тебе ж є квитки на зворотній рейс?"
    she robe sceptical "Так звісно..."
    me "То яка там дата?"
    she robe sad "Вони вже прострочені..."
    she robe disappointed "Я якраз збиралась подзвонити і розібратися з квитками."
    "Вона втікла!"
    me neutral "А твої родичі взагалі знають де ти?"
    she robe sad "В мене немає близьких родичів."
    me "Коли ти в останній раз була дома?"
    show she robe sceptical
    "Вона роздратованно встала з дивану."
    she """
    Чи не забагато питань? 

    Хіба я тобі за це плачу?"""

    hide she
    with moveoutright
    "Вона вийшла на балкон."
    play sound sliding_door
    if isHobby:
        "Чорт. Я перегнув палку!"
    else:
        "Нащо я це зробив? Це дійсно не моя справа!"

    "Раптово задзеленчав її телефон."
    play sound message
    "Телефон був старий, потертий, а вугол экрану був пошкодженний."
    "Ну що ж. Я взяв телефон і пішов з ним на балкон."
    play sound sliding_door
    scene bg balcony
    with fade
    show she robe disappointed
    me serious "Вибач."
    "Я віддав їй телефон."
    she robe sad "Пробачений."
    "Вона мовчки переглянула повідомлення на телефоні."
    show she robe disappointed
    me "Чому ти не придбаєш новий?"
    "Вона поклала телефон на долоню і болісно посміхнулась."
    she robe neutral "Це його подарунок."
    she robe sad """
    ...

    Так, я втікла. Ти правильно все зрозумів.

    Але я... не можу повернутися.

    Ти просто не уявляєш собі... Як добре мені з ним було...

    То були найкращі часи мого життя...
    """
    play music tragic fadeout 2.0 fadein 2.0
    she robe crying """
    Ми збиралися завести дитину...

    Якби була дівчинка - він хотів щоб її звали Анастасія...

    А якби був хлопчик...

    Я хотіла назвати його Віталій...
    """
    she robe sad "Так само як і чоловіка..."
    she robe crying "Моє майбутнє більше не існує!"
    "Вона підішла до краю балкона."
    she robe disappointed "Можна покінчити з цим тут і зараз..."
    "Я схопив її ззаду і відтягнув її від огорожі."
    if isHobby:
        me disturbed "Ти що робиш!?"
    else:
        me disturbed "Мертві клієнти - то погано для бізнесу!"

    menu:
        she "Тоді що мені робити!?"
        "Нічого, ти і так молодець.":
            me serious "Нічого. З часом біль мине."
            me "Це ок - нічого не робити."
            me "Ти нічого не мусиш."
            if itsOkToEscapeFromReality:
                she robe sad "Дякую..."
                she robe sad "Залишишся зі мною до ранку? Будь ласка?"
                me serious "Звісно. Тебе зараз небезпечно залишати одну."
                show she robe smiling
                pause 0.5
                jump bluePill
            else:
                stop music fadeout 2.0
                she robe disappointed "Тиж казав що бігати від реальності не має сенсу!"
                she robe sad "Хоча, що я кажу."
                she robe neutral """
                Вибач, то був жарт. 
                
                На сьогодні досить.
                """
                jump fail
        "Повертайся до дому.":
            show she robe sad
            me neutral "Досить бігати."
            me serious "Так, повернутися буде боляче."
            me "Але це треба зробити. Це як гіркі ліки - спочатку важко, а потім буде легше."
            if itsOkToEscapeFromReality:
                stop music fadeout 2.0
                she robe disappointed """
                Як так?
                Ти ж казав, що якщо я нікому не заважаю,\nто можу бігати від реальності скільки мені заманеться!
                """
                she robe sad "Хоча, що я кажу."
                she robe neutral """
                Вибач, то був жарт. 
                
                На сьогодні досить.
                """
                jump fail
            else:
                show she robe sad
                "Вона достала телефон."
                she "Є ранковий рейс..."
                me serious "Бери. Я залишусь з тобою до ранку, а потім посаджу на літак."
                she "Дякую."
                me smiling "До ранку ще далеко, та й вино теж ще э."
                show she robe smiling
                pause 0.5
                jump redPill

    jump titleDrop

label fail:
    scene bg black
    with fade
    "Зі мною вона більше не зв'язувалася."
    jump titleDrop

label redPill:
    scene bg black
    with fade
    "Зранку ми разом позбирали її речі, а потім я відвіз її в аеропорт."
    "Ми й надалі підтримували зв'язок, але вже просто як друзі."
    jump titleDrop


label bluePill:
    scene bg black
    with fade
    "Вона й далі продовжувала користуватися моїми послугами."
    "Врешті решт вона продала свою частку в компанії і поїхала за кордон."
    jump titleDrop


label titleDrop:
    stop music fadeout 2.0
    "..."
    "Відносини то складно. А потім ми вмираємо."
    return
