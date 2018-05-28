# encoding:'utf-8'
from wxpy import *
import gresocket


def sendMsg():
    # bot = Bot(True,True,None,None,None,None)
    # my = bot.friends().search('Centaur')[0]
    # my.send('我是棒棒哒Centaur!')
    logger = get_wechat_logger()
    logger.warning('warning sample')

    try:
        # finished = False
        # while not finished:
        #     req = gresocket.addHeader(header, req)
        #     finished = gresocket.sendRequest(req)
        #     if finished :
        #         print('done.')
        #     else :   
        #         sleep(600)
        gresocket.test()
    except:
        logger.exception('exception')

sendMsg()