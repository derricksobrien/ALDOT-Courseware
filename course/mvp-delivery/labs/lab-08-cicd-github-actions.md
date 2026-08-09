# Lab 08: CI/CD with GitHub Actions

## Module
Module 08 - CI/CD with GitHub Actions

## Tier
Core MVP Lab

## Goal
Create a working build-test-deploy workflow with quality gates.

## Prerequisites

- A fork of the app repository in your GitHub account with Actions enabled
- Required secrets configured
- App from prior modules committed

## Steps

0. Fork the repository to your own GitHub account and use that fork as the workflow target.
1. Add workflow triggers for push and pull request.
2. Add build and test jobs.
3. Add container build and publish stage.
4. Add deployment job and environment guardrails.
5. Enforce test and coverage quality gates.
6. Add branch protection with required checks.

## Validation

- Workflow executes end to end from the forked repository.
- Failed tests block the deploy stage.

## Evidence

- Workflow YAML file
- Branch protection or required-checks proof
- Successful run URL
- Failed run URL showing gate enforcement
