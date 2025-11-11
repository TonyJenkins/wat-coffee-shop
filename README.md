# The WAT Coffee Counter

A simple Django project, with one app. The project represents a coffee shop, and the app is the coffee (drinks) counter.

The `main` branch contains the initial setup. All development is in the `amj-americano` branch.

## Development

1. Create a model to represent a drink at the coffee counter. It will need attributes such as a name, description, and maybe price. Don't forget to add a slug field for useful URLs.
2. Create a migration, and create the database. Populate it with a test fixture (use AI to generate these!). Remember to register the app in `settings.py`.
3. Register the model for admin. Customise if desired. Check the admin screens by creating a superuser.
4. Create a URL mapping for the app (linked from the project), including a URL for a drink based on the slug. Add a view to return the correct record.
5. Create the template to display a single drink.
6. Create an index page and URL for the drinks counter, with placeholder for drink list.
7. Modify the index view to display a list of all the drinks.
