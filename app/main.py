from fastapi import FastAPI
from app.core.error_handlers import register_exception_handlers
from app.core import logger  # Ensures logging is configured
from app.api.routes import user
from app.api.routes import auth


app = FastAPI()

# Register custom exception handlers
register_exception_handlers(app)

# Include your routes
app.include_router(user.router, prefix="/api/users", tags=["users"])
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
