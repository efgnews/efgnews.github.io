---
name: add-article
description: "Add a new digitalized newspaper article to the efgnews Hugo site. Use when: adding an article, creating a new post, digitalizing a newspaper article, new article from newspaper."
argument-hint: "Optional: paste the article title and/or metadata to get started"
---

# Add New Article

## When to Use
When digitizing a newspaper article and adding it to the Hugo site as a new post.

## Information to Collect
Gather from the user (in any order, all optional except date and title):

| Field | Notes |
|-------|-------|
| **Date** | Publication date from the newspaper (YYYY-MM-DD) |
| **Title** | Bulgarian title — used verbatim in front matter; slugified for filename |
| **Description** | Subtitle or deck line under the headline (optional) |
| **Author** | Journalist's name in Bulgarian (optional) |
| **Source** | Newspaper, issue number, page(s) — e.g. `168 часа, бр. 23/1994, стр. 20` |
| **Tags** | Bulgarian keywords (optional, can suggest from content) |
| **Body text** | Full article body (optional — use placeholder if not yet available) |
| **Cover image** | Whether a scan/photo exists and the caption (optional) |

If the user doesn't have some fields yet, use the placeholders defined below and move on.

## Step 1 — Derive the Filename

Format: `YYYY-MM-DD-<slug>.md`

Run [slugify.py](./scripts/slugify.py) to transliterate the Bulgarian title to a slug:

```bash
python3 .github/skills/add-article/scripts/slugify.py "YYYY-MM-DD" "Българско заглавие"
# prints: YYYY-MM-DD-balgarsko-zaglavie
```

The script handles all transliteration rules: spaces → `-`, punctuation and Bulgarian quotes (`„"`) dropped, lowercase output.

## Step 2 — Optional Issue Lookup (No Script)

If you keep a mapping text file with lines like:

- `бр. 8 21.02.1994`
- `Бр. 9 28.02.1995`

you can prefill the issue number before creating the article file.

Use this reference format: [issue-by-date-format.md](./references/issue-by-date-format.md)

Lookup rules:
- Find the line whose date (`DD.MM.YYYY`) matches the article date (`YYYY-MM-DD`).
- If found, use that issue number in the source line: `168 часа, бр. <issue>/<YYYY>, стр. ???`
- If not found, keep placeholder: `168 часа, бр. ???/<YYYY>, стр. ???`

## Step 3 — Create the File

Create `content/posts/<filename>.md` with this template:

```markdown
---
title: <Bulgarian title>
description: <description or empty>
author: 
  - <Author name or empty>
  - 168 часа, бр. ???/<YYYY>, стр. ???
date: YYYY-MM-DD
tags: []
cover:
  image: ./images/<filename-without-extension>/cover.webp
  caption: ""
  hiddenInSingle: false
---

„“
```

**Placeholder rules:**
- `description`: leave value empty (no value after the colon)
- `author` name: leave the list item empty (`- `)
- Issue number and page: use `???` as placeholder, fill in `<YYYY>` from the article date (or prefill issue from Step 2)
- `tags`: use `[]` (empty array)
- `caption`: use `""` (empty string)
- Body text: use `„“` as the placeholder (a pair of Bulgarian quotation marks)

## Step 4 — Fill in Known Fields

Replace placeholders with actual values as the user provides them:
- `description`: one-line subtitle from the article
- Author name: journalist's name in Bulgarian
- Issue/page: replace `???` with actual numbers (issue can already be prefilled from Step 2)
- Tags: Bulgarian keywords in single quotes, comma-separated: `['tag1', 'tag2']`
- Body: replace `„“` with the full article text
- Caption: text under the cover image, e.g. `"Снимка: Архив „168 часа""`

## Step 5 — Body Text Formatting

Use Bulgarian blockquote syntax for section headers inside the article:
```markdown
> **Заглавие на раздела**
```

Footnotes use standard Markdown syntax:
```markdown
Text with footnote.[^1]

[^1]: *Footnote text here.*
```

## Notes
- Source line always references `168 часа` newspaper
- Cover image path always follows the pattern `./images/<slug>/cover.webp` where `<slug>` matches the filename without date and `.md`
- `hiddenInSingle: false` is always set on the cover block
- Tags are in Bulgarian, in single quotes inside a YAML array
