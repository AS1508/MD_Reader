## ADDED Requirements

### Requirement: Display filename in minimal header
The system SHALL show a thin header bar at the top of the window displaying the current file's basename.

#### Scenario: File opened shows name in header
- **WHEN** a `.md` file is opened
- **THEN** the header bar displays the file's basename (e.g., `readme.md`)

#### Scenario: No file loaded shows placeholder
- **WHEN** no file has been opened
- **THEN** the header bar shows a subtle hint text (e.g., "No file open")

### Requirement: Header blends into window
The header SHALL use the same background color as the content area and be visually minimal with no distinct border or shadow.

#### Scenario: Header appearance
- **WHEN** the application is running
- **THEN** the header bar has no bottom border, no shadow, and matches the content background color
