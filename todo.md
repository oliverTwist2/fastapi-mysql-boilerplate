# 📌 TODO — FastAPI + MySQL Boilerplate

This file lists all the planned and recommended features that haven't been implemented yet.  
Feel free to pick one and contribute!

---

## 🔐 Auth & Security

- [ ] Blacklist old tokens on logout
- [ ] Store refresh/access tokens in a database or Redis
- [ ] Protect refresh token endpoint with stricter validation (e.g. IP, user-agent, token rotation)
- [ ] Optional two-factor authentication support
- [ ] Add rate limiting middleware (e.g. slowapi)

---

## 🧰 Dev Tools & Quality

- [ ] Add pre-commit hooks with lack, lake8, and isort
- [ ] Integrate automated testing (e.g. Pytest)
- [ ] Add CI/CD workflow (GitHub Actions)
- [ ] Add code coverage reports
- [ ] Add Makefile or un.ps1 to simplify development scripts

---

## 📊 Features & Enhancements

- [ ] User roles and permissions system
- [ ] Admin dashboard or CLI admin tools
- [ ] API versioning strategy
- [ ] Pagination utility
- [ ] Soft delete for models
- [ ] Audit logging (track who did what)

---

## 📦 Packaging

- [ ] Dockerize the application
- [ ] Add docker-compose support for full stack (API + MySQL + Redis)
- [ ] Production-ready .env.example and config validation

---

## 🧪 Test Coverage Suggestions

- [ ] Auth flow (login, refresh, logout)
- [ ] Token expiration scenarios
- [ ] Alembic migration tests
- [ ] Database schema validation
- [ ] 404 and global error handling

---

## 🧑‍💻 Contributions

- Contributors are encouraged to pick any task here and start implementing.
- If unsure where to begin, check the [Issues tab](https://github.com/<your-username>/fastapi-mysql-boilerplate/issues) or open a new one.
- Create a feature branch like eature/task-name, then make a pull request.

---

*Maintained by [Oliver Ikegah](mailto:ikegaholiver@gmail.com)*
