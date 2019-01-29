# Info over de bestanden

DB Code
In deze map staat de code waarmee de database ingericht is, om deze in te richten zal die wel eerst aangemaakt moeten worden in PostgreSQL

Sensor Code
In deze map staat de code om de sensoren van de container te laten werken en om deze signalen door te sturen naar de database
client.py moet gerunt worden op de Raspberry Pi waarop het sensor systeem is aangesloten
containerCode.py moet gerunt worden op de computer waarop de database en de website staan
connectSensorToDatabase is de code die de container sensoren verbind met de database

testBuzzer.py is de code waarmee het ledje getest kan worden
testLightsensor.py is de code waarmee de LDR getest kan worden


Website Code
Hier staan de bestanden in die samen de website zijn
Als deze bestanden in de 'htdocs' map in Xampp worden gezet zal Xampp de website juist tonen
In de code van de website staat ook de connectie met de database
