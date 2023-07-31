# Blogee - A Blogging App

Blogee is a Django web application that serves as a simple and customizable blogging platform.

## Features

- User registration and authentication system
- Create, edit, and delete blog posts
- Rich text editor for writing blog content
- Categories and archives for organizing posts
- Responsive and user-friendly interface

## Technologies Used

- Django
- Python
- HTML/CSS
- JavaScript

## Setup

Follow these steps to set up the Blogee app on your local machine:

1. Clone the repository: `git clone https://github.com/azhrbhr/blogee.git`
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
4. Install the dependencies: `pip install -r requirements.txt`
5. Create the database: `python manage.py migrate`
6. Run the development server: `python manage.py runserver`
7. Visit `http://localhost:8000` in your web browser to access the Blogee app.


## Usage

Once the Blogee app is set up, you can register as a new user, log in, and start creating your blog posts. The rich text editor allows you to format your posts easily, and you can categorize them using tags and categories.


## Creating a Superuser

To access the Django admin interface and manage the application's data, you need to create a superuser account. Follow these steps to create a superuser:

1. Make sure the Django development server is running: `python manage.py runserver`.
2. Open a web browser and go to `http://localhost:8000/admin`.
3. Click on the "Log in" link.
4. If you haven't created a superuser yet, run the following command in the terminal or command prompt: `python manage.py createsuperuser`.
5. You will be prompted to enter a username, email address, and password for the superuser account.
6. Once the superuser is created, go back to the admin login page and log in using the superuser credentials.
7. You will now have access to the Django admin interface to manage the application's data.

## Contributing

If you would like to contribute to Blogee, please fork the repository, make your changes, and submit a pull request.



## Credits

Blogee was created by [Azhar Bihari](https://github.com/azhrbhr).

## Contact

For any questions or inquiries, you can reach me at [azhrbhr@gmail.com](mailto:azhrbhr@gmail.com).
