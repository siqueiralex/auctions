# auctions
Simple Auctions System

To run this project, follow the steps below:

1. Install the project in editable mode:
   ```
   pip install -e .
   ```

2. Set the `DJANGO_SETTINGS_MODULE` environment variable to `auctions.settings`:
   ```
   export DJANGO_SETTINGS_MODULE=auctions.settings
   ```

3. Run migrations:
   ```
   django-admin makemigrations
   django-admin migrate
   ```

4. Start the development server:
   ```
   django-admin runserver
   ```

You should now be able to access the project at `http://127.0.0.1:8000/`. 

Happy auctioning! 🎉
********************************************************************************
