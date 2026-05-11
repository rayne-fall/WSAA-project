# DAO
# author: Sylvia Chapman Kent
# interacts with a database containing details of various examples of media
import mysql.connector
import config as cfg

class MediaDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    # initialise
    def __init__(self):
        self.host=       cfg.mysql['host_cred']
        self.user=       cfg.mysql['user_cred']
        self.password=   cfg.mysql['pass_cred']
        self.database=   cfg.mysql['db']
    # get the cursor
    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    # close the cursor
    def closeAll(self):
        self.connection.close()
        self.cursor.close
    # display all entries in the table of tv shows
    def getAlltv(self):
        cursor = self.getcursor()
        sql="select * from tv_shows"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result))
        self.closeAll()
        return returnArray
    # search the table for an id and display that tv show
    def findTVByID(self, id):
        cursor = self.getcursor()
        sql="select * from tv_shows where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue
    # add a tv show to the database
    def createTV(self, tvshow):
        cursor = self.getcursor()
        sql = "insert into tv_shows title, genre, year) values (%s %s,%s)"
        values = (tvshow.get("title"), tvshow.get("genre"), tvshow.get("year"))
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        tvshow["id"] = newid
        self.closeAll()
        return tvshow
    # update a tv show
    def updateTV(self, id, tvshow):
        cursor = self.getcursor()
        sql = "update tv_shows set title= %s, genre =%s, year= %s where id =%s"
        print(f"Update TV Show {tvshow}?")
        values = (tvshow.get("title"), tvshow.get("genre"), tvshow.get("year"),id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        print(f"Updated {tvshow}")
    # delete a tv show
    def deleteTV(self, id):
        cursor = self.getcursor()
        sql = "delete from tv_shows where id = %S"
        values=(id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
    # display all entries in the table of video games
    def getAllVideoGames(self):
        cursor = self.getcursor()
        sql="select * from video_games"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result))
        self.closeAll()
        return returnArray
    # search the table for an id and display that video game
    def findVideoGameByID(self, id):
        cursor = self.getcursor()
        sql="select * from video_games where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue
    # add a video game to the database
    def createVideoGame(self, videogame):
        cursor = self.getcursor()
        sql = "insert into video_games title, genre, year) values (%s %s,%s)"
        values = (videogame.get("title"), videogame.get("genre"), videogame.get("year"))
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        videogame["id"] = newid
        self.closeAll()
        return videogame
    # update a video game
    def updateVideoGame(self, id, videogame):
        cursor = self.getcursor()
        sql = "update video_games set title= %s, genre =%s, year= %s where id =%s"
        print(f"Update Video Game {videogame}?")
        values = (videogame.get("title"), videogame.get("genre"), videogame.get("year"),id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        print(f"Updated {videogame}")
    # delete a video game
    def deleteVideoGame(self, id):
        cursor = self.getcursor()
        sql = "delete from video_games where id = %S"
        values=(id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
    # convert the details and their columns to a dictionary object
    def convertToDictionary(self, resultLine):
        attkeys=['id','title','genre', "year"]
        tv_show = {}
        currentkey = 0
        for attrib in resultLine:
            tv_show[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return tv_show
    
mediaDAO=MediaDAO