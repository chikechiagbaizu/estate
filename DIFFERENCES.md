# Odoo 16/17 (Course) vs Odoo 19.0 (Mine)

A running log of everything that differed between what the instructor shows (Odoo 16/17)
and what I had to do in Odoo 19.0. Updated as I finish each section.

**How to read an entry:** what the course does → what Odoo 19 needs → why it matters.

> ⚠️ Entries marked **(verify)** are things I expect to hit based on Odoo's version
> history. I confirm each one against the Odoo 19 source/docs when I reach that section,
> then remove the marker.

## Known changes (to confirm as I go)

| Area | Course (16/17) | Odoo 19.0 | Section | Status |
|---|---|---|---|---|
| View modifiers | `attrs="{'invisible': [('state','=','done')]}"` (16); direct attributes (17) | Direct attributes only: `invisible="state == 'done'"` | 4, 5 | (verify) |
| List view tag | `<tree>` | `<list>` | 3, 5 | (verify) |
| SQL constraints | `_sql_constraints = [(...)]` | `models.Constraint(...)` class attributes | 4 | (verify) |
| Client actions / JS | Legacy widgets (16) / early OWL (17) | OWL components | 7 | (verify) |

## Log by section

### Section 1: Introduction
*No code differences.*

### Section 2: Environment setup

This course uses **Docker Compose** to run Odoo 19 and PostgreSQL 15 in separate containers.

- **Odoo:** `odoo:19.0`
- **Database:** `postgres:15-alpine`
- **Python:** Bundled with the Odoo Docker image.
- **Access URL:** `http://localhost:8070`
- **Configuration:** `odoo.conf`, mounted into the Odoo container.
- **Custom addons:** `./custom_addons` mounted at `/mnt/extra-addons`.
- **Persistent storage:** Docker named volumes for database and Odoo data.
- **Development settings:** `--dev=all` and `--workers=0`.

**Comparison with native installation:** In a native setup, Odoo, its Python dependencies, and PostgreSQL are installed and managed directly on the host operating system. In this course, Docker containers provide the application and database environments, reducing host-level installation and dependency-management requirements. Odoo connects to PostgreSQL through the Docker Compose service hostname `web-db`.

### Section 3: First Odoo application
*(to fill in)*