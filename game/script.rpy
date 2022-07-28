﻿define she = Character("Вона", image="she")
define me = Character("Я", image="me")

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
image she dress neutral = "lady/neutral.png"

image she robe crying = "lady/crying 2.png"
image she robe disappointed = "lady/disappointed 2.png"
image she robe sad = "lady/sad 2.png"
image she robe smiling = "lady/smiling 2.png"
image she robe surprised = "lady/surprised 2.png"
image she robe neutral = "lady/neutral 2.png"

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
    "Замок впізнав ключ-карту і радісно пропищав.\nДвері в номер відкрилися"
    play sound door
    "Номер був в суцільній темряві, Тож вона ще досі на вечірці.\nЯ звичним рухом, наосліп, намацав вимикач."
    scene bg room
    with fade

    "Люкс був в ідеальному стані, вочевидь покоївка поприбира в номері, поки хозяйки не було."
    
    me neutral "Час прийняти душ!"
    scene bg black
    with fade
    play sound shower
    "Вона дуже любить чистоту, це я швидко зрозумів."
    scene bg room
    with fade

    menu:
        "Я був в чудовому настрої, тому що:"
        "Чоловічий ескорт то моє хоббі":
            $ isHobby = True
            "Хоч вона і мій клієнт, вона просто чудова людина, з якою приємно і поспілкуватися!"
            "А не тільки мати справи."
        "Чоловічий ескорт то добрий заробіток":
            $ isHobby = False
            "Робота є робота.\nКлієнти бувають різні, далеко не завжди приємні."
            "Але вона чудовий клієнт!\nІ гроші зароблю і задоволення отримаю."

    "Застібаючи свіжу сорочку я відсунув скляні двері на балкон."
    play sound sliding_door
    scene bg balcony
    with fade
    "Зорі на небі, приглушені ліхтарями міста, ледь мерехтіли."
    "Я глянув вниз, на вулицях майже нікого не було, адже курортний сезон вже закінчився."
    me neutral "Огорожа за низька для мого комфорту!"
    "Пропищав замок і відкрилися вхідні двері."
    me smiling "А ось і вона!"
    play sound door
    scene bg room
    with fade

    show she dress neutral
    with moveinleft

    me smiling "Добрий вечір!"
    she dress smiling "Капець, ледь втікла!"
    "Вона причепила табличку не турбувати на ручку і закрила двері."

    me neutral "Чудово. Як вечірка?"
    she dress sceptical "Світлана знову потягла мене до того бару!"
    me smiling "Сама винна що погодилась, ти ж її знаєш!"
    she dress neutral "Та я не могла відмовити. В неї новий кавалер, розумієш вона хотіла щоб я допомогла справити на нього враження."
    me "Яким чином??"
    she "Цитую: Ти солідна дама що вселяэ довіру."
    me "Правду каже!"
    show she dress smiling
    "Вона позбулася сумочки."
    me "Зачекай. А де твій ноут? Загубила?"
    she dress sceptical "Я нічого не гублю. Я залишила ноут в коворкінгу, нащо він мені на вечірці?"


    me "Добре!"
    me "Ну розповідай, чи вдалося справити враження на кавалера?"
    she dress neutral "О так, то твої послуги їй найближчим часом не знадобляться!"
    if isHobby:
        me smiling "Ну то й нехай. Головне щоб людина була хороша."
        she dress sceptical "Ось це якраз не факт."
    else:
        me neutral "Шкода, втрачаю клієнтів!"
        she dress neutral "Гадаю незабаром вона знову до тебе повернеться!"
    me neutral "Чому?"
    she dress neutral "Він геймер, постійно у віар зависає. Капець, весь час про ігри розказував!"
    me "Її завжди тягнуло на пригоди."
    she "Це точно. В них навіть було побачення в віарі!"
    menu:
        "Я вважаю що:"
        "Це їхні проблеми. Якщо вони нікому не заважають, нехай собі що хочуть те і роблять":
            $ itsOkToEscapeFromReality = True
            me smiling "Ха ха. Треба з цією темою познайомитися по ближче."
            me "Може мені не треба буди нікуди їздити?"
            she dress sceptical "Сподіваюсь ти жартуєш."
            me neutral "Так, я жартую!"
            she "Мені ніяково стає поруч з людьми що сидять у віарі.\nНачебто вони якісь навіжені."
            me "Однак, якщо вони нікому не заважають, нехай собі що хочуть то і роблять. Чи не так?"
            she dress sad "Напевно ти правий..."
        "Йому потрібна допомога. Він хворий, навіть якщо сам цього не усвідомлює":
            $ itsOkToEscapeFromReality = False
            me neutral "Світлана як завжди. Знайшла чегову жертву яка потребує допомоги!" 
            me "Хоч би не довелося потім її саму рятувати."
            she dress sceptical "Капець ти перебільшуєш, то лише ігри."
            me  neutral "У всьому потрібна міра.\nБігти від реальності немає сенсу. Вона тебе наздожене.\nІ у віарі також."
            me "Інколи люди цього не розуміють, вони як діти, і потребують допомоги."
            me "Інколи вони навіть чинять спротив - наприклад наркомани. Але їх все одно треба рятувати."
            she dress sad "Напевно ти правий..."
    "Вона зітхає."

    "Треба змінити тему!"
    if isHobby:
        me neutral "До речі, я збираюсь поїхати до космодрому Куру, подивитися на запуск Аріан 5!"
        she dress neutral "Нічого собі! Коли це буде?\nЯк же ж я без твоїх послуг!"
        me "Та це ще не скоро."
    else:
        me neutral "Ти коли небудь була в Діснейленді? Я завжди мріяв туди потрапити."
        she dress neutral "Ні, не була. Та й мені не дуже цікаво."
    me neutral "А є таке місце куди би ти хотіла поїхати?"

    play music sad fadeout 2.0 fadein 2.0
    she """
    Ні. Та й подорожувати я не люблю. Це завжди якісь проблеми.

    Хоча, було якось ми з чоловіком поїхали на концерт відомого піаніста... Як його...

    Пітер Бенс, начебто.\nМи прилетіли - а концерт, просто за годину до початку, відмінили!
    
    Уявляєшь?
    """
    me "Невдача!"
    she dress smiling """
    Однак то була найкраща подорож в моєму житті.

    Ми цілий день тинялися містом.

    Ходили по кафешках. Потрапили під дощ! 

    Ходили в кіно. 
    """

    "Отакої. Вона вочевидь кохає свого чоловіка!"
    if isHobby:
        "Треба допомогти їм налагодити відносини!"
    else:
        "Якщо вони помиряться я залишусь без клієнта!"
        
    me "То що трапилось?\nЧому він не приїхав з тобою сюди?"
    she "Він помер."
    "..."
    me serious "Вибач."
    she dress smiling "О, ні не треба вибачатися!\nЯ не хочу сумувати!"
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
    "Раніше я думав що її чоловік то якийсь старий мішок грошей,\nа вона разважається за його рахунок."
    "Я відкрив вино"
    play sound [bottle, pour]
    "А незабаром я дізнався що вона директор компанії і сама дуже гарно заробляє."
    "А тепер виявляється що її чоловік помер."
    "Це якось дивно. В її оточенні має бути чимало чоловіків яки залюбки з нею зустрічались би."
    "Чому вона сидить тут?"
    play sound sliding_door
    show she robe neutral
    with moveinleft
    she "Я обожнюю душ!"
    "Я подав її вина, а сам сів на диван."
    "Вона слідом примостилася до мене на дивані."
    me neutral "То коли твоє відрядження закінчується?"
    she robe smiling "О такої, ти боїшся втратити клієнта? Не хвилюйся!"
    me serious "В тебе ж є квітки на зворотній рейс?"
    she robe neutral "Так звісно..."
    me "То яка там дата?"
    she "Вони вже прострочені... Я якраз збиралась подзвонити і розібратися з квитками."
    "Вона втікла!"
    me "А твої родичи взагалі знають де ти?"
    she robe sad "В мене немає близьких родичів."
    me "Коли ти в останній раз була дома?"
    "Вона роздратованно встала з дивану."
    she "Чи не забагато питань? Хіба я тобі за це плачу?"

    hide she
    with moveoutright
    "Вона вийшла на балкон"
    play sound sliding_door
    if isHobby:
        "Чорт. Я перегнув палку!"
    else:
        "Нащо я це зробив? Це дійсно не моя справа!"

    "Раптово задзеленчав її телефон."
    play sound message
    "Телефон був старий, навіть без сенсорного єкрану."
    "Ну що ж. Я взяв телефон і пішов з ним на балкон."
    play sound sliding_door
    scene bg balcony
    with fade
    show she robe neutral
    me "Вибач."
    "Я віддав їй телефон."
    she "Пробачений."
    "Вона мовчки переглянула повідомлення на телефоні."
    me "Чому ти не придбаєш новий?"
    "Вона поклала телефон на долонь і болісно посміхнулась."
    she robe sad """
    Це його подарунок.
    
    Так, я втікла. Ти правильно все зрозумів.
    
    Але я ... не можу повернутися.

    Ти просто не уявляєш собі... Як добре мені з ним було...

    То були найкращі часи мого життя...
    """
    play music tragic fadeout 2.0 fadein 2.0
    she robe crying """
    Ми збиралися завести дитину...

    Якби була дівчинка - він хотів щоб її звали Анастасія...

    А якби був хлопчик...

    Я хотіла назвати його Віталій...

    Так само як і чоловіка...

    Моє майбутнє більше не існує!
    """
    "Вона підішла до краю балкона"
    she "Можна покінчити з цим тут і зараз..."

    menu:
        "Вона перехилилася через огорожу."
        "Відтягнути її від огорожі.":
            "Я схопив її ззаду і витягнув її від огорожі."
            if itsOkToEscapeFromReality:
                she "Пробач. Я тебе налякала?"
                if isHobby:
                    me disturbed "Дуже."
                else:
                    me disturbed "Мертві клієнти то погано для бізнесу."
                she robe smiling "Залишишся зі мною до ранку? Будь ласка?"
                me "Ще б пак. Тебе зараз небезпечно залишати одну."
                show she robe smiling
                pause 0.5
                jump bluePill
            else:
                stop music fadeout 2.0
                she robe disappointed "Тиж казав що бігати від реальності не має сенсу!"
                she "Хоча, що я кажу. Вибач, то був жарт. На сьогодні досить."
                jump fail
        "Краще випити снодійного.":
            me "Краще випити снодійного. Хтось може бути внизу і постраждати ні за що."
            if itsOkToEscapeFromReality:
                stop music fadeout 2.0
                she robe disappointed "Отакої, тиж казав що якщо я нікому не заважаю,\nто можу бігати від реальності скільки мені заманеться!"
                she "Хоча, що я кажу. Вибач, то був невдалий жарт. На сьогодні досить."
                jump fail
            else:
                she robe sad "Прослідкуєш щоб мене поховали поряд з чоловіком?"
                "Вона подивилась мені в очі.\nВона не жартувала."
                if isHobby:
                    me "Звичайно."
                else:
                    me "Так. Але спочатку напиши записку, щоб мене не посадили."
                she "Потримаэш мене заруку? Поки я буду засинати?"
                me "Звістно."
                show she robe smiling
                pause 0.5
                jump redPill

    jump titleDrop

label fail:
    scene bg black
    with fade
    "З тобою вона більше не зв'язувалася." 
    jump titleDrop

label redPill:
    scene bg black
    with fade
    "З ранку ти викликав поліцю і швидку."
    "Парамедики зафіксували факт смерті."
    "Поліції ти сказав що нічого не знав про її чоловіка, ви лише недавно познайомилися, а вранці ти знайшов її записку."
    "Родичив з її боку тобі розшукати не вдалося. Родичі зі сторони чоловіка не хотіли про неї нічого чути, та навіть чинили опір її похованню поряд з ним."
    "Але тобі вдалося виконати її останнє прохання."
    jump titleDrop
    

label bluePill:
    scene bg black
    with fade
    "Вона й далі продовжувала користуватися твоїми послугами."
    "Врешті решт вона продала свою частку в компаніі і компанії за кордон."
    jump titleDrop


label titleDrop:
    stop music fadeout 2.0
    "Відносини то складно. А потім ми вмираємо."
    return


