# Lab 08: CI/CD with GitHub Actions

## Module
Module 08 - CI/CD with GitHub Actions

## Tier
Core MVP Lab

## Goal
Create a working build-test-deploy workflow with quality gates.

## Prerequisites

- GitHub repository and Actions enabled
- Required secrets configured
- App from prior modules committed

## Steps

1. Add workflow triggers for push and pull request.
2. Add build and test jobs.
3. Add container build and publish stage.
4. Add deployment job and environment guardrails.
5. Enforce test and coverage quality gates.

## Validation

- Workflow executes end to end.
- Failed tests block deploy stage.

## Evidence

- Workflow YAML file
- Successful run URL
- Failed run URL showing gate enforcement
