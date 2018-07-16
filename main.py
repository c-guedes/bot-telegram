import telepot, urllib3, time, telepot.api, os, json, nltk
from random import randint

############################################# NECESSÁRIO EMOÇÃO ################################################################
basetreinamento = [('estou com medo do resultado dos meus testes', 'medo'),
                   ('eu gosto de mc donalds', 'alegria'),
                   ('eu gosto muito de hamburguer', 'alegria'),
                   ('eu amo mcdonalds', 'alegria'),
                   ('estou me sentindo triste', 'triste'),
                   ('eu sou muito infeliz', 'triste'),
                   ('perdemos um jogo ontem a noite', 'triste'),
                   ('ele me deixou sozinha', 'triste'),
                   ('hoje acordei triste', 'triste'),
                   ('hoje estou me sentindo meio para baixo', 'triste'),
                   ('me sinto só', 'triste'),
                   ('me sinto sozinho', 'triste'),
                   ('hoje acordei com vontade de ficar na cama', 'triste'),
                   ('hoje estou me sentindo amável', 'amor'),
                   ('não consigo parar de pensar em você', 'amor'),
                   ('sinto sua falta', 'triste'),
                   ('sinto sua falta', 'amor'),
                   ('eu te amo', 'amor'),
                   ('meu amor não é compreensivel', 'triste'),
                   ('você faz meu dia melhor', 'alegria'),
                   ('você é o que me falta', 'amor'),
                   ('amor é fogo que arde sem se ver', 'amor'),
                   ('eu te amo', 'amor'),
                   ('não consigo passar um dia sem lhe ver', 'amor'),
                   ('eu te amo tanto', 'amor'),
                   ('este trabalho e agradável', 'alegria'),
                   ('gosto de ficar no seu aconchego', 'alegria'),
                   ('fiz a adesão ao curso hoje', 'alegria'),
                   ('eu sou admirada por muitos', 'alegria'),
                   ('adoro como você e', 'alegria'),
                   ('adoro seu cabelo macio', 'alegria'),
                   ('adoro a cor dos seus olhos', 'alegria'),
                   ('somo tão amáveis um com o outro', 'alegria'),
                   ('sinto uma grande afeição por ele', 'alegria'),
                   ('quero agradar meus filhos', 'alegria'),
                   ('me sinto completamente amado', 'alegria'),
                   ('eu amo você', 'alegria'),
                   ('que grande alivio', 'alegria'),
                   ('a dor esta amenizando finalmente', 'alegria'),
                   ('acho que me apaixonei', 'alegria'),
                   ('amar e maravilhoso', 'alegria'),
                   ('estou me sentindo muito animada', 'alegria'),
                   ('me sinto muito bem hoje', 'alegria'),
                   ('como o luar e belo', 'alegria'),
                   ('o dia esta muito bonito', 'alegria'),
                   ('nossa como sou afortunado', 'alegria'),
                   ('as maravilhas do mundo', 'alegria'),
                   ('recebi muito carinho hoje do meus colegas', 'alegria'),
                   ('estou me sentindo reconfortada hoje', 'alegria'),
                   ('e muito bom estar com os amigos', 'alegria'),
                   ('estou muito contente com o resultado dos testes', 'alegria'),
                   ('essa pintura esta bem brilhante', 'alegria'),
                   ('temos água em abundancia', 'alegria'),
                   ('que roupa delicada', 'alegria'),
                   ('você e um grande comediante', 'alegria'),
                   ('que bondade a sua em vir aqui', 'alegria'),
                   ('o amor e lindo', 'alegria'),
                   ('nossa amizade vai durar para sempre', 'alegria'),
                   ('estou eufórica com a noticia', 'alegria'),
                   ('ele e realmente fiel a mim', 'alegria'),
                   ('vou dar uma grande festa para comemorar meu aniversário', 'alegria'),
                   ('graças a deus que eu enxerguei o certo', 'alegria'),
                   ('essa e a melhor escolhas de todas', 'alegria'),
                   ('o mais incrível e você minha bela', 'alegria'),
                   ('e tão engraçado tentar explicar', 'alegria'),
                   ('e emocionante estar neste lugar', 'alegria'),
                   ('estou cativada pelo seu olhar', 'alegria'),
                   ('estou loucamente apaixonada', 'alegria'),
                   ('eu nunca tive duvidas', 'alegria'),
                   ('estou rodeada pelo seu abraço', 'alegria'),
                   ('eu vejo estrelas pelo caminho', 'alegria'),
                   ('eu sinto o sol sempre que você esta por perto', 'alegria'),
                   ('eu estou sorrindo de orelha a orelha', 'alegria'),
                   ('isso vale a pena', 'alegria'),
                   ('finalmente você colocou meu amor em primeiro lugar', 'alegria'),
                   ('nós dançamos noite adentro', 'alegria'),
                   ('seu amor e brilhante', 'alegria'),
                   ('toquei muitos corações durante o meu caminho', 'alegria'),
                   ('eu serei sua amiga e companheira', 'alegria'),
                   ('você me traz de volta a vida', 'alegria'),
                   ('você e como um sonho doce', 'alegria'),
                   ('adoro este doce de frutas', 'alegria'),
                   ('meu suco favorito', 'alegria'),
                   ('estou agradecida pela ajuda', 'alegria'),
                   ('e um enorme prazer ter você em nossa equipe', 'alegria'),
                   ('trabalhar em equipe e o melhor', 'alegria'),
                   ('me sinto flutuando no ar', 'alegria'),
                   ('a brisa esta agradável hoje', 'alegria'),
                   ('ótimo e compatível', 'alegria'),
                   ('somos compatíveis um com o outro', 'alegria'),
                   ('o órgão e compatível com o paciente', 'alegria'),
                   ('estou contente fui aceita na faculdade', 'alegria'),
                   ('fui aprovada no meu exame', 'alegria'),
                   ('fui beneficiada pela minha empresa', 'alegria'),
                   ('eu sou muito cativante', 'alegria'),
                   ('estou contente com o apoio', 'alegria'),
                   ('como este lugar e confortável', 'alegria'),
                   ('e bom estar quente neste frio', 'alegria'),
                   ('um elogio nunca e demais', 'alegria'),
                   ('vou te chamar para comemorar', 'alegria'),
                   ('e desejável a sua presença em nossa apresentação', 'alegria'),
                   ('sou muito grata a você', 'alegria'),
                   ('me dedico muito naquilo que faço', 'alegria'),
                   ('estou completamente apaixonada ', 'alegria'),
                   ('vamos agitar essa noite ', 'alegria'),
                   ('você significa muito para mim', 'alegria'),
                   ('vamos agir sem preconceitos e julgamentos', 'alegria'),
                   ('finalmente completei a minha coleção, maravilhoso', 'alegria'),
                   ('eu sou sua rainha ', 'alegria'),
                   ('satisfatoriamente eu anuncio o vencedor dos jogos', 'alegria'),
                   ('você me atrai facilmente ', 'alegria'),
                   ('aquele rapaz e extremamente atraente', 'alegria'),
                   ('sinto-me viva ', 'alegria'),
                   ('sinto-me em paz ', 'alegria'),
                   ('estamos tendo muito lucro', 'alegria'),
                   ('muito bem esta tudo em ordem agora ', 'alegria'),
                   ('podemos arrumar um emprego juntos ', 'alegria'),
                   ('a arrumação esta terminada, que alívio', 'alegria'),
                   ('o câncer e benigno ', 'alegria'),
                   ('o amor e abundante', 'alegria'),
                   ('vamos ser caridosos este natal', 'alegria'),
                   ('com todo esse charme você irá atrair a todos', 'alegria'),
                   ('nossa como você e charmoso querido ', 'alegria'),
                   ('sou querida pelos meu amigos', 'alegria'),
                   ('seja cuidadoso com os meus sentimentos', 'alegria'),
                   ('estou comovido com tamanha caridade', 'alegria'),
                   ('um chá quente e reconfortante', 'alegria'),
                   ('que alegria ter vocês aqui ', 'alegria'),
                   ('vamos aplaudir o vencedor ', 'alegria'),
                   ('palmas para a aniversariante', 'alegria'),
                   ('desejo a você tudo de bom', 'alegria'),
                   ('hora de apreciar um bom vinho', 'alegria'),
                   ('aprecio sua presença em minha escola', 'alegria'),
                   ('anseio por seus próximos trabalhos', 'alegria'),
                   ('maravilhoso jogo amistoso', 'alegria'),
                   ('e ótimo que os ânimos tenham se apaziguado', 'alegria'),
                   ('concretizei finalmente meu sonho', 'alegria'),

                   ('você e abominável', 'desgosto'),
                   ('abomino a maneira como você age', 'desgosto'),
                   ('estou adoentado', 'desgosto'),
                   ('meu pai esta adoentado', 'desgosto'),
                   ('estamos todos doentes', 'desgosto'),
                   ('essa situação e muito amarga', 'desgosto'),
                   ('disse adeus amargamente', 'desgosto'),
                   ('tenho antipatia por aquela pessoa', 'desgosto'),
                   ('como pode ser tão antipática!', 'desgosto'),
                   ('que horrível seu asqueroso', 'desgosto'),
                   ('tenho aversão agente como você', 'desgosto'),
                   ('isso tudo e só chateação', 'desgosto'),
                   ('estou muito chateada com suas mentiras', 'desgosto'),
                   ('tão desagradável', 'desgosto'),
                   ('isso me desagrada completamente', 'desgosto'),
                   ('te desagrada isso', 'desgosto'),
                   ('estou com enjôos terríveis', 'desgosto'),
                   ('todos estão enfermos', 'desgosto'),
                   ('foi uma enfermidade terrível', 'desgosto'),
                   ('isso e muito grave', 'desgosto'),
                   ('não seja tão grosseiro', 'desgosto'),
                   ('você fez uma manobra ilegal', 'desgosto'),
                   ('sua indecente, não tem vergonha?', 'desgosto'),
                   ('você e malvado com as crianças', 'desgosto'),
                   ('que comentário maldoso', 'desgosto'),
                   ('sem escrúpulos você manipula a tudo', 'desgosto'),
                   ('sinto repulsa por você', 'desgosto'),
                   ('e repulsivo a maneira como olha para as pessoas', 'desgosto'),
                   ('estou indisposta', 'desgosto'),
                   ('a indisposição me atacou hoje', 'desgosto'),
                   ('acho que vou vomitar', 'desgosto'),
                   ('tem muito vomito lá', 'desgosto'),
                   ('que incomodo essa dor', 'desgosto'),
                   ('não me incomode nunca mais', 'desgosto'),
                   ('suas bobagens estão nos incomodando', 'desgosto'),
                   ('que nojo olha toda essa sujeira', 'desgosto'),
                   ('como isso está sujo', 'desgosto'),
                   ('tenho náuseas só de lembrar', 'desgosto'),
                   ('me sinto nauseada com o cheiro desta comida', 'desgosto'),
                   ('você esta obstruindo a passagem de ar', 'desgosto'),
                   ('você esta terrivelmente doente', 'desgosto'),
                   ('olhe que feia esta roupa', 'desgosto'),
                   ('que atitude deplorável', 'desgosto'),
                   ('nossa como você e feio', 'desgosto'),
                   ('muito mau tudo isso', 'desgosto'),
                   ('estou desgostoso com você', 'desgosto'),
                   ('você cortou o meu assunto', 'desgosto'),
                   ('para que tanta chateação?', 'desgosto'),
                   ('esse perfume e enjoativo', 'desgosto'),
                   ('ser perigoso não nada bom', 'desgosto'),
                   ('você e perigoso demais para minha filhas', 'desgosto'),
                   ('que fetido este esgoto', 'desgosto'),
                   ('que fedido você esta', 'desgosto'),
                   ('que cachorro malcheiroso', 'desgosto'),
                   ('hora que ultraje', 'desgosto'),
                   ('e ultrajante da sua parte', 'desgosto'),
                   ('situação desagradável essa', 'desgosto'),
                   ('você só me da desgosto', 'desgosto'),
                   ('tenho aversão a pessoas assim', 'desgosto'),
                   ('antipatia e um mal da sociedade', 'desgosto'),
                   ('que criatura abominável', 'desgosto'),
                   ('e depressiva a maneira como você vê o mundo', 'desgosto'),
                   ('me desagrada sua presença na festa', 'desgosto'),
                   ('sinto asco dessa coisa', 'desgosto'),
                   ('que hediondo!', 'desgosto'),
                   ('vou golfar o cafe fora', 'desgosto'),
                   ('hora que garota detestável!', 'desgosto'),
                   ('estou nauseada', 'desgosto'),
                   ('isso que você disse foi muito grave', 'desgosto'),
                   ('não seja obsceno na frente das crianças', 'desgosto'),
                   ('não seja rude com as visitas', 'desgosto'),
                   ('esse assunto me da repulsa', 'desgosto'),
                   ('que criança terrivelmente travessa', 'desgosto'),
                   ('que criança mal educada', 'desgosto'),
                   ('estou indisposta te dar o divorcio', 'desgosto'),
                   ('tão patetico, não tem nada mais rude para dizer?', 'desgosto'),
                   ('por motivo torpe, com emprego de meio cruel e com impossibilidade de defesa para a vítima',
                    'desgosto'),
                   ('a inveja e tão vil e vergonhosa que ninguem se atreve a confessá-la', 'desgosto'),
                   ('o miserável receio de ser sentimental e o mais vil de todos os receios modernos', 'desgosto'),
                   ('travesso gato quando fica com saudades do dono mija no sapato', 'desgosto'),
                   ('isso e um ato detestável e covarde', 'desgosto'),
                   ('revelam apenas o que e destrutivo e detestável para o povo', 'desgosto'),
                   ('não sei como e a vida de um patife, mais a de um homem honesto e abominável', 'desgosto'),
                   ('há coisas que temos que suportar para não acharmos a vida insuportável', 'desgosto'),
                   ('as injurias do tempo e as injustiças do homem', 'desgosto'),
                   ('odioso e desumano', 'desgosto'),
                   ('você não publicará conteúdo odiento, pornográfico ou ameaçador', 'desgosto'),
                   ('rancoroso e reprimido', 'desgosto'),
                   (
                   'não há animal mais degradante, estúpido, covarde, lamentável, egoísta, rancoroso e invejoso do que o homem',
                   'desgosto'),
                   ('o virulento debate ente políticos', 'desgosto'),

                   ('eu imploro, não me matem!', 'medo'),
                   ('tem certeza que não e perigoso?', 'medo'),
                   ('não tenho certeza se e seguro', 'medo'),
                   ('tenho que correr pra não me pegarem', 'medo'),
                   ('socorro! ele queria roubar os meus doces!', 'medo'),
                   ('esse cara está me perseguindo', 'medo'),
                   ('não entro lá, e um lugar muito perigoso', 'medo'),
                   ('este lugar continua assustador', 'medo'),
                   ('na selva tem muitos animais perigosos', 'medo'),
                   ('avancem com cautela', 'medo'),
                   ('este lugar está silencioso de mais, cuidado!', 'medo'),
                   ('por favor, deixe-me viver!', 'medo'),
                   ('vou ficar sem mesada se tirar nota baixa', 'medo'),
                   ('parece que tem olhos nos vigiando', 'medo'),
                   ('eu temo que a sentença do juiz possa ser negativa', 'medo'),
                   ('mas essa missão e arriscada', 'medo'),
                   ('salvem-se quem puder!', 'medo'),
                   ('meu plano pode ser descoberto', 'medo'),
                   ('não tive culpa, juro não fui eu', 'medo'),
                   ('tenho que tomar cuidado com o lobisomem', 'medo'),
                   ('se eu não achar, ele vai descobrir a verdade', 'medo'),
                   ('meu deus, ele desapareceu!', 'medo'),
                   ('tomara que eles não me vejam daqui!', 'medo'),
                   ('mantenha isso em segredo, se descobrirem estaremos ferrados', 'medo'),
                   ('por favor, me soltem, eu sou inocente', 'medo'),
                   ('estou ouvindo passos atrás de mim', 'medo'),
                   ('eu vou pedir socorro!', 'medo'),
                   ('cuidado com as curvas na estrada', 'medo'),
                   ('não sei não, parece perigoso', 'medo'),
                   ('estou tremendo de medo!', 'medo'),
                   ('socorro, eu vou cair!', 'medo'),
                   ('eu não vou ate a floresta negra, e muito perigoso', 'medo'),
                   ('ouço passos na minha direção', 'medo'),
                   ('acho que está arriscado de mais', 'medo'),
                   ('vamos voltar, e muito perigoso', 'medo'),
                   ('fuja, se não acabaremos mortos', 'medo'),
                   ('receio por não me livrar desta situação', 'medo'),
                   ('socorro! ele está armado!', 'medo'),
                   ('ei cuidado, você vai bater no poste!', 'medo'),
                   ('socorro, nós estamos afundando', 'medo'),
                   ('e serio, cuidado com essa arma!', 'medo'),
                   ('os tubarões estão atacando!', 'medo'),
                   ('sinto arrepios quando fico sozinho no escuro', 'medo'),
                   ('calma, eu não estou com o dinheiro', 'medo'),
                   ('eu acho que estou sendo enganado', 'medo'),
                   ('ligeiro, temos que fugir depressa', 'medo'),
                   ('tem um crocodilo selvagem vindo para cá', 'medo'),
                   ('se ficarmos quietos eles não vão nos achar', 'medo'),
                   ('fuja! o tigre parece faminto', 'medo'),
                   ('estou sem saída, preciso de um milagre', 'medo'),
                   ('tire isso de mim! socorro!', 'medo'),
                   ('não sei nadar, vou me afogar!', 'medo'),
                   ('não tenho certeza se e seguro', 'medo'),
                   ('vou apanhar se meus pais verem meu boletim', 'medo'),
                   ('não consigo sair daqui!', 'medo'),
                   ('se sair tão tarde, poderei ser assaltada', 'medo'),
                   ('não me deixe por favor!', 'medo'),
                   ('espere, não pode me largar aqui sozinho', 'medo'),
                   ('temo pela sua segurança', 'medo'),
                   ('eu te entrego o dinheiro, por favor não me mate!', 'medo'),
                   ('ele vai levar todo o meu dinheiro', 'medo'),
                   ('não dirija tão rápido assim', 'medo'),
                   ('me descobriram, irão me prender!', 'medo'),
                   ('só espero que não me façam nenhum mal', 'medo'),
                   ('vou me afogar, me ajudem a sair da água', 'medo'),
                   ('não estaremos a salvo aqui', 'medo'),
                   ('não quero nem pensar no que pode acontecer', 'medo'),
                   ('nessa cidade e uma desgraça atrás da outra', 'medo'),
                   ('alguem esta me ligando, estou assustado', 'medo'),
                   ('isso não e remedio, não me matem', 'medo'),
                   ('eu não confio nele, tenho que ter cautela', 'medo'),
                   ('muita cautela', 'medo'),
                   ('vou ser descoberto, meu deus', 'medo'),
                   ('receio que terei de ir', 'medo'),
                   ('a noite e muito perigosa', 'medo'),
                   ('estou estremecendo com essa casa', 'medo'),
                   ('olha aquela criatura se movendo monstruosamente', 'medo'),
                   ('não agüento este suspense', 'medo'),
                   ('afugente os cães', 'medo'),
                   ('estou chocado e amedrontado com este assassinato brutal', 'medo'),
                   ('e preciso afugenta com ímpeto este medo do inferno', 'medo'),
                   ('seu políticos usam suas forças para afugentar e amedrontar o povo', 'medo'),
                   ('o objetivo disso e apenas me amedrontar mais', 'medo'),
                   ('isso me apavora', 'medo'),

                   ('ele a feriu profundamente', 'raiva'),
                   ('vou despejar minha cólera em você', 'raiva'),
                   ('me sinto atormentado', 'raiva'),
                   ('não me contrarie', 'raiva'),
                   ('vou destruir tudo  que foi construído', 'raiva'),
                   ('não consigo terminar este trabalho, e muito frustrante', 'raiva'),
                   ('me frustra a sua presença aqui', 'raiva'),
                   ('esta comida me parece muito ruim', 'raiva'),
                   ('você me destrói', 'raiva'),
                   ('estamos separados', 'raiva'),
                   ('estou odiando este vestido', 'raiva'),
                   ('não pude comprar meu celular hoje', 'raiva'),
                   ('ela e uma garota ruim', 'raiva'),
                   ('estivemos em um show horroroso', 'raiva'),
                   ('o ingresso estava muito caro', 'raiva'),
                   ('se eu estragar tudo vai por água a baixo', 'raiva'),
                   ('não possuo dinheiro algum', 'raiva'),
                   ('sou muito pobre', 'raiva'),
                   ('vai prejudicar a todos esta nova medida', 'raiva'),
                   ('ficou ridículo', 'raiva'),
                   ('este sapato esta muito apertado', 'raiva'),
                   ('a musica e uma ofensa aos meus ouvidos', 'raiva'),
                   ('não consigo terminar uma tarefa muito difícil', 'raiva'),
                   ('reprovei em minha graduação', 'raiva'),
                   ('estou muito chateado com tudo', 'raiva'),
                   ('eu odeio em você', 'raiva'),
                   ('e um desprazer conhecê-lo', 'raiva'),
                   ('estou desperdiçando minhas ferias', 'raiva'),
                   ('e muito ruim este jogo', 'raiva'),
                   ('vamos ter muito rancor pela frente', 'raiva'),
                   ('não achei que seria tão terrível', 'raiva'),
                   ('vou vetar o orçamento ao cliente', 'raiva'),
                   ('meus pais não consentiram nosso casamento', 'raiva'),
                   ('eu odiei este perfume', 'raiva'),
                   ('seu descaso e frustrante', 'raiva'),
                   ('me sinto completamente amarga', 'raiva'),
                   ('desprezo muito o seu trabalho', 'raiva'),
                   ('estamos descontentes por nossa família', 'raiva'),
                   ('vou infernizar a sua empresa', 'raiva'),
                   ('estou furioso com estes valores', 'raiva'),
                   ('obrigaram o rapaz a sair', 'raiva'),
                   ('como ele pode deixar de lado?', 'raiva'),
                   ('são apenas injurias sobre mim', 'raiva'),
                   ('estou enfurecido com a situação dessa empresa', 'raiva'),
                   ('estou com o diabo no corpo', 'raiva'),
                   ('isso foi diabólico', 'raiva'),
                   ('tenho aversão à gente chata', 'raiva'),
                   ('não vou perdoar sua traição', 'raiva'),
                   ('esse dinheiro sujo e corrupto', 'raiva'),
                   ('eles me crucificam o tempo todo', 'raiva'),
                   ('eu vou enlouquecer com todo este barulho', 'raiva'),
                   ('não agüento todo esse assedio', 'raiva'),
                   ('cólera do dragão', 'raiva'),
                   ('isso e ridículo!', 'raiva'),
                   ('da próxima vez, vou inventar tudo sozinho', 'raiva'),
                   ('seus tolos! deixaram ele escapar!', 'raiva'),
                   ('jamais te perdoarei', 'raiva'),
                   ('o que e isso? outra multa', 'raiva'),
                   ('você passou dos limites!', 'raiva'),
                   ('sente-se e cale a boca', 'raiva'),
                   ('ingratosvermesvocês me pagam!', 'raiva'),
                   ('saiam da dai, se não arranco vocês dai!', 'raiva'),
                   ('você já me causou problemas suficientes', 'raiva'),
                   ('isso foi a gota d’agua', 'raiva'),
                   ('o que você tem com isso?', 'raiva'),
                   ('não vejo a hora de me livrar de você', 'raiva'),
                   ('já entendi a jogada seus safados!', 'raiva'),
                   ('você não merece piedade', 'raiva'),
                   ('saia de perto de mim', 'raiva'),
                   ('suma daqui, ou arranco seu couro!', 'raiva'),
                   ('estou revoltado com essa situação', 'raiva'),
                   ('seu idiota!', 'raiva'),
                   ('não, eu não vou te emprestar dinheiro!', 'raiva'),
                   ('você não passa de um cafajeste! vai embora', 'raiva'),
                   ('pare de frescura e vá trabalhar', 'raiva'),
                   ('eles merecem uma lição', 'raiva'),
                   ('ainda estou muito bravo com você', 'raiva'),
                   ('eu preciso surrar aquela chantagista', 'raiva'),
                   ('olha o que você fez! derramou!', 'raiva'),
                   ('você está pedindo pra apanhar!', 'raiva'),
                   ('me deixa em paz!', 'raiva'),
                   ('morra maldito, morra!', 'raiva'),
                   ('você e mais irritante de perto', 'raiva'),
                   ('e bom fechar o bico', 'raiva'),

                   ('magicamente você me surpreendeu', 'surpresa'),
                   ('e imenso esse globo', 'surpresa'),
                   ('isso e tremendamente interessante', 'surpresa'),
                   ('meu bilhete for sorteado, inacreditável!', 'surpresa'),
                   ('um assalto a mão armada!', 'surpresa'),
                   ('incrível, cabe em qualquer lugar!', 'surpresa'),
                   ('você por aqui?', 'surpresa'),
                   ('não dá pra acreditar no que ela me contou', 'surpresa'),
                   ('os convidados já estão chegando!', 'surpresa'),
                   ('puxa vida! nunca nos livramos de alguem tão depressa', 'surpresa'),
                   ('micha carteira sumiu, eu estava com ela na mão', 'surpresa'),
                   ('oh! um disco voador', 'surpresa'),
                   ('amigos, que bela surpresa!', 'surpresa'),
                   ('nunca pensei que veria isso e perto', 'surpresa'),
                   ('nem acredito que comi tanto', 'surpresa'),
                   ('não acredito que veio me ver', 'surpresa'),
                   ('não acredito que e  tão descarado', 'surpresa'),
                   ('me surpreende sua falta de tato', 'surpresa'),
                   ('o predio onde eles moravam desabou!', 'surpresa'),
                   ('inacreditável um bolo tão grande', 'surpresa'),
                   ('e serio mesmo? não dá pra acreditar', 'surpresa'),
                   ('como assim não vai ao nosso encontro?', 'surpresa'),
                   ('como assim não tem ninguem em casa?', 'surpresa'),
                   ('ue, mas para onde ele foi?!', 'surpresa'),
                   ('por essa eu não esperava', 'surpresa'),
                   ('nossa, olha só que mergulho', 'surpresa'),
                   ('minha esposa está grávida!', 'surpresa'),
                   ('meu dinheiro sumiu!', 'surpresa'),
                   ('e verdade que os dois terminaram?!?', 'surpresa'),
                   ('caramba, nem vi você chegar', 'surpresa'),
                   ('nossa, como pode alguem cozinhar tão mal?', 'surpresa'),
                   ('nossa que incrível', 'surpresa'),
                   ('a fórmula sumiu!', 'surpresa'),
                   ('eu nem acredito que já estou terminando o curso', 'surpresa'),
                   ('não acredito que esta aqui comigo novamente', 'surpresa'),
                   ('está escondendo algo de nós!', 'surpresa'),
                   ('como assim, ainda não terminou a tarefa', 'surpresa'),
                   ('pensei que já estivesse pronta!', 'surpresa'),
                   ('opa! quem apagou a luz?', 'surpresa'),
                   ('caramba! aonde vai tão rápido?', 'surpresa'),
                   ('estamos seguindo o caminho errado!', 'surpresa'),
                   ('quatro reais o litro da gasolina!', 'surpresa'),
                   ('me assustei ao vê-lo desse jeito!', 'surpresa'),
                   ('minha mãe está grávida, acredita nisso?', 'surpresa'),
                   ('parece mentira você ter crescido tanto', 'surpresa'),
                   ('me surpreende sua imaginação', 'surpresa'),
                   ('suas roupas são realmente lindas', 'surpresa'),
                   ('com consegue ser tão bela?', 'surpresa'),
                   ('essa e realmente uma casa deslumbrante', 'surpresa'),
                   ('superou minhas expectativas', 'surpresa'),
                   ('e admirável a maneira como se comporta', 'surpresa'),
                   ('isso e realmente chocante', 'surpresa'),
                   ('algumas noticias me surpreenderam no noticiário', 'surpresa'),
                   ('surpreendente sua festa', 'surpresa'),
                   ('estou tremendo de alegria', 'surpresa'),
                   ('chocou grande parte do mundo', 'surpresa'),
                   ('eu ficaria muito espantado com a sua vinda', 'surpresa'),
                   ('ele e admirável', 'surpresa'),
                   ('sua beleza me surpreendeu', 'surpresa'),
                   ('seus olhos são surpreendentemente verdes', 'surpresa'),
                   ('os políticos se surpreendem quando alguem acredita neles', 'surpresa'),
                   ('estou perplexa com essas denuncias', 'surpresa'),
                   ('fiquei perplexo com suas palavras', 'surpresa'),
                   ('estou abismado com sua prosa', 'surpresa'),
                   ('eu ficaria realmente abismado se me dissessem isso', 'surpresa'),
                   ('o grupo foi surpreendido enquanto lavava o carro', 'surpresa'),
                   ('estou boquiaberto com as imagens', 'surpresa'),
                   ('estou boquiaberto com essas suas palavras', 'surpresa'),
                   ('esse quadro e maravilhoso', 'surpresa'),
                   ('este carro me deixou maravilhado', 'surpresa'),
                   ('estou maravilhada', 'surpresa'),
                   ('essa expectativa esta me matando', 'surpresa'),
                   ('vou caminhar sempre na expectativa de encontrá-lo', 'surpresa'),
                   ('você emudece minhas palavras', 'surpresa'),
                   ('minhas palavras vão emudecer se não parar de me surpreender', 'surpresa'),
                   ('a mulher e um efeito deslumbrante da natureza', 'surpresa'),
                   ('estou deslumbrada com essas jóias', 'surpresa'),
                   ('isso e romântico e deslumbrante', 'surpresa'),
                   ('isso pode ser surpreendentemente deslumbrante', 'surpresa'),
                   ('trabalho deslumbrante', 'surpresa'),
                   ('essas pessoas são esplêndida', 'surpresa'),
                   ('e esplendido como o ceu se encontra no momento', 'surpresa'),
                   ('e um carro fantástico', 'surpresa'),
                   ('um edifício realmente fantástico', 'surpresa'),

                   ('por favor não me abandone', 'tristeza'),
                   ('não quero ficar sozinha', 'tristeza'),
                   ('não me deixe sozinha', 'tristeza'),
                   ('estou abatida', 'tristeza'),
                   ('ele esta todo abatido', 'tristeza'),
                   ('tão triste suas palavras', 'tristeza'),
                   ('seu amor não e mais meu', 'tristeza'),
                   ('estou aborrecida', 'tristeza'),
                   ('isso vai me aborrecer', 'tristeza'),
                   ('estou com muita aflição', 'tristeza'),
                   ('me aflige o modo como fala', 'tristeza'),
                   ('estou em agonia com meu intimo', 'tristeza'),
                   ('não quero fazer nada', 'tristeza'),
                   ('me sinto ansiosa e tensa', 'tristeza'),
                   ('não consigo parar de chorar', 'tristeza'),
                   ('não consigo segurar as lagrimas', 'tristeza'),
                   ('e muita dor perder um ente querido', 'tristeza'),
                   ('estou realmente arrependida', 'tristeza'),
                   ('acho que o carma volta, pois agora sou eu quem sofro', 'tristeza'),
                   ('você não cumpriu suas promessas', 'tristeza'),
                   ('me sinto amargurada', 'tristeza'),
                   ('coitado esta tão triste', 'tristeza'),
                   ('já e tarde de mais', 'tristeza'),
                   ('nosso amor acabou', 'tristeza'),
                   ('essa noite machuca só para mim', 'tristeza'),
                   ('eu não estou mais no seu coração', 'tristeza'),
                   ('você mudou comigo', 'tristeza'),
                   ('quando eu penso em você realmente dói', 'tristeza'),
                   ('como se fosse nada você vê minhas lagrimas', 'tristeza'),
                   ('você disse cruelmente que não se arrependeu', 'tristeza'),
                   ('eu nunca mais vou te ver', 'tristeza'),
                   ('ela esta com depressão', 'tristeza'),
                   ('a depressão aflige as pessoas', 'tristeza'),
                   ('estar depressivo e muito ruim', 'tristeza'),
                   ('estou derrotada e deprimida depois deste dia', 'tristeza'),
                   ('e comovente te ver dessa maneira', 'tristeza'),
                   ('e comovente ver o que os filhos do brasil passam', 'tristeza'),
                   ('como me sinto culpada', 'tristeza'),
                   ('estou abatida', 'tristeza'),
                   ('a ansiedade tomou conta de mim', 'tristeza'),
                   ('as pessoas não gostam do meu jeito', 'tristeza'),
                   ('adeus passamos bons momentos juntos', 'tristeza'),
                   ('sinto sua falta', 'tristeza'),
                   ('ele não gostou da minha comida', 'tristeza'),
                   ('estou sem dinheiro para a comida', 'tristeza'),
                   ('queria que fosse o ultimo dia da minha vida', 'tristeza'),
                   ('você está com vergonha de mim', 'tristeza'),
                   ('ela não aceitou a minha proposta', 'tristeza'),
                   ('era o meu ultimo centavo', 'tristeza'),
                   ('reprovei de ano na faculdade', 'tristeza'),
                   ('afinal você só sabe me desfazer', 'tristeza'),
                   ('eu falhei em tudo nessa vida', 'tristeza'),
                   ('eu fui muito humilhado', 'tristeza'),
                   ('e uma história muito triste', 'tristeza'),
                   ('ninguem acredita em mim', 'tristeza'),
                   ('eu não sirvo para nada mesmo', 'tristeza'),
                   ('droga, não faço nada direito', 'tristeza'),
                   ('sofrimento em dobro na minha vida', 'tristeza'),
                   ('fui demitida essa semana', 'tristeza'),
                   ('as crianças sofrem ainda mais que os adultos', 'tristeza'),
                   ('pra mim um dia e ruim, o outro e pior', 'tristeza'),
                   ('de repente perdi o apetite', 'tristeza'),
                   ('oh que dia infeliz', 'tristeza'),
                   ('estamos afundados em contas', 'tristeza'),
                   ('nem um milagre pode nos salvar', 'tristeza'),
                   ('só me resta a esperança', 'tristeza'),
                   ('pior que isso não pode ficar', 'tristeza'),
                   ('meu salário e baixo', 'tristeza'),
                   ('não passei no vestibular', 'tristeza'),
                   ('ninguem se importa comigo', 'tristeza'),
                   ('ninguem lembrou do meu aniversário', 'tristeza'),
                   ('tenho tanto azar', 'tristeza'),
                   ('o gosto da vingança e amargo', 'tristeza'),
                   ('sou uma mulher amargurada depois de que você me deixou', 'tristeza'),
                   ('estou desanimada com a vida', 'tristeza'),
                   ('e um desanimo só coitadinha', 'tristeza'),
                   ('a derrota e depressiva', 'tristeza'),
                   ('discriminar e desumano', 'tristeza'),
                   ('que desanimo', 'tristeza'),
                   ('e uma desonra para o pais', 'tristeza'),
                   ('a preocupação deveria nos levar a ação não a depressão', 'tristeza'),
                   ('passamos ao desalento e a loucura', 'tristeza'),
                   ('aquele que nunca viu a tristeza nunca reconhecerá a alegria', 'tristeza'),
                   ('cuidado com a tristeza ela e um vicio', 'tristeza')]
baseteste = [('não precisei pagar o ingresso', 'alegria'),
             ('se eu ajeitar tudo fica bem', 'alegria'),
             ('minha fortuna ultrapassa a sua', 'alegria'),
             ('sou muito afortunado', 'alegria'),
             ('e benefico para todos esta nova medida', 'alegria'),
             ('ficou lindo', 'alegria'),
             ('achei esse sapato muito simpático', 'alegria'),
             ('estou ansiosa pela sua chegada', 'alegria'),
             ('congratulações pelo seu aniversário', 'alegria'),
             ('delicadamente ele a colocou para dormir', 'alegria'),
             ('a musica e linda', 'alegria'),
             ('sem musica eu não vivo', 'alegria'),
             ('conclui uma tarefa muito difícil', 'alegria'),
             ('conclui minha graduação', 'alegria'),
             ('estou muito contente com tudo', 'alegria'),
             ('eu confio em você', 'alegria'),
             ('e um prazer conhecê-lo', 'alegria'),
             ('o coleguismo de vocês e animador', 'alegria'),
             ('estou aproveitando as ferias', 'alegria'),
             ('vamos aproveitar as ferias', 'alegria'),
             ('e muito divertido este jogo', 'alegria'),
             ('vamos ter muita diversão', 'alegria'),
             ('não achei que me divertiria tanto assim', 'alegria'),
             ('vou consentir o orçamento ao cliente', 'alegria'),
             ('com o consentimento dos meus pais podemos nos casar', 'alegria'),
             ('eu adorei este perfume', 'alegria'),
             ('sua bondade e cativante', 'alegria'),
             ('estou despreocupada', 'alegria'),
             ('não me preocupo com o que aconteceu', 'alegria'),
             ('me sinto completamente segura', 'alegria'),
             ('estimo muito o seu trabalho', 'alegria'),
             ('somos estimados por nossa família', 'alegria'),
             ('concretizamos nossa ideia', 'alegria'),
             ('nosso ideal foi alcançado', 'alegria'),
             ('estamos muito felizes juntos', 'alegria'),
             ('estou tão animada com os preparativos para o casamento', 'alegria'),
             ('você será muito amado meu filho', 'alegria'),
             ('os apaixonados são maravilhosos', 'alegria'),
             ('agradeço imensamente o seu apoio nestes dias', 'alegria'),
             ('esta comida me parece muito atraente', 'alegria'),
             ('você me completa', 'alegria'),
             ('poderemos completar o projeto hoje!', 'alegria'),
             ('estamos namorando', 'alegria'),
             ('estou namorando este vestido a um tempo', 'alegria'),
             ('pude comprar meu celular hoje', 'alegria'),
             ('e um deleite poder compartilhar minhas vitórias', 'alegria'),
             ('ela e um boa garota', 'alegria'),
             ('estivemos em um ótimo show', 'alegria'),

             ('o mundo e feio como o pecado', 'desgosto'),
             ('a coisa mais difícil de esconder e aquilo que não existe', 'desgosto'),
             ('você errou feio aquele gol', 'desgosto'),
             ('nunca vou me casar sou muito feia', 'desgosto'),
             ('os golpes da adversidade são terrivelmente amargos', 'desgosto'),
             ('os homem ficam terrivelmente chatos', 'desgosto'),
             ('abominavelmente convencido', 'desgosto'),
             ('terrivelmente irritado', 'desgosto'),
             ('as instituições publicas estão terrivelmente decadentes', 'desgosto'),
             ('a população viveu em isolamento por muito tempo', 'desgosto'),
             ('estou terrivelmente preocupada', 'desgosto'),
             ('o nacionalismo e uma doença infantil', 'desgosto'),
             ('se me es antipático a minha negação esta pronta', 'desgosto'),
             ('muitos documentários sobre esse casal antipático', 'desgosto'),
             ('sua beleza não desfaça sua antipatia', 'desgosto'),
             ('esta e uma experiência desagradável', 'desgosto'),
             ('desagradável estrago nos banheiros', 'desgosto'),
             ('o mais irritante no amor e que se trata de um crime que precisa de um cúmplice', 'desgosto'),
             ('a situação nos causa grande incomodo', 'desgosto'),
             ('estou preocupado com o incomodo na garganta', 'desgosto'),
             ('simplesmente não quero amolação da policia', 'desgosto'),
             ('você e uma criaturinha muito impertinente', 'desgosto'),
             ('o peso e a dor da vida', 'desgosto'),
             ('me arrependo amargamente de minhas ações', 'desgosto'),
             ('o destino e cruel e os homens não são dignos de compaixão', 'desgosto'),
             ('o ódio conduz ao isolamento cruel e ao desespero', 'desgosto'),
             ('encerrou com o massacre mais repudiável e asqueroso que se conhece', 'desgosto'),
             ('de mal gosto e asqueroso', 'desgosto'),
             ('tudo e inserto neste mundo hediondo', 'desgosto'),
             ('o crime de corrupção e um crime hediondo', 'desgosto'),
             ('o rio esta fetido e de cor escura', 'desgosto'),
             ('muito lixo no rio o deixa malcheiroso', 'desgosto'),
             ('existe uma laranja podre no grupo e já desconfiamos quem e', 'desgosto'),
             ('foi de repente estou machucado e me sentindo enjoado', 'desgosto'),
             ('eu fiquei enojado', 'desgosto'),
             ('daqui alguns meses vou embora deste pais que já estou nauseado', 'desgosto'),

             ('que abominável esse montro!', 'medo'),
             ('vamos alarmar a todos sobre a situação', 'medo'),
             ('estou amedrontada', 'medo'),
             ('estou com muito medo da noite', 'medo'),
             ('ele esta me ameaçando a dias', 'medo'),
             ('quanta angustia', 'medo'),
             ('estou angustiada', 'medo'),
             ('angustiadamente vou sair e casa', 'medo'),
             ('isso me deixa apavorada', 'medo'),
             ('você esta me apavorando', 'medo'),
             ('estou desconfiada de você', 'medo'),
             ('não confio em você', 'medo'),
             ('ate o cachorro está apavorado', 'medo'),
             ('estou assustado com as ações do meu colega', 'medo'),
             ('agora se sente humilhado, apavorado', 'medo'),
             ('assustou a população e provocou mortes', 'medo'),
             ('estou com dificuldades para respirar e muito assustado', 'medo'),
             ('os policiais se assustaram quando o carro capotou', 'medo'),
             ('o trabalhador e assombrado pelo temor do desemprego', 'medo'),
             ('este lugar e mal assombrado', 'medo'),
             ('estou assombrado pela crise financeira', 'medo'),
             ('mesmo aterrorizado lembro de você', 'medo'),
             ('aterrorizado e suando frio', 'medo'),
             ('um grupo de elefantes selvagens tem aterrorizado vilas', 'medo'),
             ('me sinto intimidada pela sua presença', 'medo'),
             ('tenho medo de ser advertida novamente', 'medo'),
             ('estou correndo o risco de ser advertido', 'medo'),
             ('estou correndo riscos de saúde', 'medo'),
             ('os riscos são reais', 'medo'),
             ('podemos perder muito dinheiro com essa investida', 'medo'),
             ('socorro, fui intimado a depor', 'medo'),
             ('fui notificado e estou com medo de perde a guarda da minha filha', 'medo'),
             ('estou angustiada com meus filhos na rua', 'medo'),
             ('e abominável o que fazem com os animais', 'medo'),
             ('foi terrível o tigre quase o matou', 'medo'),
             ('me advertiram sobre isso', 'medo'),

             ('ate que enfim, não agüentava mais te esperar', 'raiva'),
             ('eu quero meu dinheiro de volta agora!', 'raiva'),
             ('eu odeio a escola!', 'raiva'),
             ('vou fazer picadinho de você', 'raiva'),
             ('detesto trabalhar no verão', 'raiva'),
             ('quero minha comida, e quero agora!', 'raiva'),
             ('melhor você recolher minhas compras agora!', 'raiva'),
             ('quero descer agora sua maluca', 'raiva'),
             ('vou reclamar com o gerente!', 'raiva'),
             ('vai engolir o que disse!', 'raiva'),
             ('ele me ridiculariza diante de todos', 'raiva'),
             ('não quero mais saber de você', 'raiva'),
             ('vejo você na cadeia safado!', 'raiva'),
             ('agora vou ter que pagar mais isso ainda!', 'raiva'),
             ('saia logo do banheiro!', 'raiva'),
             ('suba já para o seu quarto!', 'raiva'),
             ('eu falei para calar a boca seu idiota!', 'raiva'),
             ('eu disse para você cair fora!', 'raiva'),
             ('não agüento mais que fiquem me culpando sem motivo!', 'raiva'),
             ('não suporto olhar na sua cara!', 'raiva'),
             ('eu não sou um elefante', 'raiva'),
             ('juro que se olhar pra mim eu o mato!', 'raiva'),
             ('chega, não quero saber mais deste assunto', 'raiva'),
             ('como pode ser tão burro?', 'raiva'),
             ('não me aborreça seu moleque', 'raiva'),
             ('não quero me aborrecer com estas bobagens', 'raiva'),
             ('ele me agrediu!', 'raiva'),
             ('eu amaldiçôo você e a sua família', 'raiva'),
             ('não me amole', 'raiva'),
             ('não venha me amolar', 'raiva'),
             ('isso tudo e uma tormenta', 'raiva'),
             ('eu vou matar você', 'raiva'),
             ('para que simplificar se você pode sempre complicar', 'raiva'),
             ('isso esta me enlouquecendo', 'raiva'),
             ('estou furiosa com você', 'raiva'),
             ('isso mesmo fique furioso', 'raiva'),

             ('esses livros são magníficos', 'surpresa'),
             ('esse vinho e magnífico', 'surpresa'),
             ('seria magnífico ver o esperaculo', 'surpresa'),
             ('o casamento foi estupendo', 'surpresa'),
             ('e um jogador bárbaro estupendo', 'surpresa'),
             ('esse dia esta excelente', 'surpresa'),
             ('o cantor estava excelente', 'surpresa'),
             ('o universo e assombroso', 'surpresa'),
             ('o amor e sublime', 'surpresa'),
             ('sua sublime atuação', 'surpresa'),
             ('e formidável meu caro walter', 'surpresa'),
             ('como e formidável a presença de todos', 'surpresa'),
             ('e formidável ter a quem dizer adeus', 'surpresa'),
             ('e um conselheiro formidável o seu', 'surpresa'),
             ('o artigo foi formidável', 'surpresa'),
             ('pica pau e um destaque no imaginário brasileiro', 'surpresa'),
             ('ah! o absoluto do imaginário', 'surpresa'),
             ('isso foi surreal', 'surpresa'),
             ('uma historia completamente surreal', 'surpresa'),
             ('essas pinturas beiram o surreal', 'surpresa'),
             ('você nem acreditam de tão surreal', 'surpresa'),
             ('incrível!', 'surpresa'),
             ('fiquei pasma com tudo isso', 'surpresa'),
             ('você me deixa pasmo', 'surpresa'),
             ('estou admirado com a sua astucia', 'surpresa'),
             ('que bela surpresa você me fez', 'surpresa'),
             ('não acredito que fez isso!', 'surpresa'),
             ('isso foi apavorante', 'surpresa'),
             ('isso tão de repente', 'surpresa'),
             ('estou chocada com isso', 'surpresa'),
             ('estou surpresa e desconsertada', 'surpresa'),
             ('esta realmente deslumbrante querida', 'surpresa'),
             ('fiquei completamente sem plavras', 'surpresa'),
             ('e espantoso o modo como ele nos olha', 'surpresa'),
             ('incrivel você estar aqui', 'surpresa'),
             ('que fantástica festa minha querida', 'surpresa'),

             ('isso tudo e um erro', 'tristeza'),
             ('eu sou errada eu sou errante', 'tristeza'),
             ('tenho muito dó do cachorro', 'tristeza'),
             ('e dolorida a perda de um filho', 'tristeza'),
             ('essa tragedia vai nos abalar para sempre', 'tristeza'),
             ('perdi meus filhos', 'tristeza'),
             ('perdi meu curso', 'tristeza'),
             ('sou só uma chorona', 'tristeza'),
             ('você e um chorão', 'tristeza'),
             ('se arrependimento matasse', 'tristeza'),
             ('me sinto deslocado em sala de aula', 'tristeza'),
             ('foi uma passagem fúnebre', 'tristeza'),
             ('nossa condolências e tristeza a sua perda', 'tristeza'),
             ('desanimo, raiva, solidão ou vazies, depressão', 'tristeza'),
             ('vivo te desanimando', 'tristeza'),
             ('estou desanimado', 'tristeza'),
             ('imperador sanguinário, depravado e temeroso', 'tristeza'),
             ('meu ser esta em agonia', 'tristeza'),
             ('este atrito entre nos tem que acabar', 'tristeza'),
             ('a escuridão desola meu ser', 'tristeza'),
             ('sua falsa preocupação', 'tristeza'),
             ('sua falsidade me entristece', 'tristeza'),
             ('quem esta descontente com os outros esta descontente consigo próprio', 'tristeza'),
             ('a torcida esta descontente com a demissão do tecnico', 'tristeza'),
             ('estou bastante aborrecido com o jornal', 'tristeza'),
             ('me sinto solitário e entediado', 'tristeza'),
             ('a vida e solitária para aqueles que não são falsos', 'tristeza'),
             ('como com compulsão depois da depressão', 'tristeza'),
             ('estou me desencorajando a viver', 'tristeza'),
             ('ele desencoraja minhas vontades', 'tristeza'),
             ('isso vai deprimindo por dentro', 'tristeza'),
             ('acho que isso e defeituoso', 'tristeza'),
             ('os remedios me derrubam na cama', 'tristeza'),
             ('a depressão vai me derrubar', 'tristeza'),
             ('suas desculpas são falsas', 'tristeza'),
             ('não magoe as pessoas', 'tristeza')]
stopwordsnltk = ['último', 'é', 'acerca', 'agora', 'algmas', 'alguns', 'ali', 'ambos', 'antes', 'apontar', 'aquela',
                 'aquelas', 'aquele', 'aqueles', 'aqui', 'atrás', 'bem', 'bomde', 'a', 'o', 'que', 'e', 'do', 'da',
                 'em', 'um', 'para', 'é', 'com', 'não', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos',
                 'como', 'mas', 'foi', 'ao', 'ele', 'das', 'tem', 'à', 'seu', 'sua', 'ou', 'ser', 'quando', 'muito',
                 'há', 'nos', 'já', 'está', 'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso', 'ela', 'entre', 'era',
                 'depois', 'sem', 'mesmo', 'aos', 'ter', 'seus', 'quem', 'nas', 'me', 'esse', 'eles', 'estão', 'você',
                 'tinha', 'foram', 'essa', 'num', 'nem', 'suas', 'meu', 'às', 'minha', 'têm', 'numa', 'pelos', 'elas',
                 'havia', 'seja', 'qual', 'será', 'nós', 'tenho', 'lhe', 'deles', 'essas', 'esses', 'pelas', 'este',
                 'fosse', 'dele', 'tu', 'te', 'vocês', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas',
                 'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela',
                 'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'está', 'estamos', 'estão', 'estive', 'esteve',
                 'estivemos', 'estiveram', 'estava', 'estávamos', 'estavam', 'estivera', 'estivéramos', 'esteja',
                 'estejamos', 'estejam', 'estivesse', 'estivéssemos', 'estivessem', 'estiver', 'estivermos',
                 'estiverem', 'hei', 'há', 'havemos', 'hão', 'houve', 'houvemos', 'houveram', 'houvera', 'houvéramos',
                 'haja', 'hajamos', 'hajam', 'houvesse', 'houvéssemos', 'houvessem', 'houver', 'houvermos', 'houverem',
                 'houverei', 'houverá', 'houveremos', 'houverão', 'houveria', 'houveríamos', 'houveriam', 'sou',
                 'somos', 'são', 'era', 'éramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'fôramos', 'seja',
                 'sejamos', 'sejam', 'fosse', 'fôssemos', 'fossem', 'for', 'formos', 'forem', 'serei', 'será',
                 'seremos', 'serão', 'seria', 'seríamos', 'seriam', 'tenho', 'tem', 'temos', 'tém', 'tinha', 'tínhamos',
                 'tinham', 'tive', 'teve', 'tivemos', 'tiveram', 'tivera', 'tivéramos', 'tenha', 'tenhamos', 'tenham',
                 'tivesse', 'tivéssemos', 'tivessem', 'tiver', 'tivermos', 'tiverem', 'terei', 'terá', 'teremos',
                 'terão', 'teria', 'teríamos', 'teriam', 'ir', 'irá', 'ista', 'iste', 'isto', 'ligado', 'maioria',
                 'maiorias', 'mais', 'mas', 'mesmo', 'meu', 'muito', 'muitos', 'nós', 'não', 'nome', 'nosso', 'novo',
                 'o', 'onde', 'os', 'ou', 'outro', 'para', 'parte', 'pegar', 'pelo', 'pessoas', 'pode', 'poderá\tpodia',
                 'por', 'porque', 'povo', 'promeiro', 'quê', 'qual', 'qualquer', 'quando', 'quem', 'quieto', 'são',
                 'saber', 'sem', 'ser', 'seu', 'somente', 'têm', 'tal', 'também', 'tem', 'tempo', 'tenho', 'tentar',
                 'tentaram', 'tente', 'tentei', 'teu', 'teve', 'tipo', 'tive', 'todos', 'trabalhar', 'trabalho', 'tu',
                 'um', 'uma', 'umas', 'uns', 'usa', 'usar', 'valor', 'veja', 'ver', 'verdade', 'verdadeiro', 'você']
def remov_stop(texto):
    frases = []
    for (palavras, emocao) in texto:
        semstop = [p for p in palavras.split() if p not in stopwordsnltk]
        frases.append((semstop, emocao))
    return frases


def stem(texto):
    stemm = nltk.stem.RSLPStemmer()
    frasesstemming = []
    for (palavras, emocao) in texto:
        comstem = [str(stemm.stem(p)) for p in palavras.split() if p not in stopwordsnltk]
        frasesstemming.append((comstem, emocao))
    return frasesstemming


# frasescomstemin = stem(base)
frasescomstemintreinamento = stem(basetreinamento)
frasescomstemmingteste = stem(baseteste)


# print(frasescomstemin)

def busca_palavra(frases):
    todaspalavras = []
    for (palavras, emocao) in frases:
        todaspalavras.extend(palavras)
    return todaspalavras


palavrastreinamento = busca_palavra(frasescomstemintreinamento)
palavrasteste = busca_palavra(frasescomstemmingteste)


# print(palavras)

def busca_freq(palavras):
    palavras = nltk.FreqDist(palavras)
    return palavras


frequenciatreinamento = busca_freq(palavrastreinamento)
frequenciateste = busca_freq(palavrasteste)


# print(frequencia.most_common(50))

def busca_unicas(frequencia):
    freq = frequencia.keys()
    return freq


unicas = busca_unicas(frequenciatreinamento)
unicasteste = busca_unicas(frequenciateste)


# print(unicas)

def extrair(documento):
    doc = set(documento)
    caract = {}
    for palavras in unicas:
        caract['%s' % palavras] = (palavras in doc)
    return caract


caracteres = extrair(['am', 'nov', 'dia'])
# print(caracteres)

basecompletatreinamento = nltk.classify.apply_features(extrair, frasescomstemintreinamento)
basecompletateste = nltk.classify.apply_features(extrair, frasescomstemmingteste)
# print(basecompleta[15])

# constroi a tabela de probabilidade
classificador = nltk.NaiveBayesClassifier.train(basecompletatreinamento)
# print(classificador.labels())
# print(classificador.show_most_informative_features(20))

# print(nltk.classify.accuracy(classificador, basecompletateste))

erros = []
for (frase, classe) in basecompletateste:
    # print(frase)
    # print(classe)
    resultado = classificador.classify(frase)
    if resultado != classe:
        erros.append((classe, resultado, frase))
# for (classe, resultado, frase) in erros:
#    print(classe, resultado, frase)

# from nltk.metrics import ConfusionMatrix
esperado = []
previsto = []



for (frase, classe) in basecompletateste:
    resultado = classificador.classify(frase)
    previsto.append(resultado)
    esperado.append(classe)
stemm = nltk.stem.RSLPStemmer()
######################################### FIM DO CARREGAMENTO NLTK ###############################################################
############################################ BOT ##################################################

'''# You can leave this bit out if you're using a paid PythonAnywhere account
proxy_url = 'http://proxy.server:3128'
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
# end of the stuff that's only needed for free accounts'''

bot = telepot.Bot('578012223:AAFjXoFrzYwfE4vCNUM-hcOFKrgLOn0dnE4')
ids = {'MestreSsplinter': 609679275, 'Trizquei': 469633382, 'BlAcKClay': 73598018, 'gueedes': 579917403, 'Banks666': 438637688, 'ThigSchuch': 112212677, 'johnrs1': 611945798, 'Paulathaynnara': 477534824, 'Yuichi_VLS': 538809225}



def escreve(texto):# Gera a temp pra enviar arquivo subsequente
    json.dump(texto, open('temp.txt', 'w'))
def ler(): # Lê o json para enviar arquivo, baseando na id e chat id
    dict = json.load(open('temp.txt'))
    return dict
def handle(msg):
    global ids
    content_type, chat_type, chat_id = telepot.glance(msg)
    username = msg['from']['username']
    userid = msg['from']['id']
    rpli = msg['message_id']
    user = msg['from']['username']
    id = msg['from']['id']

    ids[username] = userid

    if content_type == 'text':
    ####################################### DB ###################################
        if '/comandosdba' == msg['text']:
            bot.sendMessage(chat_id, '*/cadastrar disciplina* ## Sempre com espaço\n*/mostramaterias* ## Irá mostrar as matéria cadastradas\n*/mostracont disciplina*  ## Mostra os conteúdos cadastrados\n*/enviar disciplina* conteudo  ## Envia arquivo ao db\n*/down disciplina* conteudo  ## Faz o download do arquivo, consulte "mostracont" primeiro', parse_mode='Markdown')

        if '/cadastrar' in msg['text']:
            ori = msg['text'].split(' ')
            disc = ori[1].lower()
            os.makedirs('./materias/'+disc)
            bot.sendMessage(chat_id, 'Matéria cadastrada: *'+ str(disc)+'*', parse_mode='Markdown')

        if '/mostramaterias' in msg['text']:
            files = os.listdir(r"./materias/")
            arq = open('./materias/pastas.txt', 'a')
            for i in files:
                arq.write(i + '\n')
            arq.close()
            leu = open('./materias/pastas.txt', 'r')
            bot.sendMessage(chat_id, '*Matérias cadastradas:* \n' + leu.read(), parse_mode='Markdown')
            leu.close()
            os.remove('./materias/pastas.txt')

        if '/mostracont' in msg['text']:
            ori = msg['text'].split(' ')
            disc = ori[1].lower()
            files = os.listdir(r'./materias/' + disc + '/')
            arq = open('./materias/temp.txt', 'a')
            for i in files:
                arq.write(i + '\n')
            arq.close()
            leu = open('./materias/temp.txt', 'r')
            bot.sendMessage(chat_id, '*Conteúdos cadastrados:* \n' + leu.read(), parse_mode='Markdown')
            leu.close()
            os.remove('./materias/temp.txt')

        if '/enviar' in msg['text']:
            novo = msg['text'].split(' ')
            del novo[0]
            materia = novo[0].lower()
            bot.sendMessage(chat_id, 'Envie o arquivo, ele estará em ' + str(materia) + 'com o nome de '+ str(novo[1]))
            arquivo = {'message_id': msg['message_id'], 'chat_id': chat_id, 'user': id, 'local': materia, 'conteudo': novo[1]}
            escreve(arquivo)

        if '/down' in msg['text']:
            ori = msg['text'].split(' ')
            materia = ori[1].lower()
            conteudo = ori[2].lower()
            files = os.listdir(r'./materias/' + materia)
            for i in files:
                if (conteudo in i) and ('.jpg' in i):
                    bot.sendPhoto(chat_id, photo=open('./materias/' + materia + '/' + conteudo + '.jpg', 'rb'))
                if (conteudo in i) and (('.docx' in i) or ('.pptx' in i) or ('.txt' in i) or ('.pdf' in i)):
                    if ('.docx' in i):
                        bot.sendDocument(chat_id, document=open('./materias/' + materia + '/' + conteudo + '.docx', 'rb'))
                    if ('.pptx' in i):
                        bot.sendDocument(chat_id, document=open('./materias/' + materia + '/' + conteudo + '.pptx', 'rb'))
                    if ('.txt' in i):
                        bot.sendDocument(chat_id, document=open('./materias/' + materia + '/' + conteudo + '.txt', 'rb'))
                    if ('.pdf' in i):
                        bot.sendDocument(chat_id, document=open('./materias/' + materia + '/' + conteudo + '.pdf', 'rb'))
        ####################################### FIM DO DB #####################################################################

        if '.u' in msg['text']:
            editado = msg['text'].replace('.u', '')
            bot.deleteMessage((chat_id, rpli))
            bot.sendMessage(chat_id, editado, parse_mode='Markdown')

        if "/comandos@dedno_bot" == msg['text']:
            bot.deleteMessage((chat_id, rpli))
            bot.sendMessage(chat_id, "*Comandos e dedo no seu cu:*\n*.u* - Faça o bot falar o que você quiser \n*.w* - Adicione frase, palavras, o que quiser na base de dados do bot \n*faladedo* - O bot usa alguma frase do banco de dados para conversar \n*/mil @* - O bot coloca o dedo no outro /mil usuario no usuario \n*Ah, ainda tem esses stickers lixos:*\nhelo\nsk, skate, charlie\nto brabo\nopora\n", parse_mode= 'Markdown')
        if "faladedo" == msg['text']:
            arq = open('base_dados.txt', 'r')
            arquivo= arq.read().split('\n')
            limite = len(arquivo)
            linha = str(arquivo[randint(0,limite)])
            bot.deleteMessage((chat_id, rpli))
            bot.sendMessage(chat_id, linha)
            arq.close()

        if '.w' in msg['text']:
            texto = msg['text'].split(' ')
            del texto[0]
            arq = open('base_dados.txt', 'a')
            arq.write(' '.join(texto)+'\n')
            arq.close()
            bot.sendMessage(chat_id, "Frase adicionada ao banco de dados: "+"'"+' '.join(texto)+"'"+'\n'+'\nObrigado por me tornar mais inteligente!', reply_to_message_id=rpli)

        from PIL import Image
        if '/mil @' in msg['text']:
            palavras = msg['text'].split(' ')
            pal = palavras[1].replace('@','')
            pal2 = palavras[3].replace('@','')
            user1 = ids[pal]
            user2 = ids[pal2]

            img = bot.getUserProfilePhotos(user1)
            img2 = bot.getUserProfilePhotos(user2)
            bot.download_file(img['photos'][0][0]['file_id'], './temp.png')
            bot.download_file(img2['photos'][0][0]['file_id'], './temp2.png')
            colar1 = Image.open('temp.png')
            colar2 = Image.open('temp2.png')
            merge = Image.open('naruto.jpg')
            colar2.thumbnail((160,200))
            colar1.thumbnail((160,200))
            merge.paste(colar2,(50,110))
            merge.paste(colar1,(700,220))
            merge.save('dedono.webp')
            #deleta arquivo
            os.remove('./temp.png')
            os.remove('./temp2.png')
            bot.sendSticker(chat_id, sticker=open('dedono.webp','rb'), reply_to_message_id=rpli)

        if 'dedo no cu' in msg['text']:
            bot.sendMessage(chat_id, "E GRITARIA MEU BOM ?", reply_to_message_id=rpli)

        if 'dedo' in msg['text']:
            if 'oi' in msg['text']:
                bot.sendMessage(chat_id,"Eae meu parsero "+'@'+user+" oq ce manda?")
            elif ('sk' or 'skate') in msg['text']:
                bot.sendMessage(chat_id,"SK88888 CHARLI BRAU")
            elif ('fode' or 'vsf' or 'pau no cu') in msg['text']:
                bot.sendMessage(chat_id,"Coe meu bom, também tenho sentimentos :c")
            elif 'tic toc' in msg['text']:
                bot.sendMessage(chat_id,"tic play eh charli brau", reply_to_message_id=rpli)
            elif 'comandos' in msg['text']:
                bot.sendMessage(chat_id, "Eae meu bom, tá afim de uns comandos? \n/dedo \n/nocu")
            elif msg['text'] == '/dedo':
                    bot.sendMessage(chat_id, "Para utilizar o comando?, voc� deve digitar po comando seguido do usuário ex: \n /dedo @xitaozinho")
                    if '/dedo @' in msg['text']:
                        print(msg['text'])

        if 'mostraid' == msg['text']:
            dict = json.load(open('ids.txt'))
            bot.sendMessage(chat_id, dict)

        if 'criaid' == msg['text']:
            json.dump(ids, open('ids.txt', 'w'))

        if msg['text'] in ['Opora','opora']:
            bot.sendSticker(chat_id, sticker=open('opora.webp','rb'), reply_to_message_id=rpli)

        if msg['text'] in ['Helo', 'helo']:
            bot.sendSticker(chat_id, sticker=open('tia_helo.webp','rb'), reply_to_message_id=rpli)

        sk =['charlie','skate','sk8']
        if msg['text'] in sk:
            bot.sendSticker(chat_id, sticker=open('charli.webp', 'rb'), reply_to_message_id=rpli)

        if msg['text'] == 'to brabo':
            bot.sendSticker(chat_id, sticker=open('tomc.webp', 'rb'), reply_to_message_id=rpli)

    ############### NLTK AQUI ############################
        def gatilho(msg):
            teste = msg
            testem = []
            for (palavras) in teste.split():
                comstem = [p for p in palavras.split()]
                testem.append(str(stemm.stem(comstem[0])))

            novo = extrair(testem)
            print('TA SENTINDO OQ:', classificador.classify(novo))
            ######################### INTERAÇÕES ########################

            if classificador.classify(novo) == 'alegria':
                bot.sendMessage(chat_id, '@' + user + ' está radiante!')
            if classificador.classify(novo) == 'tristeza':
                bot.sendMessage(chat_id, 'Não se sinta triste @' + user + ' bora andar de skate')
            ########################### FIM INTERAÇÕES ###################

        if 'estou' in msg['text']:
            gatilho(msg['text'])
    ############# FIM NLTK ##################################
##################################################################################################
    else:
        if (content_type == 'photo')  and chat_id == ler()['chat_id'] and id == ler()['user']:
            id_file = msg['photo'][1]['file_id']
            if ler()['conteudo']+'.jpg' in os.listdir('./materias/'+ler()['local']+'/'):
                files = os.listdir('./materias/'+ler()['local']+'/')
                total = 0
                for i in files:
                    if ler()['conteudo']+'.jpg' == i:
                        total+=1
                total = total +1
                bot.download_file(id_file, './materias/'+ler()['local']+'/'+ler()['conteudo']+'('+str(total)+').jpg')
                bot.sendMessage(chat_id, 'Arquivo cadastrado na matéria '+ler()['local'])
                os.remove('./temp.txt')
            else:
                bot.download_file(id_file, './materias/'+ler()['local']+'/'+ler()['conteudo']+'.jpg')
                bot.sendMessage(chat_id, 'Arquivo cadastrado na matéria '+ler()['local'])
                os.remove('./temp.txt')

        if (content_type == 'document') and chat_id == ler()['chat_id'] and id == ler()['user']:
            file_name = msg['document']['file_name']
            id_file = msg['document']['file_id']
            bot.download_file(id_file,'./materias/'+ler()['local']+'/'+file_name)
            bot.sendMessage(chat_id, 'Arquivo cadastrado na matéria '+ ler()['local'])
            os.remove('./temp.txt')

bot.message_loop(handle)
print ('Rodando ...')

# Keep the program running.
while 1:
    time.sleep(10)