import os
import datetime
import logging
import common_const

# ----- 出力名を設定 -----
_logger = logging.getLogger(str(datetime.date.today()))

# ----- ログフォルダ ------
_strLogName = './log'

# ----- ログファイル名 -----
_strLogFileName = str(datetime.date.today()) + '.log'

# ----- 出力ファイルの設定 -----
_fileLog = logging.FileHandler(_strLogName + '/' + _strLogFileName)
_logger.addHandler(_fileLog)

# ----- コンソール出力の設定 -----
_dispLog = logging.StreamHandler()
_logger.addHandler(_dispLog)

class Log_Operation:

    # ----- ログレベル設定 -----
    def SetLogLevel(strLogLevel):

        # ----- DEBUG -----
        if strLogLevel == common_const.LOG_LEVEL_DEBUG:
            _logger.setLevel(logging.DEBUG)

        # ----- INFO -----
        elif strLogLevel == common_const.LOG_LEVEL_INFO:
            _logger.setLevel(logging.INFO)

        # ----- WARNING -----
        elif strLogLevel == common_const.LOG_LEVEL_WARNING:
            _logger.setLevel(logging.WARNING)

        # ----- ERROR -----
        elif strLogLevel == common_const.LOG_LEVEL_ERROR:
            _logger.setLevel(logging.ERROR)
        
        # ----- CRITICAL -----
        elif strLogLevel == common_const.LOG_LEVEL_CRITICAL:
            _logger.setLevel(logging.CRITICAL)

        # ----- 例外発生 -----
        else:
            raise ValueError('引数の値が適切ではありません。')

    # ----- ログファイル出力 -----
    def OutputLogName(strLogLevel, strLogContent):

        # ----- ログフォルダ確認(なければ、作成) -----
        if os.path.exists(_strLogName) == False:
            os.mkdir(_strLogName)

        strNow = str(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))

        # ----- DEBUG -----
        if strLogLevel == common_const.LOG_LEVEL_DEBUG:
            _logger.debug('【' + strNow + '】\r\n' + 'DEBUG Message:\r\n' + strLogContent + '\r\n')

        # ----- INFO -----
        elif strLogLevel == common_const.LOG_LEVEL_INFO:
            _logger.info('【' + strNow + '】\r\n' + 'INFO Message:\r\n' + strLogContent + '\r\n')

        # ----- WARNING -----
        elif strLogLevel == common_const.LOG_LEVEL_WARNING:
            _logger.warning('【' + strNow + '】\r\n' + 'WARNING Message:\r\n' + strLogContent + '\r\n')

        # ----- ERROR -----
        elif strLogLevel == common_const.LOG_LEVEL_ERROR:
            _logger.error('【' + strNow + '】\r\n' + 'ERROR Message:\r\n' + strLogContent + '\r\n')

        # ----- CRITICAL -----
        else:
            _logger.critical('【' + strNow + '】\r\n' + 'CRITICAL Message:\r\n' + strLogContent + '\r\n')
