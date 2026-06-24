# React Login Client Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a minimal Vite + React page in `frontend/` that logs in against the deployed FastAPI backend at `https://mykda4.onrender.com/login/` and displays the backend's response message.

**Architecture:** Single-page Vite + React app with one component (`App.jsx`) holding form state and a result message. No routing, no state library, no tests (per spec, this is a manual verification tool).

**Tech Stack:** Vite, React 18, native `fetch`.

---

### Task 1: Scaffold the Vite React project

**Files:**
- Create: `frontend/` (via Vite scaffold — generates `package.json`, `index.html`, `vite.config.js`, `src/main.jsx`, `src/App.jsx`, `src/index.css`, etc.)

- [ ] **Step 1: Scaffold with Vite's React template**

Run from the repo root:
```bash
npm create vite@latest frontend -- --template react
```

Expected: a new `frontend/` directory containing `package.json`, `index.html`, `src/main.jsx`, `src/App.jsx`, `src/App.css`, `src/index.css`, `vite.config.js`.

- [ ] **Step 2: Install dependencies**

```bash
cd frontend && npm install
```

Expected: exits 0, creates `frontend/node_modules` and `frontend/package-lock.json`.

- [ ] **Step 3: Verify the default scaffold runs**

```bash
cd frontend && npm run dev -- --port 5173
```

Expected: terminal prints a `Local: http://localhost:5173/` URL. Stop the server (Ctrl+C) once confirmed — this is just a scaffold sanity check before we write real code.

- [ ] **Step 4: Commit the scaffold**

```bash
git add frontend/package.json frontend/package-lock.json frontend/index.html frontend/vite.config.js frontend/src frontend/public frontend/.gitignore frontend/eslint.config.js
git commit -m "frontend: scaffold Vite React app"
```

(`frontend/node_modules` must NOT be committed — Vite's scaffold includes a `.gitignore` that excludes it; confirm with `git status` that `node_modules` shows as ignored, not staged.)

---

### Task 2: Replace App.jsx with the login form

**Files:**
- Modify: `frontend/src/App.jsx`

- [ ] **Step 1: Write the component**

Replace the full contents of `frontend/src/App.jsx` with:

```jsx
import { useState } from 'react'
import './App.css'

const LOGIN_URL = 'https://mykda4.onrender.com/login/'

function App() {
  const [userid, setUserid] = useState('')
  const [password, setPassword] = useState('')
  const [message, setMessage] = useState('')

  async function handleSubmit(event) {
    event.preventDefault()
    setMessage('')

    try {
      const response = await fetch(LOGIN_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ userid, password }),
      })
      const data = await response.json()
      setMessage(data.message)
    } catch (error) {
      setMessage('서버에 연결할 수 없습니다.')
    }
  }

  return (
    <div className="login-page">
      <h1>로그인</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="userid">아이디</label>
          <input
            id="userid"
            type="text"
            value={userid}
            onChange={(event) => setUserid(event.target.value)}
          />
        </div>
        <div>
          <label htmlFor="password">비밀번호</label>
          <input
            id="password"
            type="password"
            value={password}
            onChange={(event) => setPassword(event.target.value)}
          />
        </div>
        <button type="submit">로그인</button>
      </form>
      {message && <p className="login-message">{message}</p>}
    </div>
  )
}

export default App
```

- [ ] **Step 2: Simplify App.css**

Replace the full contents of `frontend/src/App.css` with:

```css
.login-page {
  max-width: 320px;
  margin: 80px auto;
  font-family: sans-serif;
  text-align: center;
}

.login-page form > div {
  margin-bottom: 12px;
  text-align: left;
}

.login-page label {
  display: block;
  margin-bottom: 4px;
}

.login-page input {
  width: 100%;
  padding: 6px;
  box-sizing: border-box;
}

.login-page button {
  width: 100%;
  padding: 8px;
}

.login-message {
  margin-top: 16px;
  font-weight: bold;
}
```

- [ ] **Step 3: Remove unused default assets**

The Vite React template ships `frontend/src/assets/react.svg` and references it nowhere after this change. Delete it:

```bash
rm -f frontend/src/assets/react.svg
```

---

### Task 3: Manual verification

**Files:** none (verification only)

- [ ] **Step 1: Start the dev server**

```bash
cd frontend && npm run dev -- --port 5173
```

Expected: `Local: http://localhost:5173/` printed.

- [ ] **Step 2: Open the page and test the success path**

Open `http://localhost:5173/` in a browser. Enter userid `user` and password `1234`, click 로그인.

Expected: page shows `로그인에 성공하셨습니다.` below the form.

- [ ] **Step 3: Test the wrong-userid path**

Enter userid `wrong` and password `1234`, click 로그인.

Expected: page shows `로그인 실패`.

- [ ] **Step 4: Test the wrong-password path**

Enter userid `user` and password `wrong`, click 로그인.

Expected: page shows `비밀번호가 다릅니다.`.

- [ ] **Step 5: Confirm no CORS errors**

Open the browser dev tools console while repeating Step 2. Expected: no CORS error logged (the backend's `allow_origins=["*"]` should permit this).

If a CORS error appears instead, stop and re-check the backend's CORS middleware (`day8_2login.py`) before continuing — do not work around it client-side.

- [ ] **Step 6: Stop the dev server**

Ctrl+C in the terminal running `npm run dev`.

---

### Task 4: Commit the implementation

**Files:**
- Modify: `frontend/src/App.jsx`, `frontend/src/App.css`
- Delete: `frontend/src/assets/react.svg`

- [ ] **Step 1: Commit**

```bash
git add frontend/src/App.jsx frontend/src/App.css
git rm --cached frontend/src/assets/react.svg 2>/dev/null
git add -u frontend/src/assets
git commit -m "frontend: build login form against deployed backend"
```
