# comando para rodar como servico esse app em python (pyinstaller -F pointDatacom.py)
# comando para rodar como exe um  esse app em python (pyinstaller -w pointDatacom.py)
import csv, sys
import string
import os
import configparser
import socket
import time
import hashlib
from datetime import date
import os.path
import pymysql
import sqlite3

condP = True
while(True):
    time.sleep(2)
    print("i la vamos nos ")
    #faz a leitura do conn.ini
    cfg = configparser.ConfigParser()
    cfg.read('conn.ini', encoding='utf-8')

    #variaveis do config.ini para fazer a conexão com o servidor principal
    hostServ  = cfg.get('connServe','host');
    # portc     = cfg.get('connServe','porta');
    dbServ    = cfg.get('connServe','db');
    uServ     = cfg.get('connServe','usuario');
    passServ  = cfg.get('connServe','senha');


    try:
        #conexão com o Mysql
        con = pymysql.connect(host=str(hostServ), database= str(dbServ) ,user=str(uServ), password=str(passServ))
        cur = con.cursor()
        condP = False
    except:
        # se não conseguir conectar ele nao quebra o laço
        condP = True


    if (condP == False):
        try:
            #conexão com o Mysql
            con = pymysql.connect(host=str(hostServ), database= str(dbServ) ,user=str(uServ), password=str(passServ))
            cur = con.cursor()
            condP = True
        except:
            # se não conseguir conectar ele nao quebra o laço
            condP = True

        #leitura dos arquivos de texto para a insersão no banco de dados
        if(os.path.exists("CMP_DEL.TXT") == True):
            with open("CMP_DEL.TXT") as arquivo:
                texto = arquivo.readlines()
                for linha in texto:
                    cur.execute(linha)

        path = "."
        dir = os.listdir(path)
        for file in dir:
            if file == 'CMP_DEL.TXT':
                os.remove(file)

        # 1000314807140620180829
        compDel = True
        while(compDel):
            cur.execute("SELECT id_temp_del_compras,chave FROM temp_del_compras")
            consuDelete = cur.fetchone()


            if(consuDelete != None):
                id_temp_del_compras = consuDelete[0]
                chaveDel            = consuDelete[1]


                cur.execute("SELECT id_compras,id_transportadora,litros, chave FROM compras where chave = " + chaveDel)
                consuComp  = cur.fetchone()

                if(consuComp != None):
                    id_compras = consuComp[0]
                    id_transp  = consuComp[1]
                    litrosComp = consuComp[2]
                    chaveComp  = consuComp[3]

                    cur.execute("SELECT id_transportadora_saldo, saldo FROM transportadoras_saldo where id_transportadora = " + str(id_transp))
                    consuTransSald = cur.fetchone()
                    id_TransSald = consuTransSald[0]
                    saldoTrans  = consuTransSald[1]
                    totalDel = saldoTrans - litrosComp

                    upTransSald = 'update transportadoras_saldo set saldo =' + str(totalDel) + ' where id_transportadora_saldo  =  ' + str(id_TransSald)
                    cur.execute(upTransSald)

                    cur.execute("delete from compras where chave =" + str(id_compras))

                    cur.execute("delete from temp_del_compras where chave =" + str(chaveDel))



                else:
                    cur.execute("delete from temp_del_compras where chave =" + str(chaveDel))

                    cur.execute("SELECT id_temp_del_compras,chave FROM temp_del_compras")
                    consuDelete = cur.fetchone()

                    if(consuDelete == None):
                        compDel = False

            else:
                cur.execute("SELECT id_temp_del_compras,chave FROM temp_del_compras")
                consuDelete = cur.fetchone()


                if(consuDelete == None):
                    compDel = False


        #leitura dos arquivos de texto para a insersão no banco de dados
        if(os.path.exists("COMPRAS.TXT") == True):
            with open("COMPRAS.TXT") as arquivo:
                texto = arquivo.readlines()
                for linha in texto:
                    cur.execute(linha)
        path = "."
        dir = os.listdir(path)
        for file in dir:
            if file == 'COMPRAS.TXT':
                os.remove(file)

        compInsert = True
        while(compInsert):
            cur.execute('SELECT * FROM tmp_cmp')
            consultTmpCmp = cur.fetchone()

            if(consultTmpCmp != None):

                idProdTempComp  = consultTmpCmp[1]
                idTransTempComp = consultTmpCmp[2]
                litrosTempComp  = consultTmpCmp[3]
                numDocTempComp  = consultTmpCmp[4]
                dataTempComp    = consultTmpCmp[5]
                horaTempComp    = consultTmpCmp[6]
                forneTempComp   = consultTmpCmp[7]
                chaveTempComp   = consultTmpCmp[8]

                cur.execute('SELECT id_compras, chave FROM compras where chave = '+ str(chaveTempComp))
                consultChaveComp = cur.fetchone()

                if(consultChaveComp == None):
                    cur.execute("INSERT INTO compras (id_produto,id_transportadora,litros,numero_documento,data,hora,fornecedor,chave,sinc) values " + "('" + str(idProdTempComp) + "','" + str(idTransTempComp) + "','" + str(litrosTempComp) + "','" + str(numDocTempComp) + "','" + str(dataTempComp) + "','" + str(horaTempComp) + "','" + str(forneTempComp) + "','"+ str(chaveTempComp) + "','0')")

                    cur.execute("delete from tmp_cmp where chave =" + str(chaveTempComp))
                else:
                    cur.execute("delete from tmp_cmp where chave =" + str(chaveTempComp))
            else:
                cur.execute('SELECT * FROM tmp_cmp')
                consultTmpCmp = cur.fetchone()
                if(consultTmpCmp == None):
                    compInsert = False


        # leitura dos arquivos de texto para a insersão no banco de dados
        if(os.path.exists("ABASTEC.TXT") == True):
            with open("ABASTEC.TXT") as arquivo:
                texto = arquivo.readlines()
                for linha in texto:
                    cur.execute(linha)
        path = "."
        dir = os.listdir(path)
        for file in dir:
            if file == 'ABASTEC.TXT':
                os.remove(file)

        abastInsert=True
        while(abastInsert):

            cur.execute("SELECT * FROM tmp_abastec")
            consulTmpAbast = cur.fetchone()

            if(consulTmpAbast != None):
                idTempAbast     = consulTmpAbast[0]
                transTmpAbastec = consulTmpAbast[1]
                prodTmp         = consulTmpAbast[2]
                dataTmp         = consulTmpAbast[3]
                horaTmp         = consulTmpAbast[4]
                placaTmp        = consulTmpAbast[5]
                kmTmp           = consulTmpAbast[6]
                kmAntTmp        = consulTmpAbast[7]
                mediaTmp        = consulTmpAbast[8]
                litroTmp        = consulTmpAbast[9]
                numContTmp      = consulTmpAbast[10]
                cur.execute("SELECT * FROM abastecimentos where num_cont = "+ str(numContTmp))
                consulAbast = cur.fetchone()

                if(consulAbast == None):
                    cur.execute("INSERT INTO abastecimentos (id_produto,id_transportadora,data,hora,placa,km,km_ant,media,litros,num_cont,sinc)VALUES" + "('" + str(transTmpAbastec) +"','"+ str(prodTmp)+"','"+ str(dataTmp)+"','"+ str(horaTmp)+"','"+ str(placaTmp)+"','"+ str(kmTmp)+"','"+ str(kmAntTmp)+"','"+ str(mediaTmp)+"','"+ str(litroTmp)+"','"+str(numContTmp)+"','0')")
                elif(consulAbast != None):
                    idAbastec        = consulAbast[0]
                    transAbastec     = consulAbast[1]
                    prodAbastec      = consulAbast[2]
                    dataAbastec      = consulAbast[3]
                    horaAbastec      = consulAbast[4]
                    placaAbastec     = consulAbast[5]
                    kmAbastec        = consulAbast[6]
                    kmAntAbastec     = consulAbast[7]
                    mediaAbastec     = consulAbast[8]
                    litroAbastec     = consulAbast[9]
                    numContAbastec   = consulAbast[10]

                    consultaAbastec =  str(transAbastec)+ str(prodAbastec)+str(dataAbastec)+str(horaAbastec)+str(placaAbastec)+str(kmAbastec)+str(kmAntAbastec)+str(mediaAbastec)+str(litroAbastec)+str(numContAbastec)

                    consultaTempAbast = str(transTmpAbastec)+ str(prodTmp)+ str(dataTmp)+str(horaTmp)+str(placaTmp)+str(kmTmp)+str(kmAntTmp)+str(mediaTmp)+str(litroTmp)+str(numContTmp)

                    if(consultaTempAbast == consultaAbastec):
                        cur.execute("delete from tmp_abastec where num_cont =" + str(numContTmp))

                    if(consultaTempAbast != consultaAbastec):
                        cur.execute("SELECT saldo FROM transportadoras_saldo where id_transportadora = " + str(transAbastec))
                        consulTranspSald = cur.fetchone()
                        saldoTransportadoraSaldo  = consulTranspSald[0]

                        toltaRetirado = saldoTransportadoraSaldo + litroAbastec

                        cur.execute("UPDATE FROM transportadoras_saldo SET saldo = " + str(toltaRetirado) + "WHERE =" + str(transAbastec))

                        cur.execute("DELETE FROM abastecimentos WHERE id_abastecimento =" + str(idAbastec))

                        cur.execute("INSERT INTO abastecimentos (id_produto,id_transportadora,data,hora,placa,km,km_ant,media,litros,num_cont,sinc)VALUES" + "('" +  str(transTmpAbastec) +"','"+ str(prodTmp)+"','"+ str(dataTmp)+"','"+ str(horaTmp)+"','"+ str(placaTmp)+"','"+ str(kmTmp)+"','"+ str(kmAntTmp)+"','"+ str(mediaTmp)+"','"+ str(litroTmp)+"','"+str(numContTmp)+"','0')")

                        cur.execute("DELETE FROM abastecimentos WHERE id_abastecimento =" + str(idTempAbast))
            else:
                cur.execute("DELETE FROM tmp_abastec WHERE id_abastecimento <> 0")

                cur.execute("SELECT * FROM tmp_abastec")
                consulTmpAbast = cur.fetchone()
                if(consulTmpAbast == None):
                    abastInsert = False





        cur.execute("SELECT * FROM compras WHERE sinc = 0")
        resultCompra = cur.fetchone()
        if(resultCompra != None):

            compCond = True
            while(compCond):
                cur.execute("SELECT * FROM compras WHERE sinc = 0")
                consultaCompra = cur.fetchone()
                idCompra = str(consultaCompra[0])
                prod     = str(consultaCompra[1])
                trans    = str(consultaCompra[2])
                litros   =     consultaCompra[3]
                data     = str(consultaCompra[5])
                hrs      = str(consultaCompra[6])

                consultaTransportadoraCompra = "SELECT * FROM transportadoras_saldo WHERE id_produto = " + prod +" and id_transportadora = " + trans
                cur.execute(consultaTransportadoraCompra)
                resultTransportadoraCompra = cur.fetchone()

            #se a consulta para ver se ja esta no transportadoras_saldo for nulo ele ira cadastrar
                if(resultTransportadoraCompra == None):

                    consProd = "SELECT codigo FROM produtos where codigo =" + prod
                    cur.execute(consProd)
                    consultaProd = cur.fetchone()

                    consTrans = "SELECT cod_pes FROM transportadoras where cod_pes =" + trans
                    cur.execute(consTrans)
                    consultaTrans = cur.fetchone()



                    a = "INSERT INTO transportadoras_saldo (id_produto, id_transportadora, saldo, data, hora) values " + "("
                    b =  str(consultaProd).strip('(,)') +",'"
                    c = str(consultaTrans).strip('(,)')+"','"
                    d = str(litros) +"','"
                    e = str(data) +"','"
                    f = str(hrs)+ "')"
                    buildSql = a+b+c+d+e+f
                    cur.execute(buildSql)

                    # fazer o update

                    upSincCompra = 'update compras set sinc = 1 where id_compras = ' + str(idCompra)
                    cur.execute(upSincCompra)

                    cur.execute("SELECT * FROM compras WHERE sinc = 0")
                    lacoConsultaCompra = cur.fetchone()

                    if(lacoConsultaCompra == None):
                        compCond = False

                else:
                    consultaTransportadoraCompra = "SELECT * FROM transportadoras_saldo WHERE id_produto = " + prod + " and id_transportadora = " + trans
                    cur.execute(consultaTransportadoraCompra)
                    resultTransportadoraCompra = cur.fetchone()
                    idTranspSaldo = resultTransportadoraCompra[0]
                    litrosTranspSaldo = resultTransportadoraCompra[3]

                    somaLitros = litros + litrosTranspSaldo

                    upSaldoCompra = "update transportadoras_saldo set saldo = " + str(somaLitros) + ", data ='" + str(data) + "', hora ='" + str(hrs) + "' where id_transportadora_saldo = "+ str(idTranspSaldo)
                    cur.execute(upSaldoCompra)

                    upSincCompra = 'update compras set sinc = 1 where id_compras = ' + str(idCompra)
                    cur.execute(upSincCompra)

                    cur.execute("SELECT * FROM compras WHERE sinc = 0")
                    lacoConsultaCompra = cur.fetchone()

                    if(lacoConsultaCompra == None):
                        compCond = False


        cur.execute("SELECT * FROM abastecimentos WHERE sinc = 0")
        resultAbastcimento = cur.fetchone()
        if(resultAbastcimento != None):

            abastecCond = True
            while(abastecCond):
                cur.execute("SELECT * FROM abastecimentos WHERE sinc = 0")
                consultaAbastec = cur.fetchone()
                idAbastecimento = str(consultaAbastec[0])
                prod            = str(consultaAbastec[1])
                trans           = str(consultaAbastec[2])
                data            = str(consultaAbastec[3])
                hrs             = str(consultaAbastec[4])
                litros          = consultaAbastec[9]


                consultaTransportadoraAbastec = "SELECT * FROM transportadoras_saldo WHERE id_produto = " + prod +" and id_transportadora = " + trans
                cur.execute(consultaTransportadoraAbastec)
                resultTransportadoraAbastec = cur.fetchone()


            #se a consulta para ver se ja esta no transportadoras_saldo for nulo ele ira cadastrar
                if(resultTransportadoraAbastec == None):

                    consProd = "SELECT codigo FROM produtos where codigo =" + prod
                    cur.execute(consProd)
                    consultaProd = cur.fetchone()

                    consTrans = "SELECT cod_pes FROM transportadoras where cod_pes =" + trans
                    cur.execute(consTrans)
                    consultaTrans = cur.fetchone()



                    a = "INSERT INTO transportadoras_saldo (id_produto, id_transportadora, saldo, data, hora) values " + "("
                    b =  str(consultaProd).strip('(,)') +",'"
                    c = str(consultaTrans).strip('(,)')+"','"
                    d = str(litros) +"','"
                    e = str(data) +"','"
                    f = str(hrs)+ "')"
                    buildSql = a+b+c+d+e+f
                    cur.execute(buildSql)

                    # fazer o update

                    upSincAbastec = 'update abastecimentos set sinc = 1 where id_abastecimento = ' + str(idAbastecimento)
                    cur.execute(upSincAbastec)

                    cur.execute("SELECT * FROM abastecimentos WHERE sinc = 0")
                    lacoConsultaAbastec = cur.fetchone()

                    if(lacoConsultaAbastec == None):
                        abastecCond = False

                else:

                    consultaTransportadoraAbastec = "SELECT * FROM transportadoras_saldo WHERE id_produto = " + prod + " and id_transportadora = " + trans
                    cur.execute(consultaTransportadoraAbastec)
                    resultTransportadoraAbastec = cur.fetchone()
                    idTranspSaldo = resultTransportadoraAbastec[0]
                    litrosTranspSaldo = resultTransportadoraAbastec[3]

                    somaLitros =  litrosTranspSaldo - litros

                    upSaldoAbastec = "update transportadoras_saldo set saldo = " + str(somaLitros) + ", data ='" + str(data) + "', hora ='" + str(hrs) + "' where id_transportadora_saldo = "+ str(idTranspSaldo)
                    cur.execute(upSaldoAbastec)

                    upSincAbastec = 'update abastecimentos set sinc = 1 where id_abastecimento = ' + str(idAbastecimento)
                    cur.execute(upSincAbastec)

                    cur.execute("SELECT * FROM abastecimentos WHERE sinc = 0")
                    lacoConsultaAbastec = cur.fetchone()

                    if(lacoConsultaAbastec == None):
                        abastecCond = False
