# -*- coding: UTF-8 -*-
import json
import os
import time

class placeholder():
    def __init__(self):
        __TEMP_TIME = time.localtime(time.time())
        self.timeYears = time.strftime('%Y', __TEMP_TIME)
        self.timeMonths = time.strftime('%m', __TEMP_TIME)
        self.timeDays = time.strftime('%d', __TEMP_TIME)
        self.timeHours = time.strftime('%H', __TEMP_TIME)
        self.timeMinutes = time.strftime('%M', __TEMP_TIME)
        self.timeSeconds = time.strftime('%S', __TEMP_TIME)
    
    def replace(self, content):
        content = content.replace("{YEAR}", self.timeYears)
        content = content.replace("{MONTH}", self.timeMonths)
        content = content.replace("{DAY}", self.timeDays)
        content = content.replace("{HOUR}", self.timeHours)
        content = content.replace("{MINUTE}", self.timeMinutes)
        content = content.replace("{SECOND}", self.timeSeconds)
        return content

class RunServerTask():
    __DEFAULT_CONFIG = [
        {
            "name": "example0",
            "description": "This is a example item.",
            "runCommands": [
                "cmd1", 
                "cmd2", 
                "..."
            ],
            "sleep": 1
        }
    ]
    def __init__(self):
        self.configFullPath = self.getSelfName().replace(".py", "") + ".json"
        self.config = self.loadConfig(self.configFullPath)
        self.debug = False
    
    def getSelfName(self):
        return os.path.basename(__file__)
    
    def loadConfig(self, filePath):
        if (not os.path.isfile(filePath)):
            self.saveJSON(filePath, self.__DEFAULT_CONFIG)
        return self.loadJSON(filePath)

    def loadJSON(self, filePath):
        try:
            with open(filePath, 'r') as f:
                return json.load(f)
        except:
            print("读取 json 异常")
            return None
        
    def process(self):
        print("[Main/INFO]开始执行")
        for item in self.config:
            print("[Main/INFO]名称: {}".format(item["name"]))
            print("[Main/INFO]  描述: {}".format(item["description"]))
            print("[Main/INFO]  名称: {}".format(item["name"]))
            print("[Main/INFO]  时延: {}".format(item["sleep"]))
            time.sleep(item["sleep"])
            print("[Main/INFO]  执行命令:")
            for command in item["runCommands"]:
                print("[Main/INFO]  - {}".format(command))
                os.system(placeholder().replace(command))
    
    def saveJSON(self, filePath, configObject):
        try:
            with open(filePath, 'w') as f:
                json.dump(configObject, f, ensure_ascii = False, indent = 4)
        except:
            print("保存 json 异常")
            return None
    
    def showInfo(self):
        for item in self.config:
            print("名称: {}".format(item["name"]))
            print("  描述: {}".format(item["description"]))
            print("  名称: {}".format(item["name"]))
            print("  执行命令:")
            for command in item["runCommands"]:
                print("  - {}".format(command))
            print("  执行时延: {}".format(item["sleep"]))
            
    def refreshConfig(self):
        self.loadConfig()
        
p = RunServerTask()
p.showInfo()
p.process()