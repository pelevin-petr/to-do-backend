# To-Do App 

#### Это пример приложения для управления задачами, использующее Docker, PostgreSQL и FastAPI.


## Установка и запуск

1. **Клонируйте репозиторий:**

   ```bash
   git clone <ссылка_на_репозиторий>
   cd <папка_с_репозиторием>
   
2. **Настройте файл .env:**

   ```bash
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_SERVER=db
   POSTGRES_PORT=5432
   POSTGRES_DB=to_do_db

3. **Запустите проект с помощью Docker Compose:**
   
   ```bash
   docker-compose up --build

#### Всё, далее вам надо проследовать [сюда]() и подгрузить репозиторий с фронтендом