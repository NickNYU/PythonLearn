
import time
import os


def create_page():
    Page = '''\
    <html>
    <body>
    <table>
    <tr>  <td>Header</td>         <td>Value</td>          </tr>
    <tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
    <tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
    <tr>  <td>Client port</td>    <td>{client_port}s</td> </tr>
    <tr>  <td>Command</td>        <td>{command}</td>      </tr>
    <tr>  <td>Path</td>           <td>{path}</td>         </tr>
    </table>
    </body>
    </html>
    '''
    values = {
        'date_time'   : time.time(),
        'client_host' : '192.168.1.1',
        'client_port' : '8080',
        'command'     : 'ls -al',
        'path'        : os.path
    }
    page = Page.format(**values)
    return page

if __name__ == '__main__':
    page = create_page()
    print page
