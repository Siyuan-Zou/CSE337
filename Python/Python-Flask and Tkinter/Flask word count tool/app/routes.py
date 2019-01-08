from flask import *
from app import app
from app.forms import TextAnalyzerForm
import re
import operator

def count_char(text):
    return len(list(text))

def count_word(text, delimiter):
    for c in delimiter:
        text=text.replace(c, ' ')
    words=text.split(' ')
    return len(words)

def top(text, delimiter):
    for c in delimiter:
        text=text.replace(c, ' ')
    words=text.split(' ')
    freqTable={}
    for w in words:
        if(w in freqTable):
            freqTable[w] = freqTable[w]+1
        else:
            freqTable[w] = 1
    sorted_freqTable = sorted(freqTable.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_freqTable[0:5]

@app.route('/', methods=['GET', 'POST'])
def index():
    output = 0
    form = TextAnalyzerForm()
    if form.validate_on_submit():
        text = form.text.data
        delimiter = form.delimiter.data
        options = form.options.data
        if (not text or not options):
            return redirect(url_for('result', operationname='error'))
        if(options == 'countchar'):
            output=count_char(text)
        else:
            if(options == 'countword'):
                output=count_word(text, delimiter)
            else:
                if(options == 'top5'):
                    output = top(text, delimiter)
                else:
                    return redirect(url_for('result', operationname='error'))

        session['value'] = output
        return redirect(url_for('result', operationname=options))
    return render_template('index.html', form=form)

@app.route("/result/<operationname>", methods=['GET', 'POST'])
def result(operationname):
   if(operationname=='error'):
       return render_template('result.html', output = 'Error')
   return render_template('result.html', output = session.get('value', None))

@app.errorhandler(403)
def forbidden(error):
    return render_template('403.html'), 403

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
