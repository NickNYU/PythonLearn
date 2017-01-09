

def fast_filter(payload):
    relations = payload.get('relations')
    if not relations:
        print r'No items are under path /Library/DynamicTypes/Configuration/ on vRO'
        return None
    if relations['total'] != 1:
        print r'Should be only one item under /Library/DynamicTypes/Configuration/ on vRO'
        return None
    resouceElement = relations['link'][1]
    resourceId = filter(lambda item: item['name'] == 'id',
                        [attribute for attribute in resouceElement['attributes']])[0]['value']
    print resourceId


if __name__ == '__main__':
    payload = {
        "attributes": [
            {
                "value": "Configuration",
                "name": "name"
            },
            {
                "value": "402883f7582bc1b001582bc2c2bc1a3d",
                "name": "id"
            },
            {
                "value": "ResourceElementCategory",
                "name": "type"
            }
        ],
        "href": "https://192.168.3.119:8281/vco/api/inventory/System/Resources/Library/DynamicTypes/Configuration/",
        "relations": {
            "total": 1,
            "link": [
                {
                    "href": "https://192.168.3.119:8281/vco/api/inventory/System/Resources/Library/DynamicTypes/",
                    "rel": "up"
                },
                {
                    "attributes": [
                        {
                            "value": "nick-test",
                            "name": "name"
                        },
                        {
                            "value": "6b17b052-3e2e-4b85-8534-324c895d215b",
                            "name": "id"
                        },
                        {
                            "value": "ResourceElement",
                            "name": "type"
                        }
                    ],
                    "href": "https://192.168.3.119:8281/vco/api/inventory/System/Resources/Library/DynamicTypes/Configuration/nick-test/",
                    "rel": "down"
                }
            ]
        }
    }
    fast_filter(payload)
