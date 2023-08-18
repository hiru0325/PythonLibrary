import sqlite3
import common_const

class DB_Operation:

    # ----- テーブル作成 -----
    def sqlitef3_DBCreate(strDBFileName, strTableName):
        
        # ----- 初期化 -----
        __conDB = None

        try:
            # ----- DB接続 -----
            __conDB = sqlite3.connect(strDBFileName)
            __curDB = __conDB.cursor()

            __strSQL = 'SELECT '
            __strSQL += '* ' 
            __strSQL += 'FROM '
            __strSQL += 'sqlite_master '
            __strSQL += 'WHERE '
            __strSQL += 'type = \'table\' '
            __strSQL += 'AND '
            __strSQL += 'tbl_name = \'' + strTableName + '\''

            # ----- SQL実行 -----
            __curDB.execute(__strSQL)

            __row = __curDB.fetchall()

            if len(__row) <= 0:

                __strSQL = 'create table '
                __strSQL += '[' + strTableName + '] '
                __strSQL += '( '
                __strSQL += 'id INTEGER PRIMARY KEY AUTOINCREMENT'
                __strSQL += ',trading_date TEXT NOT NULL '
                __strSQL += ',trading_time TEXT NOT NULL '
                __strSQL += ',amount REAL NOT NULL '
                __strSQL += ')'

                # ----- SQL実行 -----
                __curDB.execute(__strSQL)

        finally:

            # ----- DB切断 -----
            if __conDB != None:

                __conDB.close()

    # ----- SELECT -----
    def sqlite3_DBSelect(strSQL):

        # ----- 初期化 -----
        __conDB = None

        try:
            # ----- DB接続 -----
            __conDB = sqlite3.connect(common_const.DB_FILE_NAME)
            __curDB = __conDB.cursor()

            # ----- SQL実行 -----
            __curDB.execute(strSQL)

            return __curDB

        finally:

            # ----- DB切断 -----
            if __conDB != None:

                __conDB.close()

    # ----- INSERT、UPDATE、DELETE -----
    def sqlite3_DBExecute(strDBfileName, strSQL):

        __conDB = None
        try:
            # ----- DB接続 -----
            __conDB = sqlite3.connect(strDBfileName)
            __curDB = __conDB.cursor()

            # ----- SQL実行 -----
            __curDB.execute(strSQL)

            # ----- コミット -----
            __conDB.commit()

            # ----- DB切断 -----
            __conDB.close()
            
            __conDB = None

        finally:

            if __conDB != None:

                # ----- ロールバック -----
                __conDB.rollback()

                # ----- DB切断 -----            
                __conDB.close()



    