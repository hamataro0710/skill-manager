# Project Rules (Source of Truth)

This file is the single source of truth for all AI agents (Gemini CLI, Claude Code, GitHub Copilot, etc.) working on this project.

## 📖 Project Overview
- **Name**: {PROJECT_NAME}
- **Description**: {PROJECT_DESCRIPTION}
- **Tech Stack**: {TECH_STACK}

## 📂 Key Directory Structure
- `src/`: Core logic
- `tests/`: Automated tests
- `docs/`: Documentation

## 🛠 Development Lifecycle
- **Install**: `npm install` / `pip install -r requirements.txt`
- **Build**: `npm run build`
- **Test**: `npm test`
- **Lint**: `npm run lint`

## ✍️ Coding Standards
- Use TypeScript with strict type checking.
- Follow PEP 8 for Python code.
- Write concise, self-documenting code.

## 🤖 Agent-Specific Instructions
- Always run tests before proposing a fix.
- Do not modify `.env` or other sensitive files.
- Prefer symbolic links for cross-agent configuration.
