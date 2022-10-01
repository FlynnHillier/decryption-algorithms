from datetime import datetime
import json
import os
from pydantic.utils import deep_update

class Logger:
    def __init__(self,outpath:str = "",collections=[]):
        if os.path.isabs(outpath):
            absolute_path = outpath
        else:
            absolute_path = os.path.join(os.getcwd(),outpath)

        outpath = os.path.join(absolute_path,"out")

        if not os.path.isdir(outpath): 
            os.makedirs(outpath)  

        for collection in collections:
            collection_path = os.path.join(outpath,collection)
            if not os.path.isdir(collection_path):
                os.mkdir(collection_path)
        
        self.outpath = outpath
        self.collections = collections

    def log(self,dict : dict,collection:str = "",**kwargs):
        
        logDir = self.outpath
        store_in_collection = False

        if collection != "" :

            if collection in self.collections:
                collection_path = os.path.join(self.outpath,collection)
                if not os.path.isdir(collection_path):
                    self._repairCollection(collection)

                logDir = collection_path
                store_in_collection = True

        fileName = f"{collection}{'' if collection == '' else '-'}log {datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.json"

        

        with open(str(os.path.join(logDir,fileName)),"w") as f:
            json.dump(dict,f,indent=4)

    def _repairCollection(self,collection):
        collection_path = os.path.join(self.outPath,collection)
        if not os.path.isDir(collection_path):
            os.makedirs(collection_path)
        
 

chiperLogger = Logger("",["affine","ceaser"])
