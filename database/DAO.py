from database.DB_connect import DBConnect
from model.constructor import Constructor
from model.result import Result

class DAO():
    @staticmethod
    def get_nodi():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT distinct c.*
                    FROM constructors c"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Constructor(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def riempi_nodi(c,b):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT re.*, r.year
                    from results re, races r
                    where r.year>=%s and r.year<=%s and re.raceId =r.raceId 
                    """
        cursor.execute(query,(c,b))

        res = []
        for row in cursor:
            res.append(Result(**row))

        cursor.close()
        cnx.close()
        return res


    @staticmethod
    def get_archi(c,b):
        """Arco tra due generi se un cliente anche su invoice differenti ha comprato 2 brani di
            genere differente in quel paese"""
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = f"""with costruttori_validi as(
                    SELECT distinct re.constructorId as cid
                    from results re, races r
                    where r.year>=%s and r.year<=%s and re.raceId =r.raceId 
                    )
                select distinct least(cv.cid,cv1.cid) as id1, greatest(cv.cid,cv1.cid) as id2
                FROM costruttori_validi cv, costruttori_validi cv1
                where cv.cid!=cv1.cid 
                group by least(cv.cid,cv1.cid), greatest(cv.cid,cv1.cid)
                
                """

        cursor.execute(query,(c,b))
        res = []
        for row in cursor:
            res.append((row["id1"], row["id2"]))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def get_pesi(c,b):
        """Priority--> ogni nodo ha un peso generato dalla somma unitprice*quantity rispetto al genere

"""
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = f"""with costruttori_validi as(
                    SELECT distinct re.constructorId as cid
                    from results re, races r
                    where r.year>=%s and r.year<=%s and re.raceId =r.raceId 
                )
                select cv.cid as id, count(r.position) as peso
                from costruttori_validi cv, results r, races r2 
                where cv.cid=r.constructorId and r.position is not null and r2.raceId =r.raceId and r2.year>=%s and r2.year<=%s
                group by cv.cid
                        """

        cursor.execute(query,(c,b,c,b))
        res = {}
        for row in cursor:
            res[row["id"]] = row["peso"]

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllYears():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT distinct r.year as anno 
                        from races r
                        order by r.year desc"""

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["anno"])

        cursor.close()
        cnx.close()
        return res
