# AI Architect

AI Architect is a full-stack AI-powered home design platform that combines a modern Next.js interface with a Django backend and AI services for intelligent floor-plan recommendations, home design assistance, and conversational support.

This repository brings together:
- A marketing and user onboarding frontend for a home-design product
- Secure user authentication flows for sign-up and login
- A Django REST API for floor-plan generation and chatbot support
- AI-based recommendation services using embeddings and LLMs
- A design experience that supports architecture, interior, and home-planning ideas

## Project summary

The project is split into two major parts:

1. Frontend (`front_end/`)
   - Built with Next.js 15 + TypeScript
   - Uses Tailwind CSS, Radix UI, Framer Motion, and custom UI components
   - Includes landing page, FAQ, About Us, login/signup pages, and design onboarding screens

2. Backend (`backend/app/`)
   - Built with Django 5 and Django REST Framework
   - Hosts APIs for floor plan generation and chatbot functionality
   - Uses SQLite in development and exposes endpoints under `/api/...`
  
<img width="1896" height="907" alt="image" src="https://github.com/user-attachments/assets/1e02a1d5-7847-4c65-8393-cb1711982d9e" />


## Main features

- AI-assisted floor-plan generation based on plot size, number of floors, and bedrooms
- Similarity-based recommendation of matching floor-plan images using sentence embeddings
- Conversational chatbot using Google Gemini and LangChain retrieval
- User registration and login screens with validation and password hashing
- Modern landing page and marketing content for an architecture/design platform
- Responsive design across desktop and mobile layouts

## Tech stack

### Frontend
- Next.js 15
- React 19
- TypeScript
- Tailwind CSS
- Framer Motion
- Radix UI components
- Drizzle ORM
- Supabase / PostgreSQL-ready configuration
- Zod for validation
- React Hook Form

### Backend
- Python
- Django 5
- Django REST Framework
- SQLite
- CORS middleware
- LangChain
- Google Generative AI (Gemini)
- Sentence Transformers
- Pillow
- Diffusers / PyTorch

## Repository structure

```text
AI_Architect/
├── backend/
│   └── app/
│       ├── chatbot/
│       │   ├── views.py
│       │   ├── retriver.py
│       │   ├── urls.py
│       │   └── ...
│       ├── core/
│       │   ├── settings.py
│       │   ├── urls.py
│       │   └── ...
│       ├── floor/
│       │   ├── floorGenerator.py
│       │   ├── views.py
│       │   ├── urls.py
│       │   └── ...
│       ├── main.py
│       ├── manage.py
│       └── db.sqlite3
│
├── front_end/
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   ├── db/
│   │   ├── lib/
│   │   └── ...
│   ├── package.json
│   ├── next.config.ts
│   ├── drizzle.config.ts
│   ├── tailwind.config.ts
│   ├── tsconfig.json
│   └── README.md
│
├── .gitignore
├── .gitattributes
└── README.md
```

## Key implementation areas

### 1. Frontend landing experience
The homepage is configured in `front_end/src/app/page.tsx` and composes sections like:
- `Navbar`
- `Banner`
- `Home_details`
- `Footer`

This creates a polished homepage for a design-focused product pitch.

### 2. Authentication and user flows
The project includes login and registration views in:
- `front_end/src/app/login/page.tsx`
- `front_end/src/app/signup/page.tsx`
- `front_end/src/app/api/register/route.ts`
- `front_end/src/app/api/login/route.ts`

The registration route hashes passwords with bcrypt and stores user records using Drizzle ORM.

### 3. Floor plan generation service
The backend floor generation logic exists in:
- `backend/app/floor/floorGenerator.py`
- `backend/app/floor/views.py`
- `backend/app/floor/urls.py`

The logic uses sentence-transformers to generate embeddings of floor-plan descriptions and then finds the closest matching design based on a user's requested plot size and floors. This is a very useful pattern for recommendation-based design systems.

### 4. AI chatbot
The chatbot service is implemented in:
- `backend/app/chatbot/views.py`
- `backend/app/chatbot/retriver.py`
- `backend/app/chatbot/urls.py`

This service loads Gemini credentials from environment variables, configures a custom LangChain-backed LLM wrapper, and answers user queries using a retrieval-based QA flow.

### 5. Django project config
The project settings are defined in:
- `backend/app/core/settings.py`

This project config includes:
- Django apps registration
- CORS configuration for local frontend access
- SQLite DB configuration
- Static/media settings

## API overview

### Floor API
Base route:
```text
/api/floor/
```

Configured endpoints:
```text
/api/floor/generate/
/api/floor/images/<image_name>
/api/floor/test-images/
```

The generate endpoint accepts request data such as:
- `plot_length`
- `plot_width`
- `no_of_floors`
- `no_of_bedrooms`
- `shown_images`

It returns the closest matching metadata and an image name.

### Chatbot API
Base route:
```text
/api/chatbot/
```

Likely endpoint usage:
```text
/api/chatbot/answer/
```

The backend expects a POST request with a `query` field and returns the answer as JSON.

## Environment setup

### Frontend setup
From the repository root:

```bash
cd front_end
npm install
npm run dev
```

Then open:
```text
http://localhost:3000
```

### Backend setup
From the repository root:

```bash
cd backend/app
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# or .venv\Scripts\activate  # Windows
pip install django djangorestframework django-cors-headers google-generativeai langchain langchain-core sentence-transformers pillow diffusers torch python-dotenv
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

### Environment variables
Create a `.env` file in the backend environment or project root depending on your deployment. At minimum, the chatbot depends on:

```env
GOOGLE_API=your_google_gemini_api_key
```

If your frontend later needs database or Supabase configuration, also define those values in the frontend environment as necessary.

## Notes and observations

This project is clearly in an early-to-mid development stage. Some parts are polished and production-oriented, while others still look like prototypical or experimental code. Examples include:

- The frontend is visually complete and user-facing.
- The backend infrastructure is structured around AI-generated design workflows.
- Several modules look like experimental prototypes rather than fully hardened production services.
- `backend/app/main.py` uses a local `diffusers` model path and appears to be a standalone model-generation script rather than a production API route.
- `core/settings.py` contains hardcoded Django secret values and local-only CORS setup; this should be moved to environment variables before deployment.

## Recommended improvements before production

- Move all secrets and API keys to environment variables
- Add a real PostgreSQL database for production
- Replace SQLite with a managed DB in deployment
- Add endpoint-level validation and authentication for protected APIs
- Standardize backend naming conventions and fix inconsistent file names such as `embeding.py`, `retriver.py`, `save-data.py`, and `interior-exterior.py`
- Add logging, tests, and CI pipelines
- Add unit tests for form validation and API logic
- Clean up duplicate or temporary AI scripts and unused files
- Add a proper root-level dependency management setup for Python
- Document all API contracts in OpenAPI/Swagger

## Suggested next steps

1. Validate the frontend and backend separately
2. Connect the frontend to a stable API contract
3. Secure the backend with environment-driven secrets and auth
4. Replace local development assumptions with real deployment configuration
5. Expand the design recommendation engine with user preferences, styles, and saved projects

## License

This project does not currently declare a license in the repository metadata, so no explicit license is shown here.

## Conclusion

AI Architect is a strong concept project combining architecture design, AI recommendations, and a modern UX. It demonstrates a practical integration of generative design ideas with a user-friendly product frontend. With production hardening, cleaner API structure, and real deployment configuration, it could evolve into a compelling AI home design application.

---

If you want, I can also do one of these next:
- add a full root README in a more polished marketing style
- generate a production-ready `requirements.txt` for the Django backend
- create a proper `docker-compose.yml` for frontend + backend
- fix the project structure and clean up the README with installation commands tailored to this repo
