# Tsukuyomi

Manga crawler bot from various sites. WIP. Written in Flask.

This is probably my first project with Python. I would like to try my luck with one of my ambitous hobby.

In its core, Tsukuyomi is a plain crawler. It crawls data from various manga hosting sites such as `Mangafox`, `Mangareader` and combine them into the internal MySQL db.

Following sections show typical data schemes that I'm planning to build:

## Models

### Manga

- Title
- Authors
- Genres
- Description
- Artworks
- Source
- Chapters
- Updated

### Chapters

- Title
- Number
- Upload Date
