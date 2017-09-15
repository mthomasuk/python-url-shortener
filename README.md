## REQUIREMENTS FOR THIS TING
- python 3.6+
- redis 2+

## INSTALL THIS TING
`pip install -r requirements.txt`

## RUN THIS TING
`gunicorn -b 0.0.0.0:8000 main:app --reload`

## USE THIS TING
- `curl -X POST --data '{"url":"http://www.google.com"}' localhost:8000`
- returns a url/uuid
- `curl localhost:8000/{uuid}`

## HAMMER THIS TING
`wrk -t12 -c800 -d30s http://localhost:8000/{uuid}`

## TEST THIS TING
`python tests/*.py`