# -*- coding: utf-8 -*-

from bottle import Bottle, response, request
import json
import random

class srv:
    def __init__(self, host='', porta=8080):
        self._h = host
        self._p = porta
        self._a = Bottle()
        self._rota()
        self.estado = '0'

    def _rota(self):
        self._a.route('/breaker', callback=self.disjuntor)
        self._a.route('/breaker', callback=self.set_disjuntor, method='POST')
        self._a.route('/voltage', callback=self.tensao)
        self._a.route('/current', callback=self.corrente)

    def go(self):
        self._a.run(host=self._h, port=self._p)

    def disjuntor(self, estado=None):
        if estado:
            self.estado = estado
        response.headers['Content-Type']='application/json'
        return json.dumps(self.estado)

    def set_disjuntor(self):
        response.headers['Content-Type']='application/json'
        self.estado = request.forms.get('estado')
        return json.dumps(self.estado)

    def tensao(self):
        response.headers['Content-Type']='application/json'
        return json.dumps({'voltage':float('%d.%d' %(random.randint(218,222),random.randint(0,99))),'unit':'V'})

    def corrente(self):
        response.headers['Content-Type']='application/json'
        return json.dumps({'current':float('%d.%d' %(random.randint(1,20),random.randint(0,99))),'unit':'A'})

if __name__=='__main__':
    s = srv().go()
