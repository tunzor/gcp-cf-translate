from google.cloud import translate

translate_client = translate.Client()

def htmlWrap(word, lang, translation):
    return '''
    <html>
    <head><title>Translate!</title></head>
	<body>
    <h1 style="color: #b731b5;">{}</h1>
    <h2>in<h2> 
    <h1 style="color: #ffd311;">{}</h1> 
    <h2>translates to:</h2>
    <h1 style="color: #4286f4;">{}</h1>
	</body>
    </html>
    '''.format(word, lang, translation)

def translate(request):
    request_json = request.get_json()
    if request.args and 'text' in request.args and 'toLang' in request.args:
        text = request.args['text']
        target = request.args['toLang']
        translation = translate_client.translate(text, target_language=target)
        return htmlWrap(text, target, translation['translatedText'])
    else:
        return '<span style="color: red;">Provide text and target language with parameters: <i>text</i> and <i>toLang</i>.</span>'

