


class A:
    # Decorator as a class method

    def decorator2(func):
        def wrapper(*args, **kwargs):
            print 'Decorator 2'
            try:
                print 'now in try'
                response = func(*args, **kwargs)
                if response.ok:
                    return response
                else:
                    print 'vRO call fails'
                    return None
            except Exception, e:
                print 'now in exception'
                print e
                return None
        return wrapper


    # As a class method
    @decorator2
    def grok(self, url):
        response = open('test', 'r')
        return response

if __name__ == '__main__':
    url = 'https://192.168.3.119:8281/vco/api/inventory/System/Resources/Library/DynamicTypes/Configuration/'
    #auth = auth.HTTPBasicAuth('app_vco_vcenter@vlab.local', 'Password123!')
    a = A()
    response = a.grok(url)
    print response

