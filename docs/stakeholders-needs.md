# rozklad_kpi_bot. Запити зацікавлених осіб

## <a name="l1">1. Вступ</a>

У цьому документі описуються запити зацікавлених осіб (стрейкголдерів) стосовно розробляємої в рамках лабораторних робіт системи доступу до розкладу через API [rozklad_kpi_remake](https://github.com/naz-olegovich/rozklad_kpi_remake).

### <a name="l11">1.1. Мета</a>

Метою документа є визначення основних вимог до функціональності системи.

### <a name="l12">1.2. Контекст</a>

Перелік вимог, перерахованих в цьому документі, є основою технічного завдання на розробку системи доступу до розкладу "rozklad_kpi_bot".


## <a name="l2">2. Короткий зміст</a>

Надалі розглянемо характеристику ділових процесів та FURPS.

## <a name="l3">3. Характеристика ділових процесів</a>


#### Категорії користувачів

В системі існує дві категорії користувачів: студент та викладач.
**Студент:** може доступатися до розкладу власної групи, пропонувати викладачу провести додаткову пару.
**Викладач:** може доступатися до власного розкладу, приймати або відхиляти пропозицію щодо додаткової пари.

### Студент

#### Сценарій №1

***ID:*** SDT.01
       
***НАЗВА:*** Дізнатися розклад

***УЧАСНИКИ:*** Студент

***ПЕРЕДУМОВИ:*** Розклад сформовано

***РЕЗУЛЬТАТ:*** Студент знає свій розклад

***ВИКЛЮЧНІ СИТУАЦІЇ:***
 - EХ.001.001: Розклад ще не сформовано 

***ОСНОВНИЙ СЦЕНАРІЙ:*** 
1. Студент дізнається свій розклад


#### Сценарій №2

***ID:*** SDT.02
       
***НАЗВА:*** Запропонувати викладачу провести додаткову пару

***УЧАСНИКИ:*** Студент, викладач

***ПЕРЕДУМОВИ:*** Студент хоче мати додаткову консультацію з викладачем

***РЕЗУЛЬТАТ:*** Викладач дізнався, що студентам потрібна консультація

***ОСНОВНИЙ СЦЕНАРІЙ:*** 
1. Студент створює запит на консультацію з викладачем.
2. Інші студенти підтримують цей запит.
3. Викладач бачить, що студентам потрібна консультація.


#### Сценарій №3

***ID:*** SDT.03
       
***НАЗВА:*** Підтримати запит на додаткову пару

***УЧАСНИКИ:*** Студент

***ПЕРЕДУМОВИ:*** Студент хоче мати додаткову консультацію з викладачем(запит вже створено)

***РЕЗУЛЬТАТ:*** Викладач дізнався, що студентам потрібна консультація

***ОСНОВНИЙ СЦЕНАРІЙ:*** 
1. Студент підтримує запит.
2. Викладач бачить збільшену кількість студентів, котрим потрібна консультація.


### Викладач

#### Сценарій №1

***ID:*** TCR.01
       
***НАЗВА:*** Дізнатися розклад

***УЧАСНИКИ:*** Викладач

***ПЕРЕДУМОВИ:*** Розклад сформовано

***РЕЗУЛЬТАТ:*** Викладач знає свій розклад

***ВИКЛЮЧНІ СИТУАЦІЇ:***
 - EХ.001.001: Розклад ще не сформовано 

***ОСНОВНИЙ СЦЕНАРІЙ:*** 
1. Викладач дізнається свій розклад


#### Сценарій №2

***ID:*** TCR.02
       
***НАЗВА:*** Прийняти запит на додаткову пару

***УЧАСНИКИ:*** Викладач, студент

***ПЕРЕДУМОВИ:*** Студент створив запит на додаткову пару

***РЕЗУЛЬТАТ:*** Викладач прийняв запит та назначив час проведення консультації

***ОСНОВНИЙ СЦЕНАРІЙ:*** 
1. Викладач бачить список предметів, з яких студенти хочуть провести додаткові пари.
2. Викладач обирає пару, яку, як він вважає, треба провести.
3. Викладач обирає час проведення додаткової пари
                       
## <a name="l4">4. Короткий огляд продукту</a>

**rozklad_kpi_bot** - це система доступу до розкладу для студентів та викладачів, що допомагая організувати роботу даючи додаткові можливості щодо комунікації про проведення консультацій. Доступ до системи здійснюється через telegram бота, що являє собою "діалог" між користувачем та системою. Користувачі можуть отримувати весь розклад, або розклад тільки на сьогодні/завтра/на цей тиждень. Також для викладача автоматично буде обрані можливі варіанти часу проведення консультації(система проаналізує пари студентів та викладача щоб знайти "вікно" для консультації).

### <a name="l51">5. Функціональність</a>

#### 5.5.1. Інтерфейс студента
Функціональний простір облікового запису студента має надавати можливості доступу до розкладу. Надаються можливості:
 - переглядати розклад на сьогодні/завтра/цей тиждень або весь розклад;
 - створювати запит на додаткову пару по одному із предметів, зазначених у розкладі;
 - підтримувати вже створений запит.

#### 5.5.1. Інтерфейс викдалача
Функціональний простір облікового запису викдалача має надавати можливості доступу до розкладу. Надаються можливості:
 - переглядати розклад на сьогодні/завтра/цей тиждень або весь розклад;
 - переглядати запити студентів щодо консультації;
 - приймати запит та обирати зручний час із запропонованих системою.