# Production FastAPI Template

A production-oriented FastAPI starter that demonstrates the architecture I use for maintainable backend services: async PostgreSQL, JWT authentication, role-based access control, Redis, Celery background jobs, Docker, tests, health checks, and CI.

## Why this project exists

Many FastAPI examples stop at CRUD. This repository is intentionally structured closer to a real service: application settings are isolated, database sessions are dependency-injected, authorization is explicit, background work is separated from request handling, and infrastructure is reproducible.

## Architecture

```text
Client
  |
  v
FastAPI API
  |-- JWT authentication / RBAC
  |-- SQLAlchemy async session ---> PostgreSQL
  |-- Redis cache / broker -------> Redis
  `-- background jobs -----------> Celery worker
```

## Features

- FastAPI with versioned API routes
- Async SQLAlchemy 2.x + PostgreSQL
- Alembic-ready database structure
- JWT access tokens with password hashing
- RBAC dependency (`user` / `admin`)
- Redis integration
- Celery background jobs
- Structured settings with `pydantic-settings`
- Docker + Docker Compose
- Pytest examples
- Ruff linting
- GitHub Actions CI
- Liveness/readiness health endpoints

## Tech stack

`Python` `FastAPI` `SQLAlchemy` `PostgreSQL` `Redis` `Celery` `JWT` `Docker` `Pytest` `GitHub Actions`

## Quick start

```bash
cp .env.example .env
docker compose up --build
```

API: `http://localhost:8000`

Interactive docs: `http://localhost:8000/docs`

## Example endpoints

```text
GET  /health/live
GET  /health/ready
POST /api/v1/auth/register
POST /api/v1/auth/login
GET  /api/v1/users/me
GET  /api/v1/admin/stats
POST /api/v1/jobs/example
```

## Engineering decisions

### Thin route handlers
HTTP routes validate input and delegate work to services instead of mixing transport, persistence, and business logic.

### Explicit authorization
Authentication identifies the caller; authorization is handled separately through role-aware dependencies. This keeps permission rules visible and testable.

### Background work outside request lifecycle
Long-running tasks are dispatched to Celery so API latency is not coupled to expensive processing.

### Infrastructure parity
The same PostgreSQL and Redis services used locally through Compose can be mapped to managed cloud services in production.

## Production evolution

For a real deployment I would typically add OpenTelemetry, Sentry, a managed secrets provider, rate limiting, migration execution in the deployment pipeline, and environment-specific infrastructure as code.

## Author

**Dovlet Aydogdyyev** — Senior Software Engineer  
Python · Django · FastAPI · Flutter · React
