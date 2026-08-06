# Lab 04: Modern .NET API with SQL

## Module Alignment
Module 4: C# and .NET in the Modern Stack

## Timebox
90 minutes

## Objectives
- Add a modern REST endpoint to a .NET service.
- Integrate SQL Server using EF Core or Dapper.
- Apply configuration and secret management practices.

## Prerequisites
- `course/repos/eShopOnWeb` or `course/repos/samples`.
- Local SQL Server or Azure SQL database.

## Step-by-Step
1. Create a new API endpoint for a business entity.
2. Add dependency injection registrations.
3. Implement repository pattern using EF Core or Dapper.
4. Add async methods and cancellation tokens.
5. Add configuration sections for database settings.
6. Move secrets to environment variables or Key Vault references.
7. Add integration tests for the endpoint.

## Validation Checks
- Endpoint returns expected responses and error codes.
- Database writes and reads pass integration tests.
- No secrets are committed to source control.

## Deliverables
- API endpoint pull request.
- Integration test results.
- Configuration and secret handling notes.

## Stretch Goals
- Add OpenAPI annotations and a pagination/filtering contract.
