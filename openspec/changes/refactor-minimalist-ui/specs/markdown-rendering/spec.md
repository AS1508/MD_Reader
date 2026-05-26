## MODIFIED Requirements

### Requirement: Render basic markdown formatting
The system SHALL parse markdown text and render it with visual formatting for headings (h1-h6), bold, italic, inline code, code blocks, unordered lists, ordered lists, links, and images using a minimalist light stylesheet.

#### Scenario: Render all basic formatting elements
- **WHEN** a markdown file containing headings, bold, italic, code, lists, links, and images is opened
- **THEN** each element is displayed with distinct but understated visual formatting using a clean light theme

#### Scenario: Render empty file
- **WHEN** an empty markdown file is opened
- **THEN** the viewer shows a blank area with no errors

### Requirement: Parse markdown to HTML
The system SHALL convert markdown text to HTML using a standard markdown parser before displaying it.

#### Scenario: Convert valid markdown
- **WHEN** valid markdown text is provided
- **THEN** the system produces corresponding HTML output

#### Scenario: Handle malformed markdown
- **WHEN** markdown text contains syntax errors or unusual formatting
- **THEN** the system renders a best-effort output without crashing or showing raw HTML tags
