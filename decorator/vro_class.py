


class vRO(object):
    """
    Description: Used to encapsulate the vRO related REST Calls
    """
    def __init__(self, host=None, username=None, password=None, vroDict=None):
        self.host = vroDict.get('host', host)
        self.username = vroDict.get('username', username)
        self.password = vroDict.get('password', password)
        assert self.host, 'vRO FQDN/IP is needed'
        assert self.username, 'vRO username is needed for REST call'
        assert self.password, 'vRO password is needed for REST call'
        self.client = RESTClient(self.username, self.password)

    def __buildUrl(self, uri):
        urlHead = constants.VRO_REST_URL_HEAD.format(vroHost=self.host)
        return uri if uri.find(urlHead) > 0 else ''.join((urlHead, uri))

    def tryDecorator(func):
        """
        Description: Wrapper method used for decorating
        :param func: function
        :return:
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Get function name
            methodName = str(getattr(func, '__name__')).upper()
            vro = args[0]
            uri = args[1]
            payload = args[2] if len(args) > 2 else None
            try:
                response = func(*args, **kwargs)
                if response.ok:
                    return response
                else:
                    logging.error('vRO: %s REST call not valid: ',
                                  vro.host)
                    logging.error('%s %s\n payload: %s',
                                  methodName,
                                  uri,
                                  payload)
                    return None
            except Exception, e:
                logging.error('vRO :%s REST call failed: ', vro.host)
                logging.error('%s %s\n payload: %s',
                              methodName,
                              uri,
                              payload)
                logging.exception(e)
                return None

        return wrapper

    @tryDecorator
    def get(self, uri):
        uri = self.__buildUrl(uri)
        return self.client.get(uri)

    @tryDecorator
    def post(self, uri, payload=None):
        uri = self.__buildUrl(uri)
        return self.client.post(url=uri, json=payload)

    @tryDecorator
    def put(self, uri, payload=None):
        uri = self.__buildUrl(uri)
        return self.client.put(url=uri, json=payload)

    @tryDecorator
    def delete(self, uri):
        uri = self.__buildUrl(uri)
        return self.client.delete(uri)

    @tryDecorator
    def download(self, uri):
        uri = self.__buildUrl(uri)
        return self.client.get(url=uri, stream=True)

    def downloadToZip(self, uri, filename):
        response = self.download(uri)
        if not response:
            return None
        f = open(filename, 'wb')
        for chunk in response.iter_content():
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
        f.close()
        filePath = os.path.join(BASEDIR, filename)
        logging.debug('Download file is located in: %s', filePath)
        return filePath