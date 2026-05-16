# dsite/cli.py

import sys
from pathlib import Path


VERSION = "1.0.0"


# =========================================
# CREATE PROJECT
# =========================================

def create_project(project_name):

    root = Path(project_name)

    if root.exists():

        print(
            f"[DSite] Errore: "
            f"la cartella '{project_name}' esiste già."
        )

        return

    # ---------------------------------
    # ROOT
    # ---------------------------------

    root.mkdir()

    # ---------------------------------
    # MANAGE.PY
    # ---------------------------------

    manage_py = f'''import sys

from dsite.management.runserver import runserver
from dsite.management.migrations import (
    makemigrations,
    migrate
)
from dsite.management.adminsite import adminsite


def main():

    if len(sys.argv) < 2:

        print("DSite manage.py")
        return

    command = sys.argv[1]

    if command == "runserver":
        runserver("{project_name}")

    elif command == "makemigrations":
        makemigrations("{project_name}")

    elif command == "migrate":
        migrate("{project_name}")

    elif command == "adminsite":
        adminsite("{project_name}")

    else:
        print(f"Comando sconosciuto: {{command}}")


if __name__ == "__main__":
    main()
'''

    (root / "manage.py").write_text(
        manage_py,
        encoding="utf-8"
    )

    # ---------------------------------
    # PROJECT PACKAGE
    # ---------------------------------

    app = root / project_name

    app.mkdir()

    # __init__.py

    (app / "__init__.py").write_text(
        "",
        encoding="utf-8"
    )

    # ---------------------------------
    # URLS
    # ---------------------------------

    urls_py = '''from dsite.urls import path
from . import views

urlpatterns = []
'''

    (app / "urls.py").write_text(
        urls_py,
        encoding="utf-8"
    )

    # ---------------------------------
    # VIEWS
    # ---------------------------------

    views_py = '''from dsite.shortcuts import render


# Scrivi qua le Views
'''

    (app / "views.py").write_text(
        views_py,
        encoding="utf-8"
    )

    # ---------------------------------
    # MODELS
    # ---------------------------------

    models_py = '''from dsite.db import Model
from dsite.db import TextColumn


# Scrivi qui i tuoi modelli
'''

    (app / "models.py").write_text(
        models_py,
        encoding="utf-8"
    )

    # ---------------------------------
    # FORMS
    # ---------------------------------

    forms_py = '''from dsite.forms import Form
from dsite.forms import TextField


# Scrivi qua i Forms.
'''

    (app / "forms.py").write_text(
        forms_py,
        encoding="utf-8"
    )

    # ---------------------------------
    # ADMINSITE
    # ---------------------------------

    adminsite_py = '''from dsite.admin import register


# regsitra i modelli qui.
'''

    (app / "adminsite.py").write_text(
        adminsite_py,
        encoding="utf-8"
    )

    # ---------------------------------
    # SETTINGS
    # ---------------------------------

    settings_py = f'''PROJECT_NAME = "{project_name}"
DEBUG = True #Disattivalo in produzione!
'''

    (app / "settings.py").write_text(
        settings_py,
        encoding="utf-8"
    )

    # ---------------------------------
    # PAGES
    # ---------------------------------

    pages = app / "pages"
    pages.mkdir()

    homepage_xml = f'''<!-
Per costruire la tua prima pagina, guarda:
https://demenigeco.github.io/dsite-project/it/1.0.0/docs/init
->
'''

    (pages / "homepage.xml").write_text(
        homepage_xml,
        encoding="utf-8"
    )

    base_xml = '''<!-
Per costruire il tuo primo layout base, guarda:
https://demenigeco.github.io/dsite-project/it/1.0.0/docs/init
->
'''

    (pages / "base.xml").write_text(
        base_xml,
        encoding="utf-8"
    )

    print("")
    print("[DSite] Progetto creato!")
    print(f"[DSite] Cartella: {project_name}")
    print("")


# =========================================
# MAIN CLI
# =========================================

def main():

    args = sys.argv

    # ---------------------------------
    # VERSION
    # ---------------------------------

    if "--version" in args:

        print(f"DSite {VERSION}")
        return

    # ---------------------------------
    # CREATEPROJECT
    # ---------------------------------

    if len(args) >= 3:

        command = args[1]

        if command == "createproject":

            project_name = args[2]

            create_project(project_name)

            return

    # ---------------------------------
    # HELP
    # ---------------------------------

    print("")
    print("DSite CLI")
    print("")
    print("Comandi:")
    print("")
    print("dsite --version")
    print("dsite createproject <nome>")
    print("")


if __name__ == "__main__":
    main()
