# React Login Client — Design

## Purpose
Provide a minimal React front end that exercises the deployed FastAPI login
endpoint at `https://mykda4.onrender.com/login/`, so the backend can be
verified end-to-end from a browser.

## Backend contract (existing, not modified by this work)
- `POST /login/` on `https://mykda4.onrender.com`
- Request body: `{"userid": string, "password": string}`
- Response: always HTTP 200 with `{"message": string}`
  - Success message: `"로그인에 성공하셨습니다."`
  - Failure messages: `"로그인 실패"` (wrong userid) or
    `"비밀번호가 다릅니다."` (wrong password)
- No HTTP error status codes are used to signal failure — the caller must
  branch on the `message` text/success case, not on response status.

## Scope
- New `frontend/` folder in this repo (`c:\myenv\kda4\frontend`), separate
  from the Python backend code.
- Vite + React, single page, single component (`App.jsx`).
- No routing, no state management library, no persisted session — this is a
  throwaway verification client, not a production auth flow.

## Components
- `App.jsx`: holds `userid`, `password`, and `message` state. Renders a form
  (two inputs + submit button) and the current `message` (if any).

## Data flow
1. User fills in `userid` / `password` and submits the form.
2. `onSubmit` calls
   `fetch('https://mykda4.onrender.com/login/', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({ userid, password }) })`.
3. On a successful HTTP response, parse JSON and set `message` to
   `data.message`. The same field is used whether the login succeeded or
   failed — the backend's text is shown verbatim.
4. If `fetch` itself rejects (network failure, CORS block, server down),
   catch it and set `message` to a fixed client-side string:
   `"서버에 연결할 수 없습니다."`

## Error handling
- Backend-reported failures (wrong id/password) are not exceptions in this
  design — they're normal 200 responses with a failure message, displayed
  the same way as a success message.
- Only transport-level failures (network/CORS) get a distinct, hardcoded
  message, since there's no `message` field to read in that case.

## Out of scope
- No environment-based API URL switching (local vs prod) — the Render URL
  is hardcoded since this client's only purpose is to hit the deployed
  backend.
- No styling system beyond inline/minimal CSS.
- No tests — this is a manual verification tool for a learning exercise.
