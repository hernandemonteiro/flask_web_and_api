def template(markdown, title):
    style = '* {\
                padding: 0px;\
                margin:0px;\
                box-sizing: border-box;\
            }\
            body {\
            width: 100%;\
            height: 100vh;\
            overflow: auto;\
            background-color: rgb(41, 40, 40);\
                }\
            h1, h2, h3, h4, h5 ,h6 {\
                color: greenyellow;\
                padding: 2%;\
                user-select: none;\
                }\
            p {\
                padding: 3%;\
                font-weight: bold;\
                color: seashell;\
                user-select: none;\
                }\
            a {\
                position: fixed;\
                display: flex;\
                justify-content: center;\
                align-items: center;\
                font-size: 1.1em;\
                font-wieght: bold;\
                text-transform: uppercase;\
                text-decoration: none;\
                padding: 1%;\
                background-color: white;\
                }\
            div {\
                padding: 40 40;\
                text-align: center;\
                text-transform: uppercase;\
                font-family: sans-serif;\
                }'
    templateString = f'<html lang="pt-BR"><body>\
                        <title>{title}</title>\
                            <a href="/">\
                                Voltar ao Inicio\
                            </a>\
                            <style>{style}</style>\
                            <div>{markdown}</div>\
                        </body></html>'

    return templateString
