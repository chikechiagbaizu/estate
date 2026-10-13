# Odoo Technical Course: Learning Notes & Code (Odoo 19.0)

> 📚 **This is a personal learning repository, not an original product.**
> It documents my progress through the Udemy course
> **[The Complete Odoo 16/17 Technical Course: From Zero to Hero](https://www.udemy.com/course/the-complete-odoo-technical-course-2023-from-zero-to-hero)**
> by **Miracle Ayodele**.
>
> All course concepts and the app being built belong to the instructor's curriculum.
> The code here is my own, typed along with the lectures and **ported to Odoo 19.0**.
> No course videos or paid materials are included in this repo. If you want to learn
> this material properly, buy the course and support the instructor.

## Why this repo exists

I'm building a career as an Odoo developer. I already study with a project-based roadmap
(unit-tested custom modules, API integrations, deployment), and I use this Udemy course as a
**complement**:

- **Structured foundations.** A clear, section-by-section walk through the Odoo framework.
- **A second teaching voice.** A human instructor's explanations alongside my own project work.
- **The certificate.** Completion of the course earns a Udemy certificate of completion.
- **A visible learning trail.** One commit per section shows how I work, step by step.

## The twist: the course teaches 16/17, I code in 19.0

The course was recorded for Odoo 16 and 17. I follow it on **Odoo 19.0**, so I regularly hit
code that no longer works as shown on screen. Instead of quietly fixing it, I record every
difference in [`DIFFERENCES.md`](DIFFERENCES.md): what the tutor wrote, what Odoo 19 needs,
and why it changed. Debugging version drift is a real-world skill, and this log is the proof.

## How I work

| Rule | Detail |
|---|---|
| **One commit per section** | Each finished course section gets its own commit (tagged `section-XX`). |
| **Type it, don't copy it** | I code along, then break and rebuild parts without the video. |
| **Odoo 19.0 only** | Every difference from 16/17 gets logged in `DIFFERENCES.md`. |
| **Commit message format** | `section-04: add computed fields and onchange (19.0 port)` |

## Course progress

**Course:** 14 sections, 63 lectures, about 10.5 hours (course last updated 6/2024).

| # | Section | Status |
|---|---|---|
| 1 | Introduction | ✅ |
| 2 | Setting up the Odoo Development Environment & Understanding the Foundation | ✅ |
| 3 | Creating your First Odoo Application | ✅ |
| 4 | In-depth Understanding of Models and Logic | 🟨 |
| 5 | In-depth Understanding of Views | ⬜ |
| 6 | Expanding on Security: Groups, Access Rights and Record Rules | ⬜ |
| 7 | Understanding Automation, Actions and Reports | ⬜ |
| 8 | Internationalization (i18n and `.po` files) | ⬜ |
| 9 | Getting Advanced with Mixins and Useful Classes | ⬜ |
| 10 | Working with Emails and Templates | ⬜ |
| 11 | Logic and View Inheritance | ⬜ |
| 12 | Working with XML-RPC, JSON-RPC and Web Controller | ⬜ |
| 13 | Miscellaneous | ⬜ |
| 14 | Odoo Cloud Hosting for Custom Deployment | ⬜ |

Legend: ⬜ not started · 🟨 in progress · ✅ done

**Certificate of completion:** *pending (link will be added when finished)*

## Repository structure

```
.
├── README.md
├── DIFFERENCES.md        # Odoo 16/17 (course) vs Odoo 19 (mine), logged per section
└── <module_name>/        # the module built through the course, grows commit by commit
    ├── __manifest__.py
    ├── models/
    ├── views/
    ├── security/
    └── ...
```

## Running it

Requirements: Odoo 19.0, Python 3.10+ (check Odoo 19's supported versions), PostgreSQL.

```bash
# from your Odoo source directory
./odoo-bin -c odoo.conf -d course_db -i <module_name> --addons-path=<path-to-this-repo>,...
```

To see the code as it was after a given section:

```bash
git checkout section-04
```

## Related work

- [equipment_loan_tracker](https://github.com/chikechiagbaizu/equipment_loan_tracker): my own
  module with computed fields, constraints, a wizard, and row-level security.

## Credits & disclaimer

- Course, curriculum, and teaching by **Miracle Ayodele** on Udemy.
- This repository is an independent learning log. I am not affiliated with, endorsed by,
  or sponsored by the instructor or Udemy.
- Code is my own work, licensed LGPL-3, in line with Odoo module conventions.

## Author

**Chike Chiagbaizu**