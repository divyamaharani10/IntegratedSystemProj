import json 
from fastapi import FastAPI
with open("DataNIM.json", "r") as read_file:
	data = json.load(read_file)
app = FastAPI()
@app.get('/nim/{id}')
async def read_nim(id: int):
	for mahasiswa_item in data['DataNIM']:
		if mahasiswa_item['id'] == id:
			return mahasiswa_item
	raise HTTPException(
		status_code=404, detail=f'Item not found')
