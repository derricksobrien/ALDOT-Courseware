---
layout: default
title: "Lab 04 — Modern .NET API"
parent: Labs
nav_order: 4
---

# Lab 04: Modern .NET API with SQL

## Module
Module 04 - Modern .NET API and Data Access

## Tier
Core MVP Lab

## Goal
Add a SQL-backed API endpoint and validate it end to end.

## Prerequisites

- Repository available: `course/repos/eShopOnWeb`
- Data target available: local SQL or Azure SQL; if not available, use the in-memory fallback for a local validation pass
- .NET SDK and SQL tooling installed
- Preferred path: EF Core; Dapper is optional stretch

## Steps

1. Add a new API endpoint for a domain entity.
2. Register services via dependency injection.
3. Add EF Core data access logic (default path) or Dapper as stretch.
4. Add configuration and secure secret handling.
5. Add and run integration tests.

## Validation

- Endpoint returns expected codes and schema.
- Integration tests pass.

## Evidence

- Endpoint code changes
- Integration test output
- Config and secret handling notes

