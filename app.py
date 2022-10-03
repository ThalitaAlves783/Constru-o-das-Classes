class Documento:
    def __init__(self,numDoc,dataCriacao,dataEnvio,numEnvio,nomeDoc,situacao,setor):
        print('Construindo Objeto...')
        self.numDoc = numDoc
        self.nomeDoc = nomeDoc
        self.setor = setor
        self.dataCriacao = dataCriacao
        self.dataEnvio = dataEnvio
        self.numEnvio = numEnvio
        self.situacao = situacao

    def status(self):
        print(" O Documento: {}, do setor {}, Status:{}".format(self.nomeDoc,self.setor,self.situacao))