# Johnathan Irvin's Website

Johnathan Irvin's personal website is at [https://johnathanirvin.com](https://johnathanirvin.com).

# Usage

It is highly recommended to use a virtual environment to keep your project isolated from other projects.

Inside of a python environment, you can import the requirements and run the application using gunicorn or flask run.

```bash
pip install -r requirements.txt
FLASK_ENV=development gunicorn website:app
```

Docker may be used to run the application.

```bash
docker build -t johnathanirvin/website .
docker run -p 8000:8000 johnathanirvin/website
```

# Testing

Use pytest to run tests.

```bash
python -m pytest tests/
``` 

If you would like to update the snapshot tests, you can use the following command.

```bash
python -m pytest tests/ --snapshot-update
```

# License

This project is licensed under the MIT license. See the LICENSE file for more information, or visit [Choose A License](https://choosealicense.com/licenses/mit/).

# Contribution

This project is open source. Feel free to contribute to the project by making a pull request, creating an issue ticket, or sending an email to [Johnny Irvin](mailto:irvinjohnathan@gmail.com).
