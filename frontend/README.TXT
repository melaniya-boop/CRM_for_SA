# CRM for System Analyst

## Запуск фронтенда

1. `cd frontend`
2. `npm install`
3. `npm run dev`
4. Открой `http://localhost:5173` (или порт, который предложит Vite)

## Переменные окружения
Скопируй `.env.example` в `.env.local` и заполни значения. Не коммить `.env.local`.

## Ветки и Git
Основная ветка: `main`. После клонирования можно сразу делать `git pull` и `git push`.

## Зависимости
Версии пакетов зафиксированы в `package-lock.json`. Не запускай `npm audit fix --force`, чтобы не сломать совместимость.
