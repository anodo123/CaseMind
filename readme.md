# CaseMind ⚖️

CaseMind is a Legal AI system designed to answer queries on Indian Supreme Court judgments using a Retrieval-Augmented Generation (RAG) pipeline.

## Features (Planned)

- Supreme Court judgment ingestion
- Semantic + keyword hybrid search
- Context-aware legal Q&A
- Evaluation pipeline for answer quality
- Legal metadata extraction and indexing

## Tech Stack

- FastAPI
- Vector DB (TBD)
- PostgreSQL
- Open-source LLMs

## Current Progress

- Legal search API structure analysis completed
- Search response decomposition completed
- Initial system architecture planning in progress
- Metadata structure mapping completed
- Dockerized PostgreSQL environment configured
- SQLAlchemy ORM setup completed
- Alembic migration workflow configured
- Initial metadata database schema implementation in progress

# Level 1 Architecture

The following diagram represents the structure of the legal search API response.

It includes:
- Request search URL
- API response decomposition
- Category/filter metadata
- Pagination/query metadata
- Document metadata records

![Level 1 Architecture](docs/images/Level1Architecture.jpg)

---

# Search API Response Structure

The legal search API currently returns:


{
  "categories": [...],
  "docs": [...],
  "found": "1 - 10 of 7145",
  "encodedformInput": "fromdate:23-04-2026 todate:13-05-2026"
}


# Level 2 Architecture

The following diagram represents the structure of the detailed judgment retrieval pipeline.

After retrieving document identifiers from the Search API, the system calls the `GetDocumentAPI` to fetch a fully structured judgment.

The extracted judgment intelligence currently includes:

- Case metadata and indexing
- Full judgment text
- Paragraph semantic labels
- Legal citations
- Statutory references
- Party arguments
- Final decision / operative order

This structured representation is intended to support:
- Semantic legal retrieval
- Metadata-aware chunking
- Citation graph analysis
- Legal RAG pipelines
- Downstream legal AI workflows

![Level 2 Architecture](docs/images/Level2Architecture.jpg)


### Implemented ORM Models

## Implemented ORM Models

### JudgmentMetadata

Initial production metadata model for legal judgment indexing and retrieval.

Currently captures:

- Judgment identity and source metadata
- Publication and classification metadata
- Search API retrieval fields
- Citation statistics
- Document characteristics
- Raw payload preservation
- Audit timestamps

Supports:

- Metadata-driven retrieval
- Filtering and ranking
- Future hybrid search
- Citation expansion
- Legal RAG workflows

---

### Court

Normalized legal court reference entity.

Currently captures:

- Canonical court identity
- Court classification
- Jurisdiction metadata
- Geographic metadata
- Audit timestamps

Supports:

- Court-based retrieval filtering
- Metadata normalization
- Future multi-court expansion
- Legal analytics
- Domain graph relationships

Relationship:
Court (1) ------ (N) JudgmentMetadata


## Metadata Database Layer

CaseMind uses a normalized PostgreSQL metadata layer for structured legal intelligence storage.

Current stack:

- PostgreSQL
- SQLAlchemy ORM
- Alembic migrations

Current design philosophy:

- Normalize reusable legal entities
- Avoid overloading JSON fields
- Preserve queryability and indexing capability
- Support future legal graph expansion
- Separate metadata layer from future chunk/vector layers