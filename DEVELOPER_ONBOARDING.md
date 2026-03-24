# Developer Onboarding Guide
## RCCG Mobile World - Frontend Repository

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Tech Stack](#tech-stack)
3. [Getting Started](#getting-started)
4. [Git Workflow](#git-workflow)
5. [Vercel Deployment](#vercel-deployment)
6. [Frontend-Backend Integration](#frontend-backend-integration)
7. [API Documentation Standards](#api-documentation-standards)
8. [Code Standards](#code-standards)
9. [Communication Channels](#communication-channels)

---

## Project Overview

**Project Name:** RCCG Mobile World  
**Description:** A comprehensive digital platform for The Redeemed Christian Church of God, providing sermon streaming, event management, online giving, and member engagement.  
**Current Status:** Frontend Complete - Backend Development Phase  
**GitHub Repository:** https://github.com/jdcrux1/RCCGMobileWorld-Redesign

---

## Tech Stack

### Frontend (This Repository)
- **Framework:** HTML5, CSS3, JavaScript (Vanilla + Tailwind CSS)
- **Build Tools:** Tailwind CSS via CDN
- **Icons:** Heroicons, Font Awesome
- **Fonts:** Inter, Playfair Display (Google Fonts)
- **Hosting:** Vercel

### Backend (To Be Developed)
- **Recommended:** Node.js, Python, or PHP
- **Database:** PostgreSQL, MySQL, or MongoDB
- **Authentication:** JWT, OAuth 2.0

---

## Getting Started

### Prerequisites
```bash
# Install Git
brew install git  # macOS
# or
sudo apt install git  # Linux

# Clone the repository
git clone https://github.com/jdcrux1/RCCGMobileWorld-Redesign.git

# Start local server (Python)
cd RCCGMobileWorld-Redesign
python3 -m http.server 8000

# Or use any static server
# npx serve
# or
# php -S localhost:8000
```

### Local Development
1. Clone repository
2. Create feature branch: `git checkout -b feature/your-feature-name`
3. Make changes
4. Test locally at `http://localhost:8000`
5. Push changes and create PR

---

## Git Workflow

### Branching Strategy

```
main (production)
  │
  ├── develop (staging)
  │     │
  │     ├── feature/user-authentication
  │     ├── feature/event-management-api
  │     ├── feature/sermon-upload-system
  │     ├── bugfix/login-redirect-issue
  │     └── hotfix/security-patch
  │
  └── release/v1.0.0
```

### Naming Conventions
- `feature/` - New features
- `bugfix/` - Bug fixes
- `hotfix/` - Production fixes
- `release/` - Release preparation

### Commit Message Format
```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation
- `style` - Formatting
- `refactor` - Code restructuring
- `test` - Testing

**Example:**
```
feat(api): add user authentication endpoints

- Implemented JWT-based auth
- Added login, register, logout endpoints
- Included password reset functionality

Closes #123
```

### Pull Request Process
1. Create feature branch from `develop`
2. Make changes and commit
3. Push and create PR to `develop`
4. Request code review
5. Address feedback
6. Merge after approval

---

## Vercel Deployment

### Automatic Deployments
- **Main branch:** Production - https://rccg-mobile-world-redesign.vercel.app
- **Develop branch:** Staging (configure)
- **Pull Requests:** Preview deployments

### Manual Deployment
```bash
# Install Vercel CLI
npm i -g vercel

# Login
vercel login

# Deploy
vercel --prod
```

### Environment Variables
If backend requires API keys, add in Vercel Dashboard:
- Settings → Environment Variables
- Add KEY=VALUE pairs

---

## Frontend-Backend Integration

### API Integration Points

The frontend expects these API endpoints:

#### Authentication
```javascript
// POST /api/auth/login
// Request: { email, password }
// Response: { token, user }

// POST /api/auth/register
// Request: { name, email, password }
// Response: { token, user }

// POST /api/auth/logout
// Response: { success }
```

#### Sermons
```javascript
// GET /api/sermons
// Query: ?page=1&limit=10&series=xxx
// Response: { sermons: [], total, page }

// GET /api/sermons/:id
// Response: { sermon }

// POST /api/sermons (admin)
// Request: { title, series, speaker, videoUrl, audioUrl }
// Response: { sermon }
```

#### Events
```javascript
// GET /api/events
// Query: ?upcoming=true
// Response: { events: [] }

// GET /api/events/:id
// Response: { event }

// POST /api/events (admin)
// Request: { title, date, location, description }
// Response: { event }
```

#### Giving/Donations
```javascript
// POST /api/give
// Request: { amount, paymentMethod, transactionId }
// Response: { success, receipt }

// GET /api/give/history
// Response: { donations: [] }
```

#### User Profile
```javascript
// GET /api/user/profile
// Response: { user }

// PUT /api/user/profile
// Request: { name, phone, ministry }
// Response: { user }
```

### Integration Example

**Option 1: API Proxy (Recommended)**
```javascript
// In pages-shared.js or separate API module
const API_BASE = 'https://your-api.vercel.app/api';

async function fetchSermons() {
  const response = await fetch(`${API_BASE}/sermons`);
  return response.json();
}
```

**Option 2: Environment Variables**
```javascript
// Create .env file
REACT_APP_API_URL=https://your-api.vercel.app/api

// Use in code
const API_URL = process.env.REACT_APP_API_URL;
```

### Frontend Design System for Backend Developers

#### Component Structure
```
/components
  /navigation    - Navbar, mobile menu
  /cards         - Sermon cards, event cards
  /modals        - Login, video player
  /forms         - Contact, giving forms
  /footer        - Site footer
```

#### Data Models (For Reference)

**User:**
```json
{
  "id": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "role": "member|admin|pastor",
  "createdAt": "datetime"
}
```

**Sermon:**
```json
{
  "id": "string",
  "title": "string",
  "series": "string",
  "speaker": "string",
  "videoUrl": "string",
  "audioUrl": "string",
  "thumbnail": "string",
  "duration": "number",
  "date": "datetime",
  "description": "string"
}
```

**Event:**
```json
{
  "id": "string",
  "title": "string",
  "date": "datetime",
  "endDate": "datetime",
  "location": "string",
  "description": "string",
  "image": "string",
  "registrationUrl": "string"
}
```

---

## API Documentation Standards

All backend APIs must include:

1. **OpenAPI/Swagger Documentation**
2. **Request/Response Examples**
3. **Authentication Requirements**
4. **Rate Limiting Info**
5. **Error Codes and Messages**

### Example API Doc Format

```yaml
GET /api/sermons
---
Get all sermons with pagination

Parameters:
  - page (integer, optional): Page number (default: 1)
  - limit (integer, optional): Items per page (default: 10)
  - series (string, optional): Filter by series

Response 200:
{
  "sermons": [
    {
      "id": "123",
      "title": "Going Higher Part 75",
      "speaker": "Pastor E.A. Adeboye",
      "thumbnail": "https://...",
      "date": "2026-02-01"
    }
  ],
  "total": 50,
  "page": 1,
  "totalPages": 5
}
```

---

## Code Standards

### Frontend Guidelines
- Use semantic HTML5
- Follow BEM naming for CSS (or Tailwind classes)
- Ensure WCAG 2.1 AA accessibility
- Mobile-first responsive design
- Optimize images (WebP format)

### Required Testing
- Cross-browser testing (Chrome, Safari, Firefox)
- Mobile responsiveness testing
- Accessibility audit (Lighthouse score > 90)

---

## Communication Channels

### Daily Standup
- Time: [To be determined]
- Platform: Slack/Teams/Zoom
- Agenda: Progress, blockers, plans

### Sprint Reviews
- Frequency: Bi-weekly
- Review completed features
- Demo new functionality

### Documentation Updates
- Keep README.md current
- Update API docs with changes
- Document new features in CHANGELOG.md

---

## Support

**Frontend Lead:** [Your Name]  
**GitHub Issues:** https://github.com/jdcrux1/RCCGMobileWorld-Redesign/issues  
**Email:** [Your Email]

---

*Last Updated: March 2026*
*Version: 1.0*
