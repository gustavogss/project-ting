def create_data(word, file_name, result):
    return {
        "palavra": word,
        "arquivo": file_name,
        "ocorrencias": result,
    }


def create_result(content, line, result):
    return {"linha": line, "conteudo": content} if result else {"linha": line}


def get_result(content, word, result):
    data = []
    lines = content["linhas_do_arquivo"]

    for index in range(len(lines)):
        if word.lower() in lines[index].lower():
            data.append(create_result(lines[index], index + 1, result))

    return data


def check_word(word, instance, result=False):
    data = []

    for index in range(len(instance)):
        file_name = instance.search(index)["nome_do_arquivo"]
        result = get_result(instance.search(index), word, result)
        if result:
            data.append(create_data(word, file_name, result))

    return data


def exists_word(word, instance):
    return check_word(word, instance)


def search_by_word(word, instance):
    pass
