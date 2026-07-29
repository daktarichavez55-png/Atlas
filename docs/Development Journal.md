# Project Atlas Development Journal

---

## Sprint 1 - Genesis

**Version:** v0.0.1

### Completed
- Installed Python.
- Installed Git.
- Installed VS Code.
- Created a GitHub account.
- Created the Atlas repository.
- Built the first desktop application.
- Made the first commit.
- Pushed Atlas to GitHub.

### Lessons Learned
- How to run a Python application.
- Basic Git workflow (add, commit, push).
- Project setup.

---

## Sprint 2 - Foundation

**Version:** v0.0.2

### Completed
- Created the `src`, `docs`, `assets`, and `ui` folders.
- Built the sidebar.
- Added the Home screen.
- Added the status bar.
- Improved the application layout.
- Pushed the second version to GitHub.

### Lessons Learned
- Organizing a software project.
- Why splitting code into multiple files is important.
- How software grows one feature at a time.

### Next Goal
Build Atlas's first interactive chat interface.
---

## Sprint 3 - Interaction

**Version:** v0.0.3

### Completed
- Added the AI Chat interface.
- Added a text input field.
- Added a Send button.
- Implemented the first `send_message()` function.
- Atlas now responds to user input.
- Added a welcome message when Atlas starts.

### Lessons Learned
- Event-driven programming.
- Functions (`send_message()`).
- The difference between layout and behavior.
- Thinking about user experience (UX).

### Next Goal
Make the sidebar buttons switch between pages.
---

## Sprint 4 - Navigation (Milestone 1)

**Version:** v0.0.4 (In Progress)

### Objective
Refactor Atlas into a multi-page desktop application.

### Completed
- Split the Home page into `home.py`.
- Split the AI Chat page into `chat.py`.
- Imported page modules into `main.py`.
- Refactored `main.py` to focus on application setup.
- Implemented navigation between Home and AI Chat.
- Preserved a single content area while switching pages.

### Lessons Learned
- Modular programming.
- Importing functions from other Python modules.
- Refactoring code without changing functionality.
- Separation of concerns.
- Debugging architecture changes.

### Next Goal
Implement PDF Tools, Linux, and Settings pages.
---

## Sprint 4 - Completed

**Version:** v0.0.4

### Objective
Transform Atlas from a single-page interface into a modular multi-page desktop application.

### Completed
- Implemented sidebar navigation.
- Added Home page.
- Added AI Chat page.
- Added PDF Tools page.
- Added Linux Assistant page.
- Added Settings page.
- Refactored the project into reusable UI modules.

### Lessons Learned
- Modular programming
- Python imports
- Refactoring
- Navigation between pages
- Organizing a growing codebase

### Result
Atlas now supports multiple pages and is ready for feature expansion.
---

## Sprint 4.1 - User Interface Polish

**Version:** v0.0.4

### Improvements
- Added dynamic status bar updates.
- Status now reflects the active page.
- Improved application feedback during navigation.

### Result
Atlas now behaves more like a professional desktop application by providing clear navigation feedback.
---

## Sprint 5 - Milestones 1-3

**Version:** v0.0.5 (In Progress)

### Completed
- Created the `core` package.
- Added `chat_engine.py`.
- Added `commands.py`.
- Added `utils.py`.
- Separated UI from application logic.
- Implemented command recognition.
- Added `/help`.
- Added `/about`.
- Added unknown command handling.

### Lessons Learned
- Separation of concerns.
- Creating reusable modules.
- Command routing.
- Importing across project packages.

### Next Goal
Implement a functional `/clear` command and continue expanding Atlas's capabilities.
---

## Sprint 5 - Milestone 4

### Completed
- Added reusable welcome screen function.
- Implemented a working `/clear` command.
- Improved interaction between the chat interface and the command engine.

### Lessons Learned
- Reusable functions
- Updating UI state
- Command-driven behavior

### Result
Atlas can now execute commands that modify the application, not just return text.SS
---

## Sprint 5 - Milestone 5

### Completed
- Added Enter key support for sending messages.
- Automatically focused the cursor on the input field.
- Improved the overall chat experience.

### Result
Atlas now behaves more like a modern desktop chat application.
## Sprint 6 – Milestone 1
Created linux_database.py to separate Linux command knowledge from the UI.
Stored Linux commands in a reusable dictionary.

## Sprint 6 – Milestone 2
Imported linux_commands into the Linux Assistant page.
Connected the UI to Atlas's Linux knowledge base.

## Sprint 6 – Milestone 3 (UI)
Replaced the placeholder page with a functional interface.
Added:
- Output panel
- Command input field
- Search button

The Linux Assistant is now ready to process commands in the next milestone.
## Sprint 6 - Completed

Implemented Atlas Linux Assistant.

Features:
- Created a reusable Linux command database.
- Connected the Linux UI to the database.
- Built a searchable Linux command interface.
- Added keyboard support (Enter key).
- Implemented graceful handling of unknown commands.
- Improved output formatting for readability.

Atlas now contains its first fully functional standalone utility.
## Sprint 6 – PDF Engine Foundation

Date: 2026-07-29

Achievements:
- Investigated pypdf 6.14.2 API changes.
- Replaced the deprecated PdfMerger approach with PdfWriter and PdfReader.
- Created src/tools/pdf_tools.py.
- Implemented merge_pdfs().
- Successfully merged two PDF files into merged_test.pdf.
- Diagnosed and fixed an EmptyFileError caused by empty test PDFs.

Lessons Learned:
- Library APIs evolve, so documentation and version checks are important.
- Successful imports don't produce output.
- Test with valid input files before assuming the code is wrong.

Status:
✅ First working backend feature completed.