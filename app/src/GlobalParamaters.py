import os
import json

invalidModeArgumentException = Exception('Invalid Mode Argument')
invalidFrontentPathArgumentException = Exception('Invalid Web Frontend Path Argument')
invalidVersionArgumentException = Exception('Invalid Version Argument')
invalidInvalidApiaccesssecurityException = Exception('Invalid API Access Security Argument')
invalidInvalidApiURLException = Exception('Invalid API URL Argument')

# class to store GlobalParmaters
class GlobalParamatersClass():
  mode = None
  version = None
  webfrontendpath = None
  apiurl = None
  apiaccesssecurity = None
  
  #Read environment variable or raise an exception if it is missing and there is no default
  def readFromEnviroment(self, env, envVarName, defaultValue, exceptionToRaiseIfInvalid, acceptableValues):
    try:
      val = env[envVarName]
      if (acceptableValues != None):
        if (val not in acceptableValues):
          raise exceptionToRaiseIfInvalid
      return val
    except KeyError:
      if (defaultValue == None):
        raise exceptionToRaiseIfInvalid
      return defaultValue
  
  def __init__(self, env):
    self.mode = self.readFromEnviroment(env, 'APIAPP_MODE', None, invalidModeArgumentException, ['DEVELOPER','DOCKER'])
    self.version = self.readFromEnviroment(env, 'APIAPP_VERSION', None, invalidVersionArgumentException, None)
    self.webfrontendpath = self.readFromEnviroment(env, 'APIAPP_FRONTEND', None, invalidFrontentPathArgumentException, None)
    self.apiurl = self.readFromEnviroment(env, 'APIAPP_APIURL', None, invalidInvalidApiURLException, None)
    apiaccesssecuritySTR = self.readFromEnviroment(env, 'APIAPP_APIACCESSSECURITY', None, invalidInvalidApiaccesssecurityException, None)

    if (self.webfrontendpath != '_'):
      if (not os.path.isdir(self.webfrontendpath)):
        raise invalidFrontentPathArgumentException
    if (len(self.version) == 0):
      raise invalidVersionArgumentException

    try:
      self.apiaccesssecurity = json.loads(apiaccesssecuritySTR)
    except json.decoder.JSONDecodeError:
      print('Invalid JSON for apiaccesssecurity - ' + apiaccesssecuritySTR)
      raise invalidInvalidApiaccesssecurityException

  def getStartupOutput(self):
    r = 'Mode:' + self.mode + '\n'
    r += 'Version:' + self.version + '\n'
    r += 'Frontend Location:' + self.webfrontendpath + '\n'
    r += 'apiurl:' + self.apiurl + '\n'
    r += 'apiaccesssecurity:' + json.dumps(self.apiaccesssecurity) + '\n'
    return r

  def getDeveloperMode(self):
    return (self.mode == 'DEVELOPER')

  def getWebFrontendPath(self):
    return self.webfrontendpath

  def getWebServerInfoJSON(self):
    return json.dumps({'version': self.version,'apiurl': self.apiurl,'apiaccesssecurity': self.apiaccesssecurity})

class GlobalParamatersPointerClass():
  obj = None
  def set(self, obj):
    self.obj = obj
  def get(self):
    return self.obj

GlobalParamaters = GlobalParamatersPointerClass()
