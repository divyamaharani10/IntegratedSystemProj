import json 
from fastapi import FastAPI
with open("DataNIM.json", "r") as read_file:
	data = json.load(read_file)
app = FastAPI()
@app.get('/nim/{nim}')
async def read_nim(nim: int):
	for mahasiswa_item in data['DataNIM']:
		if mahasiswa_item['NIM'] == nim:
			return mahasiswa_item
		raise HTTPException(
			status_code=404, detail=f'Item not found')
@app.get('/name/{name}')
async def read_name(name: str):
	for mahasiswa_item in data['DataNIM']:
		name = mahasiswa_item['NamaMahasiswa']
		if name.split(' ').pop(0) == name:
			return mahasiswa_item
	raise HTTPException(
		status_code=404, detail=f'Item not found')
