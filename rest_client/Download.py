import requests


def downloadFile(self, url, enableLog=True, **kwargs):
    """
    Description:
        Will perform HTTP call for POST request for uploading file.
    Parameters:
        :param url: Complete location url path for running for REST call(STRING)
        :param enableLog: Modifying logs when required based on input parameter (BOOLEAN)
        :param kwargs: (OPTIONAL) parameters used in REST request.
    Returns:
        :return: file name [STRING]
    """
    local_filename = url.split('/')[-1]
    try:
        if enableLog:
            # logging.info("GET request URL: %s", url)
            pass
        else:
            # logging.info("Calling GET request, url is not logged as it contains password")
            pass
        response = requests.get(url, stream=True, auth=self.auth, verify=self.verify, **kwargs)
        with open(local_filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
        return local_filename

    except Exception as ex:
        # logging.exception("Request Exception : %s", ex)
        raise