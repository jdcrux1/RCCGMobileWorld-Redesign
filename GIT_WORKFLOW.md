# Git Workflow & Collaboration Guide
## RCCG Mobile World Project

---

# 1. COLLABORATION MODEL

## Roles & Responsibilities

```
┌─────────────────────────────────────────────────────────────────┐
│                     ICT BOARD (Steering)                        │
│              Strategic Decisions, Budget Approval                │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                    PROJECT MANAGER                              │
│         Sprint Planning, Resource Allocation, Timeline           │
└────────────────────────────┬────────────────────────────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│ FRONTEND TEAM │   │  BACKEND TEAM │   │   DEVOPS      │
│ (You - Lead)  │◄─►│  Developers   │◄─►│   Engineer    │
│               │   │               │   │               │
│ - UI/UX      │   │ - API Dev    │   │ - CI/CD       │
│ - Design     │   │ - Database   │   │ - Infrastructure│
│ - Frontend   │   │ - Auth      │   │ - Security    │
└───────────────┘   └───────────────┘   └───────────────┘
```

---

# 2. GIT REPOSITORY STRUCTURE

## Repository URLs
- **Frontend (This):** https://github.com/jdcrux1/RCCGMobileWorld-Redesign
- **Backend (Create):** https://github.com/jdcrux1/RCCGMobileWorld-API

## Branch Hierarchy

```
┌──────────────────────────────────────────────────────────────┐
│  main (Production)                                           │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  • Production-ready code                                     │
│  • Deployed to vercel.app (Live)                            │
│  • Only merge from release branches                          │
│  • Protected branch                                          │
└──────────────────────────────────────────────────────────────┘
                              ▲
                              │ Release merge
                              │
┌──────────────────────────────────────────────────────────────┐
│  develop (Staging)                                           │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  • Integration branch                                        │
│  • Deployed to staging.vercel.app                           │
│  • All features merged here before release                   │
│  • Protected branch                                         │
└──────────────────────────────────────────────────────────────┘
                              ▲
                              │ Feature merge
                              │
┌──────────────────────────────────────────────────────────────┐
│  feature/* (Development)                                      │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  • Created from develop                                     │
│  • One feature per branch                                   │
│  • PR to develop when complete                              │
│  • Delete after merge                                       │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│  bugfix/* (Quick Fixes)                                      │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  • Created from develop                                     │
│  • For non-critical bugs                                    │
│  • PR to develop                                           │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│  hotfix/* (Critical Fixes)                                   │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  • Created from main                                        │
│  • Critical production fixes                                │
│  • Merge to both main AND develop                           │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│  release/* (Release Prep)                                    │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  • Created from develop                                     │
│  • Final testing and bug fixes                              │
│  • Merge to main when ready                                 │
└──────────────────────────────────────────────────────────────┘
```

---

# 3. DEVELOPER ONBOARDING CHECKLIST

## Step 1: GitHub Access
```
☐ Create GitHub account
☐ Send username to admin
☐ Accept invitation to organization
☐ Enable 2FA authentication
```

## Step 2: Clone & Setup
```bash
# Clone the repository
git clone https://github.com/jdcrux1/RCCGMobileWorld-Redesign.git

# Navigate to project
cd RCCGMobileWorld-Redesign

# Configure Git
git config user.name "Your Name"
git config user.email "your.email@rccg.org"

# Check current branches
git branch -a
```

## Step 3: Create Development Branch
```bash
# Switch to develop
git checkout develop

# Pull latest
git pull origin develop

# Create your feature branch
git checkout -b feature/your-feature-name

# Push to remote
git push -u origin feature/your-feature-name
```

## Step 4: Development Workflow
```bash
# Make changes...
git add .
git commit -m "feat: add new feature"

# Push changes
git push origin feature/your-feature-name

# Create Pull Request via GitHub UI
# or use CLI
gh pr create --fill
```

---

# 4. VERSIONING STRATEGY

## Semantic Versioning Format
```
vMAJOR.MINOR.PATCH

v1.0.0
 │  │  │
 │  │  └── Bug fixes, small changes
 │  └───── New features (backward compatible)
 └──────── Major changes (breaking updates)
```

## Version Roadmap
```
v1.0.0 - MVP Launch (Current)
    ├── Basic sermon streaming
    ├── Event listing
    ├── Contact forms
    └── Basic giving page

v1.1.0 - Q2 2026
    ├── User authentication
    ├── Member dashboard
    ├── Event registration
    └── Sermon bookmarking

v2.0.0 - Q3 2026
    ├── Mobile app API
    ├── Payment integration
    ├── Live streaming
    └── Advanced analytics

v3.0.0 - Q4 2026
    ├── AI-powered recommendations
    ├── Multi-language support
    ├── Advanced reporting
    └── Church management tools
```

---

# 5. PULL REQUEST WORKFLOW

## Creating a PR
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] New feature
- [ ] Bug fix
- [ ] Documentation update
- [ ] Refactoring

## Testing
- [ ] Tested locally
- [ ] No console errors
- [ ] Responsive design works

## Screenshots
[Add screenshots if UI changes]

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-reviewed code
- [ ] Documentation updated
```

## PR Review Process
```
Author creates PR
      │
      ▼
Code Review (min 1 reviewer)
      │
      ├──► Changes requested
      │         │
      │         ▼
      │    Make fixes
      │         │
      │         ▼
      │    Re-submit
      │         │
      └─────────┘
      │
      ▼
Approved
      │
      ▼
Merge to develop
      │
      ▼
Delete feature branch
```

---

# 6. VERCEL DEPLOYMENT SETUP

## Deployment Pipeline
```
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│  Feature │──►│  Develop │──►│  Release │──►│  Main   │
│  Branch  │   │  Branch  │   │  Branch  │   │  Branch │
└──────────┘   └──────────┘   └──────────┘   └──────────┘
                   │               │               │
                   ▼               ▼               ▼
            ┌──────────┐   ┌──────────┐   ┌──────────┐
            │ Staging  │   │  QA/Test │   │Production│
            │Preview   │   │          │   │  Live    │
            └──────────┘   └──────────┘   └──────────┘
```

## Vercel Project Settings
```
Production: main branch
Preview: All PRs
Development: develop branch (optional)
```

## Environment Variables
```
# Frontend
VITE_API_URL=https://api.rccgmobileworld.org
VITE_STRIPE_KEY=pk_test_xxx

# Backend (separate repo)
DATABASE_URL=postgresql://...
JWT_SECRET=your-secret
STRIPE_SECRET=sk_test_xxx
```

---

# 7. COMMUNICATION PROTOCOL

## Daily Standup (15 min)
- **When:** Daily, 9:00 AM
- **Where:** Teams/Slack
- **Format:**
  - Yesterday: What I did
  - Today: What I'll do
  - Blockers: Any issues

## Sprint Planning (Weekly)
- **When:** Monday, 10:00 AM
- **Duration:** 1 hour
- **Agenda:**
  - Review backlog
  - Estimate stories
  - Commit to sprint goals

## Sprint Review (Bi-weekly)
- **When:** Friday, 3:00 PM
- **Duration:** 1 hour
- **Agenda:**
  - Demo completed features
  - Retrospective
  - Plan next sprint

## Issue Tracking
```
Priority Levels:
├── P0 - Critical (Production down)
├── P1 - High (Major feature broken)
├── P2 - Medium (Minor issues)
└── P3 - Low (Nice to have)
```

---

# 8. HANDOFF PROCESS: FRONTEND TO BACKEND

## What Backend Developers Need

### 1. API Endpoint Documentation
All endpoints must be documented with:
- Request/Response formats
- Authentication requirements
- Error codes
- Example calls

### 2. Mock Data
```javascript
// Example: sermons.json
[
  {
    "id": "1",
    "title": "Going Higher Part 75",
    "speaker": "Pastor E.A. Adeboye",
    "videoUrl": "https://youtube.com/embed/xxx",
    "date": "2026-02-16"
  }
]
```

### 3. Component Documentation
```javascript
// Example: Sermon Card props
{
  title: "string (required)",
  speaker: "string (required)",
  thumbnail: "string (URL)",
  date: "string (ISO date)",
  videoUrl: "string (optional)",
  duration: "number (optional)"
}
```

### 4. Integration Points
| Feature | Frontend | Backend |
|---------|----------|---------|
| Auth | Login form | /api/auth/* |
| Sermons | Sermon cards | /api/sermons/* |
| Events | Event list | /api/events/* |
| Giving | Payment form | /api/give/* |
| Profile | User dashboard | /api/user/* |

---

# 9. SECURITY PROTOCOL

## Access Control
```
Level 0 - Public: Anyone can view
Level 1 - Member: Registered users
Level 2 - Staff: Church staff
Level 3 - Admin: System administrators
Level 4 - Super Admin: Full access
```

## Security Checklist
- [ ] No secrets in code
- [ ] Environment variables for credentials
- [ ] HTTPS only
- [ ] Input validation
- [ ] SQL injection prevention
- [ ] XSS protection
- [ ] CSRF tokens
- [ ] Rate limiting

---

# 10. CONTACT & SUPPORT

**Project Lead:** [Your Name]  
**Email:** [Your Email]  
**GitHub Organization:** https://github.com/jdcrux1  
**Vercel Dashboard:** https://vercel.com/dashboard

**Emergency Contacts:**
- Production Issues: [Phone]
- GitHub Admin: [Email]
- Vercel Support: [Email]

---

*Document Version: 1.0*
*Last Updated: March 2026*
*Maintained by: Frontend Team*
