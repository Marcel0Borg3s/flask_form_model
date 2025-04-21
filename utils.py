def processar_dados(empresa, nome, email, data_nascimento, genero):
    """
    Processa os dados recebidos do formulário.

    Args:
        empresa: Nome da empresa
        nome: Nome do usuário
        email: Email do usuário
        data_nascimento: Data de nascimento do usuário
        genero: Gênero do usuário

    Returns:
        str: Mensagem de confirmação do processamento
    """
    print("==> Recebido no utils.py")
    print(f"Empresa: {empresa}")
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"Data de nascimento: {data_nascimento}")
    print(f"Gênero: {genero}")
    # Aqui você pode salvar, validar, ou transformar os dados
    return f"Dados de {nome} processados com sucesso."
