from ting_file_management.file_management import txt_importer
import sys


def is_file_exists(path_file, instance):
    for index in range(len(instance)):
        return instance.search(index)["nome_do_arquivo"] == path_file


def process(path_file, instance):
    content = txt_importer(path_file)    

    if not is_file_exists(path_file, instance):
        data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(content),
            "linhas_do_arquivo": content,
        }

        instance.enqueue(data)
        sys.stdout.write(str(data))


def remove(instance):
    try:
        
        path_file = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")

    except IndexError:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    try:
        sys.stdout.write(str(instance.search(position)))
    except IndexError:
        sys.stderr.write("Posição inválida\n")