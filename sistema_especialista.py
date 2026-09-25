def realizar_avaliacao():
    pontos = {
        "Tank": 0,
        "Healer": 0,
        "DPS": 0
    }

    perguntas = [
        {
            "texto": "Em um combate contra um chefe, qual seria a parte mais frustrante/difícil de lidar para você?",
            "opcoes": {
                "A": ("Ter que parar minhas ações para me reposicionar.", {"DPS": 2, "Tank": 1}),
                "B": ("Quando o chefe cria inimigos menores na arena.", {"DPS": 2, "Tank": 1}),
                "C": ("Quando um ataque mira em todos do grupo.", {"Healer": 2, "DPS": 1}),
                "D": ("Quando o chefe precisa ser derrotado antes de usar uma habilidade poderosa.", {"DPS": 3}),
                "E": ("Quando o chefe separa os integrantes do time.", {"Tank": 2, "Healer": 1, "DPS": 1})
            }
        },

        {
            "texto": "Durante uma luta, algo sai diferente do que você esperava. Qual situação seria mais interessante para você lidar?",
            "opcoes": {
                "A": ("O chefe muda de posição e você precisa adaptar onde está para continuar contribuindo.", {"DPS": 2, "Tank": 1}),
                "B": ("Um aliado comete um erro e a situação começa a sair do controle.", {"Healer": 2, "Tank": 1}),
                "C": ("O chefe começa a executar uma mecânica que ninguém do grupo esperava.", {"Tank": 2, "Healer": 1, "DPS": 1}),
                "D": ("Uma parte da arena deixa de ser segura e você precisa encontrar rapidamente uma nova posição.", {"DPS": 2, "Healer": 2, "Tank": 1})
            }
        },

        {
            "texto": "Durante uma luta, o grupo está tendo dificuldade. Qual situação você teria mais vontade de tentar resolver?",
            "opcoes": {
                "A": ("Descobrir por que o grupo está perdendo vida demais.", {"Healer": 3, "Tank": 1}),
                "B": ("Descobrir como organizar melhor a posição do chefe.", {"Tank": 3, "DPS": 1}),
                "C": ("Descobrir uma forma de eliminar rapidamente os inimigos que estão atrapalhando.", {"DPS": 3, "Tank": 1}),
                "D": ("Descobrir o que está fazendo o grupo perder tempo durante as mecânicas.", {"DPS": 2, "Tank": 1, "Healer": 1})
            }
        },

        {
            "texto": "Em uma situação inesperada, qual consequência você consideraria mais importante evitar?",
            "opcoes": {
                "A": ("Um aliado ficar sem suporte no momento em que mais precisa.", {"Healer": 3, "Tank": 1}),
                "B": ("O chefe ficar em uma posição ruim e prejudicar a movimentação do grupo.", {"Tank": 3, "DPS": 1}),
                "C": ("O grupo não conseguir causar dano suficiente antes que a situação fique perigosa.", {"DPS": 3, "Tank": 1}),
                "D": ("O grupo perder a organização e cada pessoa começar a agir por conta própria.", {"Tank": 2, "Healer": 2, "DPS": 1})
            }
        },

        {
            "texto": "Imagine que uma luta esteja demorando mais do que o esperado. Qual situação chamaria mais sua atenção?",
            "opcoes": {
                "A": ("O grupo está recebendo dano aos poucos e acumulando problemas ao longo do tempo.", {"Healer": 2, "Tank": 2}),
                "B": ("O chefe está se movimentando de forma que dificulta a execução do grupo.", {"Tank": 3, "DPS": 1}),
                "C": ("Os inimigos estão sobrevivendo por tempo demais e aumentando a pressão sobre o grupo.", {"DPS": 3, "Tank": 1}),
                "D": ("O grupo está executando as mecânicas corretamente, mas ainda assim o combate parece pouco eficiente.", {"DPS": 2, "Healer": 1, "Tank": 1})
            }
        },

        {
            "texto": "Uma pequena decisão sua pode afetar diretamente o restante da equipe. Qual situação seria mais interessante?",
            "opcoes": {
                "A": ("Decidir quando agir para evitar que um aliado fique em uma situação perigosa.", {"Healer": 3, "Tank": 1}),
                "B": ("Decidir onde posicionar o inimigo para tornar a próxima etapa mais segura.", {"Tank": 3, "Healer": 1}),
                "C": ("Decidir quando arriscar uma ação para conseguir terminar uma etapa mais rapidamente.", {"DPS": 3, "Tank": 1}),
                "D": ("Decidir entre continuar executando o plano ou adaptar sua ação ao que está acontecendo.", {"DPS": 2, "Tank": 1, "Healer": 1})
            }
        },

        {
            "texto": "O grupo acabou de cometer um erro e a situação ainda pode ser recuperada. O que você teria mais interesse em resolver?",
            "opcoes": {
                "A": ("Recuperar os integrantes que ficaram em uma situação perigosa.", {"Healer": 3, "Tank": 1}),
                "B": ("Fazer o inimigo voltar para uma posição controlável.", {"Tank": 3, "Healer": 1}),
                "C": ("Eliminar rapidamente a ameaça antes que ela piore.", {"DPS": 3, "Tank": 1}),
                "D": ("Adaptar sua estratégia para continuar o combate mesmo com o erro cometido.", {"DPS": 2, "Tank": 1, "Healer": 1})
            }
        },

        {
            "texto": "Em uma luta com várias coisas acontecendo ao mesmo tempo, qual situação exigiria mais da sua atenção?",
            "opcoes": {
                "A": ("Acompanhar constantemente o estado dos integrantes do grupo.", {"Healer": 3, "Tank": 1}),
                "B": ("Acompanhar a posição do inimigo e seu comportamento.", {"Tank": 3, "DPS": 1}),
                "C": ("Acompanhar suas oportunidades para causar o máximo de impacto.", {"DPS": 3, "Healer": 1}),
                "D": ("Acompanhar o ambiente e reagir rapidamente às mudanças.", {"DPS": 2, "Tank": 1, "Healer": 1})
            }
        },

        {
            "texto": "Imagine que você já conhece bem uma luta, mas uma atualização altera alguns de seus elementos. Qual mudança teria mais curiosidade de descobrir como lidar?",
            "opcoes": {
                "A": ("Os momentos em que o grupo precisa ser recuperado mudaram de lugar.", {"Healer": 3, "Tank": 1}),
                "B": ("O comportamento ou posicionamento do inimigo mudou.", {"Tank": 3, "DPS": 1}),
                "C": ("Os momentos de maior oportunidade para causar dano mudaram.", {"DPS": 3, "Tank": 1}),
                "D": ("A ordem das situações mudou e você precisa reaprender quando adaptar suas ações.", {"DPS": 2, "Healer": 1, "Tank": 1})
            }
        },

        {
            "texto": "Depois de uma luta difícil, qual aspecto faria você sentir que teve uma participação importante?",
            "opcoes": {
                "A": ("Manter o grupo funcionando mesmo quando as coisas deram errado.", {"Healer": 3, "Tank": 1}),
                "B": ("Manter a situação sob controle mesmo sob pressão.", {"Tank": 3, "Healer": 1}),
                "C": ("Aproveitar as oportunidades certas e contribuir decisivamente para derrotar o inimigo.", {"DPS": 3, "Tank": 1}),
                "D": ("Adaptar-se às situações e continuar contribuindo mesmo quando o plano mudou.", {"DPS": 2, "Tank": 1, "Healer": 1})
            }
        }
    ]

    for numero, pergunta in enumerate(perguntas, 1):
        print(f"\n--- PERGUNTA {numero} ---")
        print(pergunta["texto"])

        for letra, (texto, _) in pergunta["opcoes"].items():
            print(f"{letra}) {texto}")

        while True:
            resposta = input("\nResposta: ").upper()

            if resposta in pergunta["opcoes"]:
                break

            print("Resposta inválida. Escolha uma das opções disponíveis.")

        _, pontuacoes = pergunta["opcoes"][resposta]

        for papel, pontos_ganhos in pontuacoes.items():
            pontos[papel] += pontos_ganhos

    maior_pontuacao = max(pontos.values())
    resultado = [
        papel for papel, valor in pontos.items()
        if valor == maior_pontuacao
    ]

    print("\n==============================")
    print("       RESULTADO")
    print("==============================")

    for papel, valor in pontos.items():
        print(f"{papel}: {valor} pontos")

    if len(resultado) == 1:
        print(f"\nPapel mais compatível: {resultado[0]}")
    else:
        print("\nHouve empate entre:")
        print(", ".join(resultado))


while True:
    realizar_avaliacao()

    novamente = input("\nDeseja realizar uma nova avaliação? (S/N): ").upper()

    if novamente != "S":
        print("\nObrigado por utilizar o sistema!")
        break