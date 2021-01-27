#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django1.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

"""
python manage.py                    ---->  Mostra lista de comandos do Django manage
      ...        runserver          ---->  Inicia o servidor
      ...        createsuperuser    ---->  Cria um super-usuário
      ...        makemigrations     ---->  Atualiza os arquivos de migration das aplicações
      ...        migrate            ---->  Roda o arquivo de migration
      ...        help xxxxxxxxx     ---->  Exibe ajuda em um subcomando específico
"""

