#!/usr/bin/python
import psycopg2
from config import config
 
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
 
        # create a cursor
        cur = conn.cursor()

        #getting itens for JSON

        def getdados(idDoutor, *args):
            conn = None
            try:
                params = config()
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
                
               
                id_doutor = idDoutor
                
                cur.execute("SELECT nome FROM doutor")
                nome_doutor = cur.fetchone()

                cur.execute("SELECT dt_ciclo FROM custo_atendimento")
                dt_ciclo = cur.fetchone()
               
                cur.execute("SELECT dt_previsao_pagamento FROM custo_atendimento")
                dt_previsao_pagemento = cur.fetchone()


                cur.execute("SELECT id FROM job")
                id_job = cur.fetchone()

                cur.execute("SELECT dt_pagamento FROM custo_atendimento")
                dt_pagamento = cur.fetchone()

               
                cur.execute("SELECT total_atendimento FROM custo_atendimento")
                total_atendimento = cur.fetchone()

                cur.execute("SELECT SUM(valor_reembolso) FROM custo_atendimento")
                total_reembolso_job = cur.fetchone()

                cur.execute("SELECT SUM(valor_atendimento) FROM custo_atendimento")
                total_geral_job = cur.fetchone()

                cur.execute("SELECT tipo FROM tipo_servico")
                tipo_servico = cur.fetchone()

                cur.execute("SELECT id FROM custo_atendimento")                
                id_atendimento = cur.fetchone()

                cur.execute("SELECT valor_atendimento FROM custo_atendimento")
                valor_atendimento = cur.fetchone()

                cur.execute("SELECT valor_horas_extras FROM custo_atendimento")
                valor_horas_extras = cur.fetchone()

                cur.execute("SELECT valor_reembolso FROM custo_atendimento")
                valor_reembolso = cur.fetchone()

                cur.execute("SELECT total_atendimento FROM custo_atendimento")
                total_atendimento = cur.fetchone()

 
                cur.close()
           except (Exception, psycopg2.DatabaseError) as error:
               print(error)
           finally:
               if conn is not None:
                   conn.close()



 '''       
 execute a statement to test the connection
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
'''   
     # close the communication with the PostgreSQL
       
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
 
 
if __name__ == '__main__':
    connect()
