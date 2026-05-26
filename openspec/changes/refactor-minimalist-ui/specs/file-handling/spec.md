## MODIFIED Requirements

### Requirement: Open markdown files via file dialog
The system SHALL provide `Ctrl+O` as the keyboard shortcut to open a native file dialog filtered to `.md` files, and load the selected file's content into the viewer.

#### Scenario: User opens a .md file via keyboard shortcut
- **WHEN** user presses `Ctrl+O` and selects a `.md` file
- **THEN** the file content is loaded and rendered in the viewer

#### Scenario: User cancels file dialog
- **WHEN** user opens the file dialog and clicks cancel
- **THEN** the current viewer state remains unchanged with no errors

### Requirement: Open files via command-line argument
The system SHALL accept a file path as a command-line argument and open that file on startup.

#### Scenario: Launch with valid .md file path
- **WHEN** the application is launched with a path to an existing `.md` file
- **THEN** the file is loaded and rendered immediately

#### Scenario: Launch with invalid or missing file path
- **WHEN** the application is launched with a path to a non-existent file
- **THEN** an error message is shown and the application opens with an empty viewer

### Requirement: Display app title with filename
The system SHALL display the current file's name in the window title bar and in the header bar.

#### Scenario: File opened successfully
- **WHEN** a `.md` file is opened
- **THEN** the window title shows "mdp - <filename>" and the header bar shows "<filename>"

## REMOVED Requirements

### Requirement: File menu
**Reason**: Menu bar removed in favor of keyboard shortcuts for a cleaner UI.
**Migration**: Use `Ctrl+O` to open files and `Alt+F4` or `Esc` to close.
