# PEAT-MVP-MacQA-Tool

*Bilingual dev logs welcome
A frame-by-frame video QA and annotation tool for accessibility and localization testing (macOS MVP).

**Inspired by PEAT, built for QA/UX testers.**

## Features (MVP)
- Load any .mp4 video
- Iterate frame-by-frame
- Annotate frames (highlight, mark)
- Export annotated frames as CSV/JSON report
- Keyboard shortcuts for quick QA workflow

## Installation (macOS)
Requires Rust, C++ compiler, and basic dependencies.

```bash
# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Install C++ build tools
xcode-select --install

# Install ffmpeg for video handling
brew install ffmpeg
