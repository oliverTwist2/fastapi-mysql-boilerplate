# FastAPI MySQL Boilerplate

A modern, production-ready FastAPI boilerplate with MySQL database integration, featuring SQLAlchemy ORM, Alembic for database migrations, and a clean project structure.

## Features

- FastAPI web framework
- MySQL database integration with SQLAlchemy ORM
- Alembic for database migrations
- Environment variable configuration
- Clean project structure
- Type hints and Pydantic models
- Async database operations

## Prerequisites

- Python 3.8+
- MySQL Server
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/fastapi-mysql-boilerplate.git
cd fastapi-mysql-boilerplate
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/MacOS
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with the following variables:
```env
DATABASE_URL=mysql+pymysql://username:password@localhost:3306/database_name
```

5. Run database migrations:
```bash
alembic upgrade head
```

6. Start the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`. Visit `http://localhost:8000/docs` for the interactive API documentation.

## Project Structure

```
fastapi-mysql-boilerplate/
├── app/
│   ├── api/          # API routes
│   ├── core/         # Core functionality
│   ├── db/           # Database models and session
│   ├── schemas/      # Pydantic models
│   └── main.py       # FastAPI application
├── alembic/          # Database migrations
├── requirements.txt  # Project dependencies
└── .env             # Environment variables
```

## Contributing

We welcome contributions from the community! Here's how you can help:

1. Fork the repository
2. Create a new branch for your feature:
```bash
git checkout -b feature/your-feature-name
```

3. Make your changes and commit them:
```bash
git commit -m "Add your feature description"
```

4. Push to your fork:
```bash
git push origin feature/your-feature-name
```

5. Create a Pull Request

### Ways to Contribute

- Test the application and report any issues in the Issues tab
- Implement new features from the TODO list
- Improve documentation
- Add tests
- Fix bugs

### Need Help?

If you encounter any issues or have questions:
1. Check the Issues tab for similar problems
2. Create a new issue if your problem hasn't been reported
3. For direct assistance, email the author at [oliverikegah@gmail.com]

## Author

**Oliver Ikegah** - [GitHub Profile](https://github.com/oliverTwist2)

## License

This project is licensed under the MIT License - see the LICENSE file for details. 