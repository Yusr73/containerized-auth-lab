# Threat Model – Containerized Auth Security Lab

## 1. System Overview
A containerized authentication service running in Docker, backed by a PostgreSQL database.
The system provides user login and role-based access (user / admin).

## 2. Assets (What we protect)
- User credentials (username, password hashes)
- Authentication tokens
- User roles and privileges
- Audit logs
- Database integrity

## 3. Actors
- Legitimate user
- Admin user
- Attacker (unauthenticated)
- Attacker (authenticated low-privilege user)

## 4. Trust Boundaries
- Docker network (auth_net) between auth service and database
- Authentication boundary between unauthenticated and authenticated users
- Authorization boundary between user and admin roles

## 5. Threats (High-Level)
- Brute-force login attempts
- Credential stuffing
- Token reuse or replay
- Privilege escalation (user → admin)
- Log tampering or log flooding

## 6. Attack Surface
- Login endpoint
- Token validation logic
- Role-based authorization checks
- Database queries
- Logging mechanism

## 7. Security Observables
- Failed login attempts
- Token reuse patterns
- Access to admin endpoints
- Abnormal request frequency
- Database authentication errors

## 8. Assumptions
- Attacker has network access to the auth service
- Database is not directly exposed
- HTTPS is not the focus of this lab
