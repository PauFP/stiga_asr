#!/usr/bin/env python
import argparse
import os
import pandas as pd
import traceback

from flask import Flask, request, jsonify
from time import sleep


application = Flask(__name__)


@application.route('/alive')
def is_alive():
    return "Si estic viu!!!"


@application.route('/get_model_info')
def get_model_info():
    '''
    Gives information of both the pipeline and the model currently in use by the service
    Returns:

    '''
    clean_dict = 'Hola get model info'
    return clean_dict


@application.route('/process')
def map_pages():
    '''
    Maps the content of the website for the property_id given as argument of the request
    Returns:

    '''

    text_output='UNDEFINED'
    audio_file_name = request.args.get('audio_file_name', None)

    #Llegir arxiu audio_file_name
    # processar amb el model speech2text
    # guardat el resultat en el json de sortida[text_output]

    print(f'processant!!!!{audio_file_name}')
    sleep(5)

    return jsonify({'status': 200,
                    'audio_file_name': audio_file_name,
                    'test output': text_output,
                    })


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Activates the automapping server')
    parser.add_argument('-p', '--port',required=True, default=8080, help='Port used for the server (default: 5000)', type=int)
    args = parser.parse_args()

    print('EXECUTANT SERVEI INFERENCIA !!!!!')

    application.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

    el_meudel={'bla':25}

    application.run(host='0.0.0.0', port=args.port)
