import telepot, time, json, os

bot = telepot.Bot('578012223:AAFjXoFrzYwfE4vCNUM-hcOFKrgLOn0dnE4')

def escreve(texto):# Gera a temp pra enviar arquivo subsequente
    json.dump(texto, open('temp.txt', 'w'))

def ler(): # Lê o json para enviar arquivo, baseando na id e chat id
    dict = json.load(open('temp.txt'))
    return dict

def handle(msg):
    content_type, chat_type, chat_id= telepot.glance(msg)
    id = msg['from']['id']


    if content_type == 'text':
        if '/comandosdba' == msg['text']:
            bot.sendMessage(chat_id, '/cadastrar disciplina ## Sempre com espaço\n/mostramaterias ## Irá mostrar as matéria cadastradas\n/mostracont disciplina  ## Mostra os conteúdos cadastrados\n/enviar disciplina conteudo  ## Envia arquivo ao db\n/down disciplina conteudo  ## Faz o download do arquivo, consulte "mostracont" primeiro', parse_mode='Markdown')

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
                if (conteudo in i) and (('.docx' in i) or ('.pptx' in i) or ('.txt' in i)):
                    if ('.docx' in i):
                        bot.sendDocument(chat_id, document=open('./materias/' + materia + '/' + conteudo + '.docx'))
                    if ('.pptx' in i):
                        bot.sendDocument(chat_id, document=open('./materias/' + materia + '/' + conteudo + '.pptx'))
                    if ('.txt' in i):
                        bot.sendDocument(chat_id, document=open('./materias/' + materia + '/' + conteudo + '.txt'))

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
