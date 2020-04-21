import clr,os,sys
import bottle
from bottle import route, run, request

currentFolder = os.getcwd()     
sys.path.append(currentFolder) 
clr.AddReference("BarTender")
clr.AddReference("Seagull")

from BarTender import Formats,Application,BtCacheFlushInterval,BtSaveOptions
from Seagull import BarTender

printers = BarTender.Print.Printers()
default_printer = printers.Default.PrinterName

btApp = Application()

@route('/print', method='POST')
def print_service():
    try:
        req = request.json
        btformat = btApp.Formats.Open(currentFolder + "\\%s.btw" % req['template'], False, "")
        btformat.PrintSetup.Printer = req['printer'] if 'printer' in req else default_printer
        btformat.PrintSetup.IdenticalCopiesOfLabel = req['count'] if 'count' in req else 1
        
        for i in req['data']:
            btformat.SetNamedSubStringValue(i['key'], i['value'])

        btformat.PrintOut()
        btformat.PrintSetup.Cache.FlushInterval = BtCacheFlushInterval.btCacheFlushPerSession
        btformat.Close(BtSaveOptions.btDoNotSaveChanges)

        return {'error': 0}
    except:
        return {'error': -1}


@route('/printers')
def printers():
    printers = BarTender.Print.Printers()
    return {'error': 0, 'data': {'printers': [i.PrinterName for i in printers.GetEnumerator()]}}


if __name__ == '__main__':
    run(port=8080)
