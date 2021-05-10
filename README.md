# Телеграм бот для проекту rozklad_kpi_remake

Навчальний проект з курсу ІПЗ-2

## Про проект

В якості проекта було розроблено Telegram бота, що допомагає студентам та викладачам дізнаватися розклад.

## Встановлення

Проект розроблено мовою `python3`, тому поперше треба встановити необхідні пакети:
```
pip3 install pytelegrambotapi
```

Для функціонування бота потрібно вказати `SECRET_TOKEN` як змінну оточення(environment variable):
```
export ROZKLAD_BOT_KEY=xxx
```

Після чого запустити систему:
```
python3 ./bot.py
```

## Документація

Документація до коду: https://drewg3r.github.io/rozklad_kpi_bot/
Пояснювальна записка: https://github.com/drewg3r/rozklad_kpi_bot/blob/master/docs/README.md
