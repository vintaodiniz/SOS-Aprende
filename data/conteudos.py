"""Conteúdo educativo geral de primeiros socorros.

As orientações são introdutórias e não substituem treinamento prático,
avaliação profissional ou instruções do atendente de emergência.
"""

CONTEUDOS = {
    "Engasgos": {
        "explicacao": (
            "O engasgo acontece quando um objeto ou alimento bloqueia "
            "parcialmente ou totalmente a passagem de ar. A obstrução grave "
            "pode impedir a fala, a tosse eficaz e a respiração."
        ),
        "sinais": [
            "Dificuldade para respirar, falar ou tossir; tosse fraca ou ausente.",
            "Levar as mãos ao pescoço, agitação ou mudança de cor dos lábios.",
            "A pessoa ainda consegue tossir ou falar? A obstrução pode ser parcial.",
        ],
        "como_agir": [
            "Pergunte se a pessoa está engasgada e incentive-a a tossir se ainda conseguir tossir com força ou falar.",
            "Se a obstrução parecer grave, peça para alguém ligar para o SAMU (192) e siga as instruções do atendente.",
            "Em adultos e crianças maiores com obstrução grave, aplique apenas as manobras para as quais recebeu treinamento; siga a orientação do atendente.",
            "Se a pessoa perder a consciência, apoie-a no chão com cuidado, acione o 192 e inicie RCP somente se souber ou conforme orientação do atendente.",
        ],
        "nao_fazer": [
            "Não introduza os dedos às cegas na boca.",
            "Não ofereça água ou alimento durante o engasgo.",
            "Não aplique manobras abdominais em bebês; as técnicas variam por idade e situação.",
            "Não deixe a pessoa sozinha se a dificuldade respiratória persistir.",
        ],
        "emergencia": (
            "Acione o SAMU (192) imediatamente se a pessoa não conseguir respirar, "
            "falar ou tossir eficazmente, ficar arroxeada, desmaiar ou piorar. "
            "Em bebês, gestantes e pessoas com necessidades específicas, siga "
            "instruções profissionais, pois a abordagem pode ser diferente."
        ),
    },
    "Queimaduras": {
        "explicacao": (
            "Queimaduras podem ser causadas por calor, líquidos quentes, "
            "eletricidade, produtos químicos ou sol. A gravidade depende da "
            "profundidade, extensão, localização e causa."
        ),
        "sinais": [
            "Vermelhidão, dor, inchaço ou bolhas.",
            "Pele branca, escura, carbonizada ou com sensibilidade alterada pode indicar lesão grave.",
            "Queimadura elétrica ou química pode causar danos que não são imediatamente visíveis.",
        ],
        "como_agir": [
            "Afaste a pessoa da fonte de calor somente se isso puder ser feito com segurança.",
            "Resfrie a área com água corrente fresca, sem gelo, por cerca de 20 minutos quando possível.",
            "Retire adornos próximos à área antes que inche, desde que não estejam presos à pele.",
            "Depois de resfriar, cubra sem apertar com material limpo e não aderente.",
            "Em queimadura química, evite contato com o produto e siga a orientação do serviço de emergência ou centro de informação toxicológica.",
        ],
        "nao_fazer": [
            "Não use gelo, manteiga, pasta de dente, pomadas ou receitas caseiras.",
            "Não estoure bolhas nem puxe roupas ou objetos grudados na pele.",
            "Não toque em vítima de choque elétrico até ter certeza de que a energia foi desligada.",
        ],
        "emergencia": (
            "Ligue para o SAMU (192) ou Bombeiros (193) se a queimadura for extensa "
            "ou profunda, atingir face, mãos, pés, genitais ou articulações, tiver "
            "origem elétrica/química, houver inalação de fumaça ou sinais de choque. "
            "Em caso de dúvida, procure avaliação profissional."
        ),
    },
    "Convulsões": {
        "explicacao": (
            "Uma convulsão pode causar movimentos involuntários, alteração da "
            "consciência ou olhar fixo. A maioria termina por si, mas a pessoa "
            "pode precisar de proteção e avaliação."
        ),
        "sinais": [
            "Queda ou perda de consciência, enrijecimento e movimentos repetidos.",
            "Olhar parado, confusão ou sonolência após o episódio.",
            "Nem toda convulsão tem movimentos fortes; observe a pessoa e o tempo.",
        ],
        "como_agir": [
            "Mantenha a calma, marque o tempo e afaste objetos que possam machucar.",
            "Proteja a cabeça com algo macio e afrouxe peças apertadas ao redor do pescoço.",
            "Quando os movimentos terminarem, verifique a respiração; se estiver respirando, coloque-a de lado se for seguro e permaneça junto.",
            "Se não respirar normalmente após a crise, chame o SAMU (192) e siga as instruções do atendente.",
        ],
        "nao_fazer": [
            "Não contenha os movimentos nem tente imobilizar a pessoa.",
            "Não coloque dedos, objetos, alimentos ou líquidos na boca.",
            "Não tente acordá-la com tapas ou jogar água.",
        ],
        "emergencia": (
            "Ligue para o SAMU (192) se a crise durar 5 minutos ou mais, repetir "
            "sem recuperação, for a primeira crise conhecida, ocorrer na água, "
            "houver ferimento, gravidez, dificuldade para respirar ou a pessoa "
            "não recuperar o estado habitual."
        ),
    },
    "Desmaios": {
        "explicacao": (
            "Desmaio é uma perda breve da consciência, muitas vezes relacionada "
            "à redução temporária do fluxo de sangue ao cérebro. Pode haver "
            "causas que exigem avaliação médica."
        ),
        "sinais": [
            "Tontura, fraqueza, suor frio, palidez ou visão turva antes da queda.",
            "Perda breve da consciência e recuperação espontânea.",
            "Observe a respiração, a duração e possíveis ferimentos da queda.",
        ],
        "como_agir": [
            "Ajude a pessoa a deitar de costas em local seguro e afrouxe roupas apertadas.",
            "Se não houver suspeita de lesão e a pessoa estiver respirando, elevar as pernas pode ajudar enquanto ela se recupera.",
            "Verifique se responde e respira normalmente; se não respirar normalmente, chame o SAMU (192) e siga a orientação para RCP.",
            "Quando recuperar a consciência, deixe-a repousar e não a levante rapidamente.",
        ],
        "nao_fazer": [
            "Não dê comida, bebida ou medicamentos enquanto a pessoa estiver inconsciente ou confusa.",
            "Não a deixe sozinha nem a faça levantar de imediato.",
            "Não coloque nada na boca nem use estímulos dolorosos para despertá-la.",
        ],
        "emergencia": (
            "Acione o SAMU (192) se a pessoa não acordar rapidamente, não respirar "
            "normalmente, tiver dor no peito, dificuldade para falar ou mover um "
            "lado do corpo, convulsão, ferimento importante, desmaio durante esforço "
            "ou episódios repetidos."
        ),
    },
    "Sangramentos": {
        "explicacao": (
            "Sangramentos podem ser externos, quando o sangue é visível, ou "
            "internos, quando há lesão sem sangramento aparente. Perda intensa "
            "de sangue é uma emergência."
        ),
        "sinais": [
            "Sangue saindo de um corte ou ferida, em pequena ou grande quantidade.",
            "Palidez, pele fria, fraqueza, confusão ou desmaio podem sugerir perda importante de sangue.",
            "Dor, inchaço ou hematomas após trauma podem exigir avaliação mesmo sem sangue visível.",
        ],
        "como_agir": [
            "Proteja-se do contato com sangue usando luvas ou uma barreira limpa, se disponível.",
            "Faça pressão firme e contínua sobre a ferida com gaze ou pano limpo.",
            "Se o material encharcar, coloque outro por cima sem retirar o primeiro.",
            "Para sangramento intenso, peça ajuda e ligue para o SAMU (192); mantenha a pessoa aquecida e acompanhe sua respiração.",
            "Se houver objeto encravado, pressione ao redor, sem pressionar o objeto.",
        ],
        "nao_fazer": [
            "Não retire objetos encravados nem explore a ferida.",
            "Não remova a primeira compressa encharcada; acrescente outra sobre ela.",
            "Não aplique torniquete, a menos que tenha treinamento e siga orientação adequada.",
        ],
        "emergencia": (
            "Ligue para o SAMU (192) diante de sangramento volumoso, que não cessa "
            "com pressão direta, ferida profunda, amputação, suspeita de hemorragia "
            "interna, sinais de choque ou qualquer piora importante."
        ),
    },
    "Parada cardíaca": {
        "explicacao": (
            "A parada cardíaca é uma emergência em que o coração deixa de bombear "
            "sangue de forma eficaz. Reconhecimento rápido, chamada de emergência "
            "e RCP podem aumentar a chance de sobrevivência."
        ),
        "sinais": [
            "Pessoa inconsciente, que não responde quando chamada ou tocada.",
            "Não respira normalmente ou apresenta apenas suspiros/respiração agônica.",
            "Leigos não devem perder tempo tentando confirmar pulso.",
        ],
        "como_agir": [
            "Verifique se o local é seguro, chame a pessoa e observe se respira normalmente.",
            "Peça a alguém para ligar para o SAMU (192) e buscar um desfibrilador externo automático (DEA), se houver.",
            "Inicie compressões no centro do peito se souber como fazê-las ou siga as instruções do atendente do 192.",
            "Use o DEA assim que disponível e siga as instruções de voz do aparelho.",
            "Continue até a pessoa apresentar sinais de vida, chegar ajuda ou você não conseguir continuar.",
        ],
        "nao_fazer": [
            "Não atrase a chamada de emergência para procurar pulso ou fazer diagnóstico.",
            "Não deixe a pessoa sozinha para buscar ajuda se houver outra pessoa que possa fazer a ligação.",
            "Não interrompa compressões sem necessidade; siga o atendente e as instruções do DEA.",
        ],
        "emergencia": (
            "Acione o SAMU (192) imediatamente se a pessoa estiver inconsciente e "
            "não respirar normalmente. Coloque o telefone no viva-voz e siga "
            "exatamente as instruções do atendente."
        ),
    },
}
