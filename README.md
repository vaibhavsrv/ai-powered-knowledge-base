# Personal AI Knowledge Base

An industrial-grade AI-powered knowledge platform inspired by Notion AI and Perplexity AI.

This project is focused on building a scalable Retrieval-Augmented Generation (RAG) system capable of:

* Uploading and processing documents
* Semantic search
* Citation-based AI answers
* Multi-document reasoning
* AI summaries
* Long-term memory systems
* Study planning
* Production-ready deployment

The project is designed with clean architecture, scalable backend engineering practices, async processing pipelines, and modular AI infrastructure.

---

# Features

## Core Features

* PDF, TXT, DOCX upload support
* Document extraction and preprocessing
* Embedding generation pipeline
* Vector database integration
* Semantic similarity search
* Retrieval-Augmented Generation (RAG)
* Citation-aware responses
* AI-generated summaries
* Multi-user authentication system
* Async background processing
* Study planner foundation

---

# Tech Stack

## Frontend

* Next.js 14
* React
* TypeScript
* TailwindCSS
* React Query
* Zustand

## Backend

* FastAPI
* SQLAlchemy
* Alembic
* PostgreSQL
* Redis
* Celery

## AI / ML

* LangChain
* LlamaIndex
* OpenAI APIs
* Local LLM support (planned)
* SentenceTransformers (planned)

## Vector Database

* ChromaDB
* Pinecone (planned)
* Qdrant (planned)

## Infrastructure

* Docker
* Docker Compose
* Nginx
* Kubernetes-ready architecture
* GitHub Actions CI/CD

---

# Project Architecture

```text
personal-ai-kb/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── domain/
│   │   ├── infrastructure/
│   │   ├── workers/
│   │   └── main.py
│   ├── migrations/
│   ├── tests/
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── Dockerfile
│   └── package.json
│
├── docker-compose.yml
├── nginx/
├── .github/workflows/
└── k8s/
```

---

# Backend Architecture

The backend follows a layered clean architecture:

```text
Route Layer
↓
Service Layer
↓
Repository Layer
↓
Infrastructure Layer
↓
Database / Vector Store / AI Providers
```

## API Layer

Responsible only for:

* HTTP request handling
* Validation
* Dependency injection
* Response serialization

No business logic should exist in routes.

---

## Domain Layer

Contains:

* Services
* Business rules
* Repositories
* Schemas
* Models

This layer should remain independent from frameworks and infrastructure.

---

## Infrastructure Layer

Handles all external integrations:

* OpenAI
* Vector databases
* Redis
* S3 storage
* Embedding providers
* LLM providers

This allows provider replacement without changing business logic.

---

## Worker Layer

Celery workers handle:

* Document ingestion
* Chunking
* Embedding generation
* Summarization
* Indexing

Heavy AI tasks should never block API requests.

---

# RAG Pipeline

```text
User Upload
↓
Document Extraction
↓
Chunking
↓
Embedding Generation
↓
Vector Database Storage
↓
User Query
↓
Query Embedding
↓
Similarity Search
↓
Relevant Context Retrieval
↓
LLM Prompt Construction
↓
Citation-Based Response
```

---

# Authentication

Authentication is implemented using:

* JWT access tokens
* Refresh tokens
* Password hashing with bcrypt
* Dependency-injected user authentication

Security goals:

* Stateless authentication
* Secure password storage
* Token expiration
* Scalable multi-user architecture

---

# Database Design

Core relational entities:

* Users
* Documents
* Chunks
* Chats
* Citations
* Planner Tasks

PostgreSQL stores:

* Metadata
* User data
* Conversations
* Permissions
* Planner information

Vector databases store:

* Embeddings
* Semantic indexes
* Retrieval metadata

---

# Chunking Strategy

Initial chunking strategy:

* Recursive character chunking
* Chunk size: 500–800 tokens
* Overlap: 100–150 tokens

Why chunking matters:

* Better retrieval quality
* Reduced context loss
* Improved semantic search
* Lower token cost

---

# Async Architecture

The backend uses async-first architecture.

FastAPI + async SQLAlchemy + Redis + Celery provide:

* high concurrency
* scalable request handling
* non-blocking processing
* distributed background jobs

---

# Local Development Setup

## Clone Repository

```bash
git clone https://github.com/vaibhavsrv/ai-powered-knowledge-base.git
cd ai-powered-knowledge-base
```

---

# Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create:

```text
backend/.env
```

Example:

```env
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/personal_ai_kb
REDIS_URL=redis://localhost:6379
SECRET_KEY=your_secret_key
OPENAI_API_KEY=your_openai_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
```

---

# Run Backend

```bash
uvicorn app.main:app --reload
```

API Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Database Migrations

Generate migration:

```bash
alembic revision --autogenerate -m "create users table"
```

Apply migration:

```bash
alembic upgrade head
```

---

# Docker Setup

Build containers:

```bash
docker-compose up --build
```

Planned containers:

* backend
* frontend
* postgres
* redis
* celery worker
* nginx

---

# Development Roadmap

## Phase 1

* Backend architecture
* FastAPI setup
* PostgreSQL setup
* JWT authentication
* Docker setup

## Phase 2

* File upload pipeline
* Object storage integration
* Async workers

## Phase 3

* Text extraction
* Chunking pipeline
* Embedding generation

## Phase 4

* Vector database integration
* Semantic retrieval
* RAG system

## Phase 5

* Citation engine
* Multi-document retrieval
* Memory systems

## Phase 6

* Study planner
* Advanced retrieval optimization
* Production observability

## Phase 7

* Kubernetes deployment
* Horizontal scaling
* Distributed workers
* Enterprise optimizations

---

# Production Goals

This project is designed to evolve toward:

* scalable AI infrastructure
* distributed retrieval systems
* enterprise-grade observability
* multi-tenant architecture
* hybrid retrieval pipelines
* cost-optimized LLM orchestration
* production-ready deployment

---

# Future Improvements

Planned future upgrades:

* Hybrid search (BM25 + vector)
* Reranking pipelines
* Query expansion
* Streaming AI responses
* Multi-modal ingestion
* Local LLM inference
* GPU worker support
* Kafka event architecture
* Advanced caching
* Role-based access control
* Fine-grained permissions

---

# Engineering Principles

This project follows:

* Clean Architecture
* SOLID Principles
* Dependency Injection
* Async-first design
* Infrastructure abstraction
* Modular AI pipelines
* Production-grade engineering practices

---

# Status

Current Progress:

* Backend architecture initialized
* Virtual environment configured
* Alembic initialized
* Security layer setup in progress
* JWT authentication foundation completed
* Clean architecture structure established

---

# Author

Built by Vaibhav as a production-focused AI engineering and backend systems project.
