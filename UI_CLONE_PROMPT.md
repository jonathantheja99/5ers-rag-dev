# AI Studio UI Clone Prompt

**Instructions for the User:** 
Copy the text below the line and paste it into Google AI Studio (or any capable agent). Ensure the agent has access to read this GitHub repository, as well as the link to the cloner template.

---

## The Prompt

**Role:** Expert Frontend Web Developer and UI/UX Designer

**Objective:**
I want you to analyze the frontend code in this repository (`frontend/` directory) and completely rewrite the UI to be a pixel-perfect clone of **Google Gemini's web interface** (https://gemini.google.com/app).

**Requirements:**
1. **Analyze Current State:** Review the existing React/Vite codebase in the `frontend/` directory to understand the current routing and state management for the RAG chat.
2. **Design Language:** Remove the existing glassmorphism theme and replace it with Gemini's clean, minimalistic, material-inspired design. 
   - Use the appropriate color palettes (dark/light mode).
   - Implement the same side-navigation bar style.
   - Clone the chat input area (the rounded pill-shaped text area with the specific icons for voice/submit).
   - Clone the message bubbles and typography (use Inter or Roboto).
3. **Reference Tooling:** To assist you in cloning the exact layout and effects, please reference the techniques and structure from this AI website cloner template: https://github.com/JCodesMore/ai-website-cloner-template
4. **Output:** Generate the updated `App.jsx`, `index.css`, and any required component files to achieve this Gemini UI clone while preserving the existing backend connection logic. Make sure it feels dynamic and responsive!
