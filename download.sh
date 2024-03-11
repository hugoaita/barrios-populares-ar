#!/bin/bash

# Download files
dir='./datasets'

# ReNaBap dataset
url='https://datosabiertos.desarrollosocial.gob.ar/dataset/0d022767-9390-486a-bff4-ba53b85d730e/resource/9a951270-60dd-4f21-aa19-4ef1205620bd/download/20220131_info_publica.csv'

wget ${url} -P ${dir}


# Poblacion datasets 
url='https://www.indec.gob.ar/ftp/cuadros/poblacion/'

wget -r -A '.xls' "$url" -P "$dir" 
