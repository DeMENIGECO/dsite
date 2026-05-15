# dsite/shortcuts.py

from .response import Response
from .templates import render_template


def render(request, template_name, context=None):
    """
    Renderizza una pagina DSite (XML o HTML) con contesto.
    """

    if context is None:
        context = {}

    content = render_template(template_name, context)

    return Response(content)


def redirect(url):
    """
    Restituisce una risposta di redirect.
    """

    return Response(
        "",
        status=302,
        headers={
            "Location": url
        }
    )


def HttpResponse(text, status=200, content_type="text/html"):
    """
    Risposta HTTP semplice.
    """

    return Response(
        text,
        status=status,
        headers={
            "Content-Type": content_type
        }
    )
